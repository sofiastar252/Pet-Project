# Pet Project
# project_test_bonus.py
# Sofia Starinnova

import unittest
from datetime import datetime
import pandas as pd
from load_data import load_data
from calculate_age import calculate_age
from pet_analysis import calculate_average_price, find_pets_with_feature
from price_and_feature import clean_data


class TestPetProject(unittest.TestCase):

    # Setting up sample dataframe for testing
    def setUp(self):
        self.data = {
            'Name': ['Simba', 'Nala', 'Timon', 'Pumbaa', 'Mufasa'],
            'Birthdate': ['6/15/2020', '5/30/2019', '8/25/2018', '9/15/2017', '1/1/2015'],
            'Price': [100, 90, 50, 70, 150],
            'Species': ['Lion', 'Lion', 'Meerkat', 'Warthog', 'Lion'],
            'SpecialFeature': ['King', 'Queen', 'Wise', 'Funny', 'King']
        }
        self.df = pd.DataFrame(self.data)

    # Test loading dataframe of pets.csv
    def test_load_data(self):
        df = load_data('pets.csv')
        self.assertIsInstance(df, pd.DataFrame)
    
    # Test calculating age
    def test_calculate_age(self):
        birthdate_str = '6/15/2020'
        age = calculate_age(birthdate_str)
        expected_age = datetime.today().year - datetime.strptime(birthdate_str, "%m/%d/%Y").year
        self.assertEqual(age, expected_age)

    # Test calculating average price
    def test_calculate_average_price(self):
        species = 'Lion'
        avg_price = calculate_average_price(self.df, species)
        self.assertAlmostEqual(avg_price, 113.33, places=2)  # (100 + 90 + 150) / 3

    # Test finding pets with a specific feature
    def test_find_pets_with_feature(self):
        feature = 'King'
        pets = find_pets_with_feature(self.df, feature)
        self.assertEqual(pets, ['Simba', 'Mufasa'])
    
    # Test cleaning data
    def test_clean_data(self):
        cleaned_df = clean_data(self.df)
        self.assertIsInstance(cleaned_df, pd.DataFrame)
        self.assertEqual(len(cleaned_df.columns), 6)
        self.assertIn('PetID', cleaned_df.columns)


if __name__ == '__main__':
    unittest.main()
