import pandas as pd
import numpy as np
import seaborn as sns
import os
import matplotlib.pyplot as plt
from sklearn import preprocessing


def load_ccn_data(file_path):
    """
    Load CCN data from a CSV file and preprocess it.

    Parameters:
    file_path (str): The path to the CSV file containing CCN data.

    Returns:
    pd.DataFrame: A DataFrame containing the preprocessed CCN data.
    """
    # Load the data
    data = pd.read_csv(file_path)

    # Check for missing values and handle them
    if data.isnull().values.any():
        data.fillna(method="ffill", inplace=True)  # Forward fill for simplicity

    # Convert date column to datetime format if exists
    if "date" in data.columns:
        data["date"] = pd.to_datetime(data["date"])

    return data


# Function to visualize CCN data
def visualize_ccn_data(data):
    """
    Visualize the CCN data using matplotlib.

    Parameters:
    data (pd.DataFrame): The DataFrame containing CCN data.
    """
    plt.figure(figsize=(10, 6))

    if "date" in data.columns:
        plt.plot(data["date"], data["ccn_count"], label="CCN Count")
        plt.xlabel("Date")
    else:
        plt.plot(data.index, data["ccn_count"], label="CCN Count")
        plt.xlabel("Index")

    plt.ylabel("CCN Count")
    plt.title("CCN Data Visualization")
    plt.legend()
    plt.grid()
    plt.show()


def main():
    # Define the file path for CCN data
    file_path = "path/to/ccn_data.csv"

    # Load the CCN data
    ccn_data = load_ccn_data(file_path)

    # Visualize the CCN data
    visualize_ccn_data(ccn_data)


if __name__ == "__main__":
    main()
