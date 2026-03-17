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
            <title>UFC London: Evloev vs Murphy</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ font-family: 'Segoe UI', sans-serif; background-color: #0d0d0d; color: #fff; margin: 0; padding: 20px; }}
                .wrapper {{ max-width: 500px; margin: auto; }}
                h1 {{ font-size: 1.2em; color: #888; letter-spacing: 3px; text-align: center; }}
                .main-event {{ font-size: 1.6em; text-align: center; margin: 10px 0; font-weight: 900; color: #fff; }}
                #timer {{ text-align: center; font-size: 2.2em; color: #d32f2f; margin: 15px 0; font-family: monospace; font-weight: bold; }}
                
                .section-header {{ background: #d32f2f; color: white; padding: 5px 10px; font-size: 0.9em; font-weight: bold; margin-top: 20px; text-transform: uppercase; }}
                .match-row {{ background: #1a1a1a; padding: 12px; border-bottom: 1px solid #333; display: flex; justify-content: space-between; align-items: center; font-size: 0.95em; }}
                .rank {{ color: #d32f2f; font-size: 0.8em; margin-right: 5px; font-weight: bold; }}
                .vs-tag {{ color: #666; font-style: italic; font-size: 0.8em; }}
            </style>
        </head>
        <body>
            <div class="wrapper">
                <h1>UFC FIGHT NIGHT</h1>
                <div class="main-event">
                    <span class="rank">#1</span>EVLOEV <span style="color:#d32f2f">VS</span> <span class="rank">#3</span>MURPHY
                </div>
                
                <div id="timer">Loading...</div>

                <div class="section-header">Main Card</div>
                <div class="match-row"><span>Luke Riley</span> <span class="vs-tag">vs</span> <span>Michael Aswell</span></div>
                <div class="match-row"><span><span class="rank">#14</span>Michael Page</span> <span class="vs-tag">vs</span> <span>Sam Patterson</span></div>
                <div class="match-row"><span>Iwo Baraniewski</span> <span class="vs-tag">vs</span> <span>Austen Lane</span></div>
                <div class="match-row"><span><span class="rank">#11</span>Roman Dolidze</span> <span class="vs-tag">vs</span> <span>Christian Leroy Duncan</span></div>
                <div class="match-row"><span>Kurtis Campbell</span> <span class="vs-tag">vs</span> <span>Danny Silva</span></div>

                <div class="section-header">Prelims</div>
                <div class="match-row"><span>Mason Jones</span> <span class="vs-tag">vs</span> <span>Axel Sola</span></div>
                <div class="match-row"><span>Nathaniel Wood</span> <span class="vs-tag">vs</span> <span>Losene Keita</span></div>
                <div class="match-row"><span>Mario Pinto</span> <span class="vs-tag">vs</span> <span>Felipe Franco</span></div>
                <div class="match-row"><span>Mantas Kondratavičius</span> <span class="vs-tag">vs</span> <span>Antonio Trócoli</span></div>
                <div class="match-row"><span>Melissa Mullins</span> <span class="vs-tag">vs</span> <span>Luana Carolina</span></div>
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
                    if (distance < 0) {{ clearInterval(x); document.getElementById("timer").innerHTML = "FIGHT NIGHT"; }}
                }}, 1000);
            </script>
        </body>
    </html>
    """

if __name__ == "__main__":
    # Get the port from Render's environment, or use 5000 as a backup
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)