import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the webdriver
driver = webdriver.Chrome()

# Define the function to send the message
def send_whatsapp_message():
    # Open WhatsApp web
    driver.get("https://web.whatsapp.com/")
    time.sleep(10) # wait for the user to log in
    # Select the chat you want to send the message to
    chat = driver.find_element_by_xpath("//span[@title='CHAT NAME']")
    chat.click()
    time.sleep(5) # wait for the chat to load
    # Type the message and send it
    message_box = driver.find_element_by_xpath("//div[@class='_3u328 copyable-text selectable-text']")
    message_box.click()
    message_box.send_keys("MESSAGE TEXT")
    message_box.send_keys(Keys.RETURN)

# Schedule the message to be sent every day at 8 am
schedule.every().day.at("08:00").do(send_whatsapp_message)

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)

