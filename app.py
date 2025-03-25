from flask import Flask
import datetime
import pytz  # Import pytz for time zone handling

app = Flask(__name__)

# Set your preferred time zone (e.g., 'Asia/Kolkata', 'America/New_York', etc.)
TIMEZONE = pytz.timezone('Asia/Kolkata')  # Change to your desired time zone

@app.route('/')
def show_time():
    now = datetime.datetime.now(TIMEZONE).strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current Time ({TIMEZONE}): {now}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

