import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    fight_date = "Mar 21, 2026 22:00:00"

    return f"""
    <html>
        <head>
            <title>UFC Arbitrage Tracker</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ font-family: 'Segoe UI', sans-serif; background-color: #0a0a0a; color: #fff; margin: 0; padding: 15px; }}
                .wrapper {{ max-width: 550px; margin: auto; }}
                h1 {{ font-size: 1em; color: #666; letter-spacing: 4px; text-align: center; text-transform: uppercase; }}
                .main-event {{ font-size: 1.4em; text-align: center; font-weight: 900; margin-bottom: 5px; }}
                #timer {{ text-align: center; font-size: 2.2em; color: #d32f2f; margin-bottom: 25px; font-family: 'Courier New', monospace; }}
                
                .section-header {{ background: #1a1a1a; color: #888; padding: 8px 15px; font-size: 0.75em; font-weight: bold; margin-top: 20px; border-left: 4px solid #d32f2f; display: flex; justify-content: space-between; }}
                .match-row {{ background: #141414; padding: 15px; border-bottom: 1px solid #222; display: flex; align-items: center; }}
                .fighters {{ flex: 2; font-weight: 600; font-size: 0.95em; }}
                .odds-container {{ flex: 1; display: flex; justify-content: space-between; gap: 10px; }}
                .odds-column {{ text-align: center; flex: 1; }}
                
                .price {{ background: #222; padding: 5px; border-radius: 4px; font-weight: bold; color: #ffcc00; display: block; margin-bottom: 4px; }}
                .prob {{ font-size: 0.7em; color: #555; font-weight: bold; }}
                
                .rank {{ color: #d32f2f; font-size: 0.8em; margin-right: 4px; }}
            </style>
        </head>
        <body>
            <div class="wrapper">
                <h1>UFC London • Mar 21</h1>
                <div class="main-event">EVLOEV <span style="color:#d32f2f">VS</span> MURPHY</div>
                <div id="timer">00d 00h 00m 00s</div>

                <div class="section-header">
                    <span>Main Card Matchups</span>
                    <span>Market Odds / Implied %</span>
                </div>

                <div class="match-row">
                    <div class="fighters"><span class="rank">#1</span>Evloev <br> <span class="rank">#3</span>Murphy</div>
                    <div class="odds-container">
                        <div class="odds-column"><span class="price">-218</span><span class="prob">68.6%</span></div>
                        <div class="odds-column"><span class="price">+180</span><span class="prob">35.7%</span></div>
                    </div>
                </div>

                <div class="match-row">
                    <div class="fighters"><span class="rank">#14</span>MVP <br> Patterson</div>
                    <div class="odds-container">
                        <div class="odds-column"><span class="price">-110</span><span class="prob">52.4%</span></div>
                        <div class="odds-column"><span class="price">-110</span><span class="prob">52.4%</span></div>
                    </div>
                </div>

                <div class="match-row">
                    <div class="fighters"><span class="rank">#11</span>Dolidze <br> CLD</div>
                    <div class="odds-container">
                        <div class="odds-column"><span class="price">+145</span><span class="prob">40.8%</span></div>
                        <div class="odds-column"><span class="price">-175</span><span class="prob">63.6%</span></div>
                    </div>
                </div>
                
                <p style="text-align:center; color:#333; font-size:0.7em; margin-top:30px;">Total Market Overround (Vig): ~4.8%</p>
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
                    document.getElementById("timer").innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
                }}, 1000);
            </script>
        </body>
    </html>
    """

if __name__ == "__main__":
    # Get the port from Render's environment, or use 5000 as a backup
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)