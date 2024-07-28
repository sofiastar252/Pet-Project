# Pet Project
# pet_analysis.py
# Sofia Starinnova

def calculate_average_price(df, species):
    filtered_df = df[df['Species'] == species]
    if filtered_df.empty:
        return None
    return filtered_df['Price'].mean()

def calculate_average_age(df, species):
    filtered_df = df[df['Species'] == species]
    if filtered_df.empty:
        return None
    if 'Age' in filtered_df.columns:
        return filtered_df['Age'].mean()
    return None

def find_pets_with_feature(df, feature):
    filtered_df = df[df['SpecialFeature'] == feature]
    return filtered_df['Name'].tolist()

def get_species_statistics(df):
    species_statistics = {}
    species_list = df['Species'].unique()
    for species in species_list:
        average_price = calculate_average_price(df, species)
        average_age = calculate_average_age(df, species)
        species_statistics[species] = {'Average Price': average_price, 'Average Age': average_age}
    return species_statistics
