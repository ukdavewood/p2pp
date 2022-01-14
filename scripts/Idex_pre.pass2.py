#!/usr/bin/python3

# V1  - Initial creation



import sys
import re
import os

sourceFile=sys.argv[1]

#  Output file from P2PP after pass1 not required
os.rename(sourceFile,sourceFile+".pre_pass2.bak")


# Instead Read the ENTIRE g-code file prior to pass1 into memory
with open(sourceFile+".pre_pass1.bak" , "r") as f:
    lines = f.readlines()

destFile = sourceFile

count = 0

ignore = False
ExtTranslate = [];
MultiColourExtruder = "";

with open(destFile, "w") as of:
    for lIndex in range(len(lines)):
        oline = lines[lIndex]
        # Parse gcode line
        if oline.startswith(";IDEX_PASS2_MULTICOLOUR"):
           MultiColourExtruder = oline.strip().split("=")[1];
        if oline.startswith(";IDEX_PASS2_TRANSLATE:"):   # Extruder translations
            ExtTranslate = oline[len(";IDEX_PASS2_TRANSLATE:"):].strip().split(",");
            for trans in ExtTranslate:
                of.write(";IDEX Picked up: " + trans + "\n");
                   
        elif oline.startswith("T"):  # Translate  extruders
            translated = False
            for trans in ExtTranslate:
                if oline.startswith(trans.split("=")[0]):
                    oline2=oline.strip().replace(trans.split("=")[0],trans.split("=")[1]) + " ;IDEX translated Tx: " + trans + "\n"; 
                    of.write(oline2)
                    count = count + 1
                    translated = True
                    of.write(";IDEX Original line:" + oline)
            if translated == False:
                of.write(oline)            
        else:
            # Write original line       
            of.write(oline)

            
    of.write(";****\n;****IDEX_pass2 " + str(count) + " translations performed\n") 
of.close()
f.close()






