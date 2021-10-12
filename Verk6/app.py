from flask import Flask, render_template, request
import pyrebase

app = Flask(__name__)

config = {
    # hér kemur tengingin þín við Firebase gagnagrunninn ( realtime database )
    "apiKey": "AIzaSyDOMhzf9gyoOiqzjMVxcxEDyfi9ovo6YNg",
    "authDomain": "verkefni6-cd888.firebaseapp.com",
    "databaseURL": "https://verkefni6-cd888-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "verkefni6-cd888",
    "storageBucket": "verkefni6-cd888.appspot.com",
    "messagingSenderId": "396106619434",
    "appId": "1:396106619434:web:ece77ed02791deab7f4153",
    "measurementId": "G-MBEMMJJVF9"

}

fb = pyrebase.initialize_app(config)
db = fb.database()

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/info', methods=['GET','POST'])
def info():
    if request.method =='POST':
        notendanafn = request.form['notendanafn']
        lykilord = request.form['lykilord']
        print(notendanafn)
        print(lykilord)
        db.child("user").push({"usr":notendanafn, "pwd":lykilord})
        return "Gögn kominn i gagnagrunn"
    else:
        return "<h1>má ekki</h1>"

if __name__=="__main__":
    app.run(debug=True)