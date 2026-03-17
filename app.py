import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Target: UFC Fight Night (March 21, 2026)
    fight_date = "Mar 21, 2026 22:00:00"

    return f"""
    <html>
        <head>
            <title>UFC Live Tracker</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ text-align: center; font-family: 'Arial Black', sans-serif; background-color: #121212; color: white; margin: 0; padding: 20px; }}
                .container {{ max-width: 600px; margin: auto; border: 2px solid #333; padding: 20px; border-radius: 15px; background: #1e1e1e; }}
                h1 {{ color: #eee; font-size: 1.5em; letter-spacing: 2px; }}
                .main-event {{ font-size: 1.8em; color: #fff; margin: 10px 0; border-bottom: 2px solid #d32f2f; padding-bottom: 10px; }}
                #timer {{ font-size: 2.5em; color: #d32f2f; margin: 20px 0; font-family: monospace; }}
                .card-list {{ text-align: left; background: #2a2a2a; padding: 15px; border-radius: 10px; }}
                .matchup {{ display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #444; }}
                .vs {{ color: #d32f2f; font-style: italic; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>UPCOMING EVENT</h1>
                <div class="main-event">Evloev <span class="vs">vs</span> Murphy</div>
                
                <div id="timer">Loading...</div>

                <div class="card-list">
                    <h3 style="margin-top:0; color:#888;">FIGHT CARD</h3>
                    <div class="matchup">
                        <span>Movsar Evloev</span> <span class="vs">VS</span> <span>Lerone Murphy</span>
                    </div>
                    <div class="matchup">
                        <span>Brandon Riley</span> <span class="vs">VS</span> <span>Damon Aswell Jr.</span>
                    </div>
                </div>
                <p style="font-size: 0.8em; color: #555; margin-top: 20px;">DEPLOYED VIA RENDER + GITHUB ACTIONS</p>
            </div>

            <script>
                var countDownDate = new Date("{fight_date}").getTime();
                var x = setInterval(function() {{
                    var now = new Date().getTime();
                    var distance = countDownDate - now;
                    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                    document.getElementById("timer").innerHTML = days + "d " + hours + "h "
                    + minutes + "m " + seconds + "s ";

                    if (distance < 0) {{
                        clearInterval(x);
                        document.getElementById("timer").innerHTML = "LIVE NOW";
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