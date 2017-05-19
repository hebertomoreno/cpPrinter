import webbrowser, requests, bs4, sys, json, csv, os
from unidecode import unidecode

cpPrinterDir = r'C:\Users\hmoreno\Documents\GitHub\cpPrinter'

os.chdir(cpPrinterDir)

estados = {'Aguascalientes':'ags','Baja California':'bc','Baja California Sur':'bcs', 'Campeche':'camp',
'Chihuahua':'chih','Chiapas':'chis','Coahuila':'coah','Colima':'col','Distrito Federal':'df',
'Durango':'dgo','Guerrero':'gro','Guanajuato':'gto','Hidalgo':'hgo','Jalisco':'jal','Estado de Mexico':'mex',
'Michoacán':'mich','Morelos':'mor','Nayarit':'nay','Nuevo León':'nl','Oaxaca':'oax','Puebla':'pue',
'Querétaro':'qro','Quintana Roo':'qroo','Sinaloa':'sin','San Luis Potosí':'slp','Sonora':'son','Tabasco':'tab',
'Tamaulipas':'tamps','Tlaxcala':'tlax','Veracruz':'ver','Yucatán':'yuc','Zacatecas':'zac'}

for estado in estados:
	if(estado == 'Distrito Federal'):
		continue
	splitEstado = estado.split()
	abrev = estados[estado]
	state = ''
	if len(splitEstado) == 1:
		# Get address from command line.
		state = ''.join(estado).lower()
		state = unidecode(state)
	elif len(splitEstado) > 1:
		# If the state has more than one word in it, 
		# join it with a '-' which follows the format
		# of the page's url. 
		state = '-'.join(splitEstado).lower()
		state = unidecode(state) 

	# Open the Json file
	# stateJson = open(r'json\son.json')
	jsonName = 'json\\'+ estados[estado] +'.json'
	stateJson = open(jsonName,encoding="latin-1")
	print('Opening ' + jsonName +' ...')

	outputAddr = 'csv\\'+abrev+'.csv'

	# Open the csv file to write 
	outputFile = open(outputAddr, 'w', newline='')
	outputWriter = csv.writer(outputFile)

	# Load the json file into a variable
	# json.load is used here so that we can input a file. 
	# Usually, json.loads is used, but it does not accept a file.

	loadedJson = json.load(stateJson)
	 
	# Write the header row. 
	outputWriter.writerow(['CVEGEO','Nombre', 'CP'])

	# Open the heraldo page for the state specified in the arguments
	# webbrowser.open('http://heraldo.com.mx/'+state+'/')
	# Get the heraldo page corresponding to the state
	if (state == 'distrito-federal'):
		res = requests.get('http://heraldo.com.mx/'+state+'/delegaciones/')
	else:
		res = requests.get('http://heraldo.com.mx/'+state+'/municipios/')
	print('Requesting '+state+ ' page from Heraldo...')

	# If the page isnt found, tell us so
	res.raise_for_status()

	# Store the webpage text in a variable
	heraldoSoup = bs4.BeautifulSoup(res.text, 'html.parser')

	# Select all the municipios (which are selected by their
	# class, which in the heraldo page is either .fila_par
	# or .fila_non)
	muns = heraldoSoup.select('.fila_par,.fila_non')

	print('Writing '+state+' municipios...')
	# Cycle through the municipios 
	for mun in muns:
		# Save the original name of the municipio in a variable, so we can compare it to 
		# the json later. 
		muniName = mun.getText()

		# Initialize the other necessary variables because we need them to be
		# global.
		CVEGEO = ''
		nombreMun = ''

		# In the classes selected, we can also find letters indicating each alphabetical section. 
		# There is no class specific to the municipios, so we get the length of the text to 
		# check if it is a municipio. There are no municipios with just one letter, as far as
		# I know. 
		if(len(mun.getText())) != 2:
			print('Requesting '+muniName+' ...')

			# Replace the spaces with dashes and move everything to a lowercase, according to
			# the naming format of the page. Consider changing the join above for a replace
			# when you're done writing the program. 
			muniParsedName = mun.getText().replace(' ','-').lower()

			# Unidecode gets a string and translates it to the nearest ASCII representation. 
			# The heraldo URL's do not contain accents, so this translates the accents into
			# its ASCII equivalent. 
			muniParsedName = unidecode(muniParsedName)

			# print(muniName)

			for item in loadedJson['features']:
				parsedJsonName = item['properties']['NOMBRE']
				#print(parsedJsonName)
				if(muniName.encode('utf-8') == parsedJsonName.encode('latin-1')):

					#print(muniName.encode('utf-8'), parsedJsonName.encode('latin-1'))
					CVEGEO = item['properties']['CVEGEO']
				# print(muniName.encode('utf-8'), parsedJsonName.encode('latin-1'))
				# input("Press Enter to continue...")

			# Request the municipio page and check for 404's using the parsed name.
			cpRes = requests.get('http://heraldo.com.mx/'+state+'/'+ muniParsedName+'/')
			res.raise_for_status()

			# Get the text for the webpage and select only the tags with a CP inside them. 
			cpSoup = bs4.BeautifulSoup(cpRes.text, 'html.parser')
			codigos = cpSoup.select('.codigo_par,.codigo_non')
			print('Writing codes...')
			# Print the zipcodes. 
			for codigo in codigos:
				codigoText = codigo.getText()

				# print the CVEGEO and the name of the municipio, which is json.features[i].properties.NOMBRE
				#print(CVEGEO, parsedJsonName, muniName, codigoText)
				# Print the values to the csv.
				outputWriter.writerow([CVEGEO, muniName, codigoText])
	print('\n\n'+estado+' Done!!!!!\n\n')
	outputFile.close()



