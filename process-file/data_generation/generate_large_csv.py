import csv
from faker import Faker

def generate_large_csv(file_path, num_rows):
    """
    Generate a large CSV file with fake data.

    Parameters:
    - file_path: The path where the generated CSV file will be saved.
    - num_rows: The number of rows of data to generate.
    """
    fake = Faker()
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Write the header row to the CSV file
        writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])
        
        # Generate and write each row of fake data
        for _ in range(num_rows):
            writer.writerow([fake.first_name(), fake.last_name(), fake.address(), fake.date_of_birth()])
