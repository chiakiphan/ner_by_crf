from flask import Flask
from flask import request, jsonify
from main.ner_load_tag import ner_tag
app = Flask(__name__)
host = '127.0.0.1'
port = '8000'


@app.route('/product', methods=['GET'])
def api_detach_product():
    sent = request.args.get('sentence')
    return jsonify(ner_tag(sent, mode='text'))


if __name__ == '__main__':
    app.run(host=host, port=port)