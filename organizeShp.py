import shutil, os, subprocess

estados = {'Aguascalientes':'ags','Baja California':'bc','Baja California Sur':'bcs', 'Campeche':'camp',
'Chihuahua':'chih','Chiapas':'chis','Coahuila':'coah','Colima':'col','Distrito Federal':'df',
'Durango':'dgo','Guerrero':'gro','Guanajuato':'gto','Hidalgo':'hgo','Jalisco':'jal','Estado de Mexico':'mex',
'Michoacán':'mich','Morelos':'mor','Nayarit':'nay','Nuevo León':'nl','Oaxaca':'oax','Puebla':'pue',
'Querétaro':'qro','Quintana Roo':'qroo','Sinaloa':'sin','San Luis Potosí':'slp','Sonora':'son','Tabasco':'tab',
'Tamaulipas':'tamps','Tlaxcala':'tlax','Veracruz':'ver','Yucatán':'yuc','Zacatecas':'zac'}

destiPath =  r'C:\Users\hmoreno\Documents\GitHub\cpPrinter\tryShp'

estadosKeys = list(estados.keys())

pathToShp = ''
pathToDbf = ''
pathToPrj = ''
pathToShx = ''

os.mkdir(destiPath)

os.chdir(destiPath)

for eKey in estadosKeys:
	pathToShp = estados[eKey] + '_municipal.shp'
	pathToDbf = estados[eKey] + '_municipal.dbf'
	pathToPrj = estados[eKey] + '_municipal.prj'
	pathToShx = estados[eKey] + '_municipal.shx'

	print('Copying ' + estados[eKey] + '...')

	oriPath = 'C:\\Users\\hmoreno\\Documents\\shapefiles\\agebsymas\\scince_2010\\shps\\'+ estados[eKey] + '\\'
	
	shutil.copy(oriPath+ pathToShp + "",destiPath)
	shutil.copy('C:\\Users\\hmoreno\\Documents\\shapefiles\\agebsymas\\scince_2010\\shps\\'+ estados[eKey] + '\\'+ pathToDbf + "",destiPath)
	shutil.copy('C:\\Users\\hmoreno\\Documents\\shapefiles\\agebsymas\\scince_2010\\shps\\'+ estados[eKey] + '\\'+ pathToPrj + "",destiPath)
	shutil.copy('C:\\Users\\hmoreno\\Documents\\shapefiles\\agebsymas\\scince_2010\\shps\\'+ estados[eKey] + '\\'+ pathToShx + "",destiPath)

	print('Running OGR2OGR...')
	p1 = subprocess.Popen(['ogr2ogr','-f','GeoJSON',estados[eKey]+'.json',pathToShp])
	p1.wait()
	oriJsonPath='C:\\Users\\hmoreno\\Documents\\GitHub\\cpPrinter\\tryShp\\'+estados[eKey]+'.json'
	# Ha ha ha...destiJson
	destiJsonPath='C:\\Users\\hmoreno\\Documents\\GitHub\\cpPrinter\\json\\'
	print('Moving to JSON folder...')
	shutil.copy(oriJsonPath, destiJsonPath)

os.chdir(r'C:\Users\hmoreno\Documents\GitHub\cpPrinter')
print('Deleting...')
shutil.rmtree(r'C:\Users\hmoreno\Documents\GitHub\cpPrinter\tryShp')

print('Jsons Compiled!!!')

