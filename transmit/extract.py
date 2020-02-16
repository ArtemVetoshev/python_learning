file = open('C:\\etl_mdm\\etl-mdm-master-data\\etl-template\\vehicle_vin_identifier\\endpoints\\vehicle_vin_identifier.yaml', 'r')
fileStreams = open('streams.yaml', 'w')
array = file.readlines()
target = '''- target_field: %s
  method:
    type: %s
    field: message
    json_key: %s

'''
for i in range(2, len(array), 3):
    nameStr = array[i].strip().split(': ')[1]
    typeStr = array[i+1].strip().split(': ')[1]
    #print(nameStr, len(typeStr))
    #print(target % (nameStr, 'jsonb_extract_vpath' if typeStr =='bigint' else 'extract_origin_json_to_timestamp', nameStr))
    fileStreams.write(target % (nameStr, 'extract_origin_json_to_timestamp' if typeStr =='timestamptz' else 'jsonb_extract_vpath', nameStr))
file.close()
fileStreams.close()

