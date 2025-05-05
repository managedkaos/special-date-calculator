# Special Date Calculator

This application identifies "special dates" where the product of the month and day equals the last two digits of the year. For example, May 5, 2025 is a special date because 5 × 5 = 25 (the last two digits of 2025).

## Features

- Command-line interface with flexible date range inputs
- Web interface with user-friendly controls
- Calculates and displays special dates in a formatted table
- Shows statistics of date occurrences by decade
- Validates input and handles edge cases

## Requirements

- Python 3.6 or higher
- Flask (for web interface)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/special-date-calculator.git
   cd special-date-calculator
   ```

2. Install the required dependencies:
   ```
   pip install flask
   ```

## Usage

### Command-line Interface

Run the script with optional arguments:

```
python special_date_calculator.py [--start START_YEAR] [--end END_YEAR] [--current-date]
```

Arguments:
- `--start`: Starting year for calculation (default: current year)
- `--end`: Ending year for calculation (default: 2100)
- `--current-date`: Include current date in results if it matches criteria

Examples:
```
# Calculate special dates from current year to 2100
python special_date_calculator.py

# Calculate special dates from 2023 to 2030
python special_date_calculator.py --start 2023 --end 2030

# Calculate special dates for a specific year
python special_date_calculator.py --start 2025 --end 2025
```

### Web Interface

Run the Flask web application:

```
python app.py
```

Then open a web browser and navigate to:
```
http://localhost:5000
```

The web interface allows you to:
1. Enter a start year and end year
2. View results in a nicely formatted table
3. See decade statistics for the date range

## How It Works

The algorithm works as follows:

1. For each year in the specified range:
   - Extract the last two digits of the year
   - For each month (1-12):
     - Check if the last two digits are divisible by the month
     - If divisible, calculate the day (last two digits ÷ month)
     - Verify if the day is valid for that month (accounting for leap years)
     - If valid, add to the list of special dates

2. Display the results with appropriate formatting

## Example Output

The application displays special dates in a table format:

```
Special dates where month × day = last two digits of year (from 2025 to 2030):
----------------------------------------------------------------------
Date                 Calculation          Result
-------------------- -------------------- ----------
January 25, 2025     1 × 25               25
May 5, 2025          5 × 5                25
January 26, 2026     1 × 26               26
February 13, 2026    2 × 13               26
...
```

## License

MIT License - feel free to use and modify this code for your own projects.
