import json

with open('mats.json', 'r') as jsonFile:
    data = json.load(jsonFile)

# Get input for each line in json file
for i in data:
    while True:
        try:
            data[i] = int(input(f'Update {i} : '))
            break
        except:
            print('Enter a number u dufus.')

# Update the json file with the new data
with open('mats.json', 'w') as jsonFile:
    json.dump(data, jsonFile, indent=3)