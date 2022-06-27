from flask import Flask


app= Flask(__name__)


@app.get("/")
def index():
    return "<h1> Hello world </h1>"

@app.get("/about")
def get_about():
    me ={
        "first_name": "Hai",
        "last_name": "Nguyen",
        "hobbies": "soccer",
        "active":True
    }
    return me
