
from flask import Flask, jsonify, make_response, request
from utils import create_chain


app = Flask(__name__)

@app.route("/", methods = ['POST'])
def chat():
    if not request.is_json:
        return make_response(
            jsonify(
                {"success": False,
                 "error": "Unexpected error, request is not in JSON format"}),
            400)
    
    try:
        data = request.json
        message = data["message"]
        chatgpt_chain = create_chain()
        prediction = chatgpt_chain.predict(human_input=message)
        
        return jsonify({"success": True, "data": prediction})
    except:
        return make_response(
            jsonify(
                {"success": False, 
                 "error": "Unexpected error: failed to send the message"}),
            400)