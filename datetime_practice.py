# data comes from Johns Hopkins University. Thanks to them for making this public!
# https://github.com/CSSEGISandData/COVID-19
# you can find data beyond cumulative cases there!

"""
File: datetime_practice.py
Attempt to add a dateline - starting at Jan-22-20 - to each confirmed case value by working
with one country file as an example/milestone.
"""

# Import libraries
import pathlib
from datetime import datetime

# Constants for the country's file that contains all confirmed cases from Jan-22 to May-09
DATA_DIR_US = 'confirmed/us.txt'
TOTAL_CASES = 3877407

def main():

    # List for the currently available countries / file access
    available_countries = ['United States', 'United states', 'US', 'us',
                           'united States', 'united states', 'USA', 'usa'
                           ]

    while True:
        country_name = input("Enter the country: ")

        # United States
        if country_name == available_countries[0] or country_name == available_countries[1]:
            load_us()

        elif country_name == available_countries[2] or country_name == available_countries[3]:
            load_us()

        elif country_name == available_countries[4] or country_name == available_countries[5]:
            load_us()

        elif country_name == available_countries[6] or country_name == available_countries[7]:
            load_us()

        # Conditional for incorrect input
        else:
            print("You do not have access to that file yet! It will be available soon.")
            print("Please try again.")
            print('')


def load_us():

    country_name = 'The United States'

    # File access and having fun with the data :)
    filename = 'us.txt'
    with open(DATA_DIR_US, 'r') as f:                           # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())

        new_cases = []                                          # Create an empty list to capture the DoD difference
        for i in range(len(country_data_updated) - 1):          # Iterate over the updated country data to eliminate
            if country_data_updated[i] != 0:                    # non-zero days and capture the difference in cases
                new_cases.append(int(country_data_updated[i+1]) - int(country_data_updated[i]))  # on a day-to day basis

        for i in range(0, len(new_cases)):                      # Find the total number of cases for the country
            country_sum += int(new_cases[i])

        max_country = max(new_cases)                            # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list

        # Counts the total number of elements (days) in the list
        country_confirmed_cases = country_total_count - country_zero_count

        # Percentage of confirmed cases for country per all countries
        percentage_of_country_confirmed = int((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR US.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_US )
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR USA***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print('')


if __name__ == '__main__':
    main()
