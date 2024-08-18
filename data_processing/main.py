from data_generation.generate_large_csv import generate_large_csv
from anonymization.anonymize_data import anonymize_data

if __name__ == "__main__":
    # Step 1: Generate the large CSV file
    print("Generating large CSV file...")
    generate_large_csv('large_data.csv', 10000000)  # Adjust rows for local testing if needed
    print("CSV generation complete.")

    # Step 2: Anonymize the data
    print("Anonymizing data...")
    anonymize_data('large_data.csv', 'anonymized_data.csv')
    print("Data anonymization complete.")
