#cpPrinte
A Python programm that organizes shpfiles to be used with the zipcode visualization html.

###Usage

* python cpPrinter.py
* Comes with a bat file for easy running. 

###Scripts

* organizeShp.py - Organizes the shp files necessary for the program and converts them to GeoJSON. 
* cpPrinter.py - Gets the zipcodes for the specified state from the heraldo page and arranges them in a csv. Then, it couples each municipality with its CVEGEO for use with the javascript program. 

##Noteworth Variables In Case You Want To Use This Program Too Although I Find That Unlikely

*In OrganizeShp.py:
	**destiPath: The directory which is created and destroyed by Organize.shp and in which jsons are compiled. You should probably change this to a valid folder you want to create. 
	**oriPath: The directory in which the shapefiles are stored. You can change this, but don't touch the estados[eKey] part because you'll BREAK THE PROGRAM FOREVEEEEEEER.
*In cpPrinter.py:
	**cpPrinterDir: The root directory of this application. 