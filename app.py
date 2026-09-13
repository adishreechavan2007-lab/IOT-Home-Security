from flask import Flask, render_template_string
import random
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>IoT Home Security - ESP32</title>
<meta http-equiv="refresh" content="3">
<style>
body { font-family: Arial; background: #0f172a; color: white; text-align: center; padding-top: 30px; }
.card { background: #1e293b; width: 350px; margin: auto; padding: 25px; border-radius: 15px; box-shadow: 0 0 20px #000; }
.safe { color: #22c55e; font-size: 32px; }
.alert { color: #ef4444; font-size: 32px; animation: blink 1s infinite; }
@keyframes blink { 50% { opacity: 0.5; } }
p { font-size: 18px; }
</style>
</head>
<body>
<h1>🏠 IoT Home Security System</h1>
<h3>ESP32 + PIR + Door Sensor</h3>
<div class="card">
<h2 class="{{ 'alert' if status=='ALERT!' else 'safe' }}">{{ status }}</h2>
<p>🕵️ PIR: {{ pir }}</p>
<p>🚪 Door: {{ door }}</p>
<p>🔊 Buzzer: {{ buzzer }}</p>
<p style="font-size:12px; opacity:0.6;">Last Update: {{ time }}</p>
</div>
<p>Made by Adishree Chavan</p>
</body>
</html>
"""

@app.route('/')
def home():
    pir = random.choice(["No Motion", "Motion Detected!"])
    door = random.choice(["Door Closed", "Door Opened!"])
    is_alert = "Detected" in pir or "Opened" in door
    
    return render_template_string(HTML, 
        pir=pir, 
        door=door,
        status="ALERT!" if is_alert else "SAFE",
        buzzer="ON 🔊" if is_alert else "OFF",
        time=datetime.now().strftime("%H:%M:%S")
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
