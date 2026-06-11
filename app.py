from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load intents
with open("intents.json", "r") as file:
    data = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_message:
                return jsonify({
                    "response": intent["responses"][0]
                })

    return jsonify({
        "response": "Sorry, I don't understand."
    })

if __name__ == "__main__":
    app.run(debug=True)