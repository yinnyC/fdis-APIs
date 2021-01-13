"""
Initialize your Flask app. This is what will run your server.

Don't forget to install your dependencies from requirements.txt!
This is a doc string! It's a special kind of comment that is expected
in Python files. Usually, you use this at the top of your code and in
every function & class to explain what the code does.
"""
from flask import Flask, request, render_template, url_for
from guest import Guest
from datetime import datetime, date

app = Flask(__name__)

# Define global variables (stored here for now)

guest_list = []


@app.route('/')
def homepage():
    """Return template for home."""
    return render_template('index.html')


@app.route('/about')
def about_page():
    """Show user party information."""
    # Sometimes, a cleaner way to pass variables to templates is to create a
    # context dictionary, and then pass the data in by dictionary key

    context = {
        "date": "10/31/2020",
        "time": "10:00 pm"
    }
    return render_template('about.html', **context)


@app.route('/guests', methods=['GET', 'POST'])
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


@app.route('/rsvp')
def rsvp_guest():
    """Show form for guests to RSVP for events."""
    return render_template('rsvp.html')


if __name__ == "__main__":
    app.run(debug=True)
