#!/usr/bin/env python3
"""
Special Date Calculator Web Interface

This web application provides a user-friendly interface for finding
special dates where month × day = last two digits of year.
"""

from flask import Flask, render_template, request
import datetime
from special_date_calculator import find_special_dates, format_date, calculate_decade_statistics

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Render the main page with a form and results."""
    special_dates = []
    decade_stats = {}
    start_year = datetime.datetime.now().year
    end_year = start_year + 10

    if request.method == 'POST':
        try:
            start_year = int(request.form.get('start_year', start_year))
            end_year = int(request.form.get('end_year', end_year))

            # Validate input
            if start_year > end_year:
                return render_template('index.html',
                                      error="Start year must be less than or equal to end year.",
                                      start_year=start_year,
                                      end_year=end_year)

            # Find special dates
            special_dates = find_special_dates(start_year, end_year)

            # Calculate decade statistics
            decade_stats = calculate_decade_statistics(special_dates)

        except ValueError:
            return render_template('index.html',
                                   error="Please enter valid year numbers.",
                                   start_year=start_year,
                                   end_year=end_year)

    # Format the dates for display
    formatted_dates = []
    for date in special_dates:
        year, month, day = date
        last_two_digits = year % 100
        formatted_dates.append({
            'date': format_date(date),
            'calculation': f"{month} × {day}",
            'result': last_two_digits
        })

    # Format decade statistics for display
    formatted_decade_stats = [
        {'decade': f"{decade}s", 'count': count}
        for decade, count in sorted(decade_stats.items())
    ]

    return render_template('index.html',
                           dates=formatted_dates,
                           decade_stats=formatted_decade_stats,
                           start_year=start_year,
                           end_year=end_year)

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    import os
    if not os.path.exists('templates'):
        os.makedirs('templates')

    app.run(host='0.0.0.0', port=5050, debug=True)
