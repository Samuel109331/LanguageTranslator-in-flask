from flask import Flask,render_template,request
import googletrans as gt
import requests

app = Flask(__name__)


@app.route("/")
def homePage():
    try:
        requests.get("https://www.google.com/")
        langList = gt.LANGUAGES.values()
        return render_template("home.html",langList=langList)
    except requests.ConnectionError:
        return render_template("noInternet.html")


@app.route("/trans",methods= ["POST"])
def trans():
    try:
        title = 'Result'
        word = request.form.get("sentence")
        lang = request.form.get('language')
        spanish = gt.Translator().translate(text=word,dest=lang).text
        return render_template("result.html",title=title,spanish=spanish,lang=lang)
    except:
        return render_template("Error_page.html")
