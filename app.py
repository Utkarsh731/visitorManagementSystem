from flask import Flask, request, render_template
import os, pymongo, urllib
from src import *


app = Flask(__name__)

try:
    username = urllib.parse.quote_plus(os.environ['username'])
    password = urllib.parse.quote_plus(os.environ['password'])
    uri = os.environ['mongo'].format(username, password)
    client = pymongo.MongoClient(uri)
    db = client[os.environ['database']]
except Exception as e:
    print(e)
    print("no connection")


@app.route("/")
def index_page():
    collection = db[os.environ['collection1']]
    page = 1
    if request.args.get("page"):
        page = request.args.get("page")
    return home_page_handler(collection, page)


@app.route("/login")
def about_page():
    return render_template("pages-login.html")


if __name__=='__main__':
    app.run(debug=True)