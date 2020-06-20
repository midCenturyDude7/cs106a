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
import pandas as pd
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

    file = DATA_DIR_US

    df = pd.read_csv(file)
    print(df.head())

    # with open(file, 'r') as file:
    #     for line in file:
    #         line = line.strip()
    #         num_us = line.split()
    #         print(num_us)


if __name__ == '__main__':
    main()
