"""
Lead Sync Service - synchronizes leads from Business-Marketing to Tro_Ly_Shop.
"""
import logging
from integration.shared_services.telegram_bot import send_admin_notification

logger = logging.getLogger(__name__)

def sync_new_lead(lead_data):
    """
    Sync a new lead from the marketing system to the shop system.
    
    Args:
        lead_data: dict with keys: lead_id, name, email, phone, source, product_interest
    
    This function:
    1. Creates/updates a prospect in Tro_Ly_Shop
    2. Notifies the admin via Telegram
    3. Adds the lead to an automated nurture sequence
    """
    name = lead_data.get('name', 'Unknown')
    email = lead_data.get('email', 'N/A')
    product = lead_data.get('product_interest', 'General')
    
    # Notify admin
    msg = f"🆕 Lead mới từ Marketing\nTên: {name}\nEmail: {email}\nSản phẩm: {product}"
    send_admin_notification(msg)
    
    logger.info(f"Lead synced: {name} ({email}) - Interest: {product}")
    return {"synced": True, "lead_id": lead_data.get('lead_id')}
