# Fixed-Width File Parser

This project is a Python script designed to generate a fixed-width file based on a given specification and then parse that file into a delimited format, such as CSV.

## Requirements

- Python 3.10 or higher
- Docker (for containerization)

## How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```
2. **Run the script**:

    To run the script locally using Python:
    ```bash
    python generate_and_parse/main.py
    ```
    Ensure that `spec.json` is in the same directory as `main.py`.
3. **Run the tests**:
    You can run the tests using the following command:
    ```bash
    python -m unittest discover -s tests -v
    ```
    
## Docker

1. **Build the Docker image**:

    ```bash
    docker build -t fixed-width-parser:3.10 .
    ```
2. **Run the Docker container**:
    ```bash
    docker run --rm -v $(pwd):/app fixed-width-parser:3.10
    ```
The Docker container will execute the `main.py` script and generate the output files in your current directory.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details