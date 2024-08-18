# Using an official Python runtime (3.10)
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run tests during build
RUN python -m unittest discover -s tests -v

# Run your application
CMD ["python", "generate_and_parse/main.py"]
