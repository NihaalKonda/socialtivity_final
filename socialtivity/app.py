from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from flask import redirect

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/socialtivity"
Bootstrap(app)
mongo=PyMongo(app)

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html")
@app.route('/forum', methods=["GET", "POST"])
def forum():
    return render_template("forum.html")
@app.route('/mission', methods=["GET", "POST"])
def mission():
    return render_template("mission.html")
@app.route('/contact', methods=["GET", "POST"])
def contact():
    return render_template("contact.html")
@app.route('/corona', methods=["GET", "POST"])
def corona():
    if request.method=="GET":
        corona_docs = mongo.db.corona.find({})
        return render_template("coronavirus.html", docs=corona_docs)
    if request.method=="POST":
        doc = {'user':request.form.get("user"), 'content':request.form.get("content")}
        mongo.db.corona.insert_one(doc)
        return redirect('/corona')
@app.route('/education', methods=["GET", "POST"])
def education():
    if request.method=="GET":
        edu_docs = mongo.db.edu.find({})
        return render_template("education.html", docs=edu_docs)
    if request.method=="POST":
        doc = {'user':request.form.get("user"), 'content':request.form.get("content")}
        mongo.db.edu.insert_one(doc)
        return redirect('/education')
@app.route('/immigration', methods=["GET", "POST"])
def immigration():
    if request.method=="GET":
        imm_docs = mongo.db.immigration.find({})
        return render_template("immigration.html", docs=imm_docs)
    if request.method=="POST":
        doc = {'user':request.form.get("user"), 'content':request.form.get("content")}
        mongo.db.immgiration.insert_one(doc)
        return redirect('/immigration')
@app.route('/poverty', methods=["GET", "POST"])
def poverty():
    if request.method=="GET":
        poverty_docs = mongo.db.poverty.find({})
        return render_template("poverty.html", docs=poverty_docs)
    if request.method=="POST":
        doc = {'user':request.form.get("user"), 'content':request.form.get("content")}
        mongo.db.poverty.insert_one(doc)
        return redirect('/poverty')
@app.route('/racism', methods=["GET", "POST"])
def racism():
    if request.method=="GET":
        racism_docs = mongo.db.racism.find({})
        return render_template("racism.html", docs=racism_docs)
    if request.method=="POST":
        doc = {'user':request.form.get("user"), 'content':request.form.get("content")}
        mongo.db.racism.insert_one(doc)
        return redirect('/racism')
if __name__=='__main__':
    app.run(debug=True)