from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/postme', methods=['POST'])
def postme():
    return jsonify({'Hello':'Welcome'})

app.run(host='0.0.0.0', port=8080)