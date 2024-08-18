import unittest
import os
import csv
from data_generation.generate_large_csv import generate_large_csv

class TestGenerateLargeCSV(unittest.TestCase):

    def setUp(self):
        self.file_path = 'test_large_data.csv'

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_generate_large_csv(self):
        """Test generating a CSV file with a small number of rows."""
        generate_large_csv(self.file_path, 10)  # Generate a small CSV for testing

        # Verify that the file was created
        self.assertTrue(os.path.isfile(self.file_path))

        # Verify the content using csv.DictReader to properly handle quoted fields
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            # Debugging output to check how many rows were generated
            print(f"Number of rows in generated file: {len(rows)}")
            for row in rows:
                print(row)

            self.assertEqual(len(rows), 10)  # Expect exactly 10 data rows

if __name__ == '__main__':
    unittest.main()
