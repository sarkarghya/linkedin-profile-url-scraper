import json

# Assuming your JSON data is stored in a list named 'json_data'
# json_data = [ { "FIELD1": "", "First Name": "Aviv", ... }, { ... } ]
with open('nat_data.json') as file:
    data = json.load(file)

linkedin_groups = {}

for obj in data:
    linkedin = obj['Linkedin']
    if linkedin in linkedin_groups:
        linkedin_groups[linkedin].append(obj)
    else:
        linkedin_groups[linkedin] = [obj]

#print(json.dumps( linkedin_groups, indent=2))
#print(list(linkedin_groups.values())[0])
with open('lingrpout.json', 'w') as file:
    json.dump(linkedin_groups, file, indent=2)
#print(linkedin_groups)

for group in linkedin_groups.values():
    # Initialize an empty dictionary to store the merged data
    merged_data = {}
    #print(group)

    # Iterate over each object in the data
    for obj in group:
        # Iterate over each key-value pair in the object
        for key, value in obj.items():
            # Skip empty keys or values
            if not value:
                continue

            # If the key already exists in the merged_data dictionary,
            # update the value accordingly
            if key in merged_data:
                existing_value = merged_data[key]

                # If both values are dictionaries, merge them
                if isinstance(existing_value, dict) and isinstance(value, dict):
                    merged_value = {**existing_value, **value}
                    merged_data[key] = merged_value
                # Otherwise, update the value with the maximum
                else:
                    merged_data[key] = max(existing_value, value)
            # If the key doesn't exist in the merged_data dictionary, add it
            else:
                merged_data[key] = value

    group[:] = [merged_data]

result = [obj for group in linkedin_groups.values() for obj in group]


with open('output.json', 'w') as file:
    json.dump(result, file, indent=2)