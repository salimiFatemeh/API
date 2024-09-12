from flask import Flask, render_template

app = Flask("Website")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperture = 23
    return {"temperture": temperture,
            "date": date,
            "station": station}

app.run(debug=True)