# data comes from Johns Hopkins University. Thanks to them for making this public!
# https://github.com/CSSEGISandData/COVID-19
# you can find data beyond cumulative cases there!

"""
File: final_project.py
In its current form, this VERY BASIC program works with COVID-19 data from 10 countries and allows the user
to access data based on choosing which country he/she would like to see data about.
***
NEXT STEPS:
(1) Provide access to all the files, likely using the OS module; STATUS: COMPLETED! Used the pathlib library
(2) Include a date with each day / STATUS: PENDING
(3) Data manipulation: Work with Numpy and Pandas to perform further/more detailed data manipulation such as
cross country comparisons based on certain data points related to 'confirmed cases' or 'country with the day
of the most confirmed cases', etc. / STATUS: PENDING
(4) Data visualization: Work with Matplotlib to plot the data and
hopefully create some useful/interesting charts/graphs for the purposes of storytelling (maybe) / STATUS: PENDING
(5) Further decompose the program - likely related to #1 above - to simplify/refactor the code to make it more
efficient and easier to read / STATUS: ONGOING
***
LAST BUT NOT LEAST: THANK YOU CS106A!!! What an awesome, kick-ass, amazing and super-fun experience this has been.
Really can't say thank you enough! Everyone that contributed their time, energy and effort to this has my infinite
gratitude - and that is an understatement.
"""

# Import libraries
import pathlib
from datetime import datetime
from glob import glob
import pandas as pd

# Constants for each country's file that contains all confirmed cases from Jan-22 to May-09
DATA_DIR = 'confirmed/'
DATA_DIR_BELARUS = 'confirmed/belarus.txt'
DATA_DIR_BRAZIL = 'confirmed/brazil.txt'
DATA_DIR_IRAN = 'confirmed/iran.txt'
DATA_DIR_ITALY = 'confirmed/italy.txt'
DATA_DIR_RUSSIA = 'confirmed/russia.txt'
DATA_DIR_EGYPT = 'confirmed/egypt.txt'
DATA_DIR_KAZAKHSTAN = 'confirmed/kazakhstan.txt'
DATA_DIR_GERMANY = 'confirmed/germany.txt'
DATA_DIR_ARGENTINA = 'confirmed/argentina.txt'
DATA_DIR_US = 'confirmed/us.txt'
DATA_DIR_INDIA = 'confirmed/india.txt'
DATA_DIR_SKOREA = 'confirmed/south korea.txt'
DATA_DIR_JAPAN = 'confirmed/japan.txt'
DATA_DIR_LEBANON = 'confirmed/lebanon.txt'
DATA_DIR_MEXICO = 'confirmed/mexico.txt'

TOTAL_CASES = 3877407


def main():

    # Intro output to console
    print("Welcome! You have access to COVID-19 data from Jan-22 to May-09 for the following fifteen countries:")
    print("Belarus, Brazil, Iran, Italy, Russia, Egypt, Kazakhstan, Germany, Argentina, the United States, India, ")
    print("South Korea, Japan, Lebanon, and Mexico")
    print("Check back soon, as more countries will be made available for review!")
    print('')

    # List for the currently available countries / file access
    available_countries = ['Belarus', 'belarus',
                           'Brazil', 'brazil',
                           'Iran', 'iran',
                           'Italy', 'italy',
                           'Russia', 'russia',
                           'Egypt', 'egypt',
                           'Kazakhstan', 'kazakhstan',
                           'Germany', 'germany',
                           'Argentina', 'argentina',
                           'United States', 'United states', 'US', 'us', 'united States', 'united states', 'USA', 'usa',
                           'India', 'india',
                           'South Korea', 'south korea',
                           'Japan', 'japan',
                           'Lebanon', 'lebanon',
                           'Mexico', 'mexico',
                           'All', 'all']

    # Loop that asks user to enter country name to access COVID-19 data
    while True:
        country_name = input("Choose an available country, or type 'All' for COVID-19 data "
                             "on all 182 countries combined: ")
        print('')

        # Belarus
        if country_name == available_countries[0] or country_name == available_countries[1]:
            load_belarus()

        # Brazil
        elif country_name == available_countries[2] or country_name == available_countries[3]:
            load_brazil()

        # Iran
        elif country_name == available_countries[4] or country_name == available_countries[5]:
            load_iran()

        # Italy
        elif country_name == available_countries[6] or country_name == available_countries[7]:
            load_italy()

        # Russia
        elif country_name == available_countries[8] or country_name == available_countries[9]:
            load_russia()

        # Egypt
        elif country_name == available_countries[10] or country_name == available_countries[11]:
            load_egypt()

        # Kazakhstan
        elif country_name == available_countries[12] or country_name == available_countries[13]:
            load_kazakhstan()

        # Germany
        elif country_name == available_countries[14] or country_name == available_countries[15]:
            load_germany()

        # Argentina
        elif country_name == available_countries[16] or country_name == available_countries[17]:
            load_argentina()

        # United States
        elif country_name == available_countries[18] or country_name == available_countries[19]:
            load_us()

        elif country_name == available_countries[20] or country_name == available_countries[21]:
            load_us()

        elif country_name == available_countries[22] or country_name == available_countries[23]:
            load_us()

        elif country_name == available_countries[24] or country_name == available_countries[25]:
            load_us()

        # India
        elif country_name == available_countries[26] or country_name == available_countries[27]:
            load_india()

        # South Korea
        elif country_name == available_countries[28] or country_name == available_countries[29]:
            load_skorea()

        # Japan
        elif country_name == available_countries[30] or country_name == available_countries[31]:
            load_japan()

        # Lebanon
        elif country_name == available_countries[32] or country_name == available_countries[33]:
            load_lebanon()

        # Mexico
        elif country_name == available_countries[34] or country_name == available_countries[35]:
            load_mexico()

        # All Countries
        elif country_name == available_countries[36] or country_name == available_countries[37]:
            load_path()

        # Conditional for incorrect input
        else:
            print("You do not have access to that file yet! It will be available soon.")
            print("Please try again.")
            print("REMINDER: The following countries are currently available for review:")
            print("Belarus, Brazil, Iran, Italy, Russia, Egypt, Kazakhstan, Germany, Argentina, the United States, ")
            print("India, South Korea, Japan, Lebanon, and Mexico")
            print('')


def load_path():

    data_list = []                                                          # Initializes list to store all data in
    for path in pathlib.Path(DATA_DIR).iterdir():                           # every file in the directory as an one-
        if path.is_file():                                                  # dimensional array, data_list
            with open(str(path), 'r') as f:
                current_file = f.readlines()
                data_list = []
                for elem in current_file:
                    data_list.append(elem.strip())

                df = pd.DataFrame(data=data_list)
                df.columns = ['Cases']

                filenames = glob('*.txt')
                dataframes = [pd.read_csv(f) for f in filenames]

    new_cases_total = []                                                    # Initializes list to store newly confirmed
    total_countries_sum = 0                                                 # cases

    for i in range(len(data_list) - 1):                                     # Loops through data_list and creates new
        if data_list[i] != '0':                                             # list of confirmed cases day-over-day
            new_cases_total.append(int(data_list[i+1]) - int(data_list[i]))

    for i in range(len(new_cases_total)):                                   # Loops through day-over-day confirmed
        if new_cases_total[i] >= 1:                                         # cases and sums the total number of
            total_countries_sum += new_cases_total[i]                       # confirmed cases for all 182 countries

    max_total_all = max(new_cases_total)                                    # Largest one-day increase for 182 countries
    # max_index_value = int(new_cases_total.index(36188))                   # Index value of 18949
    zero_days_total = data_list.count('0')                                  # Total number of days for unconfirmed cases
    total_data_list = len(data_list)                                        # Total number of days recorded
    total_confirmed_cases = total_data_list - zero_days_total               # Total number of days for confirmed cases
    percentage_total_confirmed_cases = int((zero_days_total / total_confirmed_cases) * 100)  # % - confirmed/unconfirmed

    print("***COMPARISON METRICS***")
    print("For the dates encompassing Jan-22 to May-09, all 182 countries combined have the following metrics:")
    print(" <> A total of " + str(total_data_list) + " days recorded")
    print(" <> A total of " + str(zero_days_total) + " days of unconfirmed cases")
    print(" <> A total of " + str(total_confirmed_cases) + " days of confirmed cases, or " + str(
        percentage_total_confirmed_cases) + "% of the 109 day period")
    print(" <> The largest one day increase of confirmed cases is: " + str(
        max_total_all) + " cases -- which occurred in the United States")
    print(" <> The overall total number of confirmed cases is: " + str(
        total_countries_sum))
    print('')
    # print(df.info())
    print('')


def load_belarus():

    country_name = 'Belarus'

    # File access and having fun with the data :)
    filename = 'belarus.txt'
    with open(DATA_DIR_BELARUS, 'r') as f:                      # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())

        df = pd.DataFrame(country_data_updated)
        df.columns = ['Cases']

        first_date = '1-22-20'
        end_date = '5-9-20'

        date_series = pd.date_range(start=first_date, end=end_date, freq='D')
        df_dates = pd.DataFrame()
        df_dates['Date'] = date_series
        df_dates_updated = df_dates
        df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')

        df_update = pd.concat([df_dates_updated, df], axis=1)

        new_cases = []                                          # Create an empty list to capture the DoD difference
        for i in range(len(country_data_updated) - 1):          # Iterate over the updated country data to eliminate
            if country_data_updated[i] != 0:                    # non-zero days and capture the difference in cases
                new_cases.append(int(country_data_updated[i+1]) - int(country_data_updated[i]))  # on a day-to day basis

        for i in range(0, len(new_cases)):                      # Find the total number of cases for the country
            country_sum += int(new_cases[i])

        df_new_cases = pd.DataFrame(new_cases)
        df_new_cases.columns = ['New Cases']

        df_new_cases_updated = pd.concat([df_dates_updated, df_new_cases], axis=1)

        max_country = max(new_cases)                            # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list

        # Counts the total number of days with confirmed cases
        country_confirmed_cases = country_total_count - country_zero_count

        # Percentage of confirmed cases for country per all countries
        percentage_of_country_confirmed = float((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR BELARUS.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_BELARUS)
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR BELARUS***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print(" <> On " + str(df_update.at[105, 'Date']) + ", there were a total of " + str(df_update.at[105, 'Cases']) +
              " confirmed cases, including " + str(df_new_cases_updated.at[105, 'New Cases']) + " new cases of "
              "COVID-19 in " + country_name + ".")
        print('')

        # Testing date line
        # print(datetime(date_line_list))


def load_brazil():

    country_name = 'Brazil'

    # File access and having fun with the data :)
    filename = 'brazil.txt'
    with open(DATA_DIR_BRAZIL, 'r') as f:                       # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())
        
        df = pd.DataFrame(country_data_updated)
        df.columns = ['Cases']

        first_date = '1-22-20'
        end_date = '5-9-20'

        date_series = pd.date_range(start=first_date, end=end_date, freq='D')
        df_dates = pd.DataFrame()
        df_dates['Date'] = date_series
        df_dates_updated = df_dates
        df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')

        df_update = pd.concat([df_dates_updated, df], axis=1)
                
        new_cases = []                                          # Create an empty list to capture the DoD difference
        for i in range(len(country_data_updated) - 1):          # Iterate over the updated country data to eliminate
            if country_data_updated[i] != 0:                    # non-zero days and capture the difference in cases
                new_cases.append(int(country_data_updated[i+1]) - int(country_data_updated[i]))  # on a day-to day basis

        for i in range(0, len(new_cases)):                      # Find the total number of cases for the country
            country_sum += int(new_cases[i])

        df_new_cases = pd.DataFrame(new_cases)
        df_new_cases.columns = ['New Cases']

        df_new_cases_updated = pd.concat([df_dates_updated, df_new_cases], axis=1)

        max_country = max(new_cases)                            # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list

        # Counts the total number of days with confirmed cases
        country_confirmed_cases = country_total_count - country_zero_count

        # Percentage of confirmed cases for country per all countries
        percentage_of_country_confirmed = int((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR BRAZIL.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_BRAZIL)
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR BRAZIL***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print(" <> On " + str(df_update.at[105, 'Date']) + ", there were a total of " + str(df_update.at[105, 'Cases']) +
              " confirmed cases, including " + str(df_new_cases_updated.at[105, 'New Cases']) + " new cases of "
              "COVID-19 in " + country_name + ".")
        print('')


def load_iran():

    country_name = 'Iran'

    # File access and having fun with the data :)
    filename = "iran.txt"
    with open(DATA_DIR_IRAN, 'r') as f:                         # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())

        df = pd.DataFrame(country_data_updated)
        df.columns = ['Cases']

        first_date = '1-22-20'
        end_date = '5-9-20'

        date_series = pd.date_range(start=first_date, end=end_date, freq='D')
        df_dates = pd.DataFrame()
        df_dates['Date'] = date_series
        df_dates_updated = df_dates
        df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')

        df_update = pd.concat([df_dates_updated, df], axis=1)

        new_cases = []                                          # Create an empty list to capture the DoD difference
        for i in range(len(country_data_updated) - 1):          # Iterate over the updated country data to eliminate
            if country_data_updated[i] != 0:                    # non-zero days and capture the difference in cases
                new_cases.append(int(country_data_updated[i+1]) - int(country_data_updated[i]))  # on a day-to day basis

        for i in range(0, len(new_cases)):                      # Find the total number of cases for the country
            country_sum += int(new_cases[i])

        df_new_cases = pd.DataFrame(new_cases)
        df_new_cases.columns = ['New Cases']

        df_new_cases_updated = pd.concat([df_dates_updated, df_new_cases], axis=1)

        max_country = max(new_cases)                            # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list

        # Counts the total number of days with confirmed cases
        country_confirmed_cases = country_total_count - country_zero_count

        # Percentage of confirmed cases for country per all countries
        percentage_of_country_confirmed = int((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR IRAN.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_IRAN)
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR IRAN***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print(" <> On " + str(df_update.at[105, 'Date']) + ", there were a total of " + str(df_update.at[105, 'Cases']) +
              " confirmed cases, including " + str(df_new_cases_updated.at[105, 'New Cases']) + " new cases of "
              "COVID-19 in " + country_name + ".")
        print('')


def load_italy():

    country_name = 'Italy'

    # File access and having fun with the data :)
    filename = 'italy.txt'
    with open(DATA_DIR_ITALY, 'r') as f:                        # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())

        df = pd.DataFrame(country_data_updated)
        df.columns = ['Cases']

        first_date = '1-22-20'
        end_date = '5-9-20'

        date_series = pd.date_range(start=first_date, end=end_date, freq='D')
        df_dates = pd.DataFrame()
        df_dates['Date'] = date_series
        df_dates_updated = df_dates
        df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')

        df_update = pd.concat([df_dates_updated, df], axis=1)

        new_cases = []                                          # Create an empty list to capture the DoD difference
        for i in range(len(country_data_updated) - 1):          # Iterate over the updated country data to eliminate
            if country_data_updated[i] != 0:                    # non-zero days and capture the difference in cases
                new_cases.append(int(country_data_updated[i+1]) - int(country_data_updated[i]))  # on a day-to day basis

        for i in range(0, len(new_cases)):                      # Find the total number of cases for the country
            country_sum += int(new_cases[i])

        df_new_cases = pd.DataFrame(new_cases)
        df_new_cases.columns = ['New Cases']

        df_new_cases_updated = pd.concat([df_dates_updated, df_new_cases], axis=1)

        max_country = max(new_cases)                            # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list

        # Counts the total number of days with confirmed cases
        country_confirmed_cases = country_total_count - country_zero_count

        # Percentage of confirmed cases for country per all countries
        percentage_of_country_confirmed = int((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR ITALY.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_ITALY)
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR ITALY***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print(" <> On " + str(df_update.at[105, 'Date']) + ", there were a total of " + str(df_update.at[105, 'Cases']) +
              " confirmed cases, including " + str(df_new_cases_updated.at[105, 'New Cases']) + " new cases of "
              "COVID-19 in " + country_name + ".")
        print('')


def load_russia():

    country_name = 'Russia'

    # File access and having fun with the data :)
    filename = 'russia.txt'
    with open(DATA_DIR_RUSSIA, 'r') as f:                       # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())

        df = pd.DataFrame(country_data_updated)
        df.columns = ['Cases']

        first_date = '01-22-20'
        end_date = '05-09-20'

        date_series = pd.date_range(start=first_date, end=end_date, freq='D')
        df_dates = pd.DataFrame()
        df_dates['Date'] = date_series
        df_dates_updated = df_dates
        df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')

        df_update = pd.concat([df_dates_updated, df], axis=1)

        new_cases = []                                          # Create an empty list to capture the DoD difference
        for i in range(len(country_data_updated) - 1):          # Iterate over the updated country data to eliminate
            if country_data_updated[i] != 0:                    # non-zero days and capture the difference in cases
                new_cases.append(int(country_data_updated[i+1]) - int(country_data_updated[i]))  # on a day-to day basis

        for i in range(0, len(new_cases)):                      # Find the total number of cases for the country
            country_sum += int(new_cases[i])

        df_new_cases = pd.DataFrame(new_cases)
        df_new_cases.columns = ['New Cases']

        df_new_cases_updated = pd.concat([df_dates_updated, df_new_cases], axis=1)

        max_country = max(new_cases)                            # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list

        # Counts the total number of days with confirmed cases
        country_confirmed_cases = country_total_count - country_zero_count

        # Percentage of confirmed cases for country per all countries
        percentage_of_country_confirmed = int((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR RUSSIA.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_RUSSIA)
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR RUSSIA***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print(" <> On " + str(df_update.at[105, 'Date']) + ", there were a total of " + str(df_update.at[105, 'Cases']) +
              " confirmed cases, including " + str(df_new_cases_updated.at[105, 'New Cases']) + " new cases of "
              "COVID-19 in " + country_name + ".")
        print('')


def load_egypt():

    country_name = 'Egypt'

    # File access and having fun with the data :)
    filename = 'egypt.txt'
    with open(DATA_DIR_EGYPT, 'r') as f:                        # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())
        
        df = pd.DataFrame(country_data_updated)
        df.columns = ['Cases']

        first_date = '01-22-20'
        end_date = '05-09-20'

        date_series = pd.date_range(start=first_date, end=end_date, freq='D')
        df_dates = pd.DataFrame()
        df_dates['Date'] = date_series
        df_dates_updated = df_dates
        df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')

        df_update = pd.concat([df_dates_updated, df], axis=1)

        new_cases = []                                          # Create an empty list to capture the DoD difference
        for i in range(len(country_data_updated) - 1):          # Iterate over the updated country data to eliminate
            if country_data_updated[i] != 0:                    # non-zero days and capture the difference in cases
                new_cases.append(int(country_data_updated[i+1]) - int(country_data_updated[i]))  # on a day-to day basis

        for i in range(0, len(new_cases)):                      # Find the total number of cases for the country
            country_sum += int(new_cases[i])
        
        df_new_cases = pd.DataFrame(new_cases)
        df_new_cases.columns = ['New Cases']

        df_new_cases_updated = pd.concat([df_dates_updated, df_new_cases], axis=1)

        max_country = max(new_cases)                            # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list

        # Counts the total number of days with confirmed cases
        country_confirmed_cases = country_total_count - country_zero_count

        # Percentage of confirmed cases for country per all countries
        percentage_of_country_confirmed = float((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR EGYPT.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_EGYPT)
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR EGYPT***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print(" <> On " + str(df_update.at[105, 'Date']) + ", there were a total of " + str(df_update.at[105, 'Cases']) +
              " confirmed cases, including " + str(df_new_cases_updated.at[105, 'New Cases']) + " new cases of "
              "COVID-19 in " + country_name + ".")
        print('')


def load_kazakhstan():

    country_name = 'Kazakhstan'

    # File access and having fun with the data :)
    filename = 'kazakhstan.txt'
    with open(DATA_DIR_KAZAKHSTAN, 'r') as f:                   # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())

        df = pd.DataFrame(country_data_updated)
        df.columns = ['Cases']

        first_date = '01-22-20'
        end_date = '05-09-20'

        date_series = pd.date_range(start=first_date, end=end_date, freq='D')
        df_dates = pd.DataFrame()
        df_dates['Date'] = date_series
        df_dates_updated = df_dates
        df_dates_updated['Date'] = df_dates_updated['Date'].dt.strftime('%b-%d-%Y')

        df_update = pd.concat([df_dates_updated, df], axis=1)

        new_cases = []                                          # Create an empty list to capture the DoD difference
        for i in range(len(country_data_updated) - 1):          # Iterate over the updated country data to eliminate
            if country_data_updated[i] != 0:                    # non-zero days and capture the difference in cases
                new_cases.append(int(country_data_updated[i+1]) - int(country_data_updated[i]))  # on a day-to day basis

        for i in range(0, len(new_cases)):                      # Find the total number of cases for the country
            country_sum += int(new_cases[i])

        df_new_cases = pd.DataFrame(new_cases)
        df_new_cases.columns = ['New Cases']

        df_new_cases_updated = pd.concat([df_dates_updated, df_new_cases], axis=1)

        max_country = max(new_cases)                            # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list

        # Counts the total number of elements (days) in the list
        country_confirmed_cases = country_total_count - country_zero_count

        # Percentage of confirmed cases for country per all countries
        percentage_of_country_confirmed = float((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR KAZAKHSTAN.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_KAZAKHSTAN)
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR KAZAKHSTAN***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print(" <> On " + str(df_update.at[105, 'Date']) + ", there were a total of " + str(df_update.at[105, 'Cases']) +
              " confirmed cases, including " + str(df_new_cases_updated.at[105, 'New Cases']) + " new cases of "
              "COVID-19 in " + country_name + ".")
        print('')


def load_germany():

    country_name = 'Germany'

    # File access and having fun with the data :)
    filename = 'germany.txt'
    with open(DATA_DIR_GERMANY, 'r') as f:                      # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())

        df = pd.DataFrame(country_data_updated)
        df.columns = ['Cases']

        first_date = '01-22-20'
        end_date = '05-09-20'

        date_series = pd.date_range(start=first_date, end=end_date, freq='D')
        df_dates = pd.DataFrame()
        df_dates['Date'] = date_series
        df_dates_updated = df_dates
        df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')

        df_update = pd.concat([df_dates_updated, df], axis=1)

        new_cases = []                                          # Create an empty list to capture the DoD difference
        for i in range(len(country_data_updated) - 1):          # Iterate over the updated country data to eliminate
            if country_data_updated[i] != 0:                    # non-zero days and capture the difference in cases
                new_cases.append(int(country_data_updated[i+1]) - int(country_data_updated[i]))  # on a day-to day basis

        for i in range(0, len(new_cases)):                      # Find the total number of cases for the country
            country_sum += int(new_cases[i])

        df_new_cases = pd.DataFrame(new_cases)
        df_new_cases.columns = ['New Cases']

        df_new_cases_updated = pd.concat([df_dates_updated, df_new_cases], axis=1)

        max_country = max(new_cases)                            # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list

        # Counts the total number of elements (days) in the list
        country_confirmed_cases = country_total_count - country_zero_count

        # Percentage of confirmed cases for country per all countries
        percentage_of_country_confirmed = int((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR GERMANY.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_GERMANY)
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR GERMANY***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print(" <> On " + str(df_update.at[105, 'Date']) + ", there were a total of " + str(df_update.at[105, 'Cases']) +
        " confirmed cases, including " + str(df_new_cases_updated.at[105, 'New Cases']) + " new cases of "
        "COVID-19 in " + country_name + ".")
        print('')


def load_argentina():

    country_name = 'Argentina'

    filename = 'argentina.txt'
    with open(DATA_DIR_ARGENTINA, 'r') as f:                    # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())
        
        df = pd.DataFrame(country_data_updated)
        df.columns = ['Cases']

        first_date = '01-22-20'
        end_date = '05-09-20'

        date_series = pd.date_range(start=first_date, end=end_date, freq='D')
        df_dates = pd.DataFrame()
        df_dates['Date'] = date_series
        df_dates_updated = df_dates
        df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')

        df_update = pd.concat([df_dates_updated, df], axis=1)

        new_cases = []                                          # Create an empty list to capture the DoD difference
        for i in range(len(country_data_updated) - 1):          # Iterate over the updated country data to eliminate
            if country_data_updated[i] != 0:                    # non-zero days and capture the difference in cases
                new_cases.append(int(country_data_updated[i+1]) - int(country_data_updated[i]))  # on a day-to day basis

        for i in range(0, len(new_cases)):                      # Find the total number of cases for the country
            country_sum += int(new_cases[i])

        df_new_cases = pd.DataFrame(new_cases)
        df_new_cases.columns = ['New Cases']

        df_new_cases_updated = pd.concat([df_dates_updated, df_new_cases], axis=1)

        max_country = max(new_cases)                            # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list

        # Counts the total number of elements (days) in the list
        country_confirmed_cases = country_total_count - country_zero_count

        # Percentage of confirmed cases for country per all countries
        percentage_of_country_confirmed = float((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR ARGENTINA.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_ARGENTINA )
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR ARGENTINA***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print(" <> On " + str(df_update.at[105, 'Date']) + ", there were a total of " + str(df_update.at[105, 'Cases']) +
        " confirmed cases, including " + str(df_new_cases_updated.at[105, 'New Cases']) + " new cases of "
        "COVID-19 in " + country_name + ".")
        print('')


def load_us():

    country_name = 'the United States'

    # File access and having fun with the data :)
    filename = 'us.txt'
    with open(DATA_DIR_US, 'r') as f:                           # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())

        df = pd.DataFrame(country_data_updated)
        df.columns = ['Cases']

        first_date = '01-22-20'
        end_date = '05-09-20'

        date_series = pd.date_range(start=first_date, end=end_date, freq='D')
        df_dates = pd.DataFrame()
        df_dates['Date'] = date_series
        df_dates_updated = df_dates
        df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')

        df_update = pd.concat([df_dates_updated, df], axis=1)

        new_cases = []                                          # Create an empty list to capture the DoD difference
        for i in range(len(country_data_updated) - 1):          # Iterate over the updated country data to eliminate
            if country_data_updated[i] != 0:                    # non-zero days and capture the difference in cases
                new_cases.append(int(country_data_updated[i+1]) - int(country_data_updated[i]))  # on a day-to day basis

        for i in range(0, len(new_cases)):                      # Find the total number of cases for the country
            country_sum += int(new_cases[i])

        df_new_cases = pd.DataFrame(new_cases)
        df_new_cases.columns = ['New Cases']

        df_new_cases_updated = pd.concat([df_dates_updated, df_new_cases], axis=1)

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
        print(" <> On " + str(df_update.at[105, 'Date']) + ", there were a total of " + str(df_update.at[105, 'Cases']) +
              " confirmed cases, including " + str(df_new_cases_updated.at[105, 'New Cases']) + " new cases of "
              "COVID-19 in " + country_name + ".")
        print('')


def load_india():

    country_name = 'India'

    # File access and having fun with the data :)
    filename = 'india.txt'
    with open(DATA_DIR_INDIA, 'r') as f:                        # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())

        df = pd.DataFrame(country_data_updated)
        df.columns = ['Cases']

        first_date = '01-22-20'
        end_date = '05-09-20'

        date_series = pd.date_range(start=first_date, end=end_date)
        df_dates = pd.DataFrame()
        df_dates['Date'] = date_series
        df_dates_updated = df_dates
        df_dates_updated['Date'] = df_dates['Date'].dt.strftime('%b-%d-%Y')

        df_update = pd.concat([df_dates_updated, df], axis=1)

        new_cases = []                                          # Create an empty list to capture the DoD difference
        for i in range(len(country_data_updated) - 1):          # Iterate over the updated country data to eliminate
            if country_data_updated[i] != 0:                    # non-zero days and capture the difference in cases
                new_cases.append(int(country_data_updated[i+1]) - int(country_data_updated[i]))  # on a day-to day basis

        for i in range(0, len(new_cases)):                      # Find the total number of cases for the country
            country_sum += int(new_cases[i])
        
        df_new_cases = pd.DataFrame(new_cases)
        df_new_cases.columns = ['New Cases']

        df_new_cases_updated = pd.concat([df_dates_updated, df_new_cases], axis=1)

        max_country = max(new_cases)                            # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list

        # Counts the total number of elements (days) in the list
        country_confirmed_cases = country_total_count - country_zero_count

        # Percentage of confirmed cases for country per all countries
        percentage_of_country_confirmed = int((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR INDIA.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_INDIA)
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR INDIA***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print(" <> On " + str(df_update.at[108, 'Date']) + ", there were a total of " + str(df_update.at[108, 'Cases']) +
              " confirmed cases, including " + str(df_new_cases_updated.at[105, 'New Cases']) + " new cases of "
              "COVID-19 in " + country_name + ".")
        print('')


def load_skorea():

    country_name = 'South Korea'

    # File access and having fun with the data :)
    filename = 'south korea.txt'
    with open(DATA_DIR_SKOREA, 'r') as f:                       # Open the file and read it
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
        percentage_of_country_confirmed = float((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR SOUTH KOREA.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_SKOREA )
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR SOUTH KOREA***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print('')


def load_japan():

    country_name = 'Japan'

    # File access and having fun with the data :)
    filename = 'japan.txt'
    with open(DATA_DIR_JAPAN, 'r') as f:                        # Open the file and read it
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
        percentage_of_country_confirmed = float((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR JAPAN.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_JAPAN)
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR JAPAN***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print('')


def load_lebanon():

    country_name = 'Lebanon'

    # File access and having fun with the data :)
    filename = 'lebanon.txt'
    with open(DATA_DIR_LEBANON, 'r') as f:                      # Open the file and read it
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
        percentage_of_country_confirmed = float((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR LEBANON.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_LEBANON)
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR LEBANON***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print('')


def load_mexico():

    country_name = 'Mexico'

    # File access and having fun with the data :)
    filename = 'mexico.txt'
    with open(DATA_DIR_MEXICO, 'r') as f:                       # Open the file and read it
        country_data = f.readlines()                            # Create a list from the array
        country_data_updated = []                               # Empty list to manipulate data
        country_sum = 0                                         # Creating variable to count total number of cases
        for elem in country_data:                               # Remove the newline character from the list
            country_data_updated.append(elem.strip())

        new_cases = []                                          # Create an empty list to capture the DoD difference
        for i in range(len(country_data_updated) - 1):          # Iterate over the updated country data to eliminate
            if country_data_updated[i] != 0:                    # non-zero days and capture the difference in cases
                new_cases.append(int(country_data_updated[i+1]) - int(country_data_updated[i]))  # on a day-to day basis

        for i in range(0, len(new_cases)):                      # Counts the number days with unconfirmed cases
            country_sum += int(new_cases[i])

        max_country = max(new_cases)                            # Locates the max value in the list
        country_zero_count = country_data_updated.count('0')    # Counts the number days with unconfirmed cases
        country_total_count = len(country_data_updated)         # Counts the total number of elements (days) in the list

        # Counts the total number of elements (days) in the list
        country_confirmed_cases = country_total_count - country_zero_count

        # Percentage of confirmed cases for country per all countries
        percentage_of_country_confirmed = float((country_sum / TOTAL_CASES) * 100)

        # Output to console
        print("***FILE INFORMATION FOR MEXICO.TXT***")
        print("You've accessed the file: " + filename)
        print("It is located in a relative directory in the following path: " + DATA_DIR_MEXICO)
        print("The file, " + filename + " contains " + str(country_total_count) + " total days")
        print('')
        print("***COVID-19 DATA FOR MEXICO***")
        print("For the dates encompassing Jan-22 to May-09:")
        print(" <> The total number of days with confirmed cases is: " + str(country_confirmed_cases))
        print(" <> The overall total number of confirmed cases is: " + str(country_sum))
        print(" <> " + country_name + " has " + str(
            percentage_of_country_confirmed) + "% of all confirmed cases worldwide")
        print(" <> The day with the most number of confirmed cases registered a total of: " + str(max_country))
        print('')


if __name__ == '__main__':
    main()
