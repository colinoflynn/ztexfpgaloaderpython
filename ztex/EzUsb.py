#!/usr/bin/env python
""" generated source for module EzUsb """
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
# package: ztex
import java.io

import java.util

import ch.ntb.usb

# 
#  * Provides methods for uploading firmware to Cypress EZ-USB devices.
#  
class EzUsb(object):
    """ generated source for class EzUsb """
    #  ******* reset **************************************************************
    # 
    #      * Controls the reset state of a Cypress EZ-USB device.
    #      * @param handle The handle of the device.
    #      * @param r The reset state (true means reset).
    #      * @throws FirmwareUploadException if an error occurred while attempting to control the reset state.
    #      
    @classmethod
    def reset(cls, handle, r):
        """ generated source for method reset """
        buffer_ = [int((1 if r else 0))]
        k = LibusbJava.usb_control_msg(handle, 0x40, 0xA0, 0xE600, 0, buffer_, 1, 1000)
        #  upload j bytes
        if k < 0:
            raise FirmwareUploadException(LibusbJava.usb_strerror() + ": unable to set reset=" + buffer_[0])
        elif k != 1:
            raise FirmwareUploadException("Unable to set reset=" + buffer_[0])
        try:
            Thread.sleep(50 if r else 400)
            #  give the firmware some time for initialization
        except InterruptedException as e:
            pass

    #  ******* uploadFirmware ******************************************************
    # 
    #      * Uploads the Firmware to a Cypress EZ-USB device.
    #      * @param handle The handle of the device.
    #      * @param ihxFile The firmware image.
    #      * @return the upload time in ms.
    #      * @throws FirmwareUploadException if an error occurred while attempting to upload the firmware.
    #      
    @classmethod
    def uploadFirmware(cls, handle, ihxFile):
        """ generated source for method uploadFirmware """
        transactionBytes = 256
        buffer_ = [None]*transactionBytes
        cls.reset(handle, True)
        #  reset = 1
        t0 = Date().getTime()
        j = 0
        i = 0
        while len(length):
            if ihxFile.ihxData[i] < 0 or len(length) or j >= transactionBytes:
                if j > 0:
                    #  upload j bytes
                    if k < 0:
                        raise FirmwareUploadException(LibusbJava.usb_strerror())
                    elif k != j:
                        raise FirmwareUploadException()
                    try:
                        Thread.sleep(1)
                        #  to avoid package loss
                    except InterruptedException as e:
                        pass
                j = 0
            if ihxFile.ihxData[i] >= 0 and len(length) and ihxFile.ihxData[i] <= 255:
                buffer_[j] = int(ihxFile.ihxData[i])
                j += 1
            i += 1
        t1 = Date().getTime()
        try:
            EzUsb.reset(handle, False)
            #  error (may caused re-numeration) can be ignored
        except FirmwareUploadException as e:
            pass
        return t1 - t0

