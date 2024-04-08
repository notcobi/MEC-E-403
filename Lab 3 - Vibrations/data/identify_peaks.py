import os
import pandas as pd
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load data from a file and return a pandas DataFrame.
    """
    data = pd.read_csv(file_path)

    # Remove the rows 0 to 1 and reset the index
    data = data[3:].reset_index(drop=True)

    # Split the columns into separate columns by the tab delimiter
    data[["Time", "Driven Amplitude", "Driver Amplitude"]] = data.iloc[:, 0].str.split(
        "\t", expand=True
    )

    # Remove the original column
    data = data.drop(columns=data.columns[0])
    return data


def identify_peaks_and_valleys(data):
    """
    Identify peaks in the data and return the indices of the peaks and valleys.
    """
    # Convert the data to a numpy array
    data_array = data.to_numpy()

    # Get the driven amplitude
    driven_amplitude = data_array[:, 1].astype(float)
    driving_amplitude = data_array[:, 2].astype(float)

    # Identify peaks and valleys
    peaks_driven, peak_driven_properties = scipy.signal.find_peaks(
        driven_amplitude, height=0, distance=35, prominence=0.2
    )
    valleys_driven, valley_driven_properties = scipy.signal.find_peaks(
        -driven_amplitude, height=0, distance=35, prominence=0.2
    )
    peaks_driving, peak_driving_properties = scipy.signal.find_peaks(
        driving_amplitude, height=0, distance=35, prominence=0.2
    )
    valleys_driving, valley_driving_properties = scipy.signal.find_peaks(
        -driving_amplitude, height=0, distance=35, prominence=0.2
    )

    peaks_driven_df = pd.DataFrame(
        {
            "Index": peaks_driven,
            "Driven Peak Time": data_array[:, 0][peaks_driven],
            "Driven Peak Amplitude": data_array[:, 1][peaks_driven],
        }
    )
    valleys_driven_df = pd.DataFrame(
        {
            "Index": valleys_driven,
            "Driven Valley Time": data_array[:, 0][valleys_driven],
            "Driven Valley Amplitude": data_array[:, 1][valleys_driven],
        }
    )

    peaks_driving = pd.DataFrame(
        {
            "Index": peaks_driving,
            "Driving Peak Time": data_array[:, 0][peaks_driving],
            "Driving Peak Amplitude": data_array[:, 2][peaks_driving],
        }
    )
    valleys_driving = pd.DataFrame(
        {
            "Index": valleys_driving,
            "Driving Valley Time": data_array[:, 0][valleys_driving],
            "Driving Valley Amplitude": data_array[:, 2][valleys_driving],
        }
    )

    return peaks_driven_df, valleys_driven_df, peaks_driving, valleys_driving


def plot_peaks_and_valleys(data, peaks_driven, valleys_driven, peaks_driving, valleys_driving, file):
    """
    Plot the peaks and valleys on the data.
    """
    # Convert the data to a numpy array
    data_array = data.to_numpy()

    # Get the data
    time = data_array[:, 0].astype(float)
    driven_amplitude = data_array[:, 1].astype(float)

    # Plot the driven amplitude
    plt.plot(time, driven_amplitude)

    # Plot the peaks and valleys
    plt.plot(time[peaks_driven["Index"]], driven_amplitude[peaks_driven["Index"]], "x", label="Driven Peaks")
    plt.plot(time[valleys_driven["Index"]], driven_amplitude[valleys_driven["Index"]], "x", label="Driven Valleys")

    # Get the file name without the extension
    file = file.split(".xls")[0]

    # Add labels and title
    plt.xlabel("$t$, Time (s)")
    plt.ylabel("$A$, Amplitude")
    # plt.title("Driven Amplitude Peaks and Valleys for " + file)

    # plt.show()

    # Save the plot in subfolder "plots"
    plt.savefig("plots/driven/" + file + ".png")
    plt.close()

    # Now plot the driving amplitude
    driving_amplitude = data_array[:, 2].astype(float)

    # Plot the driving amplitude
    plt.plot(time, driving_amplitude)

    # Plot the peaks and valleys
    plt.plot(time[peaks_driving["Index"]], driving_amplitude[peaks_driving["Index"]], "x", label="Driving Peaks")
    plt.plot(time[valleys_driving["Index"]], driving_amplitude[valleys_driving["Index"]], "x", label="Driving Valleys")

    # Add labels and title
    plt.xlabel("$t$, Time (s)")
    plt.ylabel("$A$, Amplitude (cm)")
    # plt.title("Driving Amplitude Peaks and Valleys for " + file)

    # plt.show()

    # Save the plot in subfolder "plots"
    plt.savefig("plots/driving/" + file + ".png")
    plt.close()

def save_data(data, peaks_driven, valleys_driven, peaks_driving, valleys_driving, file_path):
    """
    Save data to a file.
    """

    # Concatenate the peaks and valleys to the data
    # time \t driven amplitude \t driver amplitude \t peak time \t peak amplitude \t valley time \t valley amplitude
    # fill in the missing values with NaN so dimensions match
    peaks_driven = peaks_driven.reindex(data.index)
    valleys_driven = valleys_driven.reindex(data.index)
    peaks_driving = peaks_driving.reindex(data.index)
    valleys_driving = valleys_driving.reindex(data.index)

    data = pd.concat([data, peaks_driven, valleys_driven, peaks_driving, valleys_driving], axis=1)

    # Strip the file extension
    file_path = file_path.split(".xls")[0] + "_analyzed.csv"
    
    # Save the data to a file
    path = "analyzed/" + file_path
    data.to_csv(path, sep=",", index=False)


# Get the current directory
current_directory = os.getcwd()

# Get a list of files in the current directory
files = os.listdir(current_directory)

# Remove the file "identify_peaks.py", and the subfolder "plots", and the subfolder "analyzed"
files.remove("identify_peaks.py")
files.remove("plots")
files.remove("analyzed")

# Print the list of files
for file in files:
    df = load_data(file)
    #peaks, valleys = identify_peaks_and_valleys(df)
    peaks_driven, valleys_driven, peaks_driving, valleys_driving = identify_peaks_and_valleys(df)
    plot_peaks_and_valleys(df, peaks_driven, valleys_driven, peaks_driving, valleys_driving, file)
    save_data(df, peaks_driven, valleys_driven, peaks_driving, valleys_driving, file)
    print(file)