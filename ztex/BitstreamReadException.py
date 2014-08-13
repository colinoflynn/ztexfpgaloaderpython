#!/usr/bin/env python
""" generated source for module BitstreamReadException """
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

#  * 	Signals that an error occurred while attempting to read a bitstream. 
class BitstreamReadException(IOException):
    """ generated source for class BitstreamReadException """
    # 
    #      * Constructs an instance from the given error message.
    #      * @param msg The error message.
    #      
    @overloaded
    def __init__(self, msg):
        """ generated source for method __init__ """
        super(BitstreamReadException, self).__init__("Cannot read bitstream: " + msg)

    #  * Constructs an instance using a standard message. 
    @__init__.register(object)
    def __init___0(self):
        """ generated source for method __init___0 """
        super(BitstreamReadException, self).__init__("Cannot read bitstream")

