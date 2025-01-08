from flask import Flask, request, jsonify, render_template
from astrapy import DataAPIClient

# Initialize Flask app
app = Flask(__name__)

# Astra DB API Token and Endpoint
ASTRA_DB_APPLICATION_TOKEN = "AstraCS:FUGZswsNMdGZIQqjhtETpPRL:e9d3be7fa13048f7e03c07e7ee9cc123e0c6f8dcc0ff96f0dda9d08f59b41c90"
ASTRA_DB_ENDPOINT = "https://9adfc868-0c92-4854-8776-c4c641f0d3e7-us-east-2.apps.astra.datastax.com"

# Initialize the Astra DB client
client = DataAPIClient(ASTRA_DB_APPLICATION_TOKEN)
db = client.get_database_by_api_endpoint(ASTRA_DB_ENDPOINT)

# Test DB connection
try:
    collections = db.list_collection_names()
    print(f"Connected to Astra DB. Collections: {collections}")
except Exception as e:
    print(f"Error connecting to Astra DB: {e}")

# Default route - Chatbot Interface
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Astra DB Chatbot</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f9f9f9;
            }
            .container {
                width: 80%;
                margin: auto;
                padding: 20px;
                text-align: center;
            }
            .chatbox {
                background: #ffffff;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 20px;
                margin: 20px auto;
                max-width: 600px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            .chat-messages {
                border: 1px solid #ddd;
                height: 300px;
                overflow-y: auto;
                padding: 10px;
                background: #fafafa;
                margin-bottom: 20px;
                border-radius: 5px;
            }
            .chat-messages .message {
                margin-bottom: 10px;
                text-align: left;
            }
            .chat-messages .message.user {
                text-align: right;
                color: #007BFF;
            }
            .chat-messages .message.bot {
                color: #444;
            }
            .chat-input {
                width: calc(100% - 60px);
                padding: 10px;
                margin: 5px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            .chat-button {
                padding: 10px 15px;
                background: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .chat-button:hover {
                background: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Astra DB Chatbot</h1>
            <div class="chatbox">
                <div class="chat-messages" id="chat-messages"></div>
                <input type="text" id="user-input" class="chat-input" placeholder="Type your query here...">
                <button id="send-button" class="chat-button">Send</button>
            </div>
        </div>

        <script>
            document.getElementById("send-button").addEventListener("click", async function () {
                const userInput = document.getElementById("user-input").value;
                const chatMessages = document.getElementById("chat-messages");

                if (userInput.trim() === "") return;

                // Display user message
                const userMessage = document.createElement("div");
                userMessage.classList.add("message", "user");
                userMessage.textContent = userInput;
                chatMessages.appendChild(userMessage);
                document.getElementById("user-input").value = "";

                // Send query to the server
                const response = await fetch("/query", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        collection_name: "Social Media Analyzer", // Updated to your correct collection name
                        filters: { query: userInput }, // Modify based on your use case
                        projection: {},
                        limit: 5,
                    }),
                });

                const result = await response.json();

                // Display bot response
                const botMessage = document.createElement("div");
                botMessage.classList.add("message", "bot");
                if (result.status === "success") {
                    botMessage.textContent = JSON.stringify(result.data, null, 2);
                } else {
                    botMessage.textContent = "Error: " + result.message;
                }
                chatMessages.appendChild(botMessage);
                chatMessages.scrollTop = chatMessages.scrollHeight;
            });
        </script>
    </body>
    </html>
    """

# Flask route for querying Astra DB
@app.route("/query", methods=["POST"])
def query_database():
    """
    Endpoint to query Astra DB.
    Example payload:
    {
        "collection_name": "social_media_analyzer",  # Updated to your correct collection name
        "filters": {"user_id": "123"},
        "projection": {"name": 1, "engagement": 1},
        "limit": 5
    }
    """
    data = request.json
    collection_name = data.get("collection_name")
    filters = data.get("filters", {})
    projection = data.get("projection", {})
    limit = data.get("limit", 10)

    try:
        # Get the collection
        collection = db.get_collection(collection_name)

        # Perform the query
        results = collection.find(filters, projection=projection, limit=limit)
        response_data = [result for result in results]

        return jsonify({"status": "success", "data": response_data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
