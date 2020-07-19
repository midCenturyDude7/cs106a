"""
Filename: file_iterate_practice
Use the glob library to iterate through the /confirmed directory and open
each file and create a pandas df that captures all the data in each file
in one table
"""

# Dependencies
import csv
import pandas as pd
import numpy as np
import glob


def main():
    open_files()


# Use glob to open each file and store the data in a pandas df
def open_files():
    path = r'C:\Users\mjgri\Programming\cs106a\confirmed'
    all_files = glob.glob(path + "/*.txt")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
    
    frame = pd.concat(li, axis=0, ignore_index=True)
    print(frame)


if __name__ == '__main__':
    main()
