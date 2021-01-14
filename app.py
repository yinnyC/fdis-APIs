from flask import Flask, request, render_template, url_for
from guest import Guest
from datetime import datetime, date
import os
import requests
from datetime import date, datetime
from pprint import PrettyPrinter


app = Flask(__name__)
API_KEY = os.getenv('API_KEY')
pp = PrettyPrinter(indent=4)

# Define global variables (stored here for now)

guest_list = []


@app.route('/')
def homepage():
    """Return template for home."""
    return render_template('index.html')


@app.route('/about')
def about_page():
    """Show user party information."""
    today = date.today()
    month = today.strftime('%m')
    year = today.strftime('%Y')

    url = 'https://calendarific.com/api/v2/holidays'
    params = {
        'api_key': API_KEY,
        'country': 'US',
        'year': year,
        'month': month
    }
    result_json = requests.get(url, params=params).json()
    holidays = []

    for holiday in result_json['response']['holidays']:
        holidays.append({'name': holiday['name'],
                         'date': holiday['date']['iso'],
                         'descriptions': holiday['description']})

    context = {
        "holidays": holidays,
        "month": today.strftime('%B'),
        "year": year
    }
    return render_template('about.html', **context)


@ app.route('/guests', methods=['GET', 'POST'])
def show_guests():
    """
    Show guests that have RSVP'd.

    Add guests to RSVP list if method is POST.
    """
    if request.method == "GET":
        return render_template("guests.html", guests=guest_list)
    elif request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        plus_one = request.form.get("plus-one")
        phone = request.form.get("phone")
        guest_list.append(Guest(name, email, plus_one, phone))
        return render_template("guests.html", guests=guest_list)


@ app.route('/rsvp')
def rsvp_guest():
    """Show form for guests to RSVP for events."""
    return render_template('rsvp.html')


if __name__ == "__main__":
    app.run(debug=True)
