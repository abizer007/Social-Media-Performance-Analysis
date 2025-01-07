import os
import json
from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# API key for Langflow, directly inserted here (not recommended for production)
APPLICATION_TOKEN = "AstraCS:pZwJOoQtdtgkosguBiFsQElm:9658cf9bd3dcc4e6bee2ffe01c5f185be4f2f6f583bf520f9aa64b513dd795da"
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "5bc0e8b1-c96b-4be0-9738-58209e4d9b22"
FLOW_ID = "14aecd59-decf-493a-8a02-67a94b283b0c"

def run_flow(message: str, endpoint: str = FLOW_ID, output_type: str = "chat", input_type: str = "chat") -> dict:
    """
    Run the Langflow API with a given message and return the response.
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type
    }
    
    headers = {
        "Authorization": "Bearer " + APPLICATION_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_flow', methods=['POST'])
def api_request():
    data = request.get_json()
    message = data.get("message")
    
    if not message:
        return jsonify({"error": "No message provided"}), 400

    response = run_flow(message)
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
