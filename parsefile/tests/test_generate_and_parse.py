import unittest
import os
import json
import sys
import csv

# Add the parent directory to the system path so we can import the main script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the functions from the main script
from generate_and_parse.main import generate_fixed_width_file, parse_fixed_width_to_csv


class TestFixedWidthConverter(unittest.TestCase):

    def setUp(self):
        # Set up the specification for the fixed-width file
        self.spec = {
            "ColumnNames": [
                "Business ID",
                "Business Name",
                "State",
                "Postal Code",
                "Industry",
                "Number of Employees",
                "Revenue",
                "Established Year",
                "ABN",
                "Website"
            ],
            "Offsets": [
                "6",
                "20",
                "3",
                "4",
                "15",
                "3",
                "7",
                "4",
                "11",
                "25"
            ],
            "FixedWidthEncoding": "windows-1252",
            "IncludeHeader": "True",
            "DelimitedEncoding": "utf-8"
        }

        # Test data
        self.data = [
            ["AUS001", "Sydney Cafe", "NSW", "2000", "Hospitality", "25", "350", "2010", "12345678901", "sydneycafe.com.au"],
            ["AUS002", "Melbourne Tech", "VIC", "3000", "Technology", "50", "1200", "2015", "98765432109", "melbournetech.com.au"],
            ["AUS003", "Brisbane Fitness", "QLD", "4000", "Health", "40", "850", "2008", "45678901234", "brisbanefitness.com.au"]
        ]

        # Expected content of the CSV after parsing
        self.expected_csv_content = [
            ["Business ID", "Business Name", "State", "Postal Code", "Industry", "Number of Employees", "Revenue", "Established Year", "ABN", "Website"],
            ["AUS001", "Sydney Cafe", "NSW", "2000", "Hospitality", "25", "350", "2010", "12345678901", "sydneycafe.com.au"],
            ["AUS002", "Melbourne Tech", "VIC", "3000", "Technology", "50", "1200", "2015", "98765432109", "melbournetech.com.au"],
            ["AUS003", "Brisbane Fitness", "QLD", "4000", "Health", "40", "850", "2008", "45678901234", "brisbanefitness.com.au"]
        ]

        # Temporary file names used in tests
        self.fixed_width_file = 'test_input.txt'
        self.csv_file = 'test_output.csv'

    def tearDown(self):
        # Clean up the generated files after each test
        try:
            os.remove(self.fixed_width_file)
            os.remove(self.csv_file)
        except OSError:
            pass

    def test_generate_fixed_width_file(self):
        # Test the function that generates the fixed-width file
        generate_fixed_width_file(self.spec, self.data, self.fixed_width_file)

        # Check that the file exists
        self.assertTrue(os.path.isfile(self.fixed_width_file))

        # Read the file and check contents
        with open(self.fixed_width_file, 'r', encoding=self.spec['FixedWidthEncoding']) as file:
            lines = file.readlines()

        # Check that header exists and is correct
        self.assertEqual(len(lines), len(self.data) + 1)  # Includes header
        self.assertTrue(lines[0].startswith("Business ID"))

    def test_parse_fixed_width_to_csv(self):
        # First generate the fixed-width file
        generate_fixed_width_file(self.spec, self.data, self.fixed_width_file)

        # Then parse it into a CSV
        parse_fixed_width_to_csv(self.spec, self.fixed_width_file, self.csv_file)

        # Check that the CSV file exists
        self.assertTrue(os.path.isfile(self.csv_file))

        # Read the CSV file and check contents
        with open(self.csv_file, 'r', encoding=self.spec['DelimitedEncoding']) as csvfile:
            reader = list(csv.reader(csvfile))
        
        # Compare the CSV content with the expected output
        self.assertEqual(reader, self.expected_csv_content)

if __name__ == '__main__':
    unittest.main()
