__author__ = 'izen'
# Imports
import csv

# Main Function
def main():
    # Takes input as either Linux or Windows
    os = raw_input("Linux/Windows OS: ")
    if os != 'Linux' and os != 'Windows':
        # Exits if not
        print 'Exiting...'
        exit()

    # Sets osfile name for loading of prices
    osfile = 'Pricing' + os + '.csv'

    # Opens osfile and reads out the instance types
    with open(osfile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print row['Name'] + ",",

    # Cause need space
    print ""
    print ""

    # Sets Instance type
    instance = raw_input("Instance Type: ")

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
                print "With a savings of $" + str(odhfloat - rhfloat) + " an hour at " + str(round(rhfloat / odhfloat, 2) * 100) + "%."

    # Cause need space
    print ""
    # Rerun main?
    main()

# Call main
if __name__ == '__main__':
    main()