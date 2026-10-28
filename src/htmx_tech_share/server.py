import time

from flask import Flask, render_template, request
import htmx_tech_share.database as database

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", images=database.get_images())

# We want to display this after clicking a button
@app.route("/clicked", methods=["GET"])
def clicky():
    time.sleep(0.5) #artificial delay to display load
    return f'<p style="color:crimson;">This message was generated dynamically with HTMX! Yippee!!</p>'

@app.route("/scroll/")
def scroll():
    time.sleep(1) #artificial delay to display load
    return render_template()


if __name__ == "__main__":
    app.run(debug=True, port=5001)
