"""
Shared SePay VietQR payment service.
Centralizes payment processing for both Business-Marketing and Tro_Ly_Shop.
"""
import logging
import hmac
import hashlib
import json
from shared.config.settings import SEPAY_API_KEY, SEPAY_SECRET_KEY

logger = logging.getLogger(__name__)

def verify_webhook_signature(payload, signature):
    """Verify HMAC signature from SePay webhook."""
    if not SEPAY_SECRET_KEY:
        logger.warning("No SePay secret key configured, skipping signature verification")
        return True
    expected = hmac.new(
        SEPAY_SECRET_KEY.encode(),
        json.dumps(payload, separators=(',', ':')).encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)

def process_payment_notification(payload):
    """Process an incoming SePay payment notification."""
    transaction_id = payload.get('transaction_id')
    amount = payload.get('amount')
    customer_name = payload.get('customer_name')
    customer_email = payload.get('customer_email')
    status = payload.get('status')
    
    logger.info(f"Payment received: {amount} VND from {customer_name} (txn: {transaction_id})")
    
    # In production, this would:
    # 1. Update order status in both systems
    # 2. Trigger delivery automation
    # 3. Send notifications
    
    return {
        "status": "processed",
        "transaction_id": transaction_id,
        "amount": amount
    }
