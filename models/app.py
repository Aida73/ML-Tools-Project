from flask import Flask,request, jsonify
import chatbot_model


app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, Flask!'


@app.route('/eptinfos', methods=['POST'])
def get_ept_infos():
    data = request.get_json()
    question = data['question']

    response = chatbot_model.getEptInfos(question)

    response = f"your question is:{question}"

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

