latest_html = ""
latest_react = ""
latest_flutter = ""

from flask import Response
from flask import send_file
import io
from flask import Flask,render_template,request
import os
import detector
import generator

app=Flask(__name__)

UPLOAD_FOLDER="uploads"
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER,exist_ok=True)
os.makedirs("static",exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html",code="",image="")

@app.route("/upload",methods=["POST"])
def upload():

    file=request.files["sketch"]

    filepath=os.path.join(app.config["UPLOAD_FOLDER"],file.filename)

    file.save(filepath)

    components,image=detector.detect_ui(filepath)

    global latest_html, latest_react, latest_flutter

    latest_html = generator.generate_html(components)

    latest_react = generator.generate_react(components)

    latest_flutter = generator.generate_flutter(components)

    return render_template(
    "index.html",
    html_code=latest_html,
    react_code=latest_react,
    flutter_code=latest_flutter,
    image=image
    )

@app.route("/download/html")
def download_html():
    return Response(
        latest_html,
        mimetype="text/html",
        headers={"Content-Disposition":"attachment;filename=ui.html"}
    )

@app.route("/download/react")
def download_react():
    return Response(
        latest_react,
        mimetype="text/javascript",
        headers={"Content-Disposition":"attachment;filename=App.jsx"}
    )

@app.route("/download/flutter")
def download_flutter():
    return Response(
        latest_flutter,
        mimetype="text/plain",
        headers={"Content-Disposition":"attachment;filename=ui.dart"}
    )

if __name__=="__main__":
    app.run(debug=True)