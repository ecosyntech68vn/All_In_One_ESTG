"""
Webhook handler for converting a marketing lead into a shop prospect.
This would be called by the Business-Marketing system when a new lead is captured.
"""
import json
import logging
from shared.config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_ADMIN_CHAT_ID, BASE_URL
import requests

logger = logging.getLogger(__name__)

def handle_lead_to_prospect(request_data):
    """
    Process a lead from the marketing system and create a prospect in the shop system.
    
    Expected request_data format:
    {
        "lead_id": "string",
        "name": "string",
        "email": "string",
        "phone": "string",
        "interest": "string",  # e.g., product or service they're interested in
        "source": "string",    # e.g., facebook_ad, google_search
        "timestamp": "ISO string"
    }
    """
    try:
        # Extract lead information
        lead_id = request_data.get('lead_id')
        name = request_data.get('name')
        email = request_data.get('email')
        phone = request_data.get('phone')
        interest = request_data.get('interest')
        source = request_data.get('source')
        
        if not all([lead_id, name, email]):
            logger.error("Missing required lead information")
            return {"error": "Missing required fields"}, 400
        
        # In a real implementation, this would:
        # 1. Create a prospect in the Tro_Ly_Shop database
        # 2. Trigger a notification to the shop owner via Telegram
        # 3. Add the prospect to a nurture sequence
        
        # For now, we'll log and simulate sending a Telegram message to the admin
        message = f"""
🆕 New Lead from Marketing System
ID: {lead_id}
Name: {name}
Email: {email}
Phone: {phone or 'Not provided'}
Interest: {interest or 'Not specified'}
Source: {source}
        """
        
        # Send notification to admin via Telegram (if configured)
        if TELEGRAM_BOT_TOKEN and TELEGRAM_ADMIN_CHAT_ID:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {
                'chat_id': TELEGRAM_ADMIN_CHAT_ID,
                'text': message,
                'parse_mode': 'HTML'
            }
            response = requests.post(url, json=payload)
            if response.status_code != 200:
                logger.error(f"Failed to send Telegram notification: {response.text}")
        
        logger.info(f"Processed lead {lead_id} and created prospect")
        return {"status": "success", "prospect_id": lead_id}, 200
        
    except Exception as e:
        logger.error(f"Error processing lead: {str(e)}")
        return {"error": "Internal server error"}, 500