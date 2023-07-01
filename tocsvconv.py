import csv
import json

def flatten_json(json_obj, parent_key='', sep='.'):
    flattened_data = {}
    for key, value in json_obj.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened_data.update(flatten_json(value, new_key, sep))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                array_key = f"{new_key}{sep}{i}"
                flattened_data.update(flatten_json(item, array_key, sep))
        else:
            flattened_data[new_key] = value
    return flattened_data

# Read JSON from file
with open('output.json') as json_file:
    data = json.load(json_file)

# Flatten JSON data
flattened_data = [flatten_json(obj) for obj in data]

# Identify all unique fields (column names)
field_names = set()
for obj in flattened_data:
    field_names.update(obj.keys())

# Write data to CSV file
with open('output2.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(field_names)  # Write column headers
    for obj in flattened_data:
        row = [obj.get(field, '') for field in field_names]
        writer.writerow(row)
