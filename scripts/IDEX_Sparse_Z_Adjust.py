#!/usr/bin/python3

#  For some reason in PrusaSlicer 2.4 Sparse Wipe towers start a little higher than the bottom layer height.
#  This post processor reacts to a directive in the Tool Change Gcode and introduces an adjustment to the Z height before
#   The Wipe tower layers are drawn

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

count = 0
G1Z=""

#G1 Z.3 F12000 ; Travel down to the last wipe tower layer.
#;IDEX Adjusted for SPARSE Z -  *** THIS ONE LOOKS GOOD TO ADJUST
#;IDEX_SPARSE_Z_ADJUST=-0.1

def check_float(potential_float):
    try:
        float(potential_float)
        # Try to convert argument into a float
        return True
    except ValueError:
        return False


count=0
errors = 0
bSparceTower = False
fAdjust = 0
# Check to see if ; wipe_tower_no_sparse_layers = 1

for lIndex in range(len(lines)):
    if lines[lIndex].startswith("; wipe_tower_no_sparse_layers = 1"):
        bSparceTower = True

if bSparceTower == True:
    os.rename(sourceFile,sourceFile+".idexsparsez.txt")

    with open(destFile, "w") as of:
        for lIndex in range(len(lines)):
            oline = lines[lIndex]
            # Parse gcode line
            if "Travel down to the last wipe tower layer" in oline and oline.startswith("G1 Z") and fAdjust != 0:
                # Store G1 Z for possible later adjustment
                G1Z = oline
                G1Zsplit = G1Z.split()
                sCurrentZ = G1Zsplit[1];
                fCurrentZ = float(sCurrentZ[1:])
                fNewZ = fCurrentZ + fAdjust;
                G1Zsplit[1] = "Z"+"{:.2f}".format(fNewZ)
                G1Znew = " ".join(G1Zsplit)
                of.write(G1Znew+" ;IDEX Adjusted\n");
                count = count + 1
            elif oline.startswith(";IDEX_SPARSE_Z_ADJUST="):
                adjust = oline.split("=")[1].strip()
                if check_float(adjust):
                    fAdjust = float(adjust)
                    of.write(";IDEX Picked by Sparse Adjuster:"+oline);
                else:
                    of.write(";IDEX Number error:" + oline);
                    errors=errors+1
            else:
                # Write original line       
                of.write(oline)
                
        of.write(";****\n;****IDEX_SPARSE_Z    " + str(count) + " lines adjusted," + str(errors) +"errors\n") 
        of.close()
f.close()






