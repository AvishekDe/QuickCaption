import os, io

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
        # filename = secure_filename(photo.filename)
        # in_memory_file = io.BytesIO()
        photo.save('/home/gaurav/images/image.jpg')
        os.system('th /home/gaurav/Github/neuraltalk2/eval.lua -model /home/gaurav/Github/model_id1-501-1448236541.t7 -image_folder /home/gaurav/images/ -num_images 1')
        # return /home/gauravwaghmare/neuraltalk2/vis/vis.json
        with open('/home/gaurav/Github/neuraltalk2/vis/vis.json') as json_data:
    		d = json.load(json_data)
    		return jsonify(d)
    else:
        abort(404)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)