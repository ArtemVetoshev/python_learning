import io

file = open('C:\\Users\\Artem_Vetoshev\\Desktop\\test.txt', 'r', encoding = 'utf8')
fileStreams = open('test2.txt', 'w')
array = file.readlines()
target = '''    - column:
        name: %s
        type: %s
'''
for i in range(0, len(array)):
    nameStr = array[i].strip().split(' ')[0]
    typeStr = array[i].strip().split(' ')[1]
    print(nameStr)
    #print(nameStr, len(typeStr))
    #print(target % (nameStr, 'jsonb_extract_vpath' if typeStr =='bigint' else 'extract_origin_json_to_timestamp', nameStr))
    fileStreams.write(target % (nameStr, typeStr))
file.close()
fileStreams.close()