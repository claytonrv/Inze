# coding: utf-8
from flask import Flask, request
from flask_cors import CORS
from service import CSVHandler
from translation import RecordTranslator
import os, random, string, json

ALLOWED_EXTENSIONS = {'csv'}

csvHandler = CSVHandler()
translator = RecordTranslator()

app = Flask(__name__)
CORS(app)

@app.route('/upload_files', methods=['POST'])
def upload_folder():
    user = randomString()
    uploaded_files = request.files.getlist("file")
    directory = os.path.join(app.root_path, 'static', user)
    record_json_list = process_csv_files(uploaded_files, directory)
    return record_json_list

def process_csv_files(uploaded_files, directory):
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            save_csv_files_locally(file, directory)
    list_of_record_json = transform_files_in_folder(directory)
    record_json_list = translator.translate_record_list_to_json_list(list_of_record_json)

def save_csv_files_locally(file, directory):
    filename = file.filename
    file_path = os.path.join(directory, filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    file.save(file_path)

def transform_files_in_folder(folder_path):
    list_of_record_json = csvHandler.transform_csv_files_into_json_by_folder(folder_path)
    return list_of_record_json

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == '__main__':
    app.run(debug=False, host="127.0.0.1", port=int('8082'))