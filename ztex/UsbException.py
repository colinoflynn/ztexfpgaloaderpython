#!/usr/bin/env python
""" generated source for module UsbException """
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
import ch.ntb.usb

#  * Signals an USB error. 
class UsbException(Exception):
    """ generated source for class UsbException """
    # 
    #      * Constructs an instance from the given error message.
    #      * @param msg The error message.
    #      
    @overloaded
    def __init__(self, msg):
        """ generated source for method __init__ """
        super(UsbException, self).__init__(msg)

    # 
    #      * Constructs an instance from the given device and error message.
    #      * @param dev The device.
    #      * @param msg The error message.
    #      
    @__init__.register(object, Usb_Device, str)
    def __init___0(self, dev, msg):
        """ generated source for method __init___0 """
        super(UsbException, self).__init__("bus=" + dev.getBus().getDirname() + "  device=" + dev.getFilename() + ": " + msg)

