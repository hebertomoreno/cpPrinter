import shutil, os, subprocess

estados = {'Aguascalientes':'ags','Baja California':'bc','Baja California Sur':'bcs', 'Campeche':'camp',
'Chihuahua':'chih','Chiapas':'chis','Coahuila':'coah','Colima':'col','Distrito Federal':'df',
'Durango':'dgo','Guerrero':'gro','Guanajuato':'gto','Hidalgo':'hgo','Jalisco':'jal','Estado de Mexico':'mex',
'Michoacán':'mich','Morelos':'mor','Nayarit':'nay','Nuevo León':'nl','Oaxaca':'oax','Puebla':'pue',
'Querétaro':'qro','Quintana Roo':'qroo','Sinaloa':'sin','San Luis Potosí':'slp','Sonora':'son','Tabasco':'tab',
'Tamaulipas':'tamps','Tlaxcala':'tlax','Veracruz':'ver','Yucatán':'yuc','Zacatecas':'zac'}

for estado in estados:
	print(estado.split())
	print(len(estado.split()))