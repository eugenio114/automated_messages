import schedule
import time
import telegram

# Set up the Telegram bot
bot = telegram.Bot(token='YOUR_BOT_TOKEN')

# Define the function to send the reminder
def send_reminder():
    # Send the reminder message
    bot.send_message(chat_id='YOUR_CHAT_ID', text='REMINDER MESSAGE')

# Schedule the reminder to be sent every day at 8 am
schedule.every().day.at('08:00').do(send_reminder)

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
