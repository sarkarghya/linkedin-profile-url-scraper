import csv
import json

# Load JSON data
with open('output.json') as file:
    json_data = json.load(file)

# Define the desired CSV columns
columns = [
    'FIELD1', 'First Name', 'Last Name', 'Type', 'Company Name', 'Gender', 'Location', 'Country',
    'Description', 'Number of Investments', 'Have invested in 2022?', 'VC Position',
    'Industry interests', 'Status', 'Notable investments and exits', 'Check size', 'Linkedin', 'Email',
    'Website', 'Phone', 'Source', 'Average Pageviews', 'Became a Lead Date', 'Create Date',
    'Created by User ID', 'Email Domain', 'First Conversion', 'First Conversion Date',
    'First Page Seen', 'First Referring Site', 'IP City', 'IP Country', 'Last Activity Date',
    'Last Contacted', 'Last Modified Date', 'Last Page Seen', 'Latest Source',
    'Latest Source Date', 'Latest Source Drill-Down 1', 'Latest Source Drill-Down 2',
    'Lead Status', 'Number of Form Submissions', 'Number of Pageviews', 'Number of Sessions',
    'Number of Unique Forms Submitted', 'Original Source Drill-Down 2', 'Recent Conversion',
    'Recent Conversion Date', 'Time First Seen'
]

# Create a list to store the rows
rows = []

# Iterate over the JSON data and extract values for each column
for item in json_data:
    row = {}
    for column in columns:
        if column in item:
            row[column] = item[column]
        else:
            row[column] = ''
    rows.append(row)

# Write the data to a CSV file
with open('output3.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)