import os
import pandas as pd

# Find the files in the directory
files = os.listdir('.')
files.remove('merge.py')

total_df = pd.DataFrame()

for file in files:
    # Read the .dat file
    df = pd.read_csv(f'{file}/specimen.dat', sep='\t', header=None, on_bad_lines='skip', skiprows = 3)

    # Clean the data
    df = df.dropna()
    df = df[(df[0] != 'Time') & (df[0] != 's')]
    df.reset_index(drop=True, inplace=True)
    df.columns = {'Time', 'Force', 'Bolt'}

    # Add the data to the total dataframe and add a column denoting which file it came from
    df['File'] = file
    total_df = pd.concat([total_df, df], ignore_index=True)

# Save the dataframe to a xlsx
total_df.to_excel('total_data.xlsx', index=False)