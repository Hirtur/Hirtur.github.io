from flask import Flask, render_template, json, jsonify
import urllib.request
app = Flask(__name__)
 
with urllib.request.urlopen("https://restcountries.eu/rest/v2/all") as url:
    gogn = json.loads(url.read().decode())


@app.route("/")
def index():
    return render_template('index.html', lf = gogn)

@app.route('/land/<alpha2Code>')
def land(alpha2Code):
    for i in gogn:
        if alpha2Code == i['alpha2Code']:
            land = i
            break
    return render_template('land.html', land=land)

@app.route('/heimsalfurnar/<region>')
def heimsalfur(region):
    fjoldi = 0
    for i in gogn:
        if i['region'] == region:
            fjoldi += 1
    return render_template('heimsalfurnar.html', lf = gogn, region = region, fjoldi = fjoldi)

if __name__ == "__main__":
    app.run(debug=True)