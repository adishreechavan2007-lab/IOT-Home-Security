# Simple Home Security Dashboard
# Made by Adishree Chavan

from flask import Flask
import random
import time

app = Flask(__name__)

# simple html page
html_code = """
<html>
<head><title>Home Security</title></head>
<body style="text-align:center; font-family: Arial; margin-top:50px;">
    <h1>Home Security System</h1>
    <h2>Made by Adishree Chavan</h2>
    <div style="border:2px solid black; padding:20px; margin:20px;">
        <p id="status">Checking...</p>
        <p id="time"></p>
    </div>
    <p>This is simulation of PIR and Door sensor</p>
    <script>
        function update() {
            let motion = Math.random() > 0.7;
            let door = Math.random() > 0.8;
            let status = document.getElementById("status");
            let time = document.getElementById("time");
            
            time.innerHTML = new Date().toLocaleTimeString();
            
            if(motion || door) {
                status.innerHTML = "<h2 style='color:red;'>ALERT! Motion or Door Open!</h2><p>Buzzer: ON</p>";
                status.style.background = "#ffcccc";
            } else {
                status.innerHTML = "<h2 style='color:green;'>SAFE - All Good</h2><p>Buzzer: OFF</p>";
                status.style.background = "#ccffcc";
            }
        }
        setInterval(update, 2000);
        update();
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return html_code

if __name__ == '__main__':
    print("Starting server...")
    app.run(host='0.0.0.0', port=5000)
