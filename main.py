from flask import Flask, jsonify, request
from requests import get

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = True

@app.route("/")
def index_page():
    base_url = "http://www.koeri.boun.edu.tr/scripts/lst9.asp"
    response = get(base_url)
    temp_list = []
    depremler = response.text.split("<pre>")[1].split("</pre>")[0].split("\n")[7:]
    depremler = depremler[:25]
    for deprem in depremler:
        vars = deprem.split()
        vars.pop(-1)
        temp_list.append(vars)
    return jsonify({"Success": True, "count": len(temp_list),"results": temp_list})

if __name__ == "__main__":
    app.run(debug=True, port = 5000, host="0.0.0.0")