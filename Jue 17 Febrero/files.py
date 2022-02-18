
file = open("chinese.txt", encoding="utf-8")
file_string = file.read()
file.close()

with open("chinese.txt", encoding="utf-8") as a_file:
    a_file.read()


line_number = 0
with open("favorite-people.txt", encoding="utf-8") as a_file:
    for a_line in a_file:
        line_number += 1
        print(f"{a_line} - {line_number}")


import csv

with open("hurricanes.csv") as csf_vile:
    csv_reader = csv.reader(csf_vile, delimiter=',')
    for row in csv_reader:
        print(row)

# try Except