__author__ = 'ihasn'
# Simple EC2 calculator for AWS.

# Imports
import csv


def osinput():
    # Takes input as either Linux or Windows
    os = raw_input("Linux/Windows OS: ")
    if os != 'Linux' and os != 'Windows':
        # Exits if not
        print 'Exiting...'
        exit()
    print ""
    return os


def printinstances(os):
    # Sets osfile name for loading of prices
    osfile = 'Pricing' + os + '.csv'

    # Opens osfile and reads out the instance types
    with open(osfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print row['Name'] + ",",
    print ""
    return osfile


def assigninstancetype():
    print ""
    return raw_input("Instance Type: ")


def calccost(os, osfile, instance):
    # Opens osfile and reads through rows
    with open(osfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # If instance equals row:name
            if instance == row['Name']:
                # Set variables
                instancetype = row['Name']
                odhfloat = float(row['ODH'])
                rhfloat = float(row['RH'])
                # Print calculations
                print "A " + os + " " + instancetype + " costs $" + str(odhfloat) + " an hour." + " $" + \
                    str(odhfloat * 24) + " a day." + " $" + str(odhfloat * 24 * 30) + " a month." + \
                    " $" + str(odhfloat * 24 * 30 * 12) + " a year."
                print "Using Reserved pricing a " + os + " " + instancetype + " costs $" + str(rhfloat) + " an hour." + " $" + \
                    str(rhfloat * 24) + " a day." + " $" + str(rhfloat * 24 * 30) + " a month." + \
                    " $" + str(rhfloat * 24 * 30 * 12) + " a year."
                print "With a savings of $" + str(odhfloat - rhfloat) + " an hour at " + \
                    str(round(rhfloat / odhfloat, 2) * 100) + "%."
    print ""


# Test Function
def test():
    print 'Testing Linux OS type'
    os = 'Linux'
    osfile = printinstances(os)
    print 'Testing m3.medium instance type'
    instance = 'm3.medium'
    calccost(os, osfile, instance)
    print 'Testing Windows OS type'
    os = 'Windows'
    osfile = printinstances(os)
    print 'Testing m2.xlarge instance type'
    instance = 'm2.xlarge'
    calccost(os, osfile, instance)
    # TODO: Fix this faulty input
    # print 'Testing faulty OS type'
    # os = 'Test'


# Main Function
def main():

    os = osinput()
    osfile = printinstances(os)

    # Sets Instance type
    instance = assigninstancetype()

    calccost(os, osfile, instance)

    # Rerun main?
    main()


# Call main
if __name__ == '__main__':
    test()
    # main()