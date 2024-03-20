import pandas as pd
import numpy as np

# load in the data
df = pd.read_excel(r"Lab 2 - Bolted Connections\matplotlib\jayden data\total_data.xlsx")

# create results
results = pd.DataFrame()

C = 0.160
E_b = 208.007
strain_to_stress = E_b * 4 / 5 / 2 / 400 * 1000

# calculate the stress
df["stress"] = df["Bolt"] * strain_to_stress

# find number of unique file names in 'file'
files = df["File"].unique()

for file in files:
    df_file = df[df["File"] == file]
    df_file = df_file.reset_index(drop=True)

    # find the maximum stress
    max_stress = df_file["stress"].max()

    # find the minimum stress
    min_stress = df_file["stress"].min()

    # mean stress
    mean_stress = (max_stress + min_stress) / 2

    # alternating stress
    alternating_stress = (max_stress - min_stress) / 2

    results = pd.concat(
        [
            results,
            pd.DataFrame(
                {
                    "file": [file],
                    "max_stress": [max_stress],
                    "min_stress": [min_stress],
                    "mean_stress": [mean_stress],
                    "alternating_stress": [alternating_stress],
                }
            ),
        ]
    )

# save the results
results.to_csv(r"Lab 2 - Bolted Connections\matplotlib\jayden data\results.csv", index=False)
