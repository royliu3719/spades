import csv
with open('./practice_104.csv', mode='r', newline='', encoding='utf8') as csv_file:

    rows = csv.reader(csv_file, delimiter=',')

    read_csv_list = [row for row in rows]
    print(*read_csv_list, sep="\n")

