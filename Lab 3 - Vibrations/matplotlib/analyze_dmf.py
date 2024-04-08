import numpy as np
import pandas as pd
import re

# read data from excel
df = pd.read_excel(
    r"Lab 3 - Vibrations\data_and_analysis.xlsx", sheet_name="dmf for pandas"
)

# find the unique dataset in 'dataset' column
datasets = df["dataset"].unique()

df_results = pd.DataFrame(columns=["dataset", "frequency", "dmf", "Mean Amplitude"])
# loop through each dataset and perform analysis
for dataset in datasets:
    # filter the dataset
    df_dataset = df[df["dataset"] == dataset]

    # perform regex on the dataset name to extract the frequency
    # dataset is formatted 'small 1.00Hz;
    frequency = float(re.search(r"\d+\.\d+", dataset).group())

    # remove outliers more than 3 standard deviations from the mean
    df_dataset = df_dataset[
        np.abs(df_dataset["amplitude"] - df_dataset["amplitude"].mean())
        <= (2 * df_dataset["amplitude"].std())
    ]

    # if any outliers were removed, print a message
    if len(df_dataset) < len(df[df["dataset"] == dataset]):
        print(f"Outliers removed from dataset: {dataset}")

    # calculate the mean amplitude
    mean_amplitude = df_dataset["amplitude"].mean()

    # calculate the dmf
    dmf = 2 * mean_amplitude / 3.55  # 3.55 is the value from lab

    # append the results to the results dataframe with concat
    # df_results = pd.concat(
    #     [df_results, pd.DataFrame([[dataset, frequency, dmf]], columns=df_results.columns)]
    # )
    df_results = df_results.append(
        pd.DataFrame([[dataset, frequency, dmf, mean_amplitude]], columns=df_results.columns)
    )

# save the results to a new excel file
df_results.to_excel(r"Lab 3 - Vibrations\matplotlib\dmf_results.xlsx", index=False)
