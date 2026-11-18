from flask import Flask, render_template, request, jsonify, session
from chatbot import get_response
from database import init_db, save_message, get_history, clear_history
import uuid

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret-key"

init_db()

@app.before_request
def ensure_session():
    if "chat_id" not in session:
        session["chat_id"] = str(uuid.uuid4())

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify({"error": "Please type a message."}), 400

    reply = get_response(message)
    save_message(session["chat_id"], message, reply)
    return jsonify({"reply": reply})

@app.route("/api/history", methods=["GET"])
def history():
    return jsonify({"messages": get_history(session["chat_id"])})

@app.route("/api/clear", methods=["POST"])
def clear():
    clear_history(session["chat_id"])
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)
