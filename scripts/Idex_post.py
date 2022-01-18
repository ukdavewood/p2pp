#!/usr/bin/python3

# Based on example from Bobs Notebook. - https://projects.ttlexceeded.com/3dprinting_prusaslicer_post-processing.html

import sys
import re
import os
import tkinter
from tkinter import messagebox


sourceFile=sys.argv[1]

# Read the ENTIRE g-code file into memory
with open(sourceFile, "r") as f:
    lines = f.readlines()

destFile = sourceFile
os.rename(sourceFile,sourceFile+".idexpost.bak")

count = 0
toolUnload=";IDEX Tool unload not captured"

with open(destFile, "w") as of:
    for lIndex in range(len(lines)):
        oline = lines[lIndex]
        # Parse gcode line
        if oline.startswith("; [--P2PP-- tool unload] - G1 Z"):
            # Store ignored unload for later IDEX_ADD_G1 Z
            toolUnload = oline[len("; [--P2PP-- tool unload] - "):]
            of.write(oline )
        elif oline.startswith(";IDEX_ADD:;IDEX_ADD_G1_Z") :
            of.write(toolUnload + ";IDEX_ADD_G1_Z\n")
        elif oline.startswith(";IDEX_ADD:"):
            # Remove comment from front of line
            of.write(oline[len(";IDEX_ADD:"):])
            count = count + 1
        else:
            # Write original line       
            of.write(oline)
            
    of.write(";****\n;****IDEX_post    " + str(count) + " lines added back\n") 
of.close()
f.close()






