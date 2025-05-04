from flask import Flask, render_template
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://disease.sh/v3/covid-19/countries")
    data = response.json()
    df = pd.DataFrame(data)
    countries = df[["country", "cases", "deaths", "recovered"]]
    return render_template("index.html", countries=countries.to_dict(orient="records"))

@app.route('/country/<name>')
def country(name):
    response = requests.get(f"https://disease.sh/v3/covid-19/countries/{name}")
    data = response.json()
    return render_template("country.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)