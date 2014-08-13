#!/usr/bin/env python
""" generated source for module IhxFile """
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
#  Reads an ihx file
#  
# package: ztex
import java.io

import java.util

import java.net

# 
#  * A class representing a firmware image loaded from an ihx (Intel Hex format) file.
#  
class IhxFile(object):
    """ generated source for class IhxFile """
    # 
    #      * This array stores the firmware image.
    #      * Values &lt;0 and &gt;255 mean that the data is undefined.
    #      
    ihxData = [None]*65536

    #  ******* readHexDigit ********************************************************
    @classmethod
    def readHexDigit(cls, in_):
        """ generated source for method readHexDigit """
        b = in_.read()
        if b >= int('0') and b <= int('9'):
            return b - int('0')
        if b >= int('a') and b <= int('f'):
            return 10 + b - int('a')
        if b >= int('A') and b <= int('F'):
            return 10 + b - int('A')
        if b == -1:
            raise IhxParseException("Inexpected end of file")
        raise IhxParseException("Hex digit expected: " + str(b))

    #  ******* readHexByte *********************************************************
    @classmethod
    def readHexByte(cls, in_):
        """ generated source for method readHexByte """
        return (cls.readHexDigit(in_) << 4) | cls.readHexDigit(in_)

    #  ******* IhxFile *************************************************************
    # 
    #      * Constructs an instance from a given file name.
    #      * This method can also read system resources, e.g. files from the current jar archive.
    #      * @param fileName The file name.
    #      * @throws IOException If an read error occurred.
    #      * @throws IhxFileDamagedException If the ihx file is damaged.
    #      
    def __init__(self, fileName):
        """ generated source for method __init__ """
        in_ = JInputStream.getInputStream(fileName)
        b = int()
        len = int()
        cs = int()
        addr = int()
        buf = [None]*255
        eof = False
        line = 0
        i = 0
        while len(ihxData):
            self.ihxData[i] = -1
            i += 1
        try:
            while not eof:
                while True:
                    b = in_.read()
                    if b < 0:
                        raise IhxParseException("Inexpected end of file")
                    if not ((b != int(':'))):
                        break
                line += 1
                len = self.readHexByte(in_)
                #  length field 
                cs = len
                b = self.readHexByte(in_)
                #  address field 
                cs += b
                addr = b << 8
                b = self.readHexByte(in_)
                cs += b
                addr |= b
                b = self.readHexByte(in_)
                #  record type field
                cs += b
                while i < len:
                    #  data
                    buf[i] = int(self.readHexByte(in_))
                    cs += buf[i]
                    i += 1
                cs += self.readHexByte(in_)
                #  checksum
                if (cs & 0xff) != 0:
                    raise IhxParseException("Checksum error")
                if b == 0:
                    #  data record
                    while i < len:
                        if self.ihxData[addr + i] >= 0:
                            System.err.println("Warning: Memory at position " + Integer.toHexString(i) + " overwritten")
                        self.ihxData[addr + i] = int((buf[i] & 255))
                        i += 1
                elif b == 1:
                    #  eof record
                    eof = True
                else:
                    raise IhxParseException("Invalid record type: " + b)
        except IhxParseException as e:
            raise IhxFileDamagedException(fileName, line, e.getLocalizedMessage())
        try:
            in_.close()
        except Exception as e:
            System.err.println("Warning: Error closing file " + fileName + ": " + e.getLocalizedMessage())

    #  ******* dataInfo ************************************************************
    # 
    #      * Print out some information about the memory usage.
    #      * @param out Where the data is printed out.
    #      
    def dataInfo(self, out):
        """ generated source for method dataInfo """
        addr = -1
        i = 0
        while i <= 65536:
            #  data
            if (i == 65536 or self.ihxData[i] < 0) and addr >= 0:
                print i - addr + " Bytes from " + Integer.toHexString(addr) + " to " + Integer.toHexString(i - 1)
                addr = -1
            if i < 65536 and self.ihxData[i] >= 0 and addr < 0:
                addr = i
            i += 1

