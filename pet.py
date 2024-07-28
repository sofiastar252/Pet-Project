# Pet Project
# pet.py
# Sofia Starinnova

from pet_analysis import get_species_statistics, calculate_average_price, find_pets_with_feature
from calculate_age import get_average_ages

import pandas as pd
from load_data import load_data


def clean_data(data_frame):
    # Load data frame
    if data_frame is not None:
        # Check for missing values in the DataFrame
        print("Missing values per column:")
        print(data_frame.isnull().sum())

        print("\nMissing values details:")
        print(data_frame.isnull().sum()[data_frame.isnull().sum() > 0])

        # Print the DataFrame before filling missing values
        print("\nDataFrame before filling missing values:")
        print(data_frame.to_string(index=False, max_rows=None))

        # Filling in missing values using forward fill
        data_frame = data_frame.ffill()

        # Making sure they have the correct column names
        data_frame.columns = ['Name', 'Birthdate', 'Price', 'Species', 'SpecialFeature']

        # Adding PetID as the first column
        data_frame.insert(0, 'PetID', data_frame.index)

        # Return the cleaned DataFrame
        return data_frame
    else:
        print(f"Error loading data.")
        return None


# Clean the data and print the cleaned DataFrame
if __name__ == "__main__":
    file_path = 'pets.csv'
    cleaned_data = clean_data(load_data(file_path))
    if cleaned_data is not None:
        print("\nCleaned DataFrame:")
        print(cleaned_data.to_string(index=False, max_rows=None))

        # Calculate and print average ages for each species
        average_ages = get_average_ages(cleaned_data)

        # Average price of a species (Rabbit)
        species = 'Rabbit'
        average_price = calculate_average_price(cleaned_data, species)
        if average_price is not None:
            # Print average price of species with dollar sign
            print(f"\nAverage price of {species}: ${average_price:.2f}")
        else:
            # If no data is found, then print the message out
            print(f"\nNo data found for species: {species}")

        # Find pets with specific special feature (flies)
        feature = 'flies'
        pets_with_feature = find_pets_with_feature(cleaned_data, feature)
        if pets_with_feature:
            # Print names with feature
            print(f"\nNames of pets with special feature '{feature}': {', '.join(pets_with_feature)}")
        else:
            # Print message if no pets were found
            print(f"\nNo pets were found with the special feature: {feature}")

        # Get species statistics
        species_stats = get_species_statistics(cleaned_data)
        print("\nSpecies Statistics:")
        printed_species = set()  # To keep track of species already printed
        for species, stats in species_stats.items():
            if species not in printed_species:
                print(f"\nSpecies: {species}")
                printed_species.add(species)  # Add the species to the printed set

            if stats['Average Price'] is not None:
                print(f"Average Price: ${stats['Average Price']:.2f}")

            # Check if average age is available and print it
            if stats['Average Age'] is not None:
                print(f"Average Age: {stats['Average Age']:.2f} years")
            else:
                # If average age is not available in species stats, try to fetch it from the calculated average ages
                if species in average_ages:
                    print(f"Average Age: {average_ages[species]:.2f} years")
                else:
                    print(f"No data found for average age of {species}")

    else:
        # Print Error message
        print("Error cleaning data.")
