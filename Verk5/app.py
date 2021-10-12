from flask import Flask, render_template, sessions, session, url_for
import os

app = Flask(__name__)

app.secret_key = os.urandom(8)

vorur = [
    [0, "Peysa",  "peysa.jpg",  2500],
    [1, "Buxur",  "buxur.jpg",  3500],
    [2, "Jakki",  "jakki.jpg",  13500],
    [3, "Skór",  "skor.jpg",  4500],
    [4, "Trefill",  "trefill.jpg",  1500],
    [5, "Húfa",  "hufa.jpg",  2000]
]

@app.route("/karfa")
def karfa():
    karfa= session['karfa']
    return render_template("karfa.html", karfa=karfa)



@app.route("/add/<int:id>")
def add(id):
    l= []
    if session:
        l = session['karfa']
        l.append(vorur[id])
        session['karfa'] = l
    else:
        l.append(vorur[id])
        session['karfa'] = l

    print(session)
    return "bættukm i körfu"

@app.errorhandler(404)
def villa(error):
    return render_template("villusida.html")

if __name__ == '__main__':
      app.run(debug=True)