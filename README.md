# Bikeshare Data Analysis

This Python script allows you to analyze bikeshare data for different cities, months, and days. It provides various statistics and insights about bike usage patterns based on user-selected filters. The script works with three cities: Chicago, New York, and Washington.

## How to Use

1. Clone the repository or download the script.
2. Ensure you have Python 3.10.12 and the required libraries (`pandas` and `numpy`) installed.

### Running the Script

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script by executing the following command: `python3 bikeshare.py`

Follow the prompts in the terminal to specify the city, month, and day for analysis. The script will then display various statistics related to bike usage patterns.

## Features

The script provides the following features:

1. **City, Month, and Day Filtering:** You can choose a city, a specific month, and a day of the week to filter the data for analysis.

2. **Time Statistics:** The script displays the most common month, day of the week, and start hour for bike trips.

3. **Station Statistics:** It presents information about the most commonly used start and end stations, as well as the most frequent combination of start and end stations.

4. **Trip Duration Statistics:** You can view the total travel time and mean travel time for bike trips.

5. **User Statistics:** The script displays counts of user types, gender information (if available), and birth year information (if available).

6. **Viewing Data:** After displaying statistics, you have the option to view individual trip data in groups of 5 rows.

7. **Restarting:** At the end of each analysis, you can choose to restart the script to perform additional analyses.

## Data Files

The script uses CSV data files for each city, containing bikeshare data. The data files for each city are named as follows:

- `chicago.csv` (for Chicago City)
- `new_york_city.csv` (for New York City)
- `washington.csv` (for Washington City)

## Notes

- Ensure that the CSV data files are present in the same directory as the script.
- The script uses `pandas` and `numpy` libraries for data analysis.
- The birth year and gender information might not be available for all cities and trips.

## Author

This script was developed by Rand Sohail.

Feel free to contact me at randsohail98@gmail.com for any questions or feedback.
