import json
filepath = "employee.json"

with open(filepath, "r") as f:
    empData = json.load(f)
    # print(empData)

# print( empData[0][""] )

for x in empData:
    print(x["name"])
    