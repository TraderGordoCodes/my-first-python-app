from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # 1. Set the date of the next big fight (Example: UFC 313)
    # Format: Year, Month, Day, Hour (24h), Minute
    fight_date = datetime(2026, 3, 21, 22, 0, 0) 
    
    # 2. Get the current time
    now = datetime.now()
    
    # 3. Calculate the difference
    countdown = fight_date - now
    
    # 4. Break it down into readable parts
    days = countdown.days
    hours, remainder = divmod(countdown.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    return f"""
    <html>
        <head><title>UFC Countdown</title></head>
        <body style="text-align: center; font-family: sans-serif; margin-top: 50px;">
            <h1>Next Big UFC Event</h1>
            <div style="font-size: 2em; color: #d32f2f;">
                {days}d : {hours}h : {minutes}m
            </div>
            <p>Live on your Flask App</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')