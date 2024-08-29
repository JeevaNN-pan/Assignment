# Bank Branches API

This repository contains a Flask-based API for retrieving information about bank branches. The API provides endpoints to get a list of banks and to fetch branch details for a specific bank.

## Problem Statement

The task was to create an API that allows users to:
1. Retrieve a list of all banks
2. Search for banks by name
3. Get branch details for a specific bank

## Solution Method

To solve this problem, we implemented the following approach:

1. **Database Setup**: 
   - We used SQLite as the database to store bank and branch information.
   - A CSV file (`bank_branches.csv`) is used as the data source.
   - On initialization, the data from the CSV file is loaded into an SQLite database.

2. **Flask Application**:
   - We created a Flask application to serve as the API backend.
   - Two main routes were implemented:
     a. `/api/banks`: To get all banks or search for banks by name
     b. `/api/branches`: To get branch details for a specific bank

3. **API Endpoints**:
   - `/api/banks`:
     - GET request
     - Optional query parameter: `name` for searching banks
     - Returns a list of bank names
   - `/api/branches`:
     - GET request
     - Required query parameter: `bank_name`
     - Returns details of all branches for the specified bank

4. **Query Handling**:
   - For the bank search, we used SQL LIKE queries to allow partial matching of bank names.
   - For branch details, we used exact matching on the bank name.

5. **Error Handling**:
   - Appropriate error messages and status codes are returned for scenarios like:
     - No banks found matching the search criteria
     - No branches found for a given bank
     - Missing required parameters

6. **Data Processing**:
   - We used pandas to read the CSV file and load it into the SQLite database.
   - Query results are converted to JSON format for API responses.

## Usage

1. Ensure you have Flask, SQLite, and pandas installed.
2. Place your `bank_branches.csv` file in the same directory as the script.
3. Run the Flask application:
   ```
   python app.py
   ```
4. Access the API endpoints:
   - Get all banks: `GET http://localhost:5000/api/banks`
   - Search banks: `GET http://localhost:5000/api/banks?name=HDFC`
   - Get branch details: `GET http://localhost:5000/api/branches?bank_name=HDFC%20BANK`

## Time Taken to Complete

The assignment was completed in approximately 7 hours. This time includes:
- Understanding the problem requirements
- Setting up the Flask application and database
- Implementing the API endpoints
- Testing and debugging
- Writing this README file


