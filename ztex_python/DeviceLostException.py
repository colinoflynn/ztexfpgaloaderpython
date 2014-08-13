#!/usr/bin/env python
""" generated source for module DeviceLostException """
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
#  * Thrown if a device went lost after renumeration. 
class DeviceLostException(Exception):
    """ generated source for class DeviceLostException """
    # 
    #      * Constructs an instance from the given input string.
    #      * @param msg A message.
    #      
    @overloaded
    def __init__(self, msg):
        """ generated source for method __init__ """
        super(DeviceLostException, self).__init__(msg)

    #  * Constructs an instance using a standard message. 
    @__init__.register(object)
    def __init___0(self):
        """ generated source for method __init___0 """
        super(DeviceLostException, self).__init__("Device lost")

