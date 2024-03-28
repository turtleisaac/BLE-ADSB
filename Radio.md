# Dongle

RTL-SDR is a very cheap ~$30 USB dongle that can be used as a computer based radio scanner for receiving live radio signals in your area (no internet required).
Depending on the particular model it could receive frequencies from 500 kHz up to 1.75 GHz. Most software for the RTL-SDR is also community developed,
and provided free of charge. Note that RTL-SDRs cannot transmit.

Dongles can be found at:

* [Dongle only (Amazon)](https://www.amazon.com/RTL-SDR-Blog-RTL2832U-Software-Defined/dp/B0BMKZCKTF)
* [Dongle only (Official RTL-SDR website)](https://www.rtl-sdr.com/buy-rtl-sdr-dvb-t-dongles/)
* [Smaller dongle with Antenna (Amazon)](https://www.amazon.com/NooElec-NESDR-Mini-Compatible-Packages/dp/B009U7WZCA/ref=sims_dp_d_dex_ai_speed_loc_mtl_v4_d_sccl_2_1/135-9408615-9400953?pd_rd_w=cdzW3&content-id=amzn1.sym.f8b81522-706a-46d3-a585-5fc6e1682ebe&pf_rd_p=f8b81522-706a-46d3-a585-5fc6e1682ebe&pf_rd_r=1GTRNY3WTZCFG77YSMC7&pd_rd_wg=NOwJB&pd_rd_r=80a2860f-1fdf-4454-b26d-5f6afbbe00ed&pd_rd_i=B009U7WZCA&psc=1)
  * This is what I have


# Antenna
In principle, any antenna designed for the radio frequency around 1 GHz can be used for receiving Mode S signals. A large variety of commercial off-the-shelf antennas can be found nowadays.

However, it is not difficult to design your own antenna. The carrier frequency of Mode S is 1090 MHz, which corresponds to the wavelength of 27.5 centimeters. In order to have an antenna that is tuned to this specific frequency, one can design the antenna simply using a piece of a conductor (metal wire) and a coaxial feeder cable. Figure 1.3 shows a few common antenna designs.

![image](https://github.com/turtleisaac/BLE-ADSB/assets/7987859/faa5b3f2-48a8-481f-afd9-33836679ee31)
Common antenna designs


The monopole antenna and the dipole antenna both are half-wavelength (<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>&#x3BB;</mi>
  <mrow data-mjx-texclass="ORD">
    <mo>/</mo>
  </mrow>
  <mn>2</mn>
</math>) antennas with a total conductor length of 13.75 cm. The ground plane antenna is a quarter-wavelength (<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>&#x3BB;</mi>
  <mrow data-mjx-texclass="ORD">
    <mo>/</mo>
  </mrow>
  <mn>4</mn>
</math>) antenna, where the main pole is 6.875 cm.

All these previous antennas are omnidirectional. Some time is also desirable to make use of directional antennas (such a Yagi antenna),
for example, to receive messages coming from the airport direction with a higher receiving gain.

If you purchase the [Smaller dongle with Antenna (Amazon)](https://www.amazon.com/NooElec-NESDR-Mini-Compatible-Packages/dp/B009U7WZCA/ref=sims_dp_d_dex_ai_speed_loc_mtl_v4_d_sccl_2_1/135-9408615-9400953?pd_rd_w=cdzW3&content-id=amzn1.sym.f8b81522-706a-46d3-a585-5fc6e1682ebe&pf_rd_p=f8b81522-706a-46d3-a585-5fc6e1682ebe&pf_rd_r=1GTRNY3WTZCFG77YSMC7&pd_rd_wg=NOwJB&pd_rd_r=80a2860f-1fdf-4454-b26d-5f6afbbe00ed&pd_rd_i=B009U7WZCA&psc=1)
then it comes with an antenna and you don't need to worry. Other options may or may not have an antenna, so just make sure you either purchase an antenna, a dongle which comes with one, or build one yourself.

> Sun, J. (2021). The 1090 Megahertz Riddle: A Guide to Decoding Mode S and ADS-B Signals (2nd ed.). TU Delft OPEN Publishing.
