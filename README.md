# Online Store Data Analysis

This project analyzes customer order data from an online store to compute various revenue metrics.

## Requirements

- Python 3.9+
- Docker and Docker Compose

## Running the Application

1. Make sure you have Docker and Docker Compose installed on your system.
2. Place the `orders.csv` file in the `data/` directory.
3. Run the following command to start the application:
```
docker-compose up app
```
This will run the main application and display the results.

## Running the Tests

To run the tests, use the following command:
```
docker-compose up test
```
This will run all the tests in the `tests/` directory.

## Project Structure

- `src/`: Contains the main application code
  - `main.py`: Main entry point of the application
  - `utils.py`: Utility functions for data processing
- `tests/`: Contains test files
- `data/`: Directory to store the input CSV file
- `Dockerfile`: Defines the Docker image for the application
- `docker-compose.yml`: Defines the services for running the app and tests
- `requirements.txt`: Lists the Python dependencies

## Notes

- Make sure the `orders.csv` file is placed in the `data/` directory before running the application or tests.
- The application handles errors gracefully and will display appropriate error messages if issues occur during execution.
