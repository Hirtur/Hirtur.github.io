from flask import Flask, render_template, session, json, request


stock = [{"item":"Húfa", "mynd":"/static/hufa.png", "verd":4000}, {"item":"buxur", "Mynd": "/static/buxur.jpg", "verd": 2599}, {"item":"Skór", "mynd":"/static/skor.jpg", "verd":5000}, {"item":"Trefill", "mynd":"/static/trefill.jpg", "verd":3400}, {"item":"Jakki", "mynd":"/static/jakki.jpg", "verd":5120}, {"item":"Peysa", "mynd":"/static/hoodie.png", "verd":2100}]
checkout = []

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'


@app.route('/')
def index():
    session['prufa'] = 'set' 
    return render_template('index.html', vl=stock)

@app.route('/add')
def add():
    item = request.args['item']
    verd = request.args['verd']
    checkout.append({'item':item ,'verd':verd})
    y=0
    for o in checkout:
        y=y+1
    return render_template('index.html', vl=stock, y=y)

@app.route('/karfa')
def karfa():
    x=0
    for i in checkout:
        x=x+int(i["verd"])
    return render_template('karfa.html', co=checkout, x=x)

@app.route('/eyda')
def eyda():
    session.pop('prufa', None)  
    checkout.clear()
    return render_template("karfa.html")

@app.route('/remove')
def remove():
    item = request.args['item']
    verd = request.args['verd']
    checkout.remove({'item':item ,'verd':verd})
    x=0
    for i in checkout:
        x=x+int(i["verd"])
    return render_template("karfa.html", co=checkout, x=x)


@app.errorhandler(404)
def villa(error):
    return render_template('error.html')

if __name__ == "__main__":
    app.run(debug=True)