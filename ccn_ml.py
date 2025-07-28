import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import scikit-learn as sk


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
        data.fillna(method='ffill', inplace=True)  # Forward fill for simplicity
    
    # Convert date column to datetime format if exists
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'])
    
    return data

