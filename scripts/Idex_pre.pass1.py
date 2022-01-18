#!/usr/bin/python3

# V2 - removed G1 Z from ignore list - to overcome P2PP Z correction problem
# V3 - Added Pass1 logic -
#  Note there may still need to be some work related to SPLICEOFFSET - as it seems to be added on
# Based on example from Bobs Notebook. - https://projects.ttlexceeded.com/3dprinting_prusaslicer_post-processing.html



import sys
import re
import os
import tkinter
from tkinter import messagebox


def swaparound(line,Trans):
    line1 = line.strip().split(" = ")
    delimiter = ";"
    line2 = line1[1].split(delimiter)
    if len(line2) < 2:
        delimiter = ","
        line2 = line1[1].split(delimiter)
        
    for tran in Trans:
        f = int(tran.split("=")[0][1:])
        t = int(tran.split("=")[1][1:])
        try:
            line2[t] = line2[f]  
        except:
            return "*** ERROR:" + str(t) + "," + str(len(line2)) 
        
    line1[1] = delimiter.join(line2)
    
    
        
    return " = ".join(line1) + "\n"
    


sourceFile=sys.argv[1]

# Read the ENTIRE g-code file into memory
with open(sourceFile, "r") as f:
    lines = f.readlines()

destFile = sourceFile
os.rename(sourceFile,sourceFile+".pre_pass1.bak")

count = 0
patchcount = 0

ignore = False
ExtTranslate = [];
ExtSwaparound = [];

StartGCRepl = [];



with open(destFile, "w") as of:
    for lIndex in range(len(lines)):
        oline = lines[lIndex]
        # Parse gcode line
        if oline.startswith(";IDEX_PASS1_TRANSLATE:"):   # Extruder translations
            ExtTranslate = oline[len(";IDEX_PASS1_TRANSLATE:"):].strip().split(",");
            for trans in ExtTranslate:
                of.write(";IDEX Picked up: " + trans + "\n");
                
        if oline.startswith(";IDEX_PASS1_SWAPAROUND1:"):  # Extruder details to swap around
            ExtSwaparound = oline[len(";IDEX_PASS1_SWAPAROUND1:"):].strip().split(",");
            for swap in ExtSwaparound:
                of.write(";IDEX Picked up: " + swap + "\n");

        if oline.startswith(";IDEX_PASS1_START_GCODE_REPL:"):
            StartGCRepl=oline[len(";IDEX_PASS1_START_GCODE_REPL:"):].strip().split(",");
            for patch in StartGCRepl:
                of.write(";IDEX Picked up: " + patch + "\n");

        if oline.startswith(";IDEX_START_IGNORE_PASS1"):
            ignore = True 
            count = count + 1
        if oline.startswith(";IDEX_END_IGNORE_PASS1"):
            ignore = False 
           
        if ignore and oline.startswith(";IDEX_ADD:") is not True:
            if oline.startswith("G1 Z") is True:
                of.write(oline);  # write G1 Z line for P2PP to pick up and remove to Z correction
            # Add comment to front of line so that P2PP ignores it
            # of.write(";IDEX_HIDE:" + oline)

        
        elif oline.startswith("T"):  # Translate and remaining extruders

            for trans in ExtTranslate:
                if oline.startswith(trans.split("=")[0]):
                    oline2=oline.strip().replace(trans.split("=")[0],trans.split("=")[1]) + " ;IDEX translated Tx: " + trans + "\n"; 
                    of.write(oline2)
            of.write(";IDEX_ADD:" + oline)
            
        elif oline.startswith("; start_gcode = "):  # Start Gcode patching
            for patch in StartGCRepl:
                oline = oline.replace(patch.split(">")[0],patch.split(">")[1]);
                patchcount = patchcount + 1
            of.write(oline);
            of.write(";IDEX PATCHED\n");

        else:
            # Check for swap arounds
            swapped = False
            for swap in ExtSwaparound:
                if oline.startswith("; "+swap): 
                    swapped = True;
                    of.write(swaparound(oline,ExtTranslate))
                    
                    of.write(";IDEX_SWAPPED:" + oline)
                    
            if not swapped:
                # Write original line       
                of.write(oline)

            
    of.write(";****\n;****IDEX_pass1 " + str(count) + " sections processed, " + str(patchcount) + " patches done\n") 
of.close()
f.close()






