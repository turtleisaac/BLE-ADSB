import pyModeS as pms
from pyModeS.extra.rtlreader import RtlReader
from pyModeS.streamer.decode import Decode

import logging
import threading
import asyncio
import time
import os

from typing import Any

from bless import (  # type: ignore
    BlessServer,
    BlessGATTCharacteristic,
    GATTCharacteristicProperties,
    GATTAttributePermissions
)

filename = "Dataset14_Mar1824.txt"

# if os.path.isfile('FlightLogs/%s' % filename):
#     print("cancel run, filename in use")
#     exit(0)

logging.basicConfig(level=logging.DEBUG
                    # , filename='FlightLogs/%s' % filename
                    )
logger = logging.getLogger(name=__name__)
trigger: threading.Event = threading.Event()

service_uuid = "2A5A0D6F-9191-4C74-ADFD-40E8EC2D280A"
characteristic_uuid = "6D15917F-7722-493B-8D38-188F7C6214AC"


class RtlSdrBluetoothSource(RtlReader):
    def __init__(self):
        super(RtlSdrBluetoothSource, self).__init__()
        # self.reset_local_buffer()
        self.local_buffer_adsb_msg = dict()
        self.server = None
        loop = asyncio.get_event_loop()
        # self.run_ble(None)
        loop.run_until_complete(self.run_ble(loop))
        self.start_time = time.time()

    async def run_ble(self, loop):
        trigger.clear()
        # Instantiate the server
        my_service_name = "BLE_ADSB"
        self.server = BlessServer(name=my_service_name, loop=loop)
        self.server.read_request_func = self.read_request
        # server.write_request_func = write_request

        # Add Service
        my_service_uuid = service_uuid
        await self.server.add_new_service(my_service_uuid)

        # Add a Characteristic to the service
        my_char_uuid = characteristic_uuid
        char_flags = (
                GATTCharacteristicProperties.read |
                # GATTCharacteristicProperties.write |
                # GATTCharacteristicProperties.indicate |
                GATTCharacteristicProperties.notify
        )
        permissions = (
            GATTAttributePermissions.readable
        )
        await self.server.add_new_characteristic(
            my_service_uuid,
            my_char_uuid,
            char_flags,
            None,
            permissions)

        logger.debug(
            self.server.get_characteristic(
                my_char_uuid
            )
        )
        await self.server.start()
        logger.debug("Advertising")
        logger.info(f"Write '0xF' to the advertised characteristic: {my_char_uuid}")
        # trigger.wait()
        # await asyncio.sleep(2)
        # logger.debug("Updating")
        # server.get_characteristic(my_char_uuid)
        # server.update_value(
        #     my_service_uuid, "51FF12BB-3ED8-46E5-B4F9-D64E2FEC021B"
        # )
        # await asyncio.sleep(5)
        # await server.stop()

    # def reset_local_buffer(self):
    #     self.local_buffer_adsb_msg = []
    #     self.local_buffer_adsb_ts = []
    #     self.local_buffer_commb_msg = []
    #     self.local_buffer_commb_ts = []

    def handle_messages(self, messages):
        if self.stop_flag.value is True:
            self.stop()
            return

        # if len(messages) != 0:
        #     print('received messages and will add to transmit buffer')

        for msg, t in messages:
            if len(msg) < 28:  # only process long messages
                continue

            # print(msg)

            df = pms.df(msg)
            crc = pms.crc(msg)  # if crc is 0 then there was no error in the message

            if crc == 0 and (df == 17 or df == 18):
                # print('transmitting new message')
                self.local_buffer_adsb_msg[msg] = t
                b = bytearray()
                byte_list = []
                for x in range(0, len(msg), 2):
                    byte_list.append(int(msg[x:x + 2], 16))
                    b.append(int(msg[x:x + 2], 16))
                self.server.get_characteristic(characteristic_uuid).value = b
                print((t-self.start_time, byte_list))
                # logger.debug(str((t-self.start_time, byte_list)))
                while not self.server.update_value(service_uuid, characteristic_uuid):
                    pass
                # self.local_buffer_adsb_ts.append(t)
            # elif df == 20 or df == 21:
            #     self.local_buffer_commb_msg.append(msg)
            #     self.local_buffer_commb_ts.append(t)
            else:
                continue

        # if len(self.local_buffer_adsb_msg) > 1:
        #     print("read message")
            # self.raw_pipe_in.send(
            #     {
            #         "adsb_ts": self.local_buffer_adsb_ts,
            #         "adsb_msg": self.local_buffer_adsb_msg,
            #         # "commb_ts": self.local_buffer_commb_ts,
            #         # "commb_msg": self.local_buffer_commb_msg,
            #     }
            # )
            # self.reset_local_buffer()

    def read_request(self,
                     characteristic: BlessGATTCharacteristic,
                     **kwargs
                     ) -> bytearray:
        # logger.debug(f"Reading {characteristic.value}")
        # characteristic.value = self.local_buffer_adsb_msg[0]
        # todo store and iterate?
        # print(self.local_buffer_adsb_msg)
        print("reading")
        return characteristic.value
        # if len(self.local_buffer_adsb_msg) > 0:
        #     for message in self.local_buffer_adsb_msg:
        #         b = bytearray()
        #         print(message)
        #         for x in range(0, len(message), 2):
        #             b.append(int(message[x:x+2], 16))
        #         characteristic.value = b
        #         return b
        # return bytearray([0x8D, 0x48, 0x40, 0xD6, 0x20, 0x2C, 0xC3, 0x71, 0xC3, 0x2C, 0xE0, 0x57, 0x60, 0x98])
