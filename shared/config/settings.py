# Shared configuration settings
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram settings
TELEGRAM_BOT_TOKEN = os.getenv('BOT_TOKEN')
TELEGRAM_ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')

# SePay settings
SEPAY_API_KEY = os.getenv('SEPAY_API_KEY')
SEPAY_SECRET_KEY = os.getenv('SEPAY_SECRET_KEY')  # For HMAC verification
SEPAY_WEBHOOK_URL = os.getenv('SEPAY_WEBHOOK_URL')

# AI API keys
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Base URL for the application (used in webhooks, redirects, etc.)
BASE_URL = os.getenv('BASE_URL')

# Database settings (if using a shared database)
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///shared.db')

# Other settings
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'