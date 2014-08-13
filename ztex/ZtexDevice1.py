#!/usr/bin/env python
""" generated source for module ZtexDevice1 """
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
#  USB device with ZTEX descriptor 1 and/or Cypress EZ-USB FX2 device
#
# package: ztex

cypressVendorId = 0x4b4

#  * EZ-USB USB product ID: 0x8613
cypressProductId = 0x8613

#  * ZTEX vendor ID: 0x221a
ztexVendorId = 0x221A

#
#      * USB product ID for ZTEX devices that support ZTEX descriptor 1: 0x100.
#      * This product ID is intended for general purpose use and can be shared by all devices that base on ZTEX modules.
#      * Different products are identified by a second product ID, namely the PRODUCT_ID field of the <a href="#descriptor"> ZTEX descriptor 1</a>.
#      * <p>
#      * Please read the <a href="http://www.ztex.de/firmware-kit/usb_ids.e.html">informations about USB vendor and product ID's<a>.
#      * @see #ztexProductIdMax
#
ztexProductId = 0x100

class ZtexDevice1(object):
    """ generated source for class ZtexDevice1 """
    #  * Cypress vendor ID: 0x4b4
    cypressVendorId = 0x4b4

    #  * EZ-USB USB product ID: 0x8613
    cypressProductId = 0x8613

    #  * ZTEX vendor ID: 0x221a
    ztexVendorId = 0x221A

    #
    #      * USB product ID for ZTEX devices that support ZTEX descriptor 1: 0x100.
    #      * This product ID is intended for general purpose use and can be shared by all devices that base on ZTEX modules.
    #      * Different products are identified by a second product ID, namely the PRODUCT_ID field of the <a href="#descriptor"> ZTEX descriptor 1</a>.
    #      * <p>
    #      * Please read the <a href="http://www.ztex.de/firmware-kit/usb_ids.e.html">informations about USB vendor and product ID's<a>.
    #      * @see #ztexProductIdMax
    #
    ztexProductId = 0x100

    #
    #      * Largest USB product ID for ZTEX devices that support ZTEX descriptor 1: 0x1ff.
    #      * USB product ID's from {@link #ztexProductId}+1 to ztexProductIdMax (0x101 to 0x1ff) are reserved for ZTEX devices and allow to identify products without reading the ZTEX descriptor.
    #      * <p>
    #      * Please read the <a href="http://www.ztex.de/firmware-kit/usb_ids.e.html">informations about USB vendor and product ID's<a>.
    #      * @see #ztexProductId
    #
    ztexProductIdMax = 0x1ff
    dev = None
    valid = False

    #  true if descriptor 1 is available
    usbVendorId = -1
    usbProductId = -1
    manufacturerString = None
    productString = None
    snString = None
    productId = [0, 0, 0, 0]

    #  product ID from the ZTEX descriptor, not the USB product ID
    fwVersion = 0
    interfaceVersion = 0
    interfaceCapabilities = [0, 0, 0, 0, 0, 0]
    moduleReserved = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #  ******* byteArrayString *****************************************************
    #
    #      * Produces a nice string representation of an array of bytes.
    #      * @param buf A byte array.
    #      * @return a nice string
    #
    @classmethod
    def byteArrayString(cls, buf):
        """ generated source for method byteArrayString """
        s = str("")
        i = 0
        while len(buf):
            if i != 0:
                s += "."
            s += buf[i] & 255
            i += 1
        return s

    #  ******* ZtexDevice1 *********************************************************
    #
    #      * Constructs an instance from a given USB device.<br>
    #      * If the given vendor and product id's match to the vendor and product id's of the given USB device,
    #      * the ZTEX descriptor 1 is attempted to read. If this fails, an {@link InvalidFirmwareException} is thrown.
    #      * To suppress this behavior (e.g. if the EZ-USB device is known to be unconfigured) the vendor and product id's
    #      * can be set to -1.
    #      * @param p_dev The USB device.
    #      * @param pUsbVendorId The given vendor ID.
    #      * @param pUsbProductId The given product ID.
    #      * @param allowUnconfigured If true, unconfigured devices are allowed.
    #      * @throws UsbException if an USB communication error occurs.
    #      * @throws InvalidFirmwareException if no valid ZTEX descriptor 1 is found.
    #      * @throws DeviceNotSupported if the device has the wrong USB ID's.
    #
    def __init__(self, p_dev, pUsbVendorId, pUsbProductId, allowUnconfigured):
        """ generated source for method __init__ """
        self.dev = p_dev
        dd = self.dev().getDescriptor()
        self.usbVendorId = dd.getIdVendor() & 65535
        self.usbProductId = dd.getIdProduct() & 65535
        if not (((self.usbVendorId == pUsbVendorId) and (self.usbProductId == pUsbProductId or (self.usbVendorId == self.ztexVendorId and pUsbProductId < 0 and self.usbProductId >= self.ztexProductId and self.usbProductId < self.ztexProductIdMax))) or (allowUnconfigured and (self.usbVendorId == self.cypressVendorId) and (self.usbProductId == self.cypressProductId))):
            raise DeviceNotSupportedException(p_dev)
        handle = LibusbJava.usb_open(self.dev)
        #  if ( handle > 0 ) {
        if dd.getIManufacturer() > 0:
            self.manufacturerString = LibusbJava.usb_get_string_simple(handle, dd.getIManufacturer())
        if dd.getIProduct() > 0:
            self.productString = LibusbJava.usb_get_string_simple(handle, dd.getIProduct())
        if dd.getISerialNumber() > 0:
            self.snString = LibusbJava.usb_get_string_simple(handle, dd.getISerialNumber())
        if self.snString == None:
            LibusbJava.usb_close(handle)
            if allowUnconfigured:
                return
            else:
                raise InvalidFirmwareException(self.dev, "Not a ZTEX device")
            #  ZTEX devices always have a SN. See also the next comment a few lines below
        buf = [None]*42
        i = LibusbJava.usb_control_msg(handle, 0xc0, 0x22, 0, 0, buf, 40, 500)
        #  Failing of this may cause problems under windows. Therefore we check for the SN above.
        if i < 0:
            LibusbJava.usb_close(handle)
            if allowUnconfigured:
                return
            else:
                raise InvalidFirmwareException(self.dev, "Error reading ZTEX descriptor: " + LibusbJava.usb_strerror())
        elif i != 40:
            LibusbJava.usb_close(handle)
            if allowUnconfigured:
                return
            else:
                raise InvalidFirmwareException(self.dev, "Error reading ZTEX descriptor: Invalid size: " + i)
        if buf[0] != 40 or buf[1] != 1 or buf[2] != 'Z' or buf[3] != 'T' or buf[4] != 'E' or buf[5] != 'X':
            LibusbJava.usb_close(handle)
            if allowUnconfigured:
                return
            else:
                raise InvalidFirmwareException(self.dev, "Invalid ZTEX descriptor")
        self.productId[0] = buf[6]
        self.productId[1] = buf[7]
        self.productId[2] = buf[8]
        self.productId[3] = buf[9]
        self.fwVersion = buf[10]
        self.interfaceVersion = buf[11]
        self.interfaceCapabilities[0] = buf[12]
        self.interfaceCapabilities[1] = buf[13]
        self.interfaceCapabilities[2] = buf[14]
        self.interfaceCapabilities[3] = buf[15]
        self.interfaceCapabilities[4] = buf[16]
        self.interfaceCapabilities[5] = buf[17]
        self.moduleReserved[0] = buf[18]
        self.moduleReserved[1] = buf[19]
        self.moduleReserved[2] = buf[20]
        self.moduleReserved[3] = buf[21]
        self.moduleReserved[4] = buf[22]
        self.moduleReserved[5] = buf[23]
        self.moduleReserved[6] = buf[24]
        self.moduleReserved[7] = buf[25]
        self.moduleReserved[8] = buf[26]
        self.moduleReserved[9] = buf[27]
        self.moduleReserved[10] = buf[28]
        self.moduleReserved[11] = buf[29]
        self.valid = True
        #  }
        #  else {
        #  throw new UsbException( dev, "Error opening device: " + LibusbJava.usb_strerror() );
        #  }
        LibusbJava.usb_close(handle)

    #  ******* toString ************************************************************
    #
    #      * Returns a string representation if the device with a lot of useful information.
    #      * @return a string representation if the device with a lot of useful information.
    #
    def __str__(self):
        """ generated source for method toString """
        return "bus=" + self.dev().getBus().getDirname() + "  device=" + self.dev().getDevnum() + " (`" + self.dev().getFilename() + "')  ID=" + Integer.toHexString(self.usbVendorId) + ":" + Integer.toHexString(self.usbProductId) + "\n" + ("" if self.manufacturerString == None else ("   Manufacturer=\"" + self.manufacturerString + "\"")) + ("" if self.productString == None else ("  Product=\"" + self.productString + "\"")) + ("" if self.snString == None else ("    SerialNumber=\"" + self.snString + "\"")) + ("\n   productID=" + self.byteArrayString(self.productId) + "  fwVer=" + (self.fwVersion & 255) + "  ifVer=" + (self.interfaceVersion & 255) if self.valid else "")

    def compatible(self, productId0, productId1, productId2, productId3):
        """ generated source for method compatible """
        return (self.productId[0] == 0 or productId0 <= 0 or (self.productId[0] & 255) == productId0) and (self.productId[1] == 0 or productId1 <= 0 or (self.productId[1] & 255) == productId1) and (self.productId[2] == 0 or productId2 <= 0 or (self.productId[2] & 255) == productId2) and (self.productId[3] == 0 or productId3 <= 0 or (self.productId[3] & 255) == productId3)

    def dev(self):
        """ generated source for method dev """
        return self.dev

    def valid(self):
        """ generated source for method valid """
        return self.valid

    def usbVendorId(self):
        """ generated source for method usbVendorId """
        return self.usbVendorId

    def usbProductId(self):
        """ generated source for method usbProductId """
        return self.usbProductId

    def manufacturerString(self):
        """ generated source for method manufacturerString """
        return self.manufacturerString

    def productString(self):
        """ generated source for method productString """
        return self.productString

    def snString(self):
        """ generated source for method snString """
        return self.snString

    @overloaded
    def productId(self):
        """ generated source for method productId """
        return self.productId

    @productId.register(object, int)
    def productId_0(self, i):
        """ generated source for method productId_0 """
        return self.productId[i] & 255

    def fwVersion(self):
        """ generated source for method fwVersion """
        return self.fwVersion & 255

    def interfaceVersion(self):
        """ generated source for method interfaceVersion """
        return self.interfaceVersion & 255

    @overloaded
    def interfaceCapabilities(self):
        """ generated source for method interfaceCapabilities """
        return self.interfaceCapabilities

    @interfaceCapabilities.register(object, int)
    def interfaceCapabilities_0(self, i):
        """ generated source for method interfaceCapabilities_0 """
        return self.interfaceCapabilities[i] & 255

    @interfaceCapabilities.register(object, int, int)
    def interfaceCapabilities_1(self, i, j):
        """ generated source for method interfaceCapabilities_1 """
        return (i >= 0) and (i <= 5) and (j >= 0) and (j < 8) and (((self.interfaceCapabilities[i] & 255) & (1 << j)) != 0)

    @overloaded
    def moduleReserved(self):
        """ generated source for method moduleReserved """
        return self.moduleReserved

    @moduleReserved.register(object, int)
    def moduleReserved_0(self, i):
        """ generated source for method moduleReserved_0 """
        return self.moduleReserved[i] & 255

