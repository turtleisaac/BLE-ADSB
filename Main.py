import multiprocessing
import traceback

from pyModeS.streamer.decode import Decode
from pyModeS.streamer.source import RtlSdrSource
from rtlsdr import RtlSdr
import pyModeS as pms

from BluetoothAdsbServer import RtlSdrBluetoothSource

"""
This is still a very much in-development solution and is mostly full of testing code currently.
Nothing here will stay and this will eventually lead towards a solution which transmits the data
over bluetooth LE to an iOS/macOS device.
"""

raw_pipe_in, raw_pipe_out = multiprocessing.Pipe()
ac_pipe_in, ac_pipe_out = multiprocessing.Pipe()
exception_queue = multiprocessing.Queue()
stop_flag = multiprocessing.Value("b", False)

source = RtlSdrBluetoothSource()
try:
    source.run(raw_pipe_in, stop_flag, exception_queue)
except(ValueError):
    pass

#
#
# recv_process = multiprocessing.Process(
#     target=source.run, args=(raw_pipe_in, stop_flag, exception_queue)
# )
#
# decode = Decode(latlon=None, dumpto=None)
#
# decode_process = multiprocessing.Process(
#     target=decode.run, args=(raw_pipe_out, ac_pipe_in, exception_queue)
# )

# decode.run(raw_pipe_out, ac_pipe_in, exception_queue)


# recv_process.start()
# decode_process.start()
#
# print('before while loop')
#
# while True:
#     try:
#         while raw_pipe_out.poll():
#             print('received data')
#             data = raw_pipe_out.recv()
#             print(data)
#             for msg in data["adsb_msg"]:
#                 print(pms.adsb.callsign(msg))
#
#     except Exception as e:
#         tb = traceback.format_exc()
#         exception_queue.put((e, tb))

# while True:
#
#     break



# while (readSamples) {
# if (!started) {
# console.log('starting...')
# started = true
# }
#
# // const samples = await sdr.readSamples(16 * 16384);
# const samples = await sdr.readSamples(128000);
# // console.log(samples)
#
# const data = new Uint8Array(samples);
# // console.log(data)
#
# demodulator.process(data, 256000, onMsg)
# }