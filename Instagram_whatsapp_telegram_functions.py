from twilio.rest import Client
from telegram import Bot
from instagram_private_api import Client as IGClient

# Set up Twilio API client
twilio_client = Client(account_sid, auth_token)

def send_whatsapp_message(message, to_number):
    """Sends a message to a WhatsApp chat."""
    message = twilio_client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to=f'whatsapp:{to_number}'
    )
    print(f"Sent WhatsApp message with ID {message.sid} to {to_number}")

# Set up Telegram API client
telegram_bot = Bot(token=telegram_token)

def send_telegram_message(message, chat_id):
    """Sends a message to a Telegram chat."""
    telegram_bot.send_message(chat_id=chat_id, text=message)
    print(f"Sent Telegram message to chat {chat_id}")

# Set up Instagram API client
ig_client = IGClient(username, password)

def send_instagram_message(message, to_username):
    """Sends a message to an Instagram user's direct messages."""
    user_id = ig_client.search_users(to_username)[0].pk
    ig_client.direct_send_message(message, user_id=user_id)
    print(f"Sent Instagram message to {to_username}")
    
message = "Hello world!"
to_whatsapp_number = "+1234567890"
to_telegram_chat_id = 123456789
to_instagram_username = "example_user"

send_whatsapp_message(message, to_whatsapp_number)
send_telegram_message(message, to_telegram_chat_id)
send_instagram_message(message, to_instagram_username)
