# Pet Project
# load_data.py
# Sofia Starinnova

import pandas as pd


def load_data(file_path):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Return the DataFrame
        return df
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


if __name__ == "__main__":
    file_path = 'pets.csv'
    data_frame = load_data(file_path)
    if data_frame is not None:
        print(data_frame.head())
