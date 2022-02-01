# p2pp - **Palette2 Post Processing tool for PrusaSlicer/Slic3r PE**

## Fork Details

Fork created by Dave Wood - to manage some additional colour POC ideas relating to Palette2 when using P2PP

The following demos are included:

1. Virtual Colours

    Works best on top surfaces - using transparent PETG stack colours to create new colours
    Yellow on top of Blue, giving green.  Orange on top of Blue giving Brown.
    
    This demo used fusion 360 to create the thin layers - no additional scripts or changes required.
    Would work with P2PP or Canvas
    
    ![Virtual Colour Demo](https://github.com/ukdavewood/p2pp/blob/colour/Demos/Palette2%20Virtual%20Colours/Virtual_Colours.JPG?raw=true)
    

2. Palette 2 on IDEX printer

    Adding an additional colour or material to Palette 2 using the 2nd extruder of an IDEX printer.
    
    This demo requires P2PP, and also needs some scripts to hide the 2nd extruder GCODE from P2PP befores its processing, then another script to add the hidden GCODE back into the Palette2 files prior to printing. 
    
    This method is fairly robust, shouldn't interfere with pings when printing in connected mode, and is also being considered for adding directly into P2PP
    
    
    Further work required to reduce unnessary purging when switching between P2 and second extruder on the IDEX printer.
    
    ![Palette 2 IDEX demo](https://github.com/ukdavewood/p2pp/blob/colour/Demos/IDEX2_Palette4/IDEX2_Palette4%20Demo.JPG?raw=true)
        
        
3. Double processing of filament through P2

    Using this method an additional 3 colours can be added per additional pass.
    
    During the first pass a 4 colour filament is created using accessory mode.
    During the second printing pass the pre-spliced filament is fed back into one of the Palette2 channels, together with 3 additional colours.
    
    The demo requires P2PP supported by some scripts.
    
    Only really suitable for fairly small uncomplicated models as a fair bit of purge is required to be added on the first pass in order to overcome feed rate changes that pinging may cause in the 2nd printer phase.
    
    
    ![Palette 2 7 Colour Demos](https://github.com/ukdavewood/p2pp/blob/colour/Demos/Palette4_Palette3/P4P3%20Colours.JPG?raw=true)
    

4. Colour Filament Management

    At present P2PP makes up its own name for the filament colours which can sometimes be difficult to keep track of, especially when printing in 7 colours.   This demo is a fairly simple post processing python script which replaces the colours generated by P2PP with the actual filament names.  It requires each colour to have its own filament record in PrusaSlicer
    
    

## Virtual Colours instructions

See example STLs - [Example](https://github.com/ukdavewood/p2pp/tree/colour/Demos/Palette2%20Virtual%20Colours/Tortoise%20virtual4)

At top of model thin layers need to be manually created for the overlay colours.



## Palette 2 on IDEX printer Instructions


1. Download scripts from [here](https://github.com/ukdavewood/p2pp/tree/colour/scripts) into a suitable python folder /User/Shared/python for example on a Mac.

2. Add scripts before and after P2PP in the Print/Output/Post-Processing scripts in PrusaSlicer

/Users/Shared/python/Idex_Sparse_Z_Adjust.py; ;    
/Users/Shared/python/Idex_pre.py;     
open -W -a P2PP.app --args;   
/Users/Shared/python/Idex_post.py;      

    NB/ First script required if using Sparse Purge Towers
    
3.  Change Printer settings from 4 to 5 virtual extruders - with No 5 being mapped to extruder 2 on the IDEX printer

4.  Change Tool changing GCode Printer/Custom G-code to something along the lines of this 
NB/. Extuder numbers 0-3 would be palette on physical extruder 1,  and 4 going to physical extruder 2.

NB/ This assumes Palette is on extruder 1 - with 
; TOOL CHANGE ---START---
; next_extruder [next_extruder]

{if next_extruder == 4}
;IDEX_START_IGNORE
;IDEX_ADD:T1
;IDEX_ADD_G1_Z:  Add back in last G1 Z removed by P2PP.

{elsif previous_extruder == 4}
;IDEX_ADD:T0
;IDEX_END_IGNORE
{endif}

;IDEX_SPARSE_Z_ADJUST=-0.1

; TOOL CHANGE ---END---

Using these parameters the Idex_pre script comments out all records relating to virtual extruder 4 prior to P2PP, the Idex_post then adds the commented out records back in.



## Double processing of filament through P2



## Colour Filament Management




## Getting strarted

Have a look at the [P2PP Wiki pages](https://github.com/tomvandeneede/p2pp/wiki/Home-%5BP2-P3%5D) to get youstarted.


## Acknowledgements

Thanks to.....
Tim Brookman for the co-development of this plugin.
Klaus, Khalil ,Casey, Jermaul, Paul, Gideon,   (and all others) for the endless testing and valuable feedback and the ongoing P2PP support to the community...it's them driving the improvements...
Kurt for making the instructional video n setting up and using p2pp.

## Make a donation...

If you like this software and want to support its development you can make a small donation to support further development of P2PP.

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=t.vandeneede@pandora.be&lc=EU&item_name=Donation+to+P2PP+Developer&no_note=0&cn=&currency_code=EUR&bn=PP-DonationsBF:btn_donateCC_LG.gif:NonHosted)



## **Good luck & happy printing !!!**





