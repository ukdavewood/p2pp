#!/usr/bin/python3

# V2 - removed G1 Z from ignore list - to overcome P2PP Z correction problem


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
os.rename(sourceFile,sourceFile+".idex.bak")

count = 0

ignore = False

with open(destFile, "w") as of:
    for lIndex in range(len(lines)):
        oline = lines[lIndex]
        # Parse gcode line
        if oline.startswith(";IDEX_START_IGNORE"):
            ignore = True 
            count = count + 1
        if oline.startswith(";IDEX_END_IGNORE"):
            ignore = False 
        
        if oline.startswith("T4 ; change extruder"):
            of.write(";IDEX_REMOVE:" + oline);
        elif ignore and oline.startswith(";IDEX_ADD:") is not True:
            if oline.startswith("G1 Z") is True:
                of.write(oline);  # write G1 Z line for P2PP to pick up and remove to Z correction
            # Add comment to front of line so that P2PP ignores it
            of.write(";IDEX_ADD:" + oline)
        else:
            # Write original line       
            of.write(oline)
            
    of.write(";****\n;****IDEX_pre " + str(count) + " sections processed\n") 
of.close()
f.close()






