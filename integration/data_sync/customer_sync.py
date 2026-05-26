"""
Customer Sync Service - synchronizes customer data between systems.
"""
import logging

logger = logging.getLogger(__name__)

def sync_customer_from_shop(customer_data):
    """
    Sync customer purchase history from Tro_Ly_Shop to Business-Marketing.
    This enables personalized marketing based on actual purchase behavior.
    
    Args:
        customer_data: dict with keys: customer_id, name, email, phone, 
                      purchase_history, total_spent, last_purchase_date
    """
    name = customer_data.get('name', 'Unknown')
    email = customer_data.get('email', 'N/A')
    total_spent = customer_data.get('total_spent', 0)
    
    # In production: update marketing segments, trigger flows
    logger.info(f"Customer synced: {name} ({email}) - Total spent: {total_spent}")
    return {"synced": True}
