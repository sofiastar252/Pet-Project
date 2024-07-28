# Pet Project
# calculate_age.py
# Sofia Starinnova

import pandas as pd
from datetime import datetime

def calculate_age(birthdate_str):
    # Calculate age in years
    birthdate = datetime.strptime(birthdate_str, "%m/%d/%Y")
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def calculate_average_age(df, species):
    # Calculate average age for specific species
    filtered_df = df[df['Species'] == species].copy()
    if filtered_df.empty:
        return None
    # Calculate age for each pet
    filtered_df.loc[:, 'Age'] = filtered_df['Birthdate'].apply(calculate_age)
    return filtered_df['Age'].mean()

def get_average_ages(df):
    # Calculate average age for each species
    species_ages = {}
    species_list = df['Species'].unique()
    for species in species_list:
        average_age = calculate_average_age(df, species)
        species_ages[species] = average_age
    return species_ages

# Testing the functions
if __name__ == "__main__":
    from pet import clean_data
    cleaned_data = clean_data()
    if cleaned_data is not None:
        average_ages = get_average_ages(cleaned_data)
        print("\nAverage Ages for Each Species:")
        for species, age in average_ages.items():
            if age is not None:
                print(f"{species}: {age:.2f} years")
            else:
                print(f"{species}: No data available")
    else:
        print("Error cleaning data.")
