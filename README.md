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

    Adding an addional colour or material to Palette 2 using the 2nd extruder of an IDEX printer.
    
    This demo requires P2PP, and also needs some scripts to hide the 2nd extruder GCODE from P2PP befores its processing, then another script to add the hidden GCODE back into the Palette2 files prior to printing. 
    
    This method is fairly robust, shouldn't interfere with pings when printing in connected mode, and is also being considered for adding directly into P2PP
    
    
    Further work required to reduce unnessary purging when switching between P2 and second extruder on the IDEX printer.
    
    ![Palette 2 IDEX demo](https://github.com/ukdavewood/p2pp/blob/colour/Demos/IDEX2_Palette4/IDEX2_Palette4%20Demo.JPG?raw=true)
        
        
3. Double processing of filament through P2

    Using this method an additional 3 colours can be added per additional pass.
    
    During the first pass a 4 colour filament is created using accessory mode.
    During the second printing pass 3 the pre-spliced filament is refed back into one of the Palette2 channels, together with 3 additional colours.
    
    The demo requires P2PP supported by some scripts.
    
    Only really suitable for fairly small uncomplicated runs due to the fact that a lot of purge is required to be added on the first pass in order to overcome feed rate changes that pinging may cause in the 2nd printer phase.
    
    
    ![Palette 2 7 Colour Demos](https://github.com/ukdavewood/p2pp/blob/colour/Demos/Palette4_Palette3/P4P3%20Colours.JPG?raw=true)
    

4. Colour Filament Management

    At present P2PP makes up its own name for the filament colours which can sometimes be difficult to keep track of, especially when printing in 7 colours.   This demo is a fairly simple post processing python script which replaces the colours generated by P2PP with the actual filament names.  It requires each colour to have its own filament record in PrusaSlicer
    
    

## Virtual Colours



## Palette 2 on IDEX printer


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





