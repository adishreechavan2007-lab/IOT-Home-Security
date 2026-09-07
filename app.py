# IOT Home Security - ESP32 to Telegram Alert
import requests

def send_alert(message):
    bot_token = "YOUR_BOT_TOKEN"
    chat_id = "YOUR_CHAT_ID"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)
    print("Alert Sent!")

# When PIR sensor detects motion
# send_alert(" Intrusion Detected at Main Door - 10:30 PM")
