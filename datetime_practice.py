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
DATA_DIR_BRZ = 'confirmed/brazil.txt'
DATA_DIR_MEX = 'confirmed/mexico.txt'

TOTAL_CASES = 3877407


def main():

    # List for the currently available countries / file access
    available_countries = ['United States', 'United states', 'US', 'us',
                           'united States', 'united states', 'USA', 'usa'
                           'Brazil', 'brazil',
                           'Mexico', 'mexico'
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

        # Brazil
        elif country_name == available_countries[8] or country_name == available_countries[9]:
            load_brazil()

        # Mexico
        elif country_name == available_countries[10] or country_name == available_countries[11]:
            load_mexico()
        
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
    end_date = '5-09-20'

    date_series = pd.date_range(start=first_date, end=end_date, freq='D')
    df_dates = pd.DataFrame()
    df_dates['Date'] = date_series
    df_dates_updated = df_dates
    df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')

    df_update = pd.concat([df_dates_updated, df], axis=1)
    print("On " + str(df_update.at[77, 'Date']) + " there were " + str(df_update.at[77, 'Cases']) +
          " confirmed cases of COVID-19 in the " + country_name + ".")


def load_brazil():

    country_name = 'Brazil'

    # File access and having fun with the data :)
    filename = 'brazil.txt'

    df = pd.read_csv(DATA_DIR_BRZ)
    df.columns = ['Cases']

    first_date = '1-22-20'
    end_date = '5-09-20'

    date_series = pd.date_range(start=first_date, end=end_date, freq='D')
    df_dates = pd.DataFrame()
    df_dates['Date'] = date_series
    df_dates_updated = df_dates
    df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')

    df_update = pd.concat([df_dates_updated, df], axis=1)
    print("On " + str(df_update.at[77, 'Date']) + " there were " + str(df_update.at[77, 'Cases']) + 
          " confirmed cases of COVID-19 in " + country_name + ".")


def load_mexico():

    country_name = 'Mexico'

    # File access and having fun with the data :)
    with open(DATA_DIR_MEX, 'r') as f:
        country_data = f.readlines()
        country_data_updated = []                                                   # Create empty list to 'import' data into and format
        for elem in country_data:                                                   # Iterate through the list and remove '\n' character
            country_data_updated.append(elem.strip())

        df = pd.DataFrame(data=country_data_updated)                                # Create a dataframe with pandas
        df.columns = ['Cases']                                                      # Assign column label
        
        first_date = '1-22-20'                                                      # Date range variable - start date
        end_date = '5-09-20'                                                        # Date range variable - end date

        date_series = pd.date_range(start=first_date, end=end_date, freq='D')       # Assign date range to date column with date range variables
        df_dates = pd.DataFrame()                                                   # Create dataframe
        df_dates['Date'] = date_series                                              # Assign column label and assign data range variable to it
        df_dates_updated = df_dates                                                 # Create new dataframe to format datetime stamp
        df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')         # Remove timestamp and format date to follow Jan-01-20

        df_update = pd.concat([df_dates_updated, df], axis=1)                       # Concatenate the dataframes to combine 'Date' and 'Cases' columns
        
        # Print result to console
        print("On " + str(df_update.at[108, 'Date']) + " there were " + str(df_update.at[108, 'Cases']) + 
          " confirmed cases of COVID-19 in " + country_name + ".")


"""
glob example
filenames = glob('*.txt')
dataframes = [pd.read_csv(f) for f in filenames]
"""


if __name__ == '__main__':
    main()
