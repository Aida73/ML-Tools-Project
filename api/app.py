import sys
import os
from flask import Flask,request, jsonify

# Add the parent directory of the current file to the module search path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from models import chatbot_model


app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, Flask!'


@app.route('/eptinfos', methods=['POST'])
def get_ept_infos():
    data = request.get_json()
    question = data['question']

    response = chatbot_model.getEptInfos(question)

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

