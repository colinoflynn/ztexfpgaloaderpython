#!/usr/bin/env python
""" generated source for module Ztex1 """
from threading import RLock

_locks = {}
def lock_for_object(obj, locks=_locks):
    return locks.setdefault(id(obj), RLock())


def synchronized(call):
    def inner(*args, **kwds):
        with lock_for_object(call):
            return call(*args, **kwds)
    return inner

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
#  Functions for USB devices with ZTEX descriptor 1
#  
# package: ztex
import java.io

import java.util

import ch.ntb.usb

# 
#  * This class implements the interface-independent part of the communication protocol for the interaction with the ZTEX firmware.<p>
#  * All firmware implementations that provide the ZTEX descriptor 1 are supported.
#  * A description of this descriptor can be found in {@link ZtexDevice1}.
#  * <p>
#  * The most important features of this class are the functions for uploading the firmware
#  * and the renumeration management.
#  * <p>
#  * The interface dependent part of the communication protocol (currently only one is supported)
#  * can be found in {@link Ztex1v1}.
#  * @see ZtexDevice1
#  * @see Ztex1v1
#  
class Ztex1(object):
    """ generated source for class Ztex1 """
    maxDevNum = 1023
    handle = long()
    dev = None
    oldDevices = [None]*maxDevNum + 1
    oldDevNum = -1
    usbBusName = None
    interfaceClaimed = [None]*256
    configurationSet = False

    #  * Setting to true enables certain workarounds, e.g. to deal with bad driver/OS implementations. 
    certainWorkarounds = False

    #  * The timeout for  control messages in ms. 
    controlMsgTimeout = 1000

    #  in ms
    lastVendorCommandT = 0

    #  ******* Ztex1 ***************************************************************
    # 
    #      * Constructs an instance from a given device.
    #      * @param pDev The given device.
    #      * @throws UsbException if an communication error occurred.
    #      
    def __init__(self, pDev):
        """ generated source for method __init__ """
        self.dev = pDev
        i = 0
        while i < 256:
            self.interfaceClaimed[i] = False
            i += 1
        self.handle = LibusbJava.usb_open(self.dev.dev())
        #  if ( handle<=0 ) 
        #  throw new UsbException(dev.dev(), "Error opening device");

    #  ******* finalize ************************************************************
    #  * The destructor closes the USB file handle. 
    def finalize(self):
        """ generated source for method finalize """
        i = 0
        while i < 256:
            if self.interfaceClaimed[i]:
                LibusbJava.usb_release_interface(self.handle, i)
            i += 1
        LibusbJava.usb_close(self.handle)

    #  ******* handle **************************************************************
    #  * Returns the USB file handle. 
    def handle(self):
        """ generated source for method handle """
        return self.handle

    #  ******* dev *****************************************************************
    # 
    #      * Returns the corresponding {@link ZtexDevice1}. 
    #      * @return the corresponding {@link ZtexDevice1}. 
    #      
    def dev(self):
        """ generated source for method dev """
        return self.dev

    #  ******* valid ***************************************************************
    # 
    #      * Returns true if ZTEX descriptor 1 is available.
    #      * @return true if ZTEX descriptor 1 is available.
    #      
    def valid(self):
        """ generated source for method valid """
        return self.dev.valid()

    #  ******* checkValid **********************************************************
    # 
    #      * Checks whether ZTEX descriptor 1 is available.
    #      * @throws InvalidFirmwareException if ZTEX descriptor 1 is not available.
    #      
    def checkValid(self):
        """ generated source for method checkValid """
        if not self.dev.valid():
            raise InvalidFirmwareException(self, "Can't read ZTEX descriptor 1")

    #  ******* vendorCommand *******************************************************
    # 
    #      * Sends a vendor command to Endpoint 0 of the EZ-USB device.
    #      * The command may be send multiple times until the {@link #controlMsgTimeout} is reached.
    #      * @param cmd The command number (0..255).
    #      * @param func The name of the command. This string is used for the generation of error messages.
    #      * @param value The value (0..65535), i.e bytes 2 and 3 of the setup data.
    #      * @param index The index (0..65535), i.e. bytes 4 and 5 of the setup data.
    #      * @param length The size of the payload data (0..65535), i.e. bytes 6 and 7 of the setup data.
    #      * @param buf The payload data buffer.
    #      * @return the number of bytes sent.
    #      * @throws UsbException if a communication error occurs.
    #      
    @synchronized
    @overloaded
    def vendorCommand(self, cmd, func, value, index, buf, length):
        """ generated source for method vendorCommand """
        t0 = Date().getTime() - 100
        trynum = 0
        i = -1
        if self.controlMsgTimeout < 200:
            self.controlMsgTimeout = 200
        #  while ( i<=0 && new Date().getTime()-t0<controlMsgTimeout ) {		// we repeat the message until the timeout has reached
        i = LibusbJava.usb_control_msg(self.handle, 0x40, cmd, value, index, buf, length, self.controlMsgTimeout)
        if self.certainWorkarounds:
            try:
                Thread.sleep(2)
            except InterruptedException as e:
                pass
        self.lastVendorCommandT = Date().getTime()
        if i < 0:
            System.err.println("Warning (try " + (trynum + 1) + "): " + LibusbJava.usb_strerror())
            try:
                Thread.sleep(1 << trynum)
                #  we don't want to bother the USB device to often
            except InterruptedException as e:
                pass
            trynum += 1
        #  } 
        if i < 0:
            raise UsbException(self.dev.dev(), (func + ": " if func != None else "") + LibusbJava.usb_strerror())
        return i

    # 
    #      * Sends a vendor command with no payload data to Endpoint 0 of the EZ-USB device.
    #      * The command may be send multiple times until the {@link #controlMsgTimeout} is reached.
    #      * @param cmd The command number (0..255).
    #      * @param func The name of the command. This string is used for the generation of error messages.
    #      * @param value The value (0..65535), i.e bytes 2 and 3 of the setup data.
    #      * @param index The index (0..65535), i.e. bytes 4 and 5 of the setup data.
    #      * @return the number of bytes sent.
    #      * @throws UsbException if a communication error occurs.
    #      
    @vendorCommand.register(object, int, str, int, int)
    def vendorCommand_0(self, cmd, func, value, index):
        """ generated source for method vendorCommand_0 """
        buf = [0]
        return self.vendorCommand(cmd, func, value, index, buf, 0)

    # 
    #      * Sends a vendor command with no payload data and no setup data to Endpoint 0 of the EZ-USB device.
    #      * The command may be send multiple times until the {@link #controlMsgTimeout} is reached.
    #      * @param cmd The command number (0..255).
    #      * @param func The name of the command. This string is used for the generation of error messages.
    #      * @return the number of bytes sent.
    #      * @throws UsbException if a communication error occurs.
    #      
    @vendorCommand.register(object, int, str)
    def vendorCommand_1(self, cmd, func):
        """ generated source for method vendorCommand_1 """
        buf = [0]
        return self.vendorCommand(cmd, func, 0, 0, buf, 0)

    #  ******* vendorRequest *******************************************************
    # 
    #      * Sends a vendor request to Endpoint 0 of the EZ-USB device.
    #      * The request may be send multiple times until the {@link #controlMsgTimeout} is reached.
    #      * @param cmd The request number (0..255).
    #      * @param func The name of the request. This string is used for the generation of error messages.
    #      * @param value The value (0..65535), i.e bytes 2 and 3 of the setup data.
    #      * @param index The index (0..65535), i.e. bytes 4 and 5 of the setup data.
    #      * @param maxlen The size of the requested payload data (0..65535), i.e. bytes 6 and 7 of the setup data.
    #      * @param buf The payload data buffer.
    #      * @return the number of bytes received.
    #      * @throws UsbException if a communication error occurs.
    #      
    @synchronized
    @overloaded
    def vendorRequest(self, cmd, func, value, index, buf, maxlen):
        """ generated source for method vendorRequest """
        t0 = Date().getTime() - 100
        trynum = 0
        i = -1
        if self.controlMsgTimeout < 200:
            self.controlMsgTimeout = 200
        while i <= 0 and Date().getTime() - t0 < self.controlMsgTimeout:
            #  we repeat the message until the timeout has reached
            # 
            #              The HSNAK mechanism of EP0 usually avoids that a request is sent before a command has been completed.
            #              Unfortunately this mechanism is only 99.99% reliable. Therefore we wait at least 1ms after the last
            #              command has been send before we transmit a new request.
            #              
            if ms < 2:
                # 
                try:
                    Thread.sleep(1)
                except InterruptedException as e:
                    pass
            i = LibusbJava.usb_control_msg(self.handle, 0xc0, cmd, value, index, buf, maxlen, self.controlMsgTimeout)
            if self.certainWorkarounds:
                try:
                    Thread.sleep(2)
                except InterruptedException as e:
                    pass
            if i < 0:
                System.err.println("Warning (try " + (trynum + 1) + "): " + LibusbJava.usb_strerror())
                try:
                    Thread.sleep(1 << trynum)
                    #  we don't want to bother the USB device to often
                except InterruptedException as e:
                    pass
                trynum += 1
        if i < 0:
            raise UsbException(self.dev.dev(), (func + ": " if func != None else "") + LibusbJava.usb_strerror())
        return i

    # 
    #      * Sends a vendor request to Endpoint 0 of the EZ-USB device.
    #      * The request may be send multiple times until the {@link #controlMsgTimeout} is reached.
    #      * @param cmd The request number (0..255).
    #      * @param func The name of the request. This string is used for the generation of error messages.
    #      * @param maxlen The size of the requested payload data (0..65535), i.e. bytes 6 and 7 of the setup data.
    #      * @param buf The payload data buffer.
    #      * @return the number of bytes sent.
    #      * @throws UsbException if a communication error occurs.
    #      
    @vendorRequest.register(object, int, str, int, int)
    def vendorRequest_0(self, cmd, func, buf, maxlen):
        """ generated source for method vendorRequest_0 """
        return self.vendorRequest(cmd, func, 0, 0, buf, maxlen)

    #  ******* vendorCommand2 ******************************************************
    # 
    #      * Sends a vendor command to Endpoint 0 of the EZ-USB device and throws an {@link UsbException} if not all of the payload has been sent.
    #      * The command may be send multiple times until the {@link #controlMsgTimeout} is reached.
    #      * @param cmd The command number (0..255).
    #      * @param func The name of the command. This string is used for the generation of error messages.
    #      * @param value The value (0..65535), i.e bytes 2 and 3 of the setup data.
    #      * @param index The index (0..65535), i.e. bytes 4 and 5 of the setup data.
    #      * @param length The size of the payload data (0..65535), i.e. bytes 6 and 7 of the setup data.
    #      * @param buf The payload data buffer.
    #      * @throws UsbException if a communication error occurs or if not all of the payload has been sent.
    #      
    @synchronized
    def vendorCommand2(self, cmd, func, value, index, buf, length):
        """ generated source for method vendorCommand2 """
        i = self.vendorCommand(cmd, func, value, index, buf, length)
        if i != length:
            raise UsbException(self.dev.dev(), (func + ": " if func != None else "") + "Send " + i + " byte of data instead of " + length + " bytes")

    #  ******* vendorRequest2 ******************************************************
    # 
    #      * Sends a vendor request to Endpoint 0 of the EZ-USB device and throws an {@link UsbException} if not all of the payload has been received.
    #      * The request may be send multiple times until the {@link #controlMsgTimeout} is reached.
    #      * @param cmd The request number (0..255).
    #      * @param func The name of the request. This string is used for the generation of error messages.
    #      * @param value The value (0..65535), i.e bytes 2 and 3 of the setup data.
    #      * @param index The index (0..65535), i.e. bytes 4 and 5 of the setup data.
    #      * @param maxlen The size of the requested payload data (0..65535), i.e. bytes 6 and 7 of the setup data.
    #      * @param buf The payload data buffer.
    #      * @throws UsbException if a communication error occurs or not all of the payload has been received.
    #      
    @overloaded
    def vendorRequest2(self, cmd, func, value, index, buf, maxlen):
        """ generated source for method vendorRequest2 """
        i = self.vendorRequest(cmd, func, value, index, buf, maxlen)
        if i != maxlen:
            raise UsbException(self.dev.dev(), (func + ": " if func != None else "") + "Received " + i + " byte of data, expected " + maxlen + " bytes")

    # 
    #      * Sends a vendor request to Endpoint 0 of the EZ-USB device and throws an {@link UsbException} if not all of the payload has been received.
    #      * The request may be send multiple times until the {@link #controlMsgTimeout} is reached.
    #      * @param cmd The request number (0..255).
    #      * @param func The name of the request. This string is used for the generation of error messages.
    #      * @param maxlen The size of the requested payload data (0..65535), i.e. bytes 6 and 7 of the setup data.
    #      * @param buf The payload data buffer.
    #      * @throws UsbException if a communication error occurs or not all of the payload has been received.
    #      
    @vendorRequest2.register(object, int, str, int, int)
    def vendorRequest2_0(self, cmd, func, buf, maxlen):
        """ generated source for method vendorRequest2_0 """
        self.vendorRequest2(cmd, func, 0, 0, buf, maxlen)

    #  ******* setConfiguration ****************************************************
    # 
    #      * Sets the configuration.
    #      * @param config The configuration number (usually 1)
    #      * @throws UsbException if an error occurs while attempting to set the configuration.
    #      
    def setConfiguration(self, config):
        """ generated source for method setConfiguration """
        if LibusbJava.usb_set_configuration(self.handle(), config) < 0:
            raise UsbException("Setting configuration to " + config + " failed: " + LibusbJava.usb_strerror())
        self.configurationSet = True

    #  ******* trySetConfiguration ****************************************************
    # 
    #      * Tries to set the configuration.
    #      * If an error occurs while attempting to set the configuration, a warning messaage is printed to stderr.
    #      * @param config The configuration number (usually 1)
    #      
    def trySetConfiguration(self, config):
        """ generated source for method trySetConfiguration """
        if LibusbJava.usb_set_configuration(self.handle(), config) < 0:
            System.err.println("Setting configuration to " + config + " failed: " + LibusbJava.usb_strerror())
        self.configurationSet = True

    #  ******* getInterfaceClaimed *************************************************
    # 
    #      * Returns true if interface is claimed.
    #      * @return true if interface is claimed
    #      * @param iface The interface number
    #      
    def getInterfaceClaimed(self, iface):
        """ generated source for method getInterfaceClaimed """
        return iface >= 0 and iface < 256 and self.interfaceClaimed[iface]

    #  ******* claimInterface ******************************************************
    # 
    #      * Claims an interface.
    #      * @param iface The interface number (usually 0)
    #      * @throws UsbException if an error occurs while attempting to claim the interface.
    #      
    def claimInterface(self, iface):
        """ generated source for method claimInterface """
        if not self.configurationSet:
            self.trySetConfiguration(1)
        if (iface < 0 or iface >= 256 or (not self.interfaceClaimed[iface])) and (LibusbJava.usb_claim_interface(self.handle(), iface) < 0):
            raise UsbException("Claiming interface " + iface + " failed: " + LibusbJava.usb_strerror())
        if iface >= 0 and iface < 256:
            self.interfaceClaimed[iface] = True

    #  ******* releaseInterface ****************************************************
    # 
    #      * Releases an interface.
    #      * @param iface The interface number (usually 0)
    #      
    def releaseInterface(self, iface):
        """ generated source for method releaseInterface """
        if iface < 0 or iface >= 256 or self.interfaceClaimed[iface]:
            LibusbJava.usb_release_interface(self.handle(), iface)
        if iface >= 0 and iface < 256:
            self.interfaceClaimed[iface] = False

    #  ******* findOldDevices ******************************************************
    @synchronized
    def findOldDevices(self):
        """ generated source for method findOldDevices """
        self.usbBusName = self.dev.dev().getBus().getDirname()
        bus = LibusbJava.usb_get_busses()
        while bus != None and not bus.getDirname() == self.usbBusName:
            bus = bus.getNext()
        if bus == None:
            raise DeviceLostException("findOldDevice: Bus dissapeared")
        i = 0
        while i <= self.maxDevNum:
            self.oldDevices[i] = False
            i += 1
        d = bus.getDevices()
        while d != None:
            if b > self.maxDevNum:
                raise DeviceLostException("Device number too large: " + b + " > " + self.maxDevNum)
            if b > 0:
                self.oldDevices[b] = True
            d = d.getNext()
        self.oldDevNum = self.dev.dev().getDevnum()

    @synchronized
    def findNewDevice(self, errMsg):
        """ generated source for method findNewDevice """
        newDev = None
        LibusbJava.usb_find_busses()
        LibusbJava.usb_find_devices()
        bus = LibusbJava.usb_get_busses()
        while bus != None and not bus.getDirname() == self.usbBusName:
            bus = bus.getNext()
        if bus == None:
            raise DeviceLostException("findNewDevice: Bus dissapeared")
        d = bus.getDevices() if bus != None else None
        while d != None:
            if b > self.maxDevNum:
                raise DeviceLostException("Device number too large: " + b + " > " + self.maxDevNum)
            if b > 0 and not self.oldDevices[b]:
                if newDev != None:
                    raise DeviceLostException(errMsg + "More than 2 new devices found: " + newDev.getDevnum() + "(`" + newDev.getFilename() + "') and " + b + "(`" + d.getFilename() + "')")
                newDev = d
            d = d.getNext()
        return newDev

    def initNewDevice(self, errBase, scanUnconfigured):
        """ generated source for method initNewDevice """
        newDev = None
        i = int()
        while i < 300 and newDev == None:
            try:
                Thread.sleep(200)
            except InterruptedException as e:
                pass
            if i > 10 and self.oldDevNum >= 0 and self.oldDevNum < self.maxDevNum:
                self.oldDevices[self.oldDevNum] = False
            newDev = self.findNewDevice(errBase + ": ")
            i += 1
        self.oldDevNum = -1
        if newDev == None:
            raise DeviceLostException(errBase + ": No new device found")
        dd = newDev.getDescriptor()
        vid = dd.getIdVendor() & 65535
        pid = dd.getIdProduct() & 65535
        try:
            self.dev = ZtexDevice1(newDev, vid, pid, scanUnconfigured)
        except DeviceNotSupportedException as e:
            raise InvalidFirmwareException(e.getLocalizedMessage())
        self.handle = LibusbJava.usb_open(self.dev.dev())

    @overloaded
    def uploadFirmware(self, ihxFile, force):
        """ generated source for method uploadFirmware """
        if not force and self.dev.valid():
            if ihxFile.interfaceVersion() != 1:
                raise IncompatibleFirmwareException("Wrong interface version: Expected 1, got " + ihxFile.interfaceVersion())
            if not self.dev.compatible(ihxFile.productId(0), ihxFile.productId(1), ihxFile.productId(2), ihxFile.productId(3)):
                raise IncompatibleFirmwareException("Incompatible productId's: Current firmware: " + ZtexDevice1.byteArrayString(self.dev.productId()) + "  Ihx File: " + ZtexDevice1.byteArrayString(ihxFile.productId()))
        self.findOldDevices()
        time = EzUsb.uploadFirmware(self.handle, ihxFile)
        self.initNewDevice("Device lost after uploading Firmware", False)
        return time

    @uploadFirmware.register(object, str, bool)
    def uploadFirmware_0(self, ihxFileName, force):
        """ generated source for method uploadFirmware_0 """
        ihxFile = ZtexIhxFile1()
        try:
            ihxFile = ZtexIhxFile1(ihxFileName)
        except IOException as e:
            raise FirmwareUploadException(e.getLocalizedMessage())
        except IhxFileDamagedException as e:
            raise FirmwareUploadException(e.getLocalizedMessage())
        return self.uploadFirmware(ihxFile, force)

    def resetEzUsb(self):
        """ generated source for method resetEzUsb """
        self.findOldDevices()
        EzUsb.reset(self.handle, True)
        try:
            EzUsb.reset(self.handle, False)
        except FirmwareUploadException as e:
            pass
        self.initNewDevice("Device lost after resetting the EZ-USB", True)

    def __str__(self):
        """ generated source for method toString """
        return self.dev.__str__()

