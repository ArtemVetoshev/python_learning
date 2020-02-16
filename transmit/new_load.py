import io
import re

file = io.open('example.txt', 'r')
fileStreams = open('result.txt', 'w')
array = file.readlines()

target = '''    - column:
        name: %s
        type: %s
'''


for i in range(0, len(array)):
    nameStr = array[i].strip('name=').split(' ')[1]
    typeStr = array[i].strip('type=').split(' ')[2]
    name = nameStr[6:-1]
    type = typeStr[6:].strip()
    fileStreams.write(target % (name, 'timestamptz' if type == 'timestamp' else type))
