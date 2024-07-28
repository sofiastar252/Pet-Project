# Pet Project
# price_and_feature.py
# Sofia Starinnova

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from pet import clean_data
from load_data import load_data
from calculate_age import calculate_age


def calculate_average_price(df, species):
    # Filter by species
    filtered_df = df[df['Species'] == species]
    # Check if empty
    if filtered_df.empty:
        # If there's no data then return None
        return None
    return filtered_df['Price'].mean()


def find_pets_with_feature(df, feature):
    # Filter by special feature
    filtered_df = df[df['SpecialFeature'] == feature]
    # Return names
    return filtered_df['Name'].tolist()


def plot_price_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['Price'], bins=30, edgecolor='k', alpha=0.7)
    plt.title('Price Distribution of Pets')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('price_distribution.png')
    plt.show()


def plot_average_price_by_species(df):
    avg_prices = df.groupby('Species')['Price'].mean().reset_index()

    plt.figure(figsize=(10, 6))
    plt.bar(avg_prices['Species'], avg_prices['Price'], color='skyblue')
    plt.title('Average Price by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Price')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.savefig('average_price_by_species.png')
    plt.show()


def plot_price_vs_age(df):
    # Calculate age
    df['Age'] = df['Birthdate'].apply(calculate_age)

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y='Price', data=df)
    plt.title('Price vs Age of Pets')
    plt.xlabel('Age (years)')
    plt.ylabel('Price')
    plt.grid(True)
    plt.savefig('price_vs_age.png')
    plt.show()


def plot_age_distribution_by_species(df):
    df['Age'] = df['Birthdate'].apply(calculate_age)

    fig = px.box(df, x='Species', y='Age', title='Age Distribution by Species', points="all")
    fig.update_layout(
        title={
            'text': 'Age Distribution by Species',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        title_font_size=24,
        title_font_color='cyan',
        plot_bgcolor='black',
        paper_bgcolor='black',
        font_color='white'
    )
    fig.write_image('age_distribution_by_species.png')
    fig.show()


# Main execution for Task 4 and Task 5
if __name__ == "__main__":
    # Load and clean data
    file_path = 'pets.csv'
    df = clean_data(load_data(file_path))

    if df is not None:
        # Task 4a: Plot Price Distribution
        plot_price_distribution(df)

        # Task 4b: Plot Average Price by Species
        plot_average_price_by_species(df)

        # Main execution for Task 5
        # Task 5a: Plot Price vs Age (Seaborn)
        plot_price_vs_age(df)

        # Task 5b: Plot Age Distribution by Species (Plotly)
        plot_age_distribution_by_species(df)
    else:
        print("Data loading and cleaning failed.")
