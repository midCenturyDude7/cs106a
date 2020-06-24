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
from glob import glob
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

    country_name = 'United States'

    # File access and having fun with the data :)
    filename = 'us.txt'

    df = pd.read_csv(DATA_DIR_US)
    df.columns = ['Cases']

    first_date = '1-22-20'
    end_date = '5-10-20'
    date_series = pd.date_range(start=first_date, end=end_date, freq='D')
    df_dates = pd.DataFrame()
    df_dates['Date'] = date_series
    df_dates_updated = df_dates
    df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')

    df_update = pd.concat([df_dates_updated, df], axis=1)
    print("On " + str(df_update.at[25, 'Date']) + " there were " + str(df_update.at[25, 'Cases']) +
          " confirmed cases of COVID-19 in the " + country_name + ".")

    print(df_update.info())
    # date_line = df_update.loc[df_update['Date'] == '2020-01-30']
    # print(date_line)

    # with open(file, 'r') as file:
    #     for line in file:
    #         line = line.strip().split()
    #         num_us = line.split()
    #         print(num_us)

    # glob example
    # filenames = glob('*.txt')
    # dataframes = [pd.read_csv(f) for f in filenames]


if __name__ == '__main__':
    main()
