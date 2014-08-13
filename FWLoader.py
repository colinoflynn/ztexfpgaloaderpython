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
import java.io

import java.util

import ch.ntb.usb

import ztex

class FWLoader(object):
    """ generated source for class FWLoader """
    #  ******* checkSnString *******************************************************
    #  make sure that snString is 10 chars long
    @classmethod
    def checkSnString(cls, snString):
        """ generated source for method checkSnString """
        if 10 > len(snString):
            snString = snString.substring(0, 10)
            System.err.println("Serial number too long (max. 10 characters), truncated to `" + snString + "'")
        while 10 < len(snString):
        return snString

    #  ******* main ****************************************************************
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        LibusbJava.usb_init()
        helpMsg = str("Global parameters:\n" + "    -c               Scan for Cypress EZ-USB devices without ZTEX firmware\n" + "    -v <VID> <PID>   Scan for devices with given Vendor ID and Product ID\n" + "    -vc              Equal to -v 0x4b4 0x8613\n" + "    -s <sn string>   Only scan for devices with that serial number\n" + "    -d <number>      Device Number (default: 0, use -p to get a list)\n" + "    -f               Force uploads\n" + "    -p               Print a list of available devices\n" + "    -w               Enable certain workarounds\n" + "    -h               This help \n\n" + "Ordered parameters:\n" + "    -i               Info\n" + "    -ii              Info + capabilities\n" + "    -if              Read FPGA state\n" + "    -ss <sn string>  Set the serial number of EZ-USB firmware (used with -uu or -ue)\n" + "    -ru              Reset EZ-USB Microcontroller\n" + "    -uu <ihx file>   Upload EZ-USB Firmware\n" + "    -bs 0|1|A        Bit swapping for bitstreams: 0: disable, 1: enable, A: automatic detection\n" + "    -rf              Reset FPGA\n" + "    -uf <bitstream>  Upload bitstream to FPGA\n" + "    -sf <number>     Select FPGA (default: 0)\n" + "    -re              Reset EEPROM Firmware\n" + "    -ue <ihx file>   Upload Firmware to EEPROM\n" + "    -rm              Reset FLASH bitstream\n" + "    -um <bitstream>  Upload bitstream to Flash\n" + "    -uxf <ihx file>  Upload Firmware / data  to ATxmega Flash\n" + "    -uxe <ihx file>  Upload data to ATxmega EEPROM\n" + "    -rxf <index>     Read ATxmega Fuse\n" + "    -wxf <index> <bitmask> <value>  Write ATxmega Fuse\n" + "Serial number strings (<sn string>) must be 10 chars long, if shorter filled with 0's.")
        #  process global parameters
        try:
            if len(args):
                System.err.println(helpMsg)
                System.exit(1)
            while len(args):
                if args[i] == "-c":
                    cypress = True
                elif args[i] == "-v":
                    i += 1
                    try:
                        if len(args):
                            raise Exception()
                        usbVendorId = Integer.decode(args[i])
                    except Exception as e:
                        System.err.println("Error: Vendor ID expected after -v")
                        System.err.println(helpMsg)
                        System.exit(1)
                    i += 1
                    try:
                        if len(args):
                            raise Exception()
                        usbProductId = Integer.decode(args[i])
                    except Exception as e:
                        System.err.println("Error: Product ID expected after -v <VID>")
                        System.err.println(helpMsg)
                        System.exit(1)
                elif args[i] == "-vc":
                    usbVendorId = ZtexDevice1.cypressVendorId
                    usbProductId = ZtexDevice1.cypressProductId
                elif args[i] == "-f":
                    forceUpload = True
                elif args[i] == "-p":
                    printBus = True
                elif args[i] == "-w":
                    workarounds = True
                elif args[i] == "-d":
                    i += 1
                    try:
                        if len(args):
                            raise Exception()
                        devNum = Integer.parseInt(args[i])
                    except Exception as e:
                        System.err.println("Error: Device number expected after -d")
                        System.err.println(helpMsg)
                        System.exit(1)
                elif args[i] == "-s":
                    i += 1
                    if len(args):
                        System.err.println("Error: String expected after -s")
                        System.err.println(helpMsg)
                        System.exit(1)
                    snString = cls.checkSnString(args[i])
                elif args[i] == "-h":
                    System.err.println(helpMsg)
                    System.exit(0)
                elif args[i] == "-i" or args[i] == "-ii" or args[i] == "-if" or args[i] == "-ru" or args[i] == "-rf" or args[i] == "-re" or args[i] == "-rm":
                elif args[i] == "-uu" or args[i] == "-uf" or args[i] == "-sf" or args[i] == "-ue" or args[i] == "-um" or args[i] == "-bs" or args[i] == "-uxf" or args[i] == "-uxe" or args[i] == "-rxf" or args[i] == "-ss":
                    i += 1
                elif args[i] == "-wxf":
                    i += 3
                else:
                    System.err.println("Error: Invalid Parameter: " + args[i])
                    System.err.println(helpMsg)
                    System.exit(1)
                i += 1
            if bus.numberOfDevices() <= 0:
                System.err.println("No devices found")
                System.exit(0)
            if printBus:
                bus.printBus(System.out)
            ztex.certainWorkarounds = workarounds
            snString = None
            while len(args):
                if args[i] == "-i":
                    print ztex
                if args[i] == "-ii":
                    print ztex
                    if str_ == "":
                        print "   No capabilities"
                    else:
                        print "   Capabilities:\n      " + str_
                if args[i] == "-if":
                    ztex.printFpgaState()
                elif args[i] == "-ss":
                    i += 1
                    if len(args):
                        System.err.println("Error: String expected after -ss")
                        System.err.println(helpMsg)
                        System.exit(1)
                    snString = cls.checkSnString(args[i])
                elif args[i] == "-ru":
                    ztex.resetEzUsb()
                elif args[i] == "-uu":
                    i += 1
                    if len(args):
                        System.err.println("Error: Filename expected after -uu")
                        System.err.println(helpMsg)
                        System.exit(1)
                    if snString != None:
                        ihxFile.setSnString(snString)
                    print "Firmware upload time: " + ztex.uploadFirmware(ihxFile, forceUpload) + " ms"
                elif args[i] == "-bs":
                    i += 1
                    if (len(args)) or not (args[i] == "0" or args[i] == "1" or args[i].lower() == "A".lower()):
                        System.err.println("Error: `0',`1' or `A' expected after -bs")
                        System.err.println(helpMsg)
                        System.exit(1)
                    if args[i] == "0":
                        bs = 0
                    elif args[i] == "1":
                        bs = 1
                    else:
                        bs = -1
                elif args[i] == "-rf":
                    ztex.resetFpga()
                elif args[i] == "-uf":
                    i += 1
                    if len(args):
                        System.err.println("Error: Filename expected after -uf")
                        System.err.println(helpMsg)
                        System.exit(1)
                    print "FPGA configuration time: " + ztex.configureFpga(args[i], forceUpload, bs) + " ms"
                elif args[i] == "-sf":
                    i += 1
                    try:
                        if len(args):
                            raise Exception()
                        fn = Integer.parseInt(args[i])
                    except Exception as e:
                        System.err.println("Error: Number expected after -sf")
                        System.err.println(helpMsg)
                        System.exit(1)
                    if fn >= 0:
                        ztex.selectFpga(fn)
                elif args[i] == "-re":
                    ztex.eepromDisable()
                elif args[i] == "-ue":
                    i += 1
                    if len(args):
                        System.err.println("Error: Filename expected after -ue")
                        System.err.println(helpMsg)
                        System.exit(1)
                    if snString != None:
                        ihxFile.setSnString(snString)
                    print "Firmware to EEPROM upload time: " + ztex.eepromUpload(ihxFile, forceUpload) + " ms"
                elif args[i] == "-rm":
                    print "First free sector: " + ztex.flashFirstFreeSector()
                    ztex.flashResetBitstream()
                    print "First free sector: " + ztex.flashFirstFreeSector()
                elif args[i] == "-um":
                    i += 1
                    if len(args):
                        System.err.println("Error: Filename expected after -uf")
                        System.err.println(helpMsg)
                        System.exit(1)
                    print "First free sector: " + ztex.flashFirstFreeSector()
                    print "FPGA configuration time: " + ztex.flashUploadBitstream(args[i], bs) + " ms"
                    print "First free sector: " + ztex.flashFirstFreeSector()
                elif args[i] == "-uxf":
                    i += 1
                    if len(args):
                        System.err.println("Error: Filename expected after -uxf")
                        System.err.println(helpMsg)
                        System.exit(1)
                    print "Firmware to ATxmega Flash upload time: " + ztex.xmegaWriteFirmware(IhxFile(args[i])) + " ms"
                elif args[i] == "-uxe":
                    i += 1
                    if len(args):
                        System.err.println("Error: Filename expected after -uxe")
                        System.err.println(helpMsg)
                        System.exit(1)
                    print "Firmware to ATxmega Flash upload time: " + ztex.xmegaWriteEeprom(IhxFile(args[i])) + " ms"
                elif args[i] == "-rxf":
                    i += 1
                    try:
                        if len(args):
                            raise Exception()
                        j = Integer.parseInt(args[i])
                    except Exception as e:
                        System.err.println("Error: Index number expected after -rxf")
                        System.err.println(helpMsg)
                        System.exit(1)
                    print "Fuse " + j + ": 0b" + Integer.toBinaryString(256 | ztex.xmegaFuseRead(j)).substring(1)
                elif args[i] == "-wxf":
                    i += 1
                    try:
                        if len(args):
                            raise Exception()
                        j = Integer.parseInt(args[i])
                    except Exception as e:
                        System.err.println("Error: Index number expected after -wxf")
                        System.err.println(helpMsg)
                        System.exit(1)
                    i += 1
                    try:
                        if len(args):
                            raise Exception()
                        k = Integer.parseInt(args[i])
                    except Exception as e:
                        System.err.println("Error: Bitmask expected after -wxf <index>")
                        System.err.println(helpMsg)
                        System.exit(1)
                    i += 1
                    try:
                        if len(args):
                            raise Exception()
                        l = Integer.parseInt(args[i])
                    except Exception as e:
                        System.err.println("Error: Value expected after -wxf <index> <bitmask>")
                        System.err.println(helpMsg)
                        System.exit(1)
                    ztex.xmegaFuseWrite(j, (ztex.xmegaFuseRead(j) & ~k) | l)
                i += 1
        except Exception as e:
            print "Error: " + e.getLocalizedMessage()


if __name__ == '__main__':
    import sys
    FWLoader.main(sys.argv)

