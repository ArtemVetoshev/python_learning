loadTab = open('loadExample.txt', 'r')
satTab = open('result.txt', 'r')

arrayLoad = loadTab.readlines()
arraySat = satTab.readlines()

dictLoad = {}
dictSat = {}

for i in range(2, len(arrayLoad), 3):
    namesLoad = arrayLoad[i].strip().split(': ')[1]
    typesLoad = arrayLoad[i+1].strip().split(': ')[1]
    dictLoad[namesLoad] = typesLoad
#print(dictLoad)

for i in range(2, len(arraySat), 3):
    namesSat = arraySat[i].strip().split(': ')[1]
    typesSat = arraySat[i+1].strip().split(': ')[1]
    dictSat[namesSat] = typesSat
#print(dictSat)

#print('*'*50)

myStr = "%s\t%s\t%s\t%s"

for key in dictLoad.keys():
    if key in dictSat.keys():
        if dictLoad[key] != dictSat[key]:
            print(myStr %(key, dictLoad[key], key, dictSat[key]))

for key in dictSat.keys():
    if key not in dictLoad.keys():
        print(myStr %(None, None, key, dictSat[key]))
for key in dictLoad.keys():
    if key not in dictSat.keys():
        print(myStr %(key, dictLoad[key], None, None))

print('='*50)

