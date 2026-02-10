from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import pdfplumber

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text

@app.route("/")
def home():
    return {"status": "JobNexAI backend running"}

@app.route("/upload-cv", methods=["POST"])
def upload_cv():
    if "cv" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["cv"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    text = extract_text_from_pdf(filepath)

    return jsonify({
        "status": "success",
        "text": text
    })

@app.route("/test")
def test():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
