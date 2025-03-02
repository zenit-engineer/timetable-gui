import csv
def save():
    textbox = 'zenit'
    with open('timetable.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='.')
        writer.writerow(textbox)

save()