#!/usr/bin/python3

# V2 - removed G1 Z from ignore list - to overcome P2PP Z correction problem
# Based on example from Bobs Notebook. - https://projects.ttlexceeded.com/3dprinting_prusaslicer_post-processing.html


import sys
import re
import os
import tkinter

def closeenough(colour1, colour2):
    print(colour1,colour2)
    difference = (int(colour1[1:3],16)-int(colour2[1:3],16)) ** 2 + (int(colour1[3:5],16)-int(colour2[3:5],16)) ** 2 + (int(colour1[5:7],16)-int(colour2[5:7],16)) ** 2
    print(difference)
   
    if difference < 256*10:
        return True
    else:
        return False 

sourceFile=sys.argv[1]

# Read the ENTIRE g-code file into memory
with open(sourceFile, "r") as f:
    lines = f.readlines()

destFile = sourceFile
os.rename(sourceFile,sourceFile+".idexcol.bak")

count = 0

ignore = False

Conversions = []


with open(destFile, "w") as of:
    for lIndex in range(len(lines)):
        oline = lines[lIndex]
        # Parse gcode line
        
        if oline.startswith(";IDEX P2PPCOLCONV="):
            entry = oline.strip().split("=")
            Conversions.append(entry[1].split(","))
            of.write(";IDEX COLLECTED:" + oline);
        elif oline.startswith("; extruder_colour = ") or oline.startswith("; filament_colour = "):
            colourline = oline.strip().split(" = ")
            print(oline)
            colours = colourline[1].split(";")
            
            for c in range(len(colours)):
                if colours[c] != "":
                    for conversion in Conversions:
                        if closeenough(conversion[0],colours[c]):
                            print(colours[c],conversion[1],conversion[2])
                            colours[c] = conversion[1]
                            count = count + 1
                            break;
                        

            if count > 0:
                of.write(";IDEX Colours translated from:" + oline);
                of.write(colourline[0] + " = " + ";".join(colours)+"\n")
                        
                
        else:
            # Write original line       
            of.write(oline)
            
    of.write(";****\n;****IDEX_col " + str(count) + " colours changed\n") 
of.close()
f.close()






