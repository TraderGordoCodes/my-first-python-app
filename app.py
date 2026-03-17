import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Set your fight date here (March 21, 2026 at 10:00 PM)
    fight_date = "Mar 21, 2026 22:00:00"

    return f"""
    <html>
        <head>
            <title>UFC Live Countdown</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body style="text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin-top: 100px; background-color: #1a1a1a; color: white;">
            <h1>NEXT BIG UFC EVENT</h1>
            <div id="timer" style="font-size: 3em; font-weight: bold; color: #d32f2f; margin: 20px 0;">
                Loading...
            </div>
            <p style="color: #888;">Live from your Render App</p>

            <script>
                // The date we are counting down to
                var countDownDate = new Date("{fight_date}").getTime();

                // Update the count down every 1 second
                var x = setInterval(function() {{
                    var now = new Date().getTime();
                    var distance = countDownDate - now;

                    // Time calculations for days, hours, minutes and seconds
                    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                    // Output the result in the element with id="timer"
                    document.getElementById("timer").innerHTML = days + "d " + hours + "h "
                    + minutes + "m " + seconds + "s ";

                    // If the count down is over, write some text 
                    if (distance < 0) {{
                        clearInterval(x);
                        document.getElementById("timer").innerHTML = "FIGHT TIME!";
                    }}
                }}, 1000);
            </script>
        </body>
    </html>
    """

if __name__ == "__main__":
    # Get the port from Render's environment, or use 5000 as a backup
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)