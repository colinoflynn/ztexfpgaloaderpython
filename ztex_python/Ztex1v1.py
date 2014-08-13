#!/usr/bin/env python
""" generated source for module Ztex1v1 """
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
#  Functions for USB devices with ZTEX descriptor 1, Interface 1
#  Interface capabilities and vendor requests (VR) / commands (VC):
#  0.0  : EEPROM support
#  VR 0x38 : read from EEPROM
#  Returns:
#  EEPROM data
#  VC 0x39 : write to EEPROM
#  VR 0x3a : EEPROM state
#  Returns:
#  Offs	Description
#  0-1   	bytes written
#  2	checksum
#  3	0:idle, 1:busy or error
#  0.1  : FPGA Configuration
#  VR 0x30 : get FPGA state
#  Returns:
#  Offs	Description
#  0	1: unconfigured, 0:configured
#  1	checksum
#  2-5	transferred bytes
#  6  	INIT_B state
#  7	Flash configuration result
#  8	Flash bitstream bit order (1=swapped)
#  VC 0x31 : reset FPGA
#  VC 0x32 : send FPGA configuration data (Bitstream)
#  0.2  : Flash memory support
#  VR 0x40 : read Flash state
#  Returns:
#  Offs	Description
#  0	1:enabled, 0:disabled
#  1-2	Sector size
#  3-6	Number of sectors
#  7	Error code
#  VR 0x41 : read from Flash
#  VC 0x42 : write to Flash
#  0.3  : Debug helper support
#  VR 0x28 : read debug data
#  Returns:
#  Offs	Description
#  0-1	number of messages
#  2	stack size in messages
#  3       message size in bytes
#  >=4	message stack
#  0.4  : XMEGA support
#  VR 0x48 : read XMEGA status information
#  Returns:
#  Offs	Description
#  0	error code
#  1-2     Flash size in pages
#  3-4     EEPROM size in pages
#  5	Flash page size as power of two	(e.g. 9 means 512 bytes)
#  6	EEPROM page size as power of two
#  VC 0x49 : reset XMEGA
#  VR 0x4A,0x4B,0x4C,0x4D : read XMEGA NVM using PDI address space / relative to Flash address base / EEPROM address base / Fuse address base
#  VC 0x4B,0x4C : write exactly one Flash / EEPROM page
#  VC 0x4D : write Fuse
#  0.5  : High speed FPGA configuration support
#  VR 0x33 : Return Endpoint settings
#  Returns:
#  Offs	Description
#  0	Endpoint number
#  1	Interface number
#  VC 0x34 : Start high speed FPGA configuration
#  VC 0x35 : Finish high speed FPGA configuration
#  0.6  : MAC EEPROM support
#  VR 0x3B : read from MAC EEPROM
#  Returns:
#  MAC EEPROM data
#  VC 0x3C : write to MAC EEPROM
#  VR 0x3D : MAC EEPROM state
#  Returns:
#  Offs	Description
#  0	0:idle, 1:busy or error
#  0.7  : Multi-FPGA support
#  VR 0x50 : Return multi-FPGA information
#  Returns:
#  Offs	Description
#  0	Number of FPGA's - 1
#  1       Selected FPGA - 1 
#  2       Parallel configuration support (0:no, 1:yes)
#  VC 0x51 : set CS
#  Parameters:
#  index: Select command
#  0 : select single FPGA
#  1 : select all FPGA's for configuration
#  value: FPGA to select - 1
#  1.0  : Temperature sensor
#  VR 0x58 : Return temperature data
#  Returns:
#  Offs	Description
#  0	Protocol number
#  1..n    Data
#  
# package: ztex
import java.io

import java.util

import ch.ntb.usb

# 
#  * This class implements the communication protocol of the interface version 1 for the interaction with the ZTEX firmware.
#  * <p>
#  * The features supported by this interface can be accessed via vendor commands and vendor requests via Endpoint 0.
#  * Each feature can be enabled or disabled by the firmware and also depends from the hardware.
#  * The presence of a feature is indicated by a 1 in the corresponding feature bit of the ZTEX descriptor 1, see {@link ZtexDevice1}.
#  * The following table gives an overview about the features
#  * <table bgcolor="#404040" cellspacing=1 cellpadding=10>
#  *   <tr>
#  *     <td bgcolor="#d0d0d0" valign="bottom"><b>Capability bit</b></td>
#  *     <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *   </tr>
#  *   <tr>
#  *     <td bgcolor="#ffffff" valign="top">0.0</td>
#  *     <td bgcolor="#ffffff" valign="top" colspan=2>
#  *	  EEPROM support<p>
#  *       <table bgcolor="#404040" cellspacing=1 cellpadding=6>
#  *         <tr>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Vendor request (VR)<br> or command (VC)</b></td>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x38</td>
#  *           <td bgcolor="#ffffff" valign="top">Read from EEPROM</td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VC 0x39</td>
#  *           <td bgcolor="#ffffff" valign="top">Write to EEPROM</td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x3a</td>
#  *           <td bgcolor="#ffffff" valign="top">Get EEPROM state. Returns:
#  *             <table bgcolor="#404040" cellspacing=1 cellpadding=4>
#  *               <tr>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Bytes</b></td>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">0-1</td>
#  *                 <td bgcolor="#ffffff" valign="top">Number of bytes written.</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">2</td>
#  *                 <td bgcolor="#ffffff" valign="top">Checksum</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">3</td>
#  *                 <td bgcolor="#ffffff" valign="top">0:idle, 1:busy or error</td>
#  *               </tr>
#  *             </table>
#  *           </td>
#  *         </tr>
#  *       </table>
#  *	</td>
#  *   </tr>
#  *   <tr>
#  *     <td bgcolor="#ffffff" valign="top">0.1</td>
#  *     <td bgcolor="#ffffff" valign="top" colspan=2>
#  *       FPGA Configuration<p>
#  *       <table bgcolor="#404040" cellspacing=1 cellpadding=6>
#  *         <tr>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Vendor request (VR)<br> or command (VC)</b></td>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x30</td>
#  *           <td bgcolor="#ffffff" valign="top">Get FPGA state. Returns:
#  *             <table bgcolor="#404040" cellspacing=1 cellpadding=4>
#  *               <tr>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Bytes</b></td>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">0</td>
#  *                 <td bgcolor="#ffffff" valign="top">1: unconfigured, 0:configured</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">1</td>
#  *                 <td bgcolor="#ffffff" valign="top">Checksum</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">2-5</td>
#  *                 <td bgcolor="#ffffff" valign="top">Number of bytes transferred.</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">6</td>
#  *                 <td bgcolor="#ffffff" valign="top">INIT_B states.</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">7</td>
#  *                 <td bgcolor="#ffffff" valign="top">Flash configuration result.</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">8</td>
#  *                 <td bgcolor="#ffffff" valign="top">Flash Bitstreambit order (1=swapped).</td>
#  *               </tr>
#  *             </table>
#  *           </td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VC 0x31</td>
#  *           <td bgcolor="#ffffff" valign="top">Reset FPGA</td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x32</td>
#  *           <td bgcolor="#ffffff" valign="top">Send Bitstream</td>
#  *         </tr>
#  *       </table>
#  *     </td>
#  *   </tr>
#  *   <tr>
#  *     <td bgcolor="#ffffff" valign="top">0.2</td>
#  *     <td bgcolor="#ffffff" valign="top" colspan=2>
#  *       Flash memory support<p>
#  *       <table bgcolor="#404040" cellspacing=1 cellpadding=6>
#  *         <tr>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Vendor request (VR)<br> or command (VC)</b></td>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x40</td>
#  *           <td bgcolor="#ffffff" valign="top">Get Flash state. Returns:
#  *             <table bgcolor="#404040" cellspacing=1 cellpadding=4>
#  *               <tr>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Bytes</b></td>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">0</td>
#  *                 <td bgcolor="#ffffff" valign="top">1:enabled, 0:disabled</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">1-2</td>
#  *                 <td bgcolor="#ffffff" valign="top">Sector size</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">3-6</td>
#  *                 <td bgcolor="#ffffff" valign="top">Number of sectors</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">7</td>
#  *                 <td bgcolor="#ffffff" valign="top">Error code</td>
#  *               </tr>
#  *             </table>
#  *           </td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x41</td>
#  *           <td bgcolor="#ffffff" valign="top">Read one sector from Flash</td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VC 0x42</td>
#  *           <td bgcolor="#ffffff" valign="top">Write one sector to Flash</td>
#  *         </tr>
#  *       </table>
#  *     </td>
#  *   </tr>
#  *   <tr>
#  *     <td bgcolor="#ffffff" valign="top">0.3</td>
#  *     <td bgcolor="#ffffff" valign="top" colspan=2>
#  *       Debug helper support<p>
#  *       <table bgcolor="#404040" cellspacing=1 cellpadding=6>
#  *         <tr>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Vendor request (VR)<br> or command (VC)</b></td>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x28</td>
#  *           <td bgcolor="#ffffff" valign="top">Get debug data. Returns:
#  *             <table bgcolor="#404040" cellspacing=1 cellpadding=4>
#  *               <tr>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Bytes</b></td>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">0-1</td>
#  *                 <td bgcolor="#ffffff" valign="top">Number of the last message</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">2</td>
#  *                 <td bgcolor="#ffffff" valign="top">Stack size in messages</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">3</td>
#  *                 <td bgcolor="#ffffff" valign="top">Message size in bytes</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">&ge;4</td>
#  *                 <td bgcolor="#ffffff" valign="top">Message stack</td>
#  *               </tr>
#  *             </table>
#  *           </td>
#  *         </tr>
#  *       </table>
#  *     </td>
#  *   </tr>
#  *   <tr>
#  *     <td bgcolor="#ffffff" valign="top">0.4</td>
#  *     <td bgcolor="#ffffff" valign="top" colspan=2>
#  *       XMEGA support<p>
#  *       <table bgcolor="#404040" cellspacing=1 cellpadding=6>
#  *         <tr>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Vendor request (VR)<br> or command (VC)</b></td>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x48</td>
#  *           <td bgcolor="#ffffff" valign="top">Read XMEGA status information. Returns:
#  *             <table bgcolor="#404040" cellspacing=1 cellpadding=4>
#  *               <tr>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Bytes</b></td>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">0</td>
#  *                 <td bgcolor="#ffffff" valign="top">Error code</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">1-2</td>
#  *                 <td bgcolor="#ffffff" valign="top">Flash size in pages</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">3-4</td>
#  *                 <td bgcolor="#ffffff" valign="top">EEPROM sie in pages</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">5</td>
#  *                 <td bgcolor="#ffffff" valign="top">Flash page size as power of two	(e.g. 9 means 512 bytes)</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">6</td>
#  *                 <td bgcolor="#ffffff" valign="top">EEPROM page size as power of two</td>
#  *               </tr>
#  *             </table>
#  *           </td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VC 0x49</td>
#  *           <td bgcolor="#ffffff" valign="top">Reset XMEGA</td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VRs 0x4A, 0x4B, 0x4C, 0x4D</td>
#  *           <td bgcolor="#ffffff" valign="top">Read XMEGA NVM using PDI address space / relative to Flash address base / EEPROM address base / Fuse address base</td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VCs 0x4B, 0x4C</td>
#  *           <td bgcolor="#ffffff" valign="top">Write exactly one Flash / EEPROM page</td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VCs 0x4D</td>
#  *           <td bgcolor="#ffffff" valign="top">Write Fuse</td>
#  *         </tr>
#  *       </table>
#  *     </td>
#  *   </tr>
#  *   <tr>
#  *     <td bgcolor="#ffffff" valign="top">0.5</td>
#  *     <td bgcolor="#ffffff" valign="top" colspan=2>
#  *	  High speed FPGA configuration support<p>
#  *       <table bgcolor="#404040" cellspacing=1 cellpadding=6>
#  *         <tr>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Vendor request (VR)<br> or command (VC)</b></td>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x33</td>
#  *           <td bgcolor="#ffffff" valign="top">Read Endpoint settings. Returns:
#  *             <table bgcolor="#404040" cellspacing=1 cellpadding=4>
#  *               <tr>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Bytes</b></td>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">0</td>
#  *                 <td bgcolor="#ffffff" valign="top">Endpoint number</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">1</td>
#  *                 <td bgcolor="#ffffff" valign="top">Interface number</td>
#  *               </tr>
#  *             </table>
#  *           </td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x34</td>
#  *           <td bgcolor="#ffffff" valign="top">Start FPGA configuration</td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VC 0x35</td>
#  *           <td bgcolor="#ffffff" valign="top">Finish FPGA configuration</td>
#  *         </tr>
#  *       </table>
#  *	</td>
#  *   </tr>
#  *   <tr>
#  *     <td bgcolor="#ffffff" valign="top">0.6</td>
#  *     <td bgcolor="#ffffff" valign="top" colspan=2>
#  *	  MAC EEPROM support<p>
#  *       <table bgcolor="#404040" cellspacing=1 cellpadding=6>
#  *         <tr>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Vendor request (VR)<br> or command (VC)</b></td>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x3B</td>
#  *           <td bgcolor="#ffffff" valign="top">Read from MAC EEPROM</td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VC 0x3C</td>
#  *           <td bgcolor="#ffffff" valign="top">Write to MAC EEPROM</td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x3D</td>
#  *           <td bgcolor="#ffffff" valign="top">Get MAC EEPROM state. Returns:
#  *             <table bgcolor="#404040" cellspacing=1 cellpadding=4>
#  *               <tr>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Bytes</b></td>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">0</td>
#  *                 <td bgcolor="#ffffff" valign="top">0:idle, 1:busy or error</td>
#  *               </tr>
#  *             </table>
#  *           </td>
#  *         </tr>
#  *       </table>
#  *	</td>
#  *   </tr>
#  *   <tr>
#  *     <td bgcolor="#ffffff" valign="top">0.7</td>
#  *     <td bgcolor="#ffffff" valign="top" colspan=2>
#  *	  Multi-FPGA support<p>
#  *       <table bgcolor="#404040" cellspacing=1 cellpadding=6>
#  *         <tr>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Vendor request (VR)<br> or command (VC)</b></td>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x50</td>
#  *           <td bgcolor="#ffffff" valign="top">Return multi-FPGA information:
#  *             <table bgcolor="#404040" cellspacing=1 cellpadding=4>
#  *               <tr>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Bytes</b></td>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">0</td>
#  *                 <td bgcolor="#ffffff" valign="top">Number of FPGA's - 1</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">1</td>
#  *                 <td bgcolor="#ffffff" valign="top">Selected FPGA - 1</td>
#  *               </tr>
#  *               <tr>
#  *		    <td bgcolor="#ffffff" valign="top">2</td>
#  *		    <td bgcolor="#ffffff" valign="top">Parallel configuration support (0:no, 1:yes)</td>
#  *               </tr>
#  *             </table>
#  *           </td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VC 0x51</td>
#  *           <td bgcolor="#ffffff" valign="top">Parameters:
#  *             <table bgcolor="#404040" cellspacing=1 cellpadding=4>
#  *               <tr>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Parameter</b></td>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">index</td>
#  *                 <td bgcolor="#ffffff" valign="top">Select command<br> 0: Select single FPGA <br> 1: Select all FPGA's for configuration</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">value</td>
#  *                 <td bgcolor="#ffffff" valign="top">FPGA to select - 1</td>
#  *               </tr>
#  *             </table>
#  *           </td>
#  *         </tr>
#  *       </table>
#  *	</td>
#  *   </tr>
#  *   <tr>
#  *     <td bgcolor="#ffffff" valign="top">1.0</td>
#  *     <td bgcolor="#ffffff" valign="top" colspan=2>
#  *	  Temperature sensor support<p>
#  *       <table bgcolor="#404040" cellspacing=1 cellpadding=6>
#  *         <tr>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Vendor request (VR)<br> or command (VC)</b></td>
#  *           <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *         </tr>
#  *         <tr>
#  *           <td bgcolor="#ffffff" valign="top">VR 0x58</td>
#  *           <td bgcolor="#ffffff" valign="top">Return temperature data:
#  *             <table bgcolor="#404040" cellspacing=1 cellpadding=4>
#  *               <tr>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Bytes</b></td>
#  *                 <td bgcolor="#d0d0d0" valign="bottom"><b>Description</b></td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">0</td>
#  *                 <td bgcolor="#ffffff" valign="top">Protocol</td>
#  *               </tr>
#  *               <tr>
#  *                 <td bgcolor="#ffffff" valign="top">1..n</td>
#  *                 <td bgcolor="#ffffff" valign="top">Data</td>
#  *               </tr>
#  *             </table>
#  *           </td>
#  *         </tr>
#  *       </table>
#  *	</td>
#  *   </tr>
#  * </table>
#  * @see ZtexDevice1
#  * @see Ztex1
#  
class Ztex1v1(Ztex1):
    """ generated source for class Ztex1v1 """
    #  * Capability index for EEPROM support. 
    CAPABILITY_EEPROM = 0

    #  * Capability index for FPGA configuration support. 
    CAPABILITY_FPGA = 1

    #  * Capability index for FLASH memory support. 
    CAPABILITY_FLASH = 2

    #  * Capability index for DEBUG helper support. 
    CAPABILITY_DEBUG = 3

    #  * Capability index for AVR XMEGA support. 
    CAPABILITY_XMEGA = 4

    #  * Capability index for AVR XMEGA support. 
    CAPABILITY_HS_FPGA = 5

    #  * Capability index for AVR XMEGA support. 
    CAPABILITY_MAC_EEPROM = 6

    #  * Capability index for multi FPGA support 
    CAPABILITY_MULTI_FPGA = 7

    #  * Capability index for Temperature sensor support 
    CAPABILITY_TEMP_SENSOR = 8

    #  * The names of the capabilities 
    capabilityStrings = ["EEPROM read/write", "FPGA configuration", "Flash memory support", "Debug helper", "XMEGA support", "High speed FPGA configuration", "MAC EEPROM read/write", "Multi FPGA Support", "Temperature Sensor Support"]

    #  * Enables extra FPGA configuration checks. Certain Bistream settings may cause false warnings.  
    enableExtraFpgaConfigurationChecks = False
    fpgaConfigured = False
    fpgaChecksum = 0
    fpgaBytes = 0
    fpgaInitB = 0
    fpgaFlashResult = 255
    fpgaFlashBitSwap = False

    #  * Number of bytes written to EEPROM. (Obtained by {@link #eepromState()}.) 
    eepromBytes = 0

    #  * Checksum of the last EEPROM transfer. (Obtained by {@link #eepromState()}.) 
    eepromChecksum = 0
    flashEnabled = -1
    flashSectorSize = -1
    flashSectors = -1

    #  * Last Flash error code obtained by {@link #flashState()}. See FLASH_EC_* for possible error codes. 
    flashEC = 0

    #  * Means no error. 
    FLASH_EC_NO_ERROR = 0

    #  * Signals an error while attempting to execute a command. 
    FLASH_EC_CMD_ERROR = 1

    #  * Signals that a timeout occurred. 
    FLASH_EC_TIMEOUT = 2

    #  * Signals that Flash memory it busy. 
    FLASH_EC_BUSY = 3

    #  * Signals that another Flash operation is pending. 
    FLASH_EC_PENDING = 4

    #  * Signals an error while attempting to read from Flash. 
    FLASH_EC_READ_ERROR = 5

    #  * Signals an error while attempting to write to Flash. 
    FLASH_EC_WRITE_ERROR = 6

    #  * Signals the the installed Flash memory is not supported. 
    FLASH_EC_NOTSUPPORTED = 7
    debugStackSize = -1
    debugMsgSize = -1
    debugLastMsg = 0

    #  * Is set by {@link #debugReadMessages(boolean,byte[])} and contains the number of new messages. 
    debugNewMessages = 0
    xmegaFlashPages = -1
    xmegaEepromPages = -1
    xmegaFlashPageSize = int()
    xmegaEepromPageSize = int()

    #  * Last ATxmega error code obtained by {@link #xmegaState()}. See XMEGA_EC_* for possible error codes. 
    xmegaEC = 0

    #  * Means no error. 
    XMEGA_EC_NO_ERROR = 0

    #  * Signals a PDI read error. 
    XMEGA_EC_PDI_READ_ERROR = 1

    #  * Signals that an NVM timeout occurred. 
    XMEGA_EC_NVM_TIMEOUT = 2

    #  * Signals that the ATxmega controller is not supported. 
    XMEGA_EC_INVALID_DEVICE = 3

    #  * Signals an address error (invalid address or wrong page size). 
    XMEGA_EC_ADDRESS_ERROR = 4

    #  * Signals that the NVM is busy. 
    XMEGA_EC_NVM_BUSY = 5
    numberOfFpgas = -1
    selectedFpga = -1
    parallelConfigSupport = False
    lastTempSensorReadTime = 0
    tempSensorBuf = [None]*9

    #  * smallest temperature sensor update interval in ms 
    tempSensorUpdateInterval = 100

    #  ******* Ztex1v1 *************************************************************
    # 
    #      * Constructs an instance from a given device.
    #      * @param pDev The given device.
    #      * @throws UsbException if an communication error occurred.
    #      
    def __init__(self, pDev):
        """ generated source for method __init__ """
        super(Ztex1v1, self).__init__(pDev)

    #  ******* valid ***************************************************************
    # 
    #      * Returns true if ZTEX interface 1 is available.
    #      * @return true if ZTEX interface 1 is available.
    #      
    @overloaded
    def valid(self):
        """ generated source for method valid """
        return dev().valid() and dev().interfaceVersion() == 1

    # 
    #      * Returns true if ZTEX interface 1 and capability i.j are available.
    #      * @param i byte index of the capability
    #      * @param j bit index of the capability
    #      * @return true if ZTEX interface 1 and capability i.j are available.
    #      
    @valid.register(object, int, int)
    def valid_0(self, i, j):
        """ generated source for method valid_0 """
        return dev().valid() and dev().interfaceVersion() == 1 and dev().interfaceCapabilities(i, j)

    #  ******* compatible **********************************************************
    # 
    #      * Checks whether the given product ID is compatible to the device corresponding to this class and whether interface 1 is supported.<br>
    #      * The given product ID is compatible
    #      * <pre>if ( this.productId(0)==0 || productId0<=0 || this.productId(0)==productId0 ) && 
    #      ( this.productId(0)==0 || productId1<=0 || this.productId(1)==productId1 ) && 
    #      ( this.productId(2)==0 || productId2<=0 || this.productId(2)==productId2 ) && 
    #      ( this.productId(3)==0 || productId3<=0 || this.productId(3)==productId3 ) </pre>
    #      * @param productId0 Byte 0 of the given product ID
    #      * @param productId1 Byte 1 of the given product ID
    #      * @param productId2 Byte 2 of the given product ID
    #      * @param productId3 Byte 3 of the given product ID
    #      * @return true if the given product ID is compatible and interface 1 is supported.
    #      
    def compatible(self, productId0, productId1, productId2, productId3):
        """ generated source for method compatible """
        return dev().valid() and dev().compatible(productId0, productId1, productId2, productId3) and dev().interfaceVersion() == 1

    #  ******* checkValid **********************************************************
    # 
    #      * Checks whether ZTEX descriptor 1 is available and interface 1 is supported.
    #      * @throws InvalidFirmwareException if ZTEX descriptor 1 is not available or interface 1 is not supported.
    #      
    def checkValid(self):
        """ generated source for method checkValid """
        super(Ztex1v1, self).checkValid()
        if dev().interfaceVersion() != 1:
            raise InvalidFirmwareException(self, "Wrong interface: " + dev().interfaceVersion() + ", expected: 1")

    #  ******* checkCapability *****************************************************
    # 
    #      * Checks whether ZTEX descriptor 1 is available and interface 1 and a given capability are supported.
    #      * @param i byte index of the capability
    #      * @param j bit index of the capability
    #      * @throws InvalidFirmwareException if ZTEX descriptor 1 is not available or interface 1 is not supported.
    #      * @throws CapabilityException if the given capability is not supported.
    #      
    @overloaded
    def checkCapability(self, i, j):
        """ generated source for method checkCapability """
        self.checkValid()
        if not dev().interfaceCapabilities(i, j):
            if k >= 0 and len(capabilityStrings):
                raise CapabilityException(self, self.capabilityStrings[k] if (k >= 0 and len(capabilityStrings)) else ("Capabilty " + i + "," + j))

    # 
    #      * Checks whether ZTEX descriptor 1 is available and interface 1 and a given capability are supported.
    #      * @param i capability index (0..47)
    #      * @throws InvalidFirmwareException if ZTEX descriptor 1 is not available or interface 1 is not supported.
    #      * @throws CapabilityException if the given capability is not supported.
    #      
    @checkCapability.register(object, int)
    def checkCapability_0(self, i):
        """ generated source for method checkCapability_0 """
        self.checkCapability(i / 8, i % 8)

    #  ******* checkCompatible *****************************************************
    # 
    #      * Checks whether the given product ID is compatible to the device corresponding to this class and whether interface 1 is supported.
    #      * See {@link #compatible(int,int,int,int)}.
    #      * @param productId0 Byte 0 of the given product ID
    #      * @param productId1 Byte 1 of the given product ID
    #      * @param productId2 Byte 2 of the given product ID
    #      * @param productId3 Byte 3 of the given product ID
    #      * @throws InvalidFirmwareException if the given product ID is not compatible or interface 1 is not supported.
    #      
    def checkCompatible(self, productId0, productId1, productId2, productId3):
        """ generated source for method checkCompatible """
        self.checkValid()
        if not dev().compatible(productId0, productId1, productId2, productId3):
            raise InvalidFirmwareException(self, "Incompatible Product ID")

    #  ******* getFpgaState ********************************************************
    def getFpgaState(self):
        """ generated source for method getFpgaState """
        buffer_ = [None]*9
        self.checkCapability(self.CAPABILITY_FPGA)
        vendorRequest2(0x30, "getFpgaState", buffer_, 9)
        self.fpgaConfigured = buffer_[0] == 0
        self.fpgaChecksum = buffer_[1] & 0xff
        self.fpgaBytes = ((buffer_[5] & 0xff) << 24) | ((buffer_[4] & 0xff) << 16) | ((buffer_[3] & 0xff) << 8) | (buffer_[2] & 0xff)
        self.fpgaInitB = buffer_[6] & 0xff
        self.fpgaFlashResult = buffer_[7]
        self.fpgaFlashBitSwap = buffer_[8] != 0

    #  ******* printFpgaState ******************************************************
    # 
    #      * Prints out the FPGA state.
    #      * @throws InvalidFirmwareException if interface 1 is not supported.
    #      * @throws UsbException if a communication error occurs.
    #      * @throws CapabilityException if FPGA configuration is not supported by the firmware.
    #      
    def printFpgaState(self):
        """ generated source for method printFpgaState """
        flashResultStr = ["Configuration successful", "FPGA already configured", "Flash error", "No bitstream found", "Configuration error"]
        self.getFpgaState()
        print "size=" + self.fpgaBytes + ";  checksum=" + self.fpgaChecksum + "; INIT_B_HIST=" + self.fpgaInitB + "; flash_configuration_result=" + self.fpgaFlashResult + (" (" + flashResultStr[self.fpgaFlashResult] + ")" if self.fpgaFlashResult >= 0 and len(flashResultStr) else "")

    #  ******* getFpgaConfiguration ************************************************
    # 
    #      * Returns true if the FPGA is configured.
    #      * @return true if the FPGA is configured.
    #      * @throws InvalidFirmwareException if interface 1 is not supported.
    #      * @throws UsbException if a communication error occurs.
    #      * @throws CapabilityException if FPGA configuration is not supported by the firmware.
    #      
    def getFpgaConfiguration(self):
        """ generated source for method getFpgaConfiguration """
        self.getFpgaState()
        return self.fpgaConfigured

    #  ******* getFpgaConfigurationStr *********************************************
    # 
    #      * Returns a string that indicates the FPGA configuration status.
    #      * @return a string that indicates the FPGA configuration status.
    #      * @throws InvalidFirmwareException if interface 1 is not supported.
    #      * @throws UsbException if a communication error occurs.
    #      * @throws CapabilityException if FPGA configuration is not supported by the firmware.
    #      
    def getFpgaConfigurationStr(self):
        """ generated source for method getFpgaConfigurationStr """
        self.getFpgaState()
        return "FPGA configured" if self.fpgaConfigured else "FPGA unconfigured"

    #  ******* resetFGPA ***********************************************************
    # 
    #      * Resets the FPGA.
    #      * @throws InvalidFirmwareException if interface 1 is not supported.
    #      * @throws UsbException if a communication error occurs.
    #      * @throws CapabilityException if FPGA configuration is not supported by the firmware.
    #      
    def resetFpga(self):
        """ generated source for method resetFpga """
        self.checkCapability(self.CAPABILITY_FPGA)
        vendorCommand(0x31, "resetFpga")

    #  ******* detectBitstreamBitOrder *********************************************
    def detectBitstreamBitOrder(self, buf):
        """ generated source for method detectBitstreamBitOrder """
        i = 0
        while i < len(buf):
            if ((buf[i] & 255) == 0xaa) and ((buf[i + 1] & 255) == 0x99) and ((buf[i + 2] & 255) == 0x55) and ((buf[i + 3] & 255) == 0x66):
                return 1
            if ((buf[i] & 255) == 0x55) and ((buf[i + 1] & 255) == 0x99) and ((buf[i + 2] & 255) == 0xaa) and ((buf[i + 3] & 255) == 0x66):
                return 0
            i += 1
        System.err.println("Warning: Unable to determine bitstream bit order: no signature found")
        return 0

    #  ******* swapBits ************************************************************
    def swapBits(self, buf, size):
        """ generated source for method swapBits """
        j = 0
        k = 0
        i = 0
        while i < size:
            while len(length):
                j += 1
                k = 0
            buf[j][k] = int((((b & 128) >> 7) | ((b & 64) >> 5) | ((b & 32) >> 3) | ((b & 16) >> 1) | ((b & 8) << 1) | ((b & 4) << 3) | ((b & 2) << 5) | ((b & 1) << 7)))
            k += 1
            i += 1

    def configureFpgaLS(self, fwFileName, force, bs):
        """ generated source for method configureFpgaLS """
        transactionBytes = 256 if certainWorkarounds else 2048
        t0 = 0
        self.checkCapability(self.CAPABILITY_FPGA)
        if not force and self.getFpgaConfiguration():
            raise AlreadyConfiguredException()
        buffer_ = [None]*16 * 1024 * 1024 / transactionBytes
        size = 0
        try:
            while j == transactionBytes and len(buffer_):
                buffer_[i] = [None]*transactionBytes
                j = 0
                while True:
                    k = inputStream.read(buffer_[i], j, transactionBytes - j)
                    if k < 0:
                        k = 0
                    j += k
                    if not ((j < transactionBytes and k > 0)):
                        break
                if j < transactionBytes and j % 64 == 0:
                    j += 1
                size += j
                i += 1
            try:
                inputStream.close()
            except Exception as e:
                System.err.println("Warning: Error closing file " + fwFileName + ": " + e.getLocalizedMessage())
        except IOException as e:
            raise BitstreamReadException(e.getLocalizedMessage())
        if size < 64 or size % 64 == 0:
            raise BitstreamReadException("Invalid file size: " + size)
        if bs < 0 or bs > 1:
            bs = self.detectBitstreamBitOrder(buffer_[0])
        if bs == 1:
            self.swapBits(buffer_, size)
        tries = 10
        while tries > 0:
            self.resetFpga()
            try:
                t0 = -Date().getTime()
                bs = 0
                while i * transactionBytes < size and len(buffer_):
                    if j > transactionBytes:
                        j = transactionBytes
                    vendorCommand2(0x32, "sendFpgaData", 0, 0, buffer_[i], j)
                    bs += j
                    while len(length):
                        cs = (cs + (buffer_[i][k] & 0xff)) & 0xff
                        k += 1
                    i += 1
                self.getFpgaState()
                if not self.fpgaConfigured:
                    raise BitstreamUploadException("FPGA configuration failed: DONE pin does not go high (size=" + self.fpgaBytes + " ,  " + (bs - self.fpgaBytes) + " bytes got lost;  checksum=" + self.fpgaChecksum + " , should be " + cs + ";  INIT_B_HIST=" + self.fpgaInitB + ")")
                if self.enableExtraFpgaConfigurationChecks:
                    if self.fpgaBytes != 0 and self.fpgaBytes != bs:
                        System.err.println("Warning: Possible FPGA configuration data loss: " + (bs - self.fpgaBytes) + " bytes got lost")
                    if self.fpgaInitB != 222:
                        System.err.println("Warning: Possible Bitstream CRC error: INIT_B_HIST=" + self.fpgaInitB)
                tries = 0
                t0 += Date().getTime()
            except BitstreamUploadException as e:
                if tries > 1:
                    System.err.println("Warning: " + e.getLocalizedMessage() + ": Retrying it ...")
                else:
                    raise e
            tries -= 1
        try:
            Thread.sleep(100)
        except InterruptedException as e:
            pass
        return t0

    def eepromState(self):
        """ generated source for method eepromState """
        buf = [None]*4
        self.checkCapability(self.CAPABILITY_EEPROM)
        vendorRequest2(0x3A, "EEPROM State", 0, 0, buf, 4)
        self.eepromBytes = (buf[0] & 255) | (buf[1] & 255) << 8
        self.eepromChecksum = buf[2] & 255
        return buf[3] == 0

    def eepromWrite(self, addr, buf, length):
        """ generated source for method eepromWrite """
        self.checkCapability(self.CAPABILITY_EEPROM)
        if (addr & 63) != 0:
            vendorCommand2(0x39, "EEPROM Write", addr, 0, buf, i)
            try:
                Thread.sleep(10)
            except InterruptedException as e:
                pass
            addr += i
            length -= i
            if length > 0:
                while j < length:
                    buf2[j] = buf[i + j]
                    j += 1
                vendorCommand2(0x39, "EEPROM Write", addr, 0, buf2, length)
        else:
            vendorCommand2(0x39, "EEPROM Write", addr, 0, buf, length)
        try:
            Thread.sleep(10)
        except InterruptedException as e:
            pass

    def eepromRead(self, addr, buf, length):
        """ generated source for method eepromRead """
        self.checkCapability(self.CAPABILITY_EEPROM)
        vendorRequest2(0x38, "EEPROM Read", addr, 0, buf, length)
        try:
            Thread.sleep(10)
        except InterruptedException as e:
            pass

    @overloaded
    def eepromUpload(self, ihxFile, force):
        """ generated source for method eepromUpload """
        pagesMax = 256
        pageSize = 256
        pages = 0
        buffer_ = [None]*pagesMax
        self.checkCapability(self.CAPABILITY_EEPROM)
        if not force and dev().valid():
            if ihxFile.interfaceVersion() != 1:
                raise IncompatibleFirmwareException("Wrong interface version: Expected 1, got " + ihxFile.interfaceVersion())
            if not dev().compatible(ihxFile.productId(0), ihxFile.productId(1), ihxFile.productId(2), ihxFile.productId(3)):
                raise IncompatibleFirmwareException("Incompatible productId's: Current firmware: " + ZtexDevice1.byteArrayString(dev().productId()) + "  Ihx File: " + ZtexDevice1.byteArrayString(ihxFile.productId()))
        dd = dev().dev().getDescriptor()
        vid = dd.getIdVendor() & 65535
        pid = dd.getIdProduct() & 65535
        buffer_[0] = [None]*pageSize
        buffer_[0][0] = int(0xc2)
        buffer_[0][1] = int((vid & 255))
        buffer_[0][2] = int(((vid >> 8) & 255))
        buffer_[0][3] = int((pid & 255))
        buffer_[0][4] = int(((pid >> 8) & 255))
        buffer_[0][5] = 0
        buffer_[0][6] = 0
        buffer_[0][7] = 0
        ptr = 8
        i = 0
        while len(length):
            if ihxFile.ihxData[i] >= 0 and ihxFile.ihxData[i] < 256:
                while ihxFile.ihxData[i + j] >= 0 and len(length) and ihxFile.ihxData[i + j] < 256:
                    j += 1
                while k < (ptr + j + 9) / pageSize + 1:
                    buffer_[k] = [None]*pageSize
                    k += 1
                buffer_[(ptr + 0) / pageSize][(ptr + 0) % pageSize] = int(((j >> 8) & 255))
                buffer_[(ptr + 1) / pageSize][(ptr + 1) % pageSize] = int((j & 255))
                buffer_[(ptr + 2) / pageSize][(ptr + 2) % pageSize] = int(((i >> 8) & 255))
                buffer_[(ptr + 3) / pageSize][(ptr + 3) % pageSize] = int((i & 255))
                ptr += 4
                while k < j:
                    buffer_[(ptr + k) / pageSize][(ptr + k) % pageSize] = int(ihxFile.ihxData[i + k])
                    k += 1
                ptr += j
                i += j
            else:
                i += 1
        buffer_[(ptr + 0) / pageSize][(ptr + 0) % pageSize] = int(0x80)
        buffer_[(ptr + 1) / pageSize][(ptr + 1) % pageSize] = int(0x01)
        buffer_[(ptr + 2) / pageSize][(ptr + 2) % pageSize] = int(0xe6)
        buffer_[(ptr + 3) / pageSize][(ptr + 3) % pageSize] = int(0x00)
        buffer_[(ptr + 3) / pageSize][(ptr + 4) % pageSize] = int(0x00)
        ptr += 5
        t0 = Date().getTime()
        rbuf = [None]*pageSize
        while i >= 0:
            while j < k:
                cs = (cs + (buffer_[i][j] & 255)) & 255
                j += 1
            while tries > 0:
                try:
                    self.eepromWrite(i * pageSize, buffer_[i], k)
                    self.eepromState()
                    if self.eepromBytes != k:
                        raise FirmwareUploadException("Error writing data to EEPROM: Wrote " + self.eepromBytes + " bytes instead of " + k + " bytes")
                    if self.eepromChecksum != cs:
                        raise FirmwareUploadException("Error writing data to EEPROM: Checksum error")
                    self.eepromRead(i * pageSize, rbuf, k)
                    while j < k:
                        if rbuf[j] != buffer_[i][j]:
                            raise FirmwareUploadException("Error writing data to EEPROM: Verification failed")
                        j += 1
                    tries = 0
                except Exception as e:
                    if tries > 1:
                        System.err.println("Warning: " + e.getLocalizedMessage() + ": Retrying it ...")
                    else:
                        raise FirmwareUploadException(e.getLocalizedMessage())
                tries -= 1
            i -= 1
        return Date().getTime() - t0

    @eepromUpload.register(object, str, bool)
    def eepromUpload_0(self, ihxFileName, force):
        """ generated source for method eepromUpload_0 """
        self.checkCapability(self.CAPABILITY_EEPROM)
        ihxFile = ZtexIhxFile1()
        try:
            ihxFile = ZtexIhxFile1(ihxFileName)
        except IOException as e:
            raise FirmwareUploadException(e.getLocalizedMessage())
        except IhxFileDamagedException as e:
            raise FirmwareUploadException(e.getLocalizedMessage())
        return self.eepromUpload(ihxFile, force)

    def eepromDisable(self):
        """ generated source for method eepromDisable """
        buf = [0]
        tries = 3
        while tries > 0:
            try:
                self.eepromWrite(0, buf, 1)
                self.eepromRead(0, buf, 1)
                if buf[0] != 0:
                    raise FirmwareUploadException("Error disabling EEPROM firmware: Verification failed")
                tries = 0
            except Exception as e:
                if tries > 1:
                    System.err.println("Warning: " + e.getLocalizedMessage() + ": Retrying it ...")
                else:
                    raise FirmwareUploadException(e.getLocalizedMessage())
            tries -= 1

    @classmethod
    @overloaded
    def flashStrError(cls, errNum):
        """ generated source for method flashStrError """
        if errNum==cls.FLASH_EC_NO_ERROR:
            return "USB error: " + LibusbJava.usb_strerror()
        elif errNum==cls.FLASH_EC_CMD_ERROR:
            return "Command error"
        elif errNum==cls.FLASH_EC_TIMEOUT:
            return "Timeout error"
        elif errNum==cls.FLASH_EC_BUSY:
            return "Busy"
        elif errNum==cls.FLASH_EC_PENDING:
            return "Another operation is pending"
        elif errNum==cls.FLASH_EC_READ_ERROR:
            return "Read error"
        elif errNum==cls.FLASH_EC_WRITE_ERROR:
            return "Write error"
        elif errNum==cls.FLASH_EC_NOTSUPPORTED:
            return "Not supported"
        return "Error " + errNum

    @flashStrError.register(object)
    def flashStrError_0(self):
        """ generated source for method flashStrError_0 """
        try:
            return self.flashStrError(getFlashEC())
        except Exception as e:
            return "Unknown error (Error receiving errorcode: " + e.getLocalizedMessage() + ")"

    def flashState(self):
        """ generated source for method flashState """
        buf = [None]*8
        self.checkCapability(self.CAPABILITY_FLASH)
        vendorRequest2(0x40, "Flash State", 0, 0, buf, 8)
        self.flashEC = buf[7] & 255
        tries = 20
        while self.flashEC == self.FLASH_EC_BUSY and tries > 0:
            try:
                Thread.sleep(200)
            except InterruptedException as e:
                pass
            tries -= 1
            vendorRequest2(0x40, "Flash State", 0, 0, buf, 8)
            self.flashEC = buf[7] & 255
        self.flashEnabled = buf[0] & 255
        self.flashSectorSize = ((buf[2] & 255) << 8) | (buf[1] & 255) if self.flashEnabled == 1 else 0
        self.flashSectors = ((buf[6] & 255) << 24) | ((buf[5] & 255) << 16) | ((buf[4] & 255) << 8) | (buf[3] & 255) if self.flashEnabled == 1 else 0
        return self.flashEnabled == 1

    def getFlashEC(self):
        """ generated source for method getFlashEC """
        buf = [None]*8
        self.checkCapability(self.CAPABILITY_FLASH)
        vendorRequest2(0x40, "Flash State", 0, 0, buf, 8)
        self.flashEC = buf[7] & 255
        return self.flashEC

    @overloaded
    def flashReadSector(self, sector, buf):
        """ generated source for method flashReadSector """
        if len(buf):
            raise IndexError(" < " + len(buf) + self.flashSectorSize())
        self.checkCapability(self.CAPABILITY_FLASH)
        if not self.flashEnabled():
            raise CapabilityException(self, "No Flash memory installed or")
        try:
            vendorRequest2(0x41, "Flash Read", sector, sector >> 16, buf, self.flashSectorSize)
        except UsbException as e:
            raise UsbException(dev().dev(), "Flash Read: " + self.flashStrError())

    @flashReadSector.register(object, int, int, int)
    def flashReadSector_0(self, sector, num, buf):
        """ generated source for method flashReadSector_0 """
        if len(buf):
            raise IndexError(" < " + len(buf) + (num * self.flashSectorSize()))
        self.checkCapability(self.CAPABILITY_FLASH)
        if not self.flashEnabled():
            raise CapabilityException(self, "No Flash memory installed or")
        try:
            vendorRequest2(0x41, "Flash Read", sector, sector >> 16, buf, self.flashSectorSize * num)
        except UsbException as e:
            raise UsbException(dev().dev(), "Flash Read: " + self.flashStrError())

    @overloaded
    def flashWriteSector(self, sector, buf):
        """ generated source for method flashWriteSector """
        if len(buf):
            raise IndexError(" < " + len(buf) + self.flashSectorSize())
        self.checkCapability(self.CAPABILITY_FLASH)
        if not self.flashEnabled():
            raise CapabilityException(self, "No Flash memory installed or")
        try:
            vendorCommand2(0x42, "Flash Write", sector, sector >> 16, buf, self.flashSectorSize)
        except UsbException as e:
            raise UsbException(dev().dev(), "Flash Write: " + self.flashStrError())

    @flashWriteSector.register(object, int, int, int)
    def flashWriteSector_0(self, sector, num, buf):
        """ generated source for method flashWriteSector_0 """
        if len(buf):
            raise IndexError(" < " + len(buf) + (num * self.flashSectorSize()))
        self.checkCapability(self.CAPABILITY_FLASH)
        if not self.flashEnabled():
            raise CapabilityException(self, "No Flash memory installed or")
        try:
            vendorCommand2(0x42, "Flash Write", sector, sector >> 16, buf, self.flashSectorSize * num)
        except UsbException as e:
            raise UsbException(dev().dev(), "Flash Write: " + self.flashStrError())

    def flashEnabled(self):
        """ generated source for method flashEnabled """
        if self.flashEnabled < 0:
            self.flashState()
        return self.flashEnabled == 1

    def flashSectorSize(self):
        """ generated source for method flashSectorSize """
        if self.flashSectorSize < 0:
            self.flashState()
        return self.flashSectorSize

    def flashSectors(self):
        """ generated source for method flashSectors """
        if self.flashSectors < 0:
            self.flashState()
        return self.flashSectors

    def flashSize(self):
        """ generated source for method flashSize """
        return self.flashSectorSize() * long(self.flashSectors())

    def printMmcState(self):
        """ generated source for method printMmcState """
        buf = [None]*23
        self.checkCapability(self.CAPABILITY_FLASH)
        vendorRequest2(0x43, "MMC State", 0, 0, buf, 23)
        print "status=" + Integer.toBinaryString(256 + (buf[0] & 255)).substring(1) + "." + Integer.toBinaryString(256 + (buf[1] & 255)).substring(1) + "   lastCmd=" + buf[3] + "   lastCmdResponse=" + Integer.toBinaryString(256 + (buf[4] & 255)).substring(1) + "   ec=" + buf[2] + "   BUSY=" + buf[22] + "   SDHC=" + buf[5] + "   buf=" + (buf[6] & 255) + " " + (buf[7] & 255) + " " + (buf[8] & 255) + " " + (buf[9] & 255) + " " + (buf[10] & 255) + " " + (buf[11] & 255) + "  " + (buf[12] & 255)
        return self.flashEnabled == 1

    @overloaded
    def flashUploadBitstream(self, fwFileName, bs):
        """ generated source for method flashUploadBitstream """
        secNum = 2048 / self.flashSectorSize
        bufferSize = secNum * self.flashSectorSize
        self.checkCapability(self.CAPABILITY_FPGA)
        self.checkCapability(self.CAPABILITY_FLASH)
        if not self.flashEnabled():
            raise CapabilityException(self, "No Flash memory installed or")
        self.getFpgaState()
        buffer_ = [None]*32768
        i = int()
        j = int()
        k = int()
        try:
            j = bufferSize
            while j == bufferSize and len(buffer_):
                buffer_[i] = [None]*bufferSize
                j = 0
                while True:
                    k = inputStream.read(buffer_[i], j, bufferSize - j)
                    if k < 0:
                        k = 0
                    j += k
                    if not ((j < bufferSize and k > 0)):
                        break
                i += 1
            try:
                inputStream.close()
            except Exception as e:
                System.err.println("Warning: Error closing file " + fwFileName + ": " + e.getLocalizedMessage())
        except IOException as e:
            raise BitstreamReadException(e.getLocalizedMessage())
        if bs < 0 or bs > 1:
            bs = self.detectBitstreamBitOrder(buffer_[0])
        if self.fpgaFlashBitSwap != (bs == 1):
            self.swapBits(buffer_, bufferSize * i)
        sector = [None]*flashSectorSize
        ID = str("ZTEXBS").getBytes()
        self.flashReadSector(0, sector)
        while k < 6:
            sector[k] = ID[k]
            k += 1
        sector[6] = 1
        sector[7] = 1
        k = (i - 1) * secNum + (j - 1) / self.flashSectorSize + 1
        sector[8] = int((k & 255))
        sector[9] = int(((k >> 8) & 255))
        k = ((j - 1) % self.flashSectorSize) + 1
        sector[10] = int((k & 255))
        sector[11] = int(((k >> 8) & 255))
        t0 = Date().getTime()
        self.flashWriteSector(0, sector)
        while k < i - 1:
            self.flashWriteSector(1 + k * secNum, secNum, buffer_[k])
            k += 1
        self.flashWriteSector(1 + k * secNum, (j - 1) / self.flashSectorSize + 1, buffer_[k])
        return Date().getTime() - t0

    @flashUploadBitstream.register(object, str)
    def flashUploadBitstream_0(self, fwFileName):
        """ generated source for method flashUploadBitstream_0 """
        return self.flashUploadBitstream(fwFileName, -1)

    def flashResetBitstream(self):
        """ generated source for method flashResetBitstream """
        self.checkCapability(self.CAPABILITY_FLASH)
        if not self.flashEnabled():
            raise CapabilityException(self, "No Flash memory installed or")
        sector = [None]*flashSectorSize
        ID = str("ZTEXBS").getBytes()
        self.flashReadSector(0, sector)
        k = 0
        while k < 6:
            if sector[k] != ID[k]:
                return
            k += 1
        if sector[6] != 1 or sector[7] != 1:
            return
        sector[8] = 0
        sector[9] = 0
        self.flashWriteSector(0, sector)

    def flashFirstFreeSector(self):
        """ generated source for method flashFirstFreeSector """
        self.checkCapability(self.CAPABILITY_FLASH)
        if not self.flashEnabled():
            raise CapabilityException(self, "No Flash memory installed or")
        sector = [None]*flashSectorSize
        ID = str("ZTEXBS").getBytes()
        self.flashReadSector(0, sector)
        k = 0
        while k < 6:
            if sector[k] != ID[k]:
                return 0
            k += 1
        if sector[6] != 1 or sector[7] != 1:
            return 0
        return (sector[8] & 255) + ((sector[9] & 255) << 8) + 1

    def debugStackSize(self):
        """ generated source for method debugStackSize """
        self.checkCapability(self.CAPABILITY_DEBUG)
        if self.debugStackSize <= 0 or self.debugMsgSize <= 0:
            vendorRequest2(0x28, "Read debug data", 0, 0, buf, 4)
            self.debugStackSize = buf[2] & 255
            self.debugMsgSize = buf[3] & 255
        return self.debugStackSize

    def debugMsgSize(self):
        """ generated source for method debugMsgSize """
        self.checkCapability(self.CAPABILITY_DEBUG)
        if self.debugMsgSize <= 0:
            self.debugStackSize()
        return self.debugMsgSize

    def debugLastMsg(self):
        """ generated source for method debugLastMsg """
        return self.debugLastMsg

    def debugReadMessages(self, all, buf):
        """ generated source for method debugReadMessages """
        self.checkCapability(self.CAPABILITY_DEBUG)
        buf2 = [None]*debugStackSize() * debugMsgSize() + 4
        vendorRequest2(0x28, "Read debug data", 0, 0, buf2, )
        lm = (buf2[0] & 255) | ((buf2[1] & 255) << 8)
        self.debugNewMessages = lm - self.debugLastMsg
        r = Math.min(Math.min(len(buf), self.debugStackSize), lm)
        if not all:
            r = Math.min(r, self.debugNewMessages)
        i = 0
        while i < r:
            while j < self.debugMsgSize:
                buf[i * self.debugMsgSize + j] = buf2[k * self.debugMsgSize + j + 4]
                j += 1
            i += 1
        self.debugLastMsg = lm
        return r

    @overloaded
    def xmegaStrError(self, errNum):
        """ generated source for method xmegaStrError """
        if errNum==self.XMEGA_EC_NO_ERROR:
            return "USB error: " + LibusbJava.usb_strerror()
        elif errNum==self.XMEGA_EC_PDI_READ_ERROR:
            return "PDI read error"
        elif errNum==self.XMEGA_EC_NVM_TIMEOUT:
            return "NVM timeout error"
        elif errNum==self.XMEGA_EC_INVALID_DEVICE:
            return "Invalid or unsupported ATxmega"
        elif errNum==self.XMEGA_EC_ADDRESS_ERROR:
            return "Address error (invalid address or wrong page size)"
        elif errNum==self.XMEGA_EC_NVM_BUSY:
            return "NVM busy"
        return "Error " + errNum

    @xmegaStrError.register(object)
    def xmegaStrError_0(self):
        """ generated source for method xmegaStrError_0 """
        try:
            return self.xmegaStrError(xmegaState())
        except Exception as e:
            return "Unknown error (Error receiving error code: " + e.getLocalizedMessage() + ")"

    def xmegaState(self):
        """ generated source for method xmegaState """
        buf = [None]*7
        self.checkCapability(self.CAPABILITY_XMEGA)
        vendorRequest2(0x48, "Xmega state", 0, 0, buf, 7)
        self.xmegaEC = buf[0] & 255
        self.xmegaFlashPages = ((buf[2] & 255) << 8) | (buf[1] & 255)
        self.xmegaEepromPages = ((buf[4] & 255) << 8) | (buf[3] & 255)
        self.xmegaFlashPageSize = 1 << (buf[5] & 15)
        self.xmegaEepromPageSize = 1 << (buf[6] & 15)
        return self.xmegaEC

    def xmegaEnabled(self):
        """ generated source for method xmegaEnabled """
        if self.xmegaFlashPages < 0 or self.xmegaEepromPages < 0:
            self.xmegaState()
        return self.xmegaFlashPages > 0 and self.xmegaEepromPages > 0

    def xmegaFlashPages(self):
        """ generated source for method xmegaFlashPages """
        if self.xmegaFlashPages < 0 or self.xmegaEepromPages < 0:
            self.xmegaState()
        return self.xmegaFlashPages

    def xmegaEepromPages(self):
        """ generated source for method xmegaEepromPages """
        if self.xmegaFlashPages < 0 or self.xmegaEepromPages < 0:
            self.xmegaState()
        return self.xmegaEepromPages

    def xmegaFlashPageSize(self):
        """ generated source for method xmegaFlashPageSize """
        if self.xmegaFlashPages < 0 or self.xmegaEepromPages < 0:
            self.xmegaState()
        return self.xmegaFlashPageSize

    def xmegaEepromPageSize(self):
        """ generated source for method xmegaEepromPageSize """
        if self.xmegaFlashPages < 0 or self.xmegaEepromPages < 0:
            self.xmegaState()
        return self.xmegaEepromPageSize

    def xmegaReset(self):
        """ generated source for method xmegaReset """
        self.checkCapability(self.CAPABILITY_XMEGA)
        try:
            vendorCommand(0x49, "XMEGA Reset")
        except UsbException as e:
            raise UsbException(dev().dev(), "NVM Reset: " + self.xmegaStrError())

    def xmegaNvmRead(self, addr, buf, length):
        """ generated source for method xmegaNvmRead """
        self.checkCapability(self.CAPABILITY_XMEGA)
        try:
            vendorRequest2(0x4a, "XMEGA NVM Read", addr, addr >> 16, buf, length)
        except UsbException as e:
            raise UsbException(dev().dev(), "NVM Read: " + self.xmegaStrError())
        try:
            Thread.sleep(3)
        except InterruptedException as e:
            pass

    def xmegaFlashRead(self, addr, buf, length):
        """ generated source for method xmegaFlashRead """
        self.checkCapability(self.CAPABILITY_XMEGA)
        try:
            vendorRequest2(0x4b, "XMEGA Flash Read", addr, addr >> 16, buf, length)
        except UsbException as e:
            raise UsbException(dev().dev(), "XMEGA Flash Read: " + self.xmegaStrError())
        try:
            Thread.sleep(3)
        except InterruptedException as e:
            pass

    def xmegaEepromRead(self, addr, buf, length):
        """ generated source for method xmegaEepromRead """
        self.checkCapability(self.CAPABILITY_XMEGA)
        try:
            vendorRequest2(0x4c, "XMEGA EEPROM Read", addr, addr >> 16, buf, length)
        except UsbException as e:
            raise UsbException(dev().dev(), "XMEGA EEPROM Read: " + self.xmegaStrError())
        try:
            Thread.sleep(3)
        except InterruptedException as e:
            pass

    @overloaded
    def xmegaFuseRead(self, addr, buf, length):
        """ generated source for method xmegaFuseRead """
        self.checkCapability(self.CAPABILITY_XMEGA)
        try:
            vendorRequest2(0x4d, "XMEGA Fuse Read", addr, addr >> 16, buf, length)
        except UsbException as e:
            raise UsbException(dev().dev(), "XMEGA Fuse Read: " + self.xmegaStrError())
        try:
            Thread.sleep(3)
        except InterruptedException as e:
            pass

    @xmegaFuseRead.register(object, int)
    def xmegaFuseRead_0(self, addr):
        """ generated source for method xmegaFuseRead_0 """
        buf = [None]*1
        self.checkCapability(self.CAPABILITY_XMEGA)
        try:
            vendorRequest2(0x4d, "XMEGA Fuse Read", addr, 0, buf, 1)
        except UsbException as e:
            raise UsbException(dev().dev(), "XMEGA Fuse Read: " + self.xmegaStrError())
        try:
            Thread.sleep(3)
        except InterruptedException as e:
            pass
        return buf[0] & 255

    def xmegaFlashPageWrite(self, addr, buf):
        """ generated source for method xmegaFlashPageWrite """
        self.checkCapability(self.CAPABILITY_XMEGA)
        if len(buf):
            raise IndexError(" < " + len(buf) + self.xmegaFlashPageSize)
        try:
            vendorCommand2(0x4b, "XMEGA Flash page write", addr, addr >> 16, buf, self.xmegaFlashPageSize)
        except UsbException as e:
            raise UsbException(dev().dev(), "XMEGA Flash page write: " + self.xmegaStrError())
        try:
            Thread.sleep(3)
        except InterruptedException as e:
            pass

    def xmegaEepromPageWrite(self, addr, buf):
        """ generated source for method xmegaEepromPageWrite """
        self.checkCapability(self.CAPABILITY_XMEGA)
        if len(buf):
            raise IndexError(" < " + len(buf) + self.xmegaEepromPageSize)
        try:
            vendorCommand2(0x4c, "XMEGA EEPROM page write", addr, addr >> 16, buf, self.xmegaEepromPageSize)
        except UsbException as e:
            raise UsbException(dev().dev(), "XMEGA EEPROM page write: " + self.xmegaStrError())
        try:
            Thread.sleep(3)
        except InterruptedException as e:
            pass

    def xmegaFuseWrite(self, addr, val):
        """ generated source for method xmegaFuseWrite """
        self.checkCapability(self.CAPABILITY_XMEGA)
        try:
            vendorCommand(0x4d, "XMEGA Fuse write", val, addr)
        except UsbException as e:
            raise UsbException(dev().dev(), "XMEGA Fuse write: " + self.xmegaStrError())
        try:
            Thread.sleep(3)
        except InterruptedException as e:
            pass

    def xmegaIhxWrite(self, toFlash, ihxFile):
        """ generated source for method xmegaIhxWrite """
        maxTries = 3
        pageSize = self.xmegaFlashPageSize() if toFlash else self.xmegaEepromPageSize()
        self.checkCapability(self.CAPABILITY_XMEGA)
        t0 = Date().getTime()
        buf1 = [None]*pageSize
        buf2 = [None]*pageSize
        i = 0
        while i < 65536:
            while (j < pageSize) and (i + j < 65536):
                b |= d
                c &= d
                j += 1
            if b:
                if not c:
                    if toFlash:
                        self.xmegaFlashRead(i, buf1, pageSize)
                    else:
                        self.xmegaEepromRead(i, buf1, pageSize)
                while (j < pageSize) and (i + j < 65536):
                    if (ihxFile.ihxData[i + j] >= 0) and (ihxFile.ihxData[i + j] <= 255):
                        buf1[j] = int(ihxFile.ihxData[i + j])
                    j += 1
                while b:
                    if toFlash:
                        self.xmegaFlashPageWrite(i, buf1)
                    else:
                        self.xmegaEepromPageWrite(i, buf1)
                    if toFlash:
                        self.xmegaFlashRead(i, buf2, pageSize)
                    else:
                        self.xmegaEepromRead(i, buf2, pageSize)
                    b = False
                    while (j < pageSize) and (not b):
                        b |= buf1[j] != buf2[j]
                        j += 1
                    if b:
                        if k < maxTries:
                            System.err.println("Warning: xmegaWriteFirmware: Verification of " + ("Flash" if toFlash else "EEPROM") + " page" + i + " failed (try " + k + ")")
                        else:
                            System.err.println("Warning: xmegaWriteFirmware: Verification of " + ("Flash" if toFlash else "EEPROM") + " page " + i + " failed")
                    b = False
                    k += 1
            i += pageSize
        return Date().getTime() - t0

    def xmegaWriteFirmware(self, ihxFile):
        """ generated source for method xmegaWriteFirmware """
        return self.xmegaIhxWrite(True, ihxFile)

    def xmegaWriteEeprom(self, ihxFile):
        """ generated source for method xmegaWriteEeprom """
        return self.xmegaIhxWrite(False, ihxFile)

    def __str__(self):
        """ generated source for method toString """
        str_ = dev().__str__()
        try:
            str_ += "\n   " + self.getFpgaConfigurationStr()
        except Exception as e:
            pass
        return str_

    def capabilityInfo(self, pf):
        """ generated source for method capabilityInfo """
        str_ = ""
        i = 0
        while i < 6:
            while j < 8:
                if dev().interfaceCapabilities(i, j):
                    if not str_ == "":
                        str_ += pf
                    if len(capabilityStrings):
                        str_ += self.capabilityStrings[i * 8 + j]
                    else:
                        str_ += i + "." + j
                j += 1
            i += 1
        return str_

    def configureFpgaHS(self, fwFileName, force, bs):
        """ generated source for method configureFpgaHS """
        transactionBytes = 16384
        t0 = 0
        settings = [None]*2
        releaseIF = bool()
        self.checkCapability(self.CAPABILITY_HS_FPGA)
        vendorRequest2(0x33, "getHSFpgaSettings", settings, 2)
        if not force and self.getFpgaConfiguration():
            raise AlreadyConfiguredException()
        releaseIF = not getInterfaceClaimed(settings[1] & 255)
        buffer_ = [None]*16 * 1024 * 1024 / transactionBytes
        size = 0
        try:
            while j == transactionBytes and len(buffer_):
                buffer_[i] = [None]*transactionBytes
                j = 0
                while True:
                    k = inputStream.read(buffer_[i], j, transactionBytes - j)
                    if k < 0:
                        k = 0
                    j += k
                    if not ((j < transactionBytes and k > 0)):
                        break
                size += j
                i += 1
            try:
                inputStream.close()
            except Exception as e:
                System.err.println("Warning: Error closing file " + fwFileName + ": " + e.getLocalizedMessage())
        except IOException as e:
            raise BitstreamReadException(e.getLocalizedMessage())
        if size < 64:
            raise BitstreamReadException("Invalid file size: " + size)
        if bs < 0 or bs > 1:
            bs = self.detectBitstreamBitOrder(buffer_[0])
        if bs == 1:
            self.swapBits(buffer_, size)
        if releaseIF:
            claimInterface(settings[1] & 255)
        tries = 3
        while tries > 0:
            vendorCommand(0x34, "initHSFPGAConfiguration")
            try:
                t0 = -Date().getTime()
                while i * transactionBytes < size and len(buffer_):
                    if j > transactionBytes:
                        j = transactionBytes
                    if j > 0:
                        if l < 0:
                            raise UsbException("Error sending Bitstream: " + l + ": " + LibusbJava.usb_strerror())
                        elif l != j:
                            raise UsbException("Error sending Bitstream: Sent " + l + " of " + j + " bytes")
                    i += 1
                try:
                    Thread.sleep((size % transactionBytes) / 1000 + 10)
                except InterruptedException as e:
                    pass
                vendorCommand(0x35, "finishHSFPGAConfiguration")
                t0 += Date().getTime()
                self.getFpgaState()
                if not self.fpgaConfigured:
                    raise BitstreamUploadException("FPGA configuration failed: DONE pin does not go high, possible USB transfer errors (INIT_B_HIST=" + self.fpgaInitB + ("" if self.fpgaBytes == 0 else "; " + (size - self.fpgaBytes) + " bytes got lost") + ")")
                if self.enableExtraFpgaConfigurationChecks:
                    if self.fpgaBytes != 0 and self.fpgaBytes != size:
                        System.err.println("Warning: Possible FPGA configuration data loss: " + (size - self.fpgaBytes) + " bytes got lost")
                    if self.fpgaInitB != 222:
                        System.err.println("Warning: Possible Bitstream CRC error: INIT_B_HIST=" + self.fpgaInitB)
                tries = 0
            except BitstreamUploadException as e:
                if tries == 1:
                    raise e
                elif tries < 3 or self.enableExtraFpgaConfigurationChecks:
                    System.err.println("Warning: " + e.getLocalizedMessage() + ": Retrying it ...")
            tries -= 1
        if releaseIF:
            releaseInterface(settings[1] & 255)
        try:
            Thread.sleep(25)
        except InterruptedException as e:
            pass
        return t0

    @overloaded
    def configureFpga(self, fwFileName, force, bs):
        """ generated source for method configureFpga """
        try:
            return self.configureFpgaHS(fwFileName, force, bs)
        except CapabilityException as e:
            return self.configureFpgaLS(fwFileName, force, bs)
        except UsbException as e:
            System.err.println("Warning: High speed FPGA configuration failed, trying low speed mode:" + e.getLocalizedMessage() + ": Trying low speed mode")
            return self.configureFpgaLS(fwFileName, force, bs)
        except BitstreamUploadException as e:
            System.err.println("Warning: High speed FPGA configuration failed, trying low speed mode:" + e.getLocalizedMessage() + ": Trying low speed mode")
            return self.configureFpgaLS(fwFileName, force, bs)

    @configureFpga.register(object, str, bool)
    def configureFpga_0(self, fwFileName, force):
        """ generated source for method configureFpga_0 """
        return self.configureFpga(fwFileName, force, -1)

    def macEepromWrite(self, addr, buf, length):
        """ generated source for method macEepromWrite """
        self.checkCapability(self.CAPABILITY_MAC_EEPROM)
        buf2 = [None]*8
        ptr = 0
        while length > 0:
            while j < i:
                buf2[j] = buf[ptr + j]
                j += 1
            vendorCommand2(0x3C, "MAC EEPROM Write", addr, 0, buf2, i)
            try:
                Thread.sleep(10)
            except InterruptedException as e:
                pass
            addr += i
            length -= i
            ptr += i

    def macEepromRead(self, addr, buf, length):
        """ generated source for method macEepromRead """
        self.checkCapability(self.CAPABILITY_MAC_EEPROM)
        vendorRequest2(0x3B, "MAC EEPROM Read", addr, 0, buf, length)
        try:
            Thread.sleep(10)
        except InterruptedException as e:
            pass

    def macEepromState(self):
        """ generated source for method macEepromState """
        buf = [None]*1
        self.checkCapability(self.CAPABILITY_MAC_EEPROM)
        vendorRequest2(0x3D, "MAC EEPROM State", 0, 0, buf, 1)
        return buf[0] == 0

    def macRead(self, buf):
        """ generated source for method macRead """
        if len(buf):
            raise IndexError("macRead: Buffer smaller than 6 Bytes")
        self.macEepromRead(250, buf, 6)

    def numberOfFpgas(self):
        """ generated source for method numberOfFpgas """
        if self.numberOfFpgas < 0:
            try:
                self.checkCapability(self.CAPABILITY_MULTI_FPGA)
                vendorRequest2(0x50, "getMultiFpgaInfo", buffer_, 3)
                self.numberOfFpgas = (buffer_[0] & 255) + 1
                self.selectedFpga = buffer_[1] & 255
                self.parallelConfigSupport = buffer_[2] == 1
            except CapabilityException as e:
                self.numberOfFpgas = 1
                self.selectedFpga = 0
                self.parallelConfigSupport = False
        return self.numberOfFpgas

    def selectFpga(self, num):
        """ generated source for method selectFpga """
        self.numberOfFpgas()
        if num < 0 or num >= self.numberOfFpgas:
            raise IndexError("selectFPGA: Invalid FPGA number")
        if self.numberOfFpgas != 1:
            try:
                self.checkCapability(self.CAPABILITY_MULTI_FPGA)
                vendorCommand(0x51, "selectFPGA", num, 0)
            except CapabilityException as e:
                pass
        self.selectedFpga = num

    def tempSensorRead(self, idx):
        """ generated source for method tempSensorRead """
        xIdx = [3, 4, 1, 2]
        self.checkCapability(self.CAPABILITY_TEMP_SENSOR)
        len = 0
        if self.tempSensorUpdateInterval < 40:
            self.tempSensorUpdateInterval = 40
        if Date().getTime() > self.lastTempSensorReadTime + self.tempSensorUpdateInterval:
            len = vendorRequest(0x58, "Temperature Sensor Read", 0, 0, self.tempSensorBuf, )
            self.lastTempSensorReadTime = Date().getTime()
            if len != 5 or self.tempSensorBuf[0] != 1:
                raise InvalidFirmwareException("tempSensorRead: Invalid temperature sensor protocol")
        if idx < 0 or idx > 3:
            raise IndexError("tempSensorRead: Invalid temperature sensor index")
        return ((self.tempSensorBuf[xIdx[idx]] & 255) - 77.2727) / 1.5454

