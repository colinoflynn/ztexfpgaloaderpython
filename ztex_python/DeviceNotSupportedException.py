#!/usr/bin/env python
""" generated source for module DeviceNotSupportedException """
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

# 
#  * Thrown if a device is not supported, i.e. has the wrong USB ID's. 
class DeviceNotSupportedException(Exception):
    """ generated source for class DeviceNotSupportedException """
    # 
    #      * Constructs an instance from the given device.
    #      * @param dev The device.
    #      
    def __init__(self, dev):
        """ generated source for method __init__ """
        super(DeviceNotSupportedException, self).__init__("bus=" + dev.getBus().getDirname() + "  device=" + dev.getFilename() + ": Device not supported")

