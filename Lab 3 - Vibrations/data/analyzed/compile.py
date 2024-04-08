import pandas as pd
import os

# Get the list of files in the data directory in 'Lab 3 - Vibrations\data\analyzed'
files = os.listdir(r'Lab 3 - Vibrations\data\analyzed')
# remove the file 'compile.py' from the list
files.remove('compile.py')

df_combined = pd.DataFrame()
for i, file in enumerate(files):
    file_path = "Lab 3 - Vibrations/data/analyzed/" + file
    df_file = pd.read_csv(file_path)

    # Take the columns ,Driver Amplitude,Index,Driven Peak Time,Driven Peak Amplitude,Index,Driven Valley Time,Driven Valley Amplitude,Index,Driving Peak Time,Driving Peak Amplitude,Index,Driving Valley Time,Driving Valley Amplitude
    results = df_file[['Driver Amplitude', 'Driven Peak Time', 'Driven Peak Amplitude', 'Driven Valley Time', 'Driven Valley Amplitude', 'Driving Peak Time', 'Driving Peak Amplitude', 'Driving Valley Time', 'Driving Valley Amplitude']]

    # If any row has a NaN value, drop the row
    results = results.dropna()

    # add a column with the file name
    results['File'] = file

    # Concatenate the results to the combined dataframe
    df_combined = pd.concat([df_combined, results])

# Save the combined dataframe to a xlsx
df_combined.to_excel("Lab 3 - Vibrations/data/analyzed/compiled.xlsx", index=False)