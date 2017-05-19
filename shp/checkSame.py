oJson = open('son.json')
sJson = open('sonNew.json')

oJsonText = oJson.read()

sJsonText = sJson.read()
print(sJsonText)

if(oJsonText == sJsonText):
	print("They're the same.")
else:
	print("They're not the same.")