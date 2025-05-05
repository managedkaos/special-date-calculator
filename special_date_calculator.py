#!/usr/bin/env python3
"""
Special Date Calculator

This script finds and displays dates where month × day = last two digits of year.
"""

import argparse
from datetime import datetime


def find_special_dates(start_year, end_year):
    """
    Find dates where month × day = last two digits of year
    
    Args:
        start_year (int): Year to start searching from
        end_year (int): Year to end searching at
    
    Returns:
        list: List of tuples (year, month, day) that satisfy the condition
    """
    special_dates = []
    
    for year in range(start_year, end_year + 1):
        # Get last two digits of the year
        last_two_digits = year % 100
        
        # For each month
        for month in range(1, 13):
            # Calculate what day would be needed
            if last_two_digits % month == 0:
                day = last_two_digits // month
                
                # Check if day is valid for this month
                days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                
                # Adjust February for leap years
                if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                    days_in_month[2] = 29
                
                if 1 <= day <= days_in_month[month]:
                    special_dates.append((year, month, day))
    
    return special_dates


def format_date(date_tuple):
    """
    Format a date tuple as a string
    
    Args:
        date_tuple (tuple): (year, month, day)
    
    Returns:
        str: Formatted date string
    """
    year, month, day = date_tuple
    month_names = [
        "", "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]
    
    return f"{month_names[month]} {day}, {year}"


def get_current_year():
    """
    Get the current year
    
    Returns:
        int: Current year
    """
    return datetime.now().year


def calculate_decade_statistics(special_dates):
    """
    Calculate occurrences per decade
    
    Args:
        special_dates (list): List of date tuples
    
    Returns:
        dict: Dictionary mapping decades to occurrence counts
    """
    decades = {}
    for date in special_dates:
        decade = (date[0] // 10) * 10
        decades[decade] = decades.get(decade, 0) + 1
    
    return decades


def print_special_dates(special_dates, start_year, end_year):
    """
    Print special dates with aligned columns
    
    Args:
        special_dates (list): List of date tuples
        start_year (int): Starting year of the range
        end_year (int): Ending year of the range
    """
    print(f"\nSpecial dates where month × day = last two digits of year (from {start_year} to {end_year}):")
    print("-" * 70)
    
    # Print header with column names
    print(f"{'Date':<20} {'Calculation':<20} {'Result':<10}")
    print(f"{'-'*20} {'-'*20} {'-'*10}")
    
    for date in special_dates:
        year, month, day = date
        last_two_digits = year % 100
        
        formatted_date = format_date(date)
        calculation = f"{month} × {day}"
        
        print(f"{formatted_date:<20} {calculation:<20} {last_two_digits:<10}")


def print_decade_statistics(decade_stats):
    """
    Print statistics about occurrences per decade
    
    Args:
        decade_stats (dict): Dictionary mapping decades to occurrence counts
    """
    print("\nOccurrences by decade:")
    print(f"{'Decade':<10} {'Count':<10}")
    print(f"{'-'*10} {'-'*10}")
    
    for decade, count in sorted(decade_stats.items()):
        print(f"{decade}s:{'':<5} {count:<10}")


def parse_arguments():
    """
    Parse command line arguments
    
    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(description='Calculate special dates where month × day = last two digits of year')
    
    current_year = get_current_year()
    
    parser.add_argument('--start', type=int, default=current_year,
                        help=f'Starting year for calculation (default: {current_year})')
    parser.add_argument('--end', type=int, default=2100,
                        help='Ending year for calculation (default: 2100)')
    parser.add_argument('--current-date', action='store_true',
                        help='Include current date in results if it matches criteria')
    
    return parser.parse_args()


def main():
    """
    Main function that orchestrates the execution of the script
    """
    # Parse command line arguments
    args = parse_arguments()
    
    # Find special dates for the given range
    special_dates = find_special_dates(args.start, args.end)
    
    # Remove today's date if needed
    if not args.current_date:
        today = datetime.now()
        today_tuple = (today.year, today.month, today.day)
        if today_tuple in special_dates and args.start <= today.year <= args.end:
            special_dates.remove(today_tuple)
    
    # Print the results in aligned columns
    print_special_dates(special_dates, args.start, args.end)
    
    # Calculate and print decade statistics
    decade_stats = calculate_decade_statistics(special_dates)
    print_decade_statistics(decade_stats)


if __name__ == "__main__":
    main()
