#!/usr/bin/python3

# Script to take P2PP output and change the colours in the generated Palette2 input file to match filament names

# Based on example from Bobs Notebook. - https://projects.ttlexceeded.com/3dprinting_prusaslicer_post-processing.html


import sys
import re
import os

sourceFile=sys.argv[1]

# Read the ENTIRE g-code file into memory
with open(sourceFile, "r") as f:
    lines = f.readlines()

destFile = sourceFile
os.rename(sourceFile,sourceFile+".preCol.bak")


outname = os.environ["SLIC3R_PP_OUTPUT_NAME"]
mafFile = outname.replace(".mcf.gcode",".mcf.maf")
print(mafFile)

# ;P2PP ACCESSORYMODE_MAF
AccessoryMode = ""

# ; filament_colour = #EEB610;#0C0C0C;#1EA4F2;#42171A;#228A42;#D5571E;#EFEFEF
filament_colour = []

# ; extruder_colour = ;;;;;;
extruder_colour = []

# ; filament_settings_id = "PETG 17 YELLOW ArtistD";"PETG 02 BLACK ARTISTD";"PETG 19 BLUE ArtistD";"PETG 14 BROWN ArtistD";"PETG 15 GREEN ArtistD";"PETG 03 ORANGE ArtistD";"PETG 13 CLEAR ArtistD"
filament_settings_id  = []


print("Pass1 collect data")

for lIndex in range(len(lines)):
        oline = lines[lIndex]
        # Parse gcode line
        
        if oline.startswith("; filament_colour = "):
            filament_colour = oline.strip().split(" = ")[1].split(";")
            
        if oline.startswith("; start_gcode = "):
            for line in oline.strip().split(" = ")[1].split("\\n"):
                # print(line)
                if line.startswith(";P2PP ACCESSORYMODE_MAF"):
                    AccessoryMode = line

        if oline.startswith("; extruder_colour = "):
            extruder_colour = oline.strip().split(" = ")[1].split(";")

        if oline.startswith("; filament_settings_id = "):
            filament_settings_id = oline.strip().split(" = ")[1].split(";")            
 
 
print("AM:",AccessoryMode)
print("FC:",filament_colour) 
print("EC:",extruder_colour)
print("FSI:",filament_settings_id)

#            omega_str += " D{}{}{}{}".format(v.used_filament_types.index(v.filament_type[i]) + 1,
#                                             v.filament_color_code[i].strip("\n"),
#                                             find_nearest_colour(v.filament_color_code[i].strip("\n")),
#                                             v.filament_type[i].strip("\n")
#                                             )
            
#Pass2

if AccessoryMode == "":
    O25patched = False
    with open(destFile, "w") as of:
        for lIndex in range(len(lines)):
            oline = lines[lIndex]
            # Parse gcode line
            
            if oline.startswith("O25 "):
                print("O25:",oline)
                O25out = "O25"
                O25in = oline.strip().split()
                for n in range(1,len(O25in)):
                    print(O25in[n])
                    if len(extruder_colour) > n and extruder_colour[n-1] != "":
                        O25out = O25out + " " + O25in[n]
                        print("No change due to filament colour being specified")
                    else:
                        O25new = O25in[n][0:8]+filament_settings_id[n-1].replace(" ","_").replace("\"","")
                        print(O25new)
                        O25out = O25out + " " + O25new 
                        O25patched = True
                of.write(O25out+"\n")
            else:
                of.write(oline)
                
        if O25patched:                
            of.write(";****\n;****IDEX_postColour - O25 line patched\n") 
        else:
            of.write(";****\n;****IDEX_postColour - O25 line NOT patched\n") 
        
    of.close()
else:
    # Process MAF file instead 
    
    print(mafFile)
    
    with open(mafFile, "r") as m:
        maflines = m.readlines()
        
    destMafFile = mafFile
    os.rename(mafFile,mafFile+".bak")
    
    m.close()
    

    O25patched = False
    with open(mafFile, "w") as mof:
        for lIndex in range(len(maflines)):
            oline = maflines[lIndex]
            # Parse gcode line
            
            if oline.startswith("O25 "):
                print("O25:",oline)
                O25out = "O25"
                O25in = oline.strip().split()
                for n in range(1,len(O25in)):
                    print(O25in[n])
                    if len(extruder_colour) > n and extruder_colour[n-1] != "":
                        O25out = O25out + " " + O25in[n]
                        print("No change due to filament colour being specified")
                    else:
                        O25new = O25in[n][0:8]+filament_settings_id[n-1].replace(" ","_").replace("\"","")
                        print(O25new)
                        O25out = O25out + " " + O25new 
                        O25patched = True
                mof.write(O25out+"\n")
            else:
                mof.write(oline)
                
            
    
    

    with open(destFile, "w") as of:
        for lIndex in range(len(lines)):
            oline = lines[lIndex]
            # Parse gcode line
            
            
            of.write(oline)
                
        if O25patched:                
            of.write(";****\n;****IDEX_postColour - O25 line patched in MCF.MAF file\n") 
        else:
            of.write(";****\n;****IDEX_postColour - O25 line NOT patchedMCF.MAF file\n") 
        
            of.close()
    
    
f.close()








