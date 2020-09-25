import csv
import re

list_of_timetables = []
list_of_list_of_names_from_timetables =[]
current_pupils = []

while True:
    timetable = input('Enter timetable here. If done, enter Done')
    if timetable == 'Done':
        break
    else:
        list_of_timetables.append(timetable)

previous_pupils = input('Enter file of previous pupils')

for item in list_of_timetables:
    tthand = open(item)
    for line in tthand:
        lst = re.findall('[A-Z][a-z]+\s[A-Z][a-z]+', line)
        list_of_list_of_names_from_timetables.append(lst)
        #added in to find the double barrelled names too
        lst_db = re.findall('[A-Z][a-z]+\s[A-Z][a-z]+.?[-].?[A-Z][a-z]+', line)
        list_of_list_of_names_from_timetables.append(lst_db)
        #added in to find Mc+uppercase
        lst_mcs = re.findall('[A-Z][a-z]+\s[A-Z][a-z]+[A-Z][a-z]+', line)
        list_of_list_of_names_from_timetables.append(lst_mcs)
        #added in to find O' surnames
        lst_os = re.findall('[A-Z][a-z]+\s[O].[A-z][a-z]+' , line)
        list_of_list_of_names_from_timetables.append(lst_os)
        #added in to find 3 word names
        lstthree = re.findall('[A-Z][a-z]+\s[A-Z][a-z]+\s[A-Z][a-z]+', line)
        list_of_list_of_names_from_timetables.append(lstthree)


for sublist in list_of_list_of_names_from_timetables:
    for item in sublist:
        current_pupils.append(item)

print(current_pupils)

with open(previous_pupils, newline='') as f:
    reader = csv.reader(f)
    names_and_emails = list(reader)

with open('updated_names_and_emails.csv', mode='w') as updated_names_and_emails:
    pupils_writer = csv.writer(updated_names_and_emails, delimiter= ',' , quotechar = '"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')

    for item in current_pupils:
        matching = [s for s in names_and_emails if item in s]
        for sublist in matching:
            x = sublist[0]
            y = sublist[1]
            pupils_writer.writerow([x,y])

updated_names_and_emails.close()
print('Your new file is ready! Celebrate with some chocolate!')
