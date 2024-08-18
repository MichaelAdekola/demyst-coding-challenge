# Data Processing and Anonymization

This project is part of a coding challenge focused on processing large datasets. The tasks include generating a CSV file with synthetic data and anonymizing specific columns in the CSV file. The solution is designed to work efficiently even with large datasets, such as a 2GB CSV file, and demonstrates the ability to handle even larger datasets using appropriate techniques.

## Usage

### 1. Generate the Large CSV File

To generate a large CSV file with synthetic data:

```bash
    python main.py
```
The `main.py` script will:
- Generate a large CSV file named large_data.csv with 10 million rows (adjustable).
- Anonymize the first_name, last_name, and address columns and save the result to anonymized_data.csv.

### 2. Anonymize the Data
If you have already generated the CSV file and just want to run the anonymization:

```bash
    python anonymization/anonymize_data.py
```
This will anonymize the data in large_data.csv and save the output to anonymized_data.csv.

###3. Run Unit Tests
To run the unit tests for the CSV generation and anonymization processes:
```bash
python -m unittest discover -s tests
```

## Scalability and Performance

- The anonymization process is designed to handle large files efficiently by processing data in chunks. The default chunk size is 10,000 rows, but this can be adjusted depending on available memory and performance requirements.
- For even larger datasets, the project includes an AWS Glue implementation (`glue_implementation.py`). AWS Glue is a serverless data integration service that makes it easy to prepare data for analysis by automatically scaling to handle large volumes of data. This implementation allows the workload to be distributed and parallelized across multiple nodes, making it suitable for processing very large datasets that go beyond the capabilities of a single machine.

## Dependencies

- Python 3.x
- Faker: Library to generate synthetic data.
```bash
pip install faker
```

## Notes

- The anonymization process uses MD5 hashing for simplicity. For more secure anonymization, consider using a stronger hashing algorithm like SHA-256 or a proper pseudonymization technique.
- The chunk size in the anonymization script is configurable to optimize memory usage and processing time.

## License

This project is licensed under the MIT License. See the LICENSE file for details.