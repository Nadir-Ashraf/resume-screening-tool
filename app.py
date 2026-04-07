from flask import Flask, render_template, request
import os

from resume_parser import extract_text
from matcher import rank_resumes

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    job_description = request.form["jd"]

    files = request.files.getlist("resumes")

    resumes = []

    for file in files:

        if file.filename == "":
            continue

        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        text = extract_text(path)

        resumes.append({
            "name": file.filename,
            "text": text
        })

    results = rank_resumes(job_description, resumes)

    return render_template("results.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)