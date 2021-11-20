import csv, sys

filename = 'Device_report.csv'
data = []

with open(filename, newline='') as csv_file:
    reader = csv.reader(csv_file)
    try:
        for row in reader:
            data.append(row)
    except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

id = input('Enter an id: ')
col = [x[1] for x in data]

if id in col:
    for x in range(0, len(data)):
        if id == data[x][1]:
            print(data[x])
else:
    print('id not found')