import csv
import json

def generate_fixed_width_file(spec, data, output_file):
    """
    Generates a fixed-width file based on the provided specification and data.

    Parameters:
    - spec: A dictionary containing the fixed-width file specification, including column names, offsets, and encoding.
    - data: A list of lists, where each inner list represents a row of data to be written to the file.
    - output_file: The name of the output fixed-width file.
    """
    # Open the output file for writing with the specified encoding
    with open(output_file, 'w', encoding=spec['FixedWidthEncoding']) as file:
        if spec.get('IncludeHeader') == "True":
            header = ''.join([name.ljust(int(offset)) for name, offset in zip(spec['ColumnNames'], spec['Offsets'])])
            file.write(header + '\n')

        # Write each row of data to the file, formatted according to the specified offsets
        for row in data:
            line = ''.join([str(value).ljust(int(offset)) for value, offset in zip(row, spec['Offsets'])])
            file.write(line + '\n')

def parse_fixed_width_to_csv(spec, fixed_width_file, output_csv):
    """
    Parses a fixed-width file into a CSV format based on the provided specification.

    Parameters:
    - spec: A dictionary containing the fixed-width file specification, including column names, offsets, and encoding.
    - fixed_width_file: The name of the input fixed-width file to be parsed.
    - output_csv: The name of the output CSV file.
    """
    # Open the fixed-width file for reading with the specified encoding
    with open(fixed_width_file, 'r', encoding=spec['FixedWidthEncoding']) as file:
        lines = file.readlines()
    
    # Convert the offset strings to integers for processing
    offsets = list(map(int, spec['Offsets']))
    
    with open(output_csv, 'w', encoding=spec['DelimitedEncoding'], newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        if spec.get('IncludeHeader') == "True":
            writer.writerow(spec['ColumnNames'])
            lines = lines[1:]  # Skip header in fixed-width file
        
        # Parse each line from the fixed-width file and write it as a row in the CSV file
        for line in lines:
            start = 0
            row = []
            for offset in offsets:
                row.append(line[start:start+offset].strip())
                start += offset
            writer.writerow(row)

if __name__ == "__main__":
    # Load the spec.json file
    with open('spec.json', 'r') as f:
        spec = json.load(f)
    
    # Example data to be used for generating the fixed-width file
    data = [
        ["AUS001", "Sydney Cafe", "NSW", "2000", "Hospitality", "25", "350", "2010", "12345678901", "sydneycafe.com.au"],
        ["AUS002", "Melbourne Tech", "VIC", "3000", "Technology", "50", "1200", "2015", "98765432109", "melbournetech.com.au"],
        ["AUS003", "Brisbane Fitness", "QLD", "4000", "Health", "40", "850", "2008", "45678901234", "brisbanefitness.com.au"],
        ["AUS004", "Perth Mining", "WA", "6000", "Mining", "300", "15000", "1998", "32109876543", "perthmining.com.au"],
        ["AUS005", "Adelaide Art", "SA", "5000", "Art & Design", "15", "150", "2012", "23456789012", "adelaideart.com.au"]
    ]

    # Generate the fixed-width file
    generate_fixed_width_file(spec, data, 'input.txt')
    print("Fixed-width file 'input.txt' generated.")

    # Parse the fixed-width file to CSV
    parse_fixed_width_to_csv(spec, 'input.txt', 'output.csv')
    print("CSV file 'output.csv' generated.")