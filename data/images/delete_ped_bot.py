import csv
lines = list()
deletelabel = 'pedestrian'
with open('gt_train.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        lines.append(row)
        for field in row:
            if field == deletelabel:
                lines.remove(row)
with open('gt_train.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)
