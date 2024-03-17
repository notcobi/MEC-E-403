import pandas as pd
import numpy as np

# load in the data
df = pd.read_csv(r"Lab 2 - Bolted Connections\matplotlib\total_data.csv")

# create results
results = pd.DataFrame()

C = 0.166915791
d = 9.525
E_b = 205.0459528
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
results.to_csv(r"Lab 2 - Bolted Connections\matplotlib\results.csv", index=False)
