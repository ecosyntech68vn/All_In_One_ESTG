"""
Shared Telegram bot service for sending messages.
Used by both Business-Marketing and Tro_Ly_Shop systems.
"""
import logging
import requests
from shared.config.settings import TELEGRAM_BOT_TOKEN

logger = logging.getLogger(__name__)

def send_message(chat_id, text, parse_mode=None):
    """
    Send a message via Telegram bot.
    
    Args:
        chat_id (str or int): The chat ID to send the message to
        text (str): The message text
        parse_mode (str, optional): Parse mode for the message (e.g., 'HTML' or 'Markdown')
    
    Returns:
        bool: True if message was sent successfully, False otherwise
    """
    if not TELEGRAM_BOT_TOKEN:
        logger.error("Telegram bot token not configured")
        return False
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    if parse_mode:
        payload['parse_mode'] = parse_mode
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            logger.info(f"Message sent successfully to chat_id {chat_id}")
            return True
        else:
            logger.error(f"Failed to send Telegram message: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        logger.error(f"Exception sending Telegram message: {str(e)}")
        return False

def send_admin_notification(text, parse_mode=None):
    """
    Send a notification to the admin chat.
    
    Args:
        text (str): The message text
        parse_mode (str, optional): Parse mode for the message
    
    Returns:
        bool: True if message was sent successfully, False otherwise
    """
    from shared.config.settings import TELEGRAM_ADMIN_CHAT_ID
    if not TELEGRAM_ADMIN_CHAT_ID:
        logger.error("Admin chat ID not configured")
        return False
    
    return send_message(TELEGRAM_ADMIN_CHAT_ID, text, parse_mode)