from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "CHX HOSTING BOT API is online"

@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "CHX HOSTING BOT",
        "runtime": "vercel"
    })
