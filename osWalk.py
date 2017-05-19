import os

for folderName, subfolders, filenames in os.walk(r'C:\Users\hmoreno\Documents\shapefiles\agebsymas\scince_2010\shps'):
	print('The current folder is ' + folderName)

	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

	for filename in filenames:
		print('FILE INSIDE : '+ filename)
		print('')