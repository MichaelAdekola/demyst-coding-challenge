import unittest
import os
import csv
from anonymization.anonymize_data import anonymize_data, anonymize_value

class TestAnonymizeData(unittest.TestCase):

    def setUp(self):
        self.input_csv = 'test_large_data.csv'
        self.output_csv = 'test_anonymized_data.csv'

        # Create a small sample CSV file for testing
        with open(self.input_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])
            writer.writerow(['Michael', 'Scott', '123 pippin Ave', '1990-12-12'])
            writer.writerow(['Jane', 'Doe', '456 peacock St', '1992-02-02'])

    def tearDown(self):
        if os.path.exists(self.input_csv):
            os.remove(self.input_csv)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)

    def test_anonymize_value(self):
        """Test that the anonymization function works as expected."""
        original = "Michael Scott"
        anonymized = anonymize_value(original)
        self.assertNotEqual(original, anonymized)
        self.assertEqual(len(anonymized), 32)  # MD5 produces a 32-character hex string

    def test_anonymize_data(self):
        """Test that the data is anonymized correctly."""
        # Run the anonymization process
        anonymize_data(self.input_csv, self.output_csv)

        # Verify that the output file exists
        self.assertTrue(os.path.isfile(self.output_csv))

        # Read the output CSV and verify the data has been anonymized
        with open(self.output_csv, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            original_dobs = ['1990-12-12', '1992-02-02']
            for row in reader:
                # Ensure first_name, last_name, and address are anonymized (hashed)
                self.assertNotEqual(row['first_name'], 'Michael')
                self.assertNotEqual(row['last_name'], 'Scott')
                self.assertNotEqual(row['address'], '123 Pippin Ave')

                # Ensure date_of_birth remains one of the original values
                self.assertIn(row['date_of_birth'], original_dobs)

    def test_anonymize_data_chunking(self):
        """Test the chunking functionality works correctly."""
        # Using a very small chunk size for testing purposes
        anonymize_data(self.input_csv, self.output_csv, chunk_size=1)

        # Verify that the output file exists
        self.assertTrue(os.path.isfile(self.output_csv))

        # Read the output CSV and verify the data has been anonymized correctly
        with open(self.output_csv, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 2)
            self.assertNotEqual(rows[0]['first_name'], 'Michael')
            self.assertNotEqual(rows[1]['first_name'], 'Jane')

if __name__ == '__main__':
    unittest.main()
