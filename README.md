Windows Registry VBIOS export script
====================================

Simple script for exporting GPU BIOS (VBIOS) from Windows Registry.
This script could be useful mostly on laptops in case that every other option was failed.


Most recommended tools for exporting VBIOS
------------------------------------------

* [GPU-Z](https://www.techpowerup.com/download/techpowerup-gpu-z/)

* [NVFlash](https://www.techpowerup.com/download/nvidia-nvflash/)

Those tools can read VBIOS directly from GPU, but they can fail on laptops.


Some alternative ways for exporting VBIOS
-----------------------------------------

* [VBiosFinder](https://github.com/coderobe/VBiosFinder)

* [UEFITool](https://github.com/LongSoft/UEFITool)

Those tools can be used unpack VBIOS update installers and find VBIOS ROMs.


Extracting VBIOS from Windows Registry
--------------------------------------

If you already tried the recommended ways to export you VBIOS and failed,
then you can try this script.

**Requirements:**

* Windows running in bare-metal mode
* NVIDIA GPU with installed drivers
* [Python](https://python.org/) 3.2+

**Usage:**

Open Windows CMD (Command Promt) and run:
```
python vbios_from_reg.py
```

Expected output:
```
Found display class
Found NVIDIA display adaptor
VBIOS saved to file "vbios.rom"
```
