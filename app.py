from flask import Flask, render_template, request, Response
import os
import detector
import generator

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("static", exist_ok=True)

latest_html = ""
latest_react = ""
latest_flutter = ""


@app.route("/")
def index():
    return render_template(
        "index.html",
        html_code="",
        react_code="",
        flutter_code="",
        image=""
    )


@app.route("/upload", methods=["POST"])
def upload():

    global latest_html, latest_react, latest_flutter

    file = request.files.get("sketch")

    if file is None or file.filename == "":
        return "No file uploaded"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    components, image = detector.detect_ui(filepath)

    framework = request.form.get("framework")

    if framework == "html":

        latest_html = generator.generate_html(components)

    elif framework == "react":

        latest_react = generator.generate_react(components)

    elif framework == "flutter":

        latest_flutter = generator.generate_flutter(components)

    else:

        latest_html = generator.generate_html(components)

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
        headers={"Content-Disposition": "attachment; filename=ui.html"}
    )


@app.route("/download/react")
def download_react():
    return Response(
        latest_react,
        mimetype="text/javascript",
        headers={"Content-Disposition": "attachment; filename=App.jsx"}
    )


@app.route("/download/flutter")
def download_flutter():
    return Response(
        latest_flutter,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment; filename=ui.dart"}
    )


if __name__ == "__main__":
    app.run(debug=True)