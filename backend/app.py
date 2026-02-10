from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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

    file.save(filepath)

    return jsonify({
    "status": "uploaded",
    "filename": filename
    })



@app.route('/test')
def test():
    return jsonify({
    "status": "uploaded",
    "filename": filename
    })

if __name__ == "__main__":
    app.run(debug=True)