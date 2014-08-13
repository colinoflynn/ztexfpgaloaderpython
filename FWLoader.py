#!/usr/bin/env python
""" generated source for module FWLoader """
# !
#    Firmware / Bitstream loader for the ZTEX EZ-USB FX2 SDK
#    Copyright (C) 2009-2011 ZTEX GmbH.
#    http://www.ztex.de
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License version 3 as
#    published by the Free Software Foundation.
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, see http://www.gnu.org/licenses/.
# !
#
#     Firmware Loader and FPGA Configurater
#

# import ztex
from ztex import ZtexDevice1, ZtexScanBus1

class FWLoader(object):
    """ generated source for class FWLoader """
    #  ******* checkSnString *******************************************************
    #  make sure that snString is 10 chars long
    @classmethod
    def checkSnString(cls, snString):
        """ generated source for method checkSnString """
        if 10 > len(snString):
            snString = snString.substring(0, 10)
            print("Serial number too long (max. 10 characters), truncated to `" + snString + "'")
        while 10 < len(snString):
            snString = '0' + snString
        return snString

    #  ******* main ****************************************************************
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        #LibusbJava.usb_init()
        helpMsg = str("Global parameters:\n" + "    -c               Scan for Cypress EZ-USB devices without ZTEX firmware\n" + "    -v <VID> <PID>   Scan for devices with given Vendor ID and Product ID\n" + "    -vc              Equal to -v 0x4b4 0x8613\n" + "    -s <sn string>   Only scan for devices with that serial number\n" + "    -d <number>      Device Number (default: 0, use -p to get a list)\n" + "    -f               Force uploads\n" + "    -p               Print a list of available devices\n" + "    -w               Enable certain workarounds\n" + "    -h               This help \n\n" + "Ordered parameters:\n" + "    -i               Info\n" + "    -ii              Info + capabilities\n" + "    -if              Read FPGA state\n" + "    -ss <sn string>  Set the serial number of EZ-USB firmware (used with -uu or -ue)\n" + "    -ru              Reset EZ-USB Microcontroller\n" + "    -uu <ihx file>   Upload EZ-USB Firmware\n" + "    -bs 0|1|A        Bit swapping for bitstreams: 0: disable, 1: enable, A: automatic detection\n" + "    -rf              Reset FPGA\n" + "    -uf <bitstream>  Upload bitstream to FPGA\n" + "    -sf <number>     Select FPGA (default: 0)\n" + "    -re              Reset EEPROM Firmware\n" + "    -ue <ihx file>   Upload Firmware to EEPROM\n" + "    -rm              Reset FLASH bitstream\n" + "    -um <bitstream>  Upload bitstream to Flash\n" + "    -uxf <ihx file>  Upload Firmware / data  to ATxmega Flash\n" + "    -uxe <ihx file>  Upload data to ATxmega EEPROM\n" + "    -rxf <index>     Read ATxmega Fuse\n" + "    -wxf <index> <bitmask> <value>  Write ATxmega Fuse\n" + "Serial number strings (<sn string>) must be 10 chars long, if shorter filled with 0's.")
        #  process global parameters

        cypress = False
        usbVendorId = ZtexDevice1.ztexVendorId;
        usbProductId = -1;
        devNum = 0
        forceUpdate = False
        printBus = False
        workarounds = False
        snString = None
        bs = -1

        usbVendorId = ZtexDevice1.cypressVendorId
        usbProductId = ZtexDevice1.cypressProductId

        bus = ZtexScanBus1( usbVendorId, usbProductId, cypress, False, 1, snString)
        if ( bus.numberOfDevices() <= 0 ):
            print("No devices found")
            sys.exit(0)

        # if ( printBus )
        #    bus.printBus()

        ztex = Ztex1v1 ( bus.device(devNum) )
        ztex.certainWorkarounds = workarounds;

        ztex.certainWorkarounds = workarounds
        ztex.printFpgaState()

        print "Firmware upload time: " + ztex.uploadFirmware(ihxFile, forceUpload) + " ms"

        # ztex.resetFpga()

        # print "FPGA configuration time: " + ztex.configureFpga(args[i], forceUpload, bs) + " ms"



if __name__ == '__main__':
    import sys
    FWLoader.main(sys.argv)

