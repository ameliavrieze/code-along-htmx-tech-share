import time
from datetime import datetime

from flask import Flask, render_template, request
app = Flask(__name__)

slop_list = [
    "That time I got reincarnated as a slime",
    "Solo Leveling",
    "The Eldest Son of Noble Martial Family Returns from Hell After 100 Years",
    "The Evergreen Records",

]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/time', methods=["GET"])
def server_time():
    time.sleep(0.5) #artificial delay
    return f'<strong>Server time: {datetime.now():%H:%M:%S}</strong>'


@app.route('/search', methods=["POST"])
def search():
    slop = request.args.get("slop","").strip().lower()
    matches = [s for s in slop_list if slop in s.lower()]
    if not matches:
        return "<li>You haven't consumed enough slop yet, larper. (No matches)</li>"
    return "".join(f"<li>{s}</li>" for s in matches)

# @app.route('/')
# def index():
#     return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=5001)

