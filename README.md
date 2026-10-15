# Automated REST API ETL Pipeline with Pytest Validation

## Project Overview

This project demonstrates an automated Extract, Transform, Load (ETL) pipeline using Python.

The pipeline extracts user data from a REST API, transforms and cleans the data using pandas, and saves the processed information into a CSV file.

Pytest is used to test important pipeline functions.

## Project Architecture

REST API
   |
   v
Extract JSON Data
   |
   v
Transform Data Using Pandas
   |
   v
Clean Email Addresses
   |
   v
Calculate Name Length
   |
   v
Save Data to CSV

## Technologies Used

- Python
- Pandas
- Requests
- Pytest
- REST API
- GitHub

## Project Features

1. Extracts user information from a REST API.
2. Handles HTTP errors using response status validation.
3. Converts JSON data into a pandas DataFrame.
4. Selects the required user information.
5. Converts email addresses to lowercase.
6. Calculates the character length of each user's name.
7. Exports the transformed data to a CSV file.
8. Includes automated tests using pytest.

## Data Source

The project uses the JSONPlaceholder REST API.

API Endpoint:

https://jsonplaceholder.typicode.com/users

## Data Transformation

The pipeline selects the following fields:

- id
- name
- username
- email
- phone
- website

It also creates an additional column:

- name_length: Number of characters in the user's name.

Email addresses are converted to lowercase for standardization.

## Output

The transformed data is saved to:

transformed_users.csv

The output contains the cleaned user records and the calculated name_length column.

## Installation

Install Python 3.8 or later.

Install the required libraries:

pip install pandas requests pytest

## Running the Project

Execute the Python script:

python etl_pipeline.py

The script retrieves the API data, transforms it, and saves the output as a CSV file.

An active internet connection is required to retrieve data from the API.

## Running Tests

Run the automated tests using:

pytest etl_pipeline.py -v

The tests validate the data transformation, API extraction behavior, and CSV output.

## Learning Outcomes

- Understanding the ETL process.
- Working with REST APIs.
- Processing JSON data using pandas.
- Cleaning and transforming datasets.
- Exporting processed data to CSV.
- Writing automated tests with pytest.
- Managing project files using GitHub.

## Future Enhancements

- Add logging and improved error handling.
- Add data validation and duplicate detection.
- Automate test execution using GitHub Actions.
- Store processed data in a database.

## License

This project is intended for educational and learning purposes.
