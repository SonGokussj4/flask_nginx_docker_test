import os
import sys
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    UPLOAD_FOLDER=os.path.join(app.root_path, 'static', 'upload'),
))

# Custom User Imports
user_paths = [
    Path('{root_path}/static/scripts'.format(root_path=app.root_path))
]
sys.path.extend([str(path.resolve()) for path in user_paths])
import beta_pdf_miner


# Main app
@app.route('/')
def hello_world():
    # return 'Hello, sWorld! Version10; ROOT_PATH: {}'.format(app.root_path)
    return render_template('main.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run(host='127.0.0.1')
    # app.run(host='flask1')
    # app.run(host='localhost')
