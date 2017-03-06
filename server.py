import os, io
from subprocess import call
import json

from flask import Flask, request, jsonify, send_file, abort, render_template
from werkzeug import secure_filename

app = Flask(__name__)

app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif', 'tif'])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route("/")

@app.route("/upload", methods=['POST'])
def upload():
    photo = request.files.get('image', '')
    if photo:
        photo.save(/path/to/image/directory)
        com = ['th', /path/to/repo/neuraltalk2/eval.lua, '-model', /path/to/model/model_id1-501-1448236541.t7, '-image_folder', /path/to/image/directory, '-num_images', num_images]
        call(com)
        with open(/path/to/saced/kson/vis.json) as json_data:
    		d = json.load(json_data)
    		return jsonify(d)
    else:
        abort(404)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)