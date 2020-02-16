file = open('C:\\etl_mdm\\etl-mdm-master-data\\etl-template\\person_original_pr\\endpoints\\sat_person_pr.yaml', 'r')
fileStreams = open('streams2.yaml', 'w')
array = file.readlines()
target = '''- target_field: %s
  method:
    type: copy_field
    field: %s

'''
for i in range(2, len(array), 3):
    nameStr = array[i].strip().split(': ')[1]
    typeStr = array[i+1].strip().split(': ')[1]
    #print(nameStr, len(typeStr))
    #print(target % (nameStr, 'jsonb_extract_vpath' if typeStr =='bigint' else 'extract_origin_json_to_timestamp', nameStr))
    fileStreams.write(target % (nameStr, nameStr))
file.close()
fileStreams.close()
