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
            <title>UFC London: Evloev vs Murphy | Betting Odds</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ font-family: 'Segoe UI', sans-serif; background-color: #0d0d0d; color: #fff; margin: 0; padding: 20px; }}
                .wrapper {{ max-width: 600px; margin: auto; }}
                h1 {{ font-size: 1.1em; color: #888; letter-spacing: 3px; text-align: center; margin-bottom: 5px; }}
                .main-event {{ font-size: 1.6em; text-align: center; margin-bottom: 10px; font-weight: 900; }}
                #timer {{ text-align: center; font-size: 2.5em; color: #d32f2f; margin-bottom: 20px; font-family: monospace; }}
                
                .section-header {{ background: #d32f2f; color: white; padding: 6px 12px; font-size: 0.85em; font-weight: bold; margin-top: 20px; text-transform: uppercase; display: flex; justify-content: space-between; }}
                .match-row {{ background: #1a1a1a; padding: 15px; border-bottom: 1px solid #333; display: flex; align-items: center; font-size: 0.9em; }}
                .fighters {{ flex: 2; }}
                .odds-box {{ flex: 1; display: flex; justify-content: space-around; }}
                .odds {{ background: #333; padding: 4px 8px; border-radius: 4px; font-weight: bold; color: #ffcc00; min-width: 45px; text-align: center; font-size: 0.85em; }}
                
                .rank {{ color: #d32f2f; font-size: 0.8em; font-weight: bold; margin-right: 4px; }}
                .vs-tag {{ color: #666; font-size: 0.75em; margin: 0 5px; }}
            </style>
        </head>
        <body>
            <div class="wrapper">
                <h1>UFC FIGHT NIGHT: LONDON</h1>
                <div class="main-event">
                    <span class="rank">#1</span>EVLOEV <span style="color:#d32f2f">VS</span> <span class="rank">#3</span>MURPHY
                </div>
                
                <div id="timer">00d 00h 00m 00s</div>

                <div class="section-header">
                    <span>Main Card</span>
                    <span>Live Odds</span>
                </div>
                
                <div class="match-row">
                    <div class="fighters">Evloev <span class="vs-tag">vs</span> Murphy</div>
                    <div class="odds-box"><span class="odds">-218</span> <span class="odds">+180</span></div>
                </div>
                <div class="match-row">
                    <div class="fighters">Luke Riley <span class="vs-tag">vs</span> Michael Aswell</div>
                    <div class="odds-box"><span class="odds">-350</span> <span class="odds">+275</span></div>
                </div>
                <div class="match-row">
                    <div class="fighters"><span class="rank">#14</span>MVP <span class="vs-tag">vs</span> Patterson</div>
                    <div class="odds-box"><span class="odds">-110</span> <span class="odds">-110</span></div>
                </div>
                <div class="match-row">
                    <div class="fighters">Baraniewski <span class="vs-tag">vs</span> Austen Lane</div>
                    <div class="odds-box"><span class="odds">-250</span> <span class="odds">+200</span></div>
                </div>
                <div class="match-row">
                    <div class="fighters"><span class="rank">#11</span>Dolidze <span class="vs-tag">vs</span> CLD</div>
                    <div class="odds-box"><span class="odds">+145</span> <span class="odds">-175</span></div>
                </div>

                <div class="section-header">Prelims</div>
                <div class="match-row">
                    <div class="fighters">Mason Jones <span class="vs-tag">vs</span> Axel Sola</div>
                    <div class="odds-box"><span class="odds">-180</span> <span class="odds">+150</span></div>
                </div>
                <div class="match-row">
                    <div class="fighters">Wood <span class="vs-tag">vs</span> Keita</div>
                    <div class="odds-box"><span class="odds">-120</span> <span class="odds">+100</span></div>
                </div>
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
                    if (distance < 0) {{ clearInterval(x); document.getElementById("timer").innerHTML = "LIVE"; }}
                }}, 1000);
            </script>
        </body>
    </html>
    """

if __name__ == "__main__":
    # Get the port from Render's environment, or use 5000 as a backup
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)