#!/usr/bin/env python
""" generated source for module ZtexIhxFile1 """
#  !
#  Java host software API of ZTEX EZ-USB FX2 SDK
#  Copyright (C) 2009-2011 ZTEX GmbH.
#  http://www.ztex.de
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 3 as
#  published by the Free Software Foundation.
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see http://www.gnu.org/licenses/.
#  !
# 
#  Reads an ihx file with ZTEX descriptor 1
#  
# package: ztex
import java.io

import java.util

# 
#  * Represents a firmware image with ZTEX descriptor 1 loaded from an ihx (Intel Hex format) file. <br>
#  * The ZTEX descriptor is usually located at the position 0x6x of the firmware image. <br>
#  * A description of the ZTEX descriptor 1 can be found in {@link ZtexDevice1}.
#  * @see ZtexDevice1
#  * @see Ztex1
#  
class ZtexIhxFile1(IhxFile):
    """ generated source for class ZtexIhxFile1 """
    defaultZtexDescriptorOffs = 0x6c
    ztexDescriptorOffs = defaultZtexDescriptorOffs
    productId = [0, 0, 0, 0]

    #  product ID from the ZTEX descriptor, not the USB product ID
    fwVersion = 0
    interfaceVersion = 0
    interfaceCapabilities = [0, 0, 0, 0, 0, 0]
    moduleReserved = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    snString = [None]*10

    #  ******* ZtexIhxFile1 ********************************************************
    # 
    #      * Constructs an instance from a given file name and descriptor position.<br>
    #      * This method can also read system resources, e.g. files from the current jar archive.
    #      * @param fileName The file name.
    #      * @param pZtexDescriptorOffs The position of the descriptor in bytes. The default position is 0x6c.
    #      * @throws IOException If an read error occurred.
    #      * @throws IhxFileDamagedException If the ihx file is damaged.
    #      * @throws IncompatibleFirmwareException If the firmware image contains no valid ZTEX descriptor 1 at the specified position.
    #      
    @overloaded
    def __init__(self, fileName, pZtexDescriptorOffs):
        """ generated source for method __init__ """
        super(ZtexIhxFile1, self).__init__(fileName)
        self.ztexDescriptorOffs = pZtexDescriptorOffs
        if ihxData[self.ztexDescriptorOffs] != 40 or ihxData[self.ztexDescriptorOffs + 1] != 1 or ihxData[self.ztexDescriptorOffs + 2] != 'Z' or ihxData[self.ztexDescriptorOffs + 3] != 'T' or ihxData[self.ztexDescriptorOffs + 4] != 'E' or ihxData[self.ztexDescriptorOffs + 5] != 'X':
            raise IncompatibleFirmwareException("Invalid ZTEX descriptor")
        self.productId[0] = int(ihxData[self.ztexDescriptorOffs + 6])
        self.productId[1] = int(ihxData[self.ztexDescriptorOffs + 7])
        self.productId[2] = int(ihxData[self.ztexDescriptorOffs + 8])
        self.productId[3] = int(ihxData[self.ztexDescriptorOffs + 9])
        self.fwVersion = int(ihxData[self.ztexDescriptorOffs + 10])
        self.interfaceVersion = int(ihxData[self.ztexDescriptorOffs + 11])
        self.interfaceCapabilities[0] = int(ihxData[self.ztexDescriptorOffs + 12])
        self.interfaceCapabilities[1] = int(ihxData[self.ztexDescriptorOffs + 13])
        self.interfaceCapabilities[2] = int(ihxData[self.ztexDescriptorOffs + 14])
        self.interfaceCapabilities[3] = int(ihxData[self.ztexDescriptorOffs + 15])
        self.interfaceCapabilities[4] = int(ihxData[self.ztexDescriptorOffs + 16])
        self.interfaceCapabilities[5] = int(ihxData[self.ztexDescriptorOffs + 17])
        self.moduleReserved[0] = int(ihxData[self.ztexDescriptorOffs + 18])
        self.moduleReserved[1] = int(ihxData[self.ztexDescriptorOffs + 19])
        self.moduleReserved[2] = int(ihxData[self.ztexDescriptorOffs + 20])
        self.moduleReserved[3] = int(ihxData[self.ztexDescriptorOffs + 21])
        self.moduleReserved[4] = int(ihxData[self.ztexDescriptorOffs + 22])
        self.moduleReserved[5] = int(ihxData[self.ztexDescriptorOffs + 23])
        self.moduleReserved[6] = int(ihxData[self.ztexDescriptorOffs + 24])
        self.moduleReserved[7] = int(ihxData[self.ztexDescriptorOffs + 25])
        self.moduleReserved[8] = int(ihxData[self.ztexDescriptorOffs + 26])
        self.moduleReserved[9] = int(ihxData[self.ztexDescriptorOffs + 27])
        self.moduleReserved[10] = int(ihxData[self.ztexDescriptorOffs + 28])
        self.moduleReserved[11] = int(ihxData[self.ztexDescriptorOffs + 29])
        i = 0
        while i < 10:
            if b >= 0 and b <= 255:
                self.snString[i] = str(b)
            else:
                raise IncompatibleFirmwareException("Invalid serial number string")
            i += 1
        #  ensure word aligned upload data
        i = 0
        while len(ihxData):
            if ihxData[i] < 0 and ihxData[i + 1] >= 0:
                ihxData[i] = 0
            i += 2

    # 
    #      * Constructs an instance from a given file name.
    #      * The ZTEX descriptor 1 is expected to be at the position 0x6c of the firmware image.<br>
    #      * This method can also read system resources, e.g. files from the current jar archive.
    #      * @param fileName The file name.
    #      * @throws IOException If an read error occurred.
    #      * @throws IhxFileDamagedException If the ihx file is damaged.
    #      * @throws IncompatibleFirmwareException If the firmware image contains no valid ZTEX descriptor 1 at the specified position.
    #      
    @__init__.register(object, str)
    def __init___0(self, fileName):
        """ generated source for method __init___0 """
        super(ZtexIhxFile1, self).__init__()
        self.__init__(fileName, self.defaultZtexDescriptorOffs)

    #  ******* productId ***********************************************************
    # 
    #      * Returns the product ID (all 4 bytes).
    #      * @return PRODUCT_ID, see {@link ZtexDevice1}.
    #      
    @overloaded
    def productId(self):
        """ generated source for method productId """
        return self.productId

    # 
    #      * Returns byte i of the product ID.
    #      * @return PRODUCT_ID[i], see {@link ZtexDevice1}.
    #      * @param i index 
    #      
    @productId.register(object, int)
    def productId_0(self, i):
        """ generated source for method productId_0 """
        return self.productId[i] & 255

    #  ******* fwVersion ***********************************************************
    # 
    #      * Returns the firmware version.
    #      * @return FW_VERSION, see {@link ZtexDevice1}.
    #      
    def fwVersion(self):
        """ generated source for method fwVersion """
        return self.fwVersion & 255

    #  ******* interfaceVersion *****************************************************
    # 
    #      * Returns the interface version.
    #      * @return INTERFACE_VERSION, see {@link ZtexDevice1}.
    #      
    def interfaceVersion(self):
        """ generated source for method interfaceVersion """
        return self.interfaceVersion & 255

    #  ******* interfaceCapabilities ************************************************
    # 
    #      * Returns the interface capabilities (all 6 bytes).
    #      * @return INTERFACE_CAPABILITIES, see {@link ZtexDevice1}.
    #      
    @overloaded
    def interfaceCapabilities(self):
        """ generated source for method interfaceCapabilities """
        return self.interfaceCapabilities

    # 
    #      * Returns byte i of the interface capabilities.
    #      * @return INTERFACE_CAPABILITIES[i], see {@link ZtexDevice1}.
    #      * @param i index 
    #      
    @interfaceCapabilities.register(object, int)
    def interfaceCapabilities_0(self, i):
        """ generated source for method interfaceCapabilities_0 """
        return self.interfaceCapabilities[i] & 255

    #  ******* moduleReserved ******************************************************
    # 
    #      * Returns the application specific information (all 12 bytes).
    #      * @return MODULE_RESERVED, see {@link ZtexDevice1}.
    #      
    @overloaded
    def moduleReserved(self):
        """ generated source for method moduleReserved """
        return self.moduleReserved

    # 
    #      * Returns byte i of the application specific information.
    #      * @return MODULE_RESERVED[i], see {@link ZtexDevice1}.
    #      * @param i index 
    #      
    @moduleReserved.register(object, int)
    def moduleReserved_0(self, i):
        """ generated source for method moduleReserved_0 """
        return self.moduleReserved[i] & 255

    #  ******* snString ************************************************************
    # 
    #      * Returns the serial number string.
    #      * @return SN_STRING, see {@link ZtexDevice1}.
    #      
    def snString(self):
        """ generated source for method snString """
        return str(self.snString)

    #  ******* setSnString **********************************************************
    # 
    #      * Modifies the serial number string. 
    #      * @param s The new serial number string which must not be longer then 10 characters. 
    #      
    def setSnString(self, s):
        """ generated source for method setSnString """
        if 10 > len(s):
            raise IncompatibleFirmwareException("Serial number too long (max. 10 characters)")
        i = 0
        while i < len(s):
            ihxData[self.ztexDescriptorOffs + 30 + i] = int(s.charAt(i))
            i += 1
        while i < 10:
            ihxData[self.ztexDescriptorOffs + 30 + i] = 0
            i += 1

    #  ******* toString ************************************************************
    # 
    #      * Returns a string representation if the instance.
    #      * @return a string representation if the instance.
    #      
    def __str__(self):
        """ generated source for method toString """
        return "productID=" + ZtexDevice1.byteArrayString(self.productId) + "  fwVer=" + (self.fwVersion & 255) + "  ifVer=" + (self.interfaceVersion & 255) + "  snString=\"" + self.snString() + "\""

