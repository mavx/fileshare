from flask import Flask, request, redirect, jsonify, abort

import filestore

app = Flask(__name__)
DOMAIN_NAME = ""

@app.route('/', methods=['GET'])
def hello():
    return "What's up.\n"

@app.route('/easteregg', methods=['GET'])
def easter():
    return "Oh hey you found the Easter Egg!\n"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file.'
        
        f = request.files['file']
        if f.filename == '':
            return 'No selected file.'
        
        # if f and filestore.allowed_file(f.filename):
        if f:
            file_id = filestore.process_upload(f)
            return jsonify({
                "key": file_id,
                "success": True,
                "url": "{}/uploads/{}".format(DOMAIN_NAME, file_id)
            })

    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <p><input type=file name=file>
            <input type=submit value=Upload>
        </form>
    '''

@app.route('/uploads/<key>', methods=['GET'])
def get_file_by_key(key):
    try:
        return redirect(filestore.show_file(key, is_key=True))
    except Exception as e:
        print(str(e))
        abort(404)

@app.route('/files/<filename>', methods=['GET'])
def get_file_by_name(filename):
    return filestore.show_file(filename, is_key=False)


if __name__ == '__main__':
    app.run(debug=True)
