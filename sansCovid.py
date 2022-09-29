import json
import requests
import os

from flask import Flask, render_template, request

app = Flask(__name__)  #creating a flask instance

@app.route("/", methods=["GET", "POST"])
def covidresult():
    if request.method == "GET":
        return render_template("covid.html", data=None)
    if request.method == "POST":
        country = request.form["country"]
        url = "https://api.covid19api.com/summary"
        response = requests.get(url).json() #whatever comes from server, comes as a string. we change it to json
        if response:
            for i in range(len(response["Countries"])):
                if response["Countries"][i]["Country"] == country:
                    data = {"confirmed": response["Countries"][i]["TotalConfirmed"],
                            "death": response["Countries"][i]["TotalDeaths"],
                            "status": 200}
                    return render_template("covid.html", country=country, data=data)
            else:
                data = {"message": "Country Name Invalid. Please enter a valid country and try again!", "status": 404}
                return render_template("covid.html", data=data)
        else:
            data = None
            return render_template("covid.html", data=data)



port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(port=port)

