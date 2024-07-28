# Pet-Project
This project involves analyzing and visualizing pet data through a pets.csv file. 
It covers the following topics: Data Loading & Cleaning, Decision Making and Loops, Functions and Modules, Python Libraries, Data Visualization with Python (Matplotlib, Seaborn, Plotly).

The tasks performed include data loading, cleaning, and generating various visualizations to gain insights into the dataset.

Environment Setup Instructions
To run this project, you need to install the following Python libraries:
* pip install pandas
* pip install matplotlib
* pip install seaborn
* pip install plotly
* pip install -U kaleido

Running the Project To run the project, you only need to run two scripts using the terminal:
* python pet.py
* python price_and_feature.py


Project Details
Data Loading and Cleaning
* File: load_data.py
* This script loads the pet data from a CSV file and handles any missing values by filling them.

Calculating Age
* File: calculate_age.py
* This script contains functions to calculate the age of pets based on their birthdays.

Analyzing Data
* File: pet_analysis.py
* This script includes functions to calculate average prices and find pets with specific features.

Main Script
* File: pet.py
* This script takes care of all the data loading, cleaning, and initial analysis, printing the results to the console.

Visualizing Data
* File: price_and_feature.py
* This script generates various visualizations:
    * Price Distribution: Shows the distribution of pet prices.
    * Average Price by Species: Displays the average price of pets by species.
    * Price vs Age: Plots the price of pets against their age.
    * Age Distribution by Species: Uses Plotly to show the distribution of pet ages by species.

Unit Tests
* File: project_test_bonus.py
* This script includes unit tests for the key functions to make sure that they work correctly.
