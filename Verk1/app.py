import random
from  flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hallo():
    return "<h1>Hello flask image</h1> <a href='/b1'> <img src='https://picsum.photos/200'>"
    
    

    
@app.route('/b1')
def b1():
    i=["Amma","Pabbi","Mamma","Afi","frændi","frænka"]
    h=i[random.randint(0,5)]
    return "<h1>Hallo %s nu er gamma </h1>" %h

@app.route("/b2/<user>")
def eih(user):
    notandi = user
    return render_template("b2.html", user=notandi) 

if __name__ == "__main__":
    app.run(debug=True)
    
    
