import hashlib
import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, send_file
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app = Flask(__name__, static_folder="assets")
db = SQL("sqlite:///virusshare.db")
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/check", methods=['GET', 'POST'])
def check():
    if request.method == "POST":
        if request.files:
            malware = request.files["uploaded_malware"]
            malware.save(os.path.join("/home/ubuntu/project/tmp/", malware.filename))
            print("Image Saved to tmp. Proceeding to detection process.")
            hashUndetected = hashlib.md5(open('/home/ubuntu/project/tmp/' + malware.filename,'rb').read()).hexdigest()
            print(hashUndetected)
            rows = db.execute("SELECT hash FROM virusshare WHERE hash=:hash", hash=hashUndetected)
            if len(rows) == 0:
                return redirect("/checkmark")
            else:
                return redirect("/x")
    else:
        return render_template("check.html")
@app.route("/download")
def download():
    return send_file('test.png')
@app.route("/x")
def x():
    return send_file('x.png')
@app.route("/checkmark")
def checkmark():
    return send_file('check.png')