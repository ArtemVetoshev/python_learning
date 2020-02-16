loadTab = open('loadExample.txt', 'r')
satTab = open('satExample.txt', 'r')

arrayLoad = loadTab.readlines()
arraySat = satTab.readlines()

dictLoad = {}
dictSat = {}

for i in range(0, len(arrayLoad)):
    namesLoad = arrayLoad[i].strip().split('\t')[0]
    typesLoad = arrayLoad[i].strip().split('\t')[1]
    dictLoad[namesLoad] = typesLoad
print(dictLoad)
    #print(namesLoad)
for i in range(0, len(arraySat)):
    namesSat = arraySat[i].strip().split('\t')[0]
    typesSat = arraySat[i].strip().split('\t')[1]
    dictSat[namesSat] = typesSat
print(dictSat)
    #print(namesSat)
print('='*50)

myStr = "%s\t%s"

for each in dictLoad.items():
    if each in dictSat.items():
        print(myStr % (each))
