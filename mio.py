import csv
import re

def extract_names(timetables):
    list_of_list_of_names_from_timetables =[]
    pupil_names = []
    for item in timetables:
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
            pupil_names.append(item)

    return pupil_names

def compare_pupils(previous_pupils, current_pupils):
    email_list = []
    with open(previous_pupils, newline='') as previous_pupils_csv:
        reader = csv.reader(previous_pupils_csv)
        for row in reader:
            if row[0] in current_pupils:
                email_list.append(row)
    return email_list

def write_new_pupils_csv(email_list, new_file):
    with open(new_file, mode='w') as updated_names_and_emails:
        pupils_writer = csv.writer(updated_names_and_emails, delimiter= ',' , quotechar = '"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
        for name_email in email_list:
            pupils_writer.writerow(name_email)

    updated_names_and_emails.close()
    return True

list_of_timetables = []
while True:
    timetable = input('Enter timetable here. If done, press Enter')
    if timetable == '':
        break
    else:
        list_of_timetables.append(timetable)

previous_pupils = input('Enter file of previous pupils')

# call the function extract_names which returned pupil_names and assign that to variable
print('extracting names from ', len(list_of_timetables), ' timetables...')
current_pupils = extract_names(list_of_timetables)

print('comparing pupils...')
email_list = compare_pupils(previous_pupils, current_pupils)

print('writing new file...')
result = write_new_pupils_csv(email_list, 'updated_names_and_emails.csv')

if result:
    print('Your new file is ready! Celebrate with some chocolate!')
