from flask import Flask, render_template, request
import os
from resume_parser import extract_text
from matcher import match_resumes

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    jd = request.form["jd"]
    files = request.files.getlist("resumes")

    resumes = []

    for file in files:
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        text = extract_text(path)
        resumes.append((file.filename, text))

    ranked = match_resumes(jd, resumes)

    return str(ranked)


if __name__ == "__main__":
    app.run(debug=True)