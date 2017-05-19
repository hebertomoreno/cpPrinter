import webbrowser, requests, bs4, sys, json, csv
from unidecode import unidecode

stateJson = open(r'shp\sonNew.json')

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

loadedJson = json.load(stateJson)

outputWriter.writerow(['CVEGEO','Nombre', 'CP'])

if len(sys.argv) == 2:
	state = ''.join(sys.argv[1:]).lower()
elif len(sys.argv) > 2:
	state = '-'.join(sys.argv[1:]).lower()
	state = unidecode(state) 

res = requests.get('http://heraldo.com.mx/'+state+'/municipios/')

res.raise_for_status()

heraldoSoup = bs4.BeautifulSoup(res.text, 'html.parser')

muns = heraldoSoup.select('.fila_par,.fila_non')

for mun in muns:

	muniName = mun.getText()
	CVEGEO = ''
	nombreMun = ''

	if(len(mun.getText())) != 2:

		muniParsedName = mun.getText().replace(' ','-').lower()

		muniParsedName = unidecode(muniParsedName)

		for item in loadedJson['features']:
			parsedJsonName = item['properties']['NOMBRE']

			if(muniName.encode('utf-8') == parsedJsonName.encode('latin-1')):
				CVEGEO = item['properties']['CVEGEO']

		cpRes = requests.get('http://heraldo.com.mx/'+state+'/'+ muniParsedName+'/')
		res.raise_for_status()

		cpSoup = bs4.BeautifulSoup(cpRes.text, 'html.parser')
		codigos = cpSoup.select('.codigo_par,.codigo_non')

		for codigo in codigos:
			codigoText = codigo.getText()
			print(CVEGEO, muniName, codigoText)
			outputWriter.writerow([CVEGEO, muniName, codigoText])
		
outputFile.close()



