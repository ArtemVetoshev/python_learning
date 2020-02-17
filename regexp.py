import re

file = open('C:/Users/artem_vetoshev/Desktop/python_learning/reg.txt', 'r')
filereg = open('C:/Users/artem_vetoshev/Desktop/python_learning/after.txt', 'w')
array = file.readlines()
target = '''	- target_field: %s
      method:
        type: %s
        field: message
        json_key: %s

'''

for i in range(2, len(array), 6):
	nameStr = array[i].strip().split(': ')[1]
	typeStr = array[i+2].strip().split(': ')[1]
	minus_ = re.sub('at_', '', nameStr)
	if minus_.find('qg_', 0) != 0:
		minus2 = minus_
	else:
		minus2 = re.sub('qg_', '', minus_)+'_Quality'
	third = ''.join(word.title() for word in minus2.split('_'))
	third2 = re.sub(r'^\w', third[:1].lower(), third)
	third3 = "'{data, " + third2 + "}'"
	filereg.write(target % (nameStr, 'extract_origin_json_to_timestamp' if typeStr =='extract_origin_json_to_timestamp' else 'jsonb_extract_vpath', third3))
file.close()
filereg.close()