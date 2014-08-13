#!/usr/bin/env python
""" generated source for module InvalidFirmwareException """
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
#  * Thrown if a device runs with no or the wrong firmware, i.e. if the ZTEX descriptor is not found or damaged. 
class InvalidFirmwareException(Exception):
    """ generated source for class InvalidFirmwareException """
    # 
    #      * Constructs an instance from the error message.
    #      * @param msg The error message.
    #      
    @overloaded
    def __init__(self, msg):
        """ generated source for method __init__ """
        super(InvalidFirmwareException, self).__init__(msg)

    # 
    #      * Constructs an instance from the given device and error message.
    #      * @param ztex The device.
    #      * @param msg The error message.
    #      
    @__init__.register(object, Ztex1, str)
    def __init___0(self, ztex, msg):
        """ generated source for method __init___0 """
        super(InvalidFirmwareException, self).__init__()
        self.__init__(ztex.dev().dev(), msg)

    # 
    #      * Constructs an instance from the given device and error message.
    #      * @param dev The device.
    #      * @param msg The error message.
    #      
    @__init__.register(object, ZtexDevice1, str)
    def __init___1(self, dev, msg):
        """ generated source for method __init___1 """
        super(InvalidFirmwareException, self).__init__()
        self.__init__(dev.dev(), msg)

    # 
    #      * Constructs an instance from the given device and error message.
    #      * @param dev The device.
    #      * @param msg The error message.
    #      
    @__init__.register(object, Usb_Device, str)
    def __init___2(self, dev, msg):
        """ generated source for method __init___2 """
        super(InvalidFirmwareException, self).__init__("bus=" + dev.getBus().getDirname() + "  device=" + dev.getFilename() + ": Invalid Firmware: " + msg)

    # 
    #      * Constructs an instance from the given device and error message.
    #      * @param ztex The device.
    #      
    @__init__.register(object, Ztex1)
    def __init___3(self, ztex):
        """ generated source for method __init___3 """
        super(InvalidFirmwareException, self).__init__()
        self.__init__(ztex.dev().dev())

    # 
    #      * Constructs an instance from the given device and error message.
    #      * @param dev The device.
    #      
    @__init__.register(object, ZtexDevice1)
    def __init___4(self, dev):
        """ generated source for method __init___4 """
        super(InvalidFirmwareException, self).__init__()
        self.__init__(dev.dev())

    # 
    #      * Constructs an instance from the given device and error message.
    #      * @param dev The device.
    #      
    @__init__.register(object, Usb_Device)
    def __init___5(self, dev):
        """ generated source for method __init___5 """
        super(InvalidFirmwareException, self).__init__("bus=" + dev.getBus().getDirname() + "  device=" + dev.getFilename() + ": Invalid Firmware")

