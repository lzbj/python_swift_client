import json

with open("VCAP_SERVICES.json") as json_file:
    json_data = json.load(json_file)
    print json_data['Object-Storage'][0]
    #print(json_data)
