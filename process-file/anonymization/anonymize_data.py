import csv
import hashlib

def anonymize_value(value):
    """Anonymize a single value using MD5 hashing."""
    return hashlib.md5(value.encode()).hexdigest()

def anonymize_data(input_file, output_file, chunk_size=10000):
    """
    Anonymize first_name, last_name, and address in the given CSV file, processing in chunks.
    
    Parameters:
    - input_file: The path to the input CSV file containing the data to be anonymized.
    - output_file: The path to the output CSV file where anonymized data will be saved.
    - chunk_size: The number of rows to process at a time before writing to the output file.
    """
    # Open the input CSV file for reading and the output CSV file for writing
    with open(input_file, 'r') as csvfile, open(output_file, 'w', newline='') as outfile:
        # Create a DictReader to read the input file as a dictionary (fieldnames -> values)
        reader = csv.DictReader(csvfile)
        # Create a DictWriter to write the anonymized data to the output file
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

        # Write the header to the output file
        writer.writeheader()
        
        chunk = []
        for row in reader:
            # Anonymize specific fields by hashing their values
            row['first_name'] = anonymize_value(row['first_name'])
            row['last_name'] = anonymize_value(row['last_name'])
            row['address'] = anonymize_value(row['address'])

            # Add the anonymized row to the current chunk
            chunk.append(row)

            # If the chunk reaches the specified chunk_size, write it to the output file
            if len(chunk) >= chunk_size:
                writer.writerows(chunk)
                chunk = []   # Reset the chunk list to start collecting new rows

        # Write any remaining rows in the final chunk to the output file
        if chunk:
            writer.writerows(chunk)

if __name__ == "__main__":
    input_csv = 'large_data.csv'
    output_csv = 'anonymized_data.csv'
    anonymize_data(input_csv, output_csv)
    print(f"Anonymization complete. Output saved to {output_csv}.")
