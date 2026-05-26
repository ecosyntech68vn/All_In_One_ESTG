"""
Tro_Ly_Shop - AI Agent 24/7 cho Shop Online
Source code: https://github.com/ecosyntech68vn/Tro_Ly_Shop
Place this repository content here for the full system.
"""
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def health():
    return jsonify({"status": "ok", "service": "tro_ly_shop"})

@app.route('/telegram-webhook', methods=['POST'])
def telegram_webhook():
    data = request.json
    # Handle incoming Telegram messages
    return jsonify({"status": "received"})

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.json
    # Handle widget chat messages
    return jsonify({"response": "AI response placeholder"})

@app.route('/sepay-webhook', methods=['POST'])
def sepay_webhook():
    data = request.json
    # Import shared SePay service for processing
    from integration.shared_services.sepay_client import process_payment_notification
    result = process_payment_notification(data)
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
