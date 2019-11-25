# coding: utf-8
from flask import Flask, request
from flask_cors import CORS
from service import CSVReader
from translation import RecordTranslator
import os, random, string, json

ALLOWED_EXTENSIONS = {'csv'}

csvReader = CSVReader()
translator = RecordTranslator()

app = Flask(__name__)
CORS(app)

@app.route('/upload_file', methods=['POST'])
def upload_file():
    #TODO the csv handler for single files is not implemented yet.
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = file.filename
        file_path = os.path.join(app.root_path, 'static', filename)
        file.save(file_path)
    return "ok"

@app.route('/upload_folder', methods=['POST'])
def upload_folder():
    user = randomString()
    uploaded_files = request.files.getlist("file")
    directory = os.path.join(app.root_path, 'static', user)
    file_paths = []
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            filename = file.filename
            print(filename)
            file_path = os.path.join(directory, filename)
            if not os.path.exists(directory):
                os.makedirs(directory)
            file.save(file_path)
    record_list = process_folder(directory)
    return translator.translate_record_list_to_json_list(record_list)

def process_file(file_path):
    return csvReader.process_csv_data_by_file(file_path)

def process_folder(folder_path):
    return csvReader.process_csv_data_by_folder(folder_path)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1", port=int('8082'))