from flask import Flask, request, jsonify
from PyPDF2 import PdfFileReader
from auth.main import auth_required

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"result": "success", "message": "Hello from Flask"}), 200


@app.route("/upload", methods=["POST"])
def upload():
    candidate = {}
    pdf_file = request.files['pdf']
    pdf = PdfFileReader(pdf_file)
    page = pdf.getPage(0)
    text = page.extractText().split('\n')
    candidate['name'] = text[0]
    candidate['vacancy'] = text[1]
    return jsonify({"result": "success","candidate": candidate}), 200


if __name__ == "__main__":
    app.run(debug=True)
