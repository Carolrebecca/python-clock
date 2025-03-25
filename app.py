from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def show_time():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Current Time: {now}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
