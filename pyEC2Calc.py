__author__ = 'izen'
import csv

os = raw_input("Linux/Windows OS: ")

osfile = 'Pricing' + os + '.csv'

with open(osfile) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print row['Name'] + ",",

print ""
print ""
instance = raw_input("Instance Type: ")
with open(osfile) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if instance == row['Name']:
            print "A " + os + " " + row['Name'] + " costs $" + row['ODH'] + " an hour." + " $" + \
                  str(float(row['ODH']) * 24) + " a day." + " $" + str(float(row['ODH']) * 24 * 30) + " a month." + \
                  " $" + str(float(row['ODH']) * 24 * 30 * 12) + " a year."
            print "Using Reserved pricing a " + os + " " + row['Name'] + " costs $" + row['RH'] + " an hour." + " $" + \
                  str(float(row['RH']) * 24) + " a day." + " $" + str(float(row['RH']) * 24 * 30) + " a month." + \
                  " $" + str(float(row['RH']) * 24 * 30 * 12) + " a year."
            print "With a savings of $" + str(float(row['ODH']) - float(row['RH'])) + " an hour at " + str(round(float(row['RH']) / float(row['ODH']), 2) * 100) + "%."