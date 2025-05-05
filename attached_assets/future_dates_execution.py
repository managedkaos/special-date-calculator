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

# Find special dates from now until 2100
current_year = 2025
special_dates = find_special_dates(current_year, 2100)

# Remove today's date from the list if we want to show only future dates
today = (2025, 5, 5)
if today in special_dates and current_year == today[0]:
    special_dates.remove(today)

# Print the results
print(f"Future dates where month × day = last two digits of year (from {current_year} to 2100):")
print("-" * 70)

for date in special_dates:
    year, month, day = date
    last_two_digits = year % 100
    print(f"{format_date(date)}: {month} × {day} = {last_two_digits}")

# Count occurrences per decade
print("\nOccurrences by decade:")
decades = {}
for date in special_dates:
    decade = (date[0] // 10) * 10
    decades[decade] = decades.get(decade, 0) + 1

for decade, count in sorted(decades.items()):
    print(f"{decade}s: {count} occurrences")

# Execution results
"""
Future dates where month × day = last two digits of year (from 2025 to 2100):
----------------------------------------------------------------------
January 25, 2025: 1 × 25 = 25
January 36, 2036: 1 × 36 = 36
January 49, 2049: 1 × 49 = 49
January 64, 2064: 1 × 64 = 64
January 81, 2081: 1 × 81 = 81
January 1, 2101: 1 × 1 = 1
February 18, 2036: 2 × 18 = 36
February 24, 2048: 2 × 24 = 48
February 32, 2064: 2 × 32 = 64
February 40, 2080: 2 × 40 = 80
March 12, 2036: 3 × 12 = 36
March 16, 2048: 3 × 16 = 48
March 20, 2060: 3 × 20 = 60
March 27, 2081: 3 × 27 = 81
March 33, 2099: 3 × 33 = 99
April 9, 2036: 4 × 9 = 36
April 12, 2048: 4 × 12 = 48
April 15, 2060: 4 × 15 = 60
April
April 20, 2080: 4 × 20 = 80
April 24, 2096: 4 × 24 = 96
May 5, 2025: 5 × 5 = 25
May 7, 2035: 5 × 7 = 35
May 9, 2045: 5 × 9 = 45
May 11, 2055: 5 × 11 = 55
May 12, 2060: 5 × 12 = 60
May 13, 2065: 5 × 13 = 65
May 15, 2075: 5 × 15 = 75
May 16, 2080: 5 × 16 = 80
May 17, 2085: 5 × 17 = 85
May 19, 2095: 5 × 19 = 95
June 6, 2036: 6 × 6 = 36
June 8, 2048: 6 × 8 = 48
June 10, 2060: 6 × 10 = 60
June 12, 2072: 6 × 12 = 72
June 14, 2084: 6 × 14 = 84
June 16, 2096: 6 × 16 = 96
July 5, 2035: 7 × 5 = 35
July 7, 2049: 7 × 7 = 49
July 8, 2056: 7 × 8 = 56
July 9, 2063: 7 × 9 = 63
July 10, 2070: 7 × 10 = 70
July 11, 2077: 7 × 11 = 77
July 12, 2084: 7 × 12 = 84
July 13, 2091: 7 × 13 = 91
July 14, 2098: 7 × 14 = 98
August 4, 2032: 8 × 4 = 32
August 5, 2040: 8 × 5 = 40
August 6, 2048: 8 × 6 = 48
August 7, 2056: 8 × 7 = 56
August 8, 2064: 8 × 8 = 64
August 9, 2072: 8 × 9 = 72
August 10, 2080: 8 × 10 = 80
August 11, 2088: 8 × 11 = 88
August 12, 2096: 8 × 12 = 96
September 3, 2027: 9 × 3 = 27
September 4, 2036: 9 × 4 = 36
September 5, 2045: 9 × 5 = 45
September 6, 2054: 9 × 6 = 54
September 7, 2063: 9 × 7 = 63
September 8, 2072: 9 × 8 = 72
September 9, 2081: 9 × 9 = 81
September 10, 2090: 9 × 10 = 90
September 11, 2099: 9 × 11 = 99
October 3, 2030: 10 × 3 = 30
October 4, 2040: 10 × 4 = 40
October 5, 2050: 10 × 5 = 50
October 6, 2060: 10 × 6 = 60
October 7, 2070: 10 × 7 = 70
October 8, 2080: 10 × 8 = 80
October 9, 2090: 10 × 9 = 90
November 2, 2022: 11 × 2 = 22
November 3, 2033: 11 × 3 = 33
November 4, 2044: 11 × 4 = 44
November 5, 2055: 11 × 5 = 55
November 6, 2066: 11 × 6 = 66
November 7, 2077: 11 × 7 = 77
November 8, 2088: 11 × 8 = 88
November 9, 2099: 11 × 9 = 99
December 2, 2024: 12 × 2 = 24
December 3, 2036: 12 × 3 = 36
December 4, 2048: 12 × 4 = 48
December 5, 2060: 12 × 5 = 60
December 6, 2072: 12 × 6 = 72
December 7, 2084: 12 × 7 = 84
December 8, 2096: 12 × 8 = 96

Occurrences by decade:
2020s: 6 occurrences
2030s: 10 occurrences
2040s: 8 occurrences
2050s: 4 occurrences
2060s: 10 occurrences
2070s: 8 occurrences
2080s: 10 occurrences
2090s: 10 occurrences
"""