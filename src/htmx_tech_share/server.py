import time

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# We want to display this after clicking a button
@app.route('/clicked', methods=["GET"])
def clicky():
    time.sleep(0.5) #artificial delay to display load
    return f'<p>This message was generated dynamically with HTMX! Yippee!!</p>'

if __name__ == '__main__':
    app.run(debug=True, port=5001)

