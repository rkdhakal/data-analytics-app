import pandas as pd

def load_and_clean_data(file_path):
    """
    Loads the CSV file and cleans the column names.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Cleaned pandas DataFrame.
    """
    # Load the dataset
    data = pd.read_csv('data\biostats.csv')

    # Clean the column names (remove quotes and whitespace)
    data.columns = data.columns.str.replace('"', '').str.strip()

    return data
