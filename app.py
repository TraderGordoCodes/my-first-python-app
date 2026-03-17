import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Fight Date: March 21, 2026
    fight_date = "Mar 21, 2026 22:00:00"

    return f"""
    <html>
        <head>
            <title>UFC London: Scout & Arb Tracker</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ font-family: 'Segoe UI', sans-serif; background-color: #0a0a0a; color: #fff; margin: 0; padding: 10px; }}
                .wrapper {{ max-width: 600px; margin: auto; }}
                h1 {{ font-size: 0.9em; color: #666; letter-spacing: 3px; text-align: center; text-transform: uppercase; margin-top: 20px; }}
                .main-event-title {{ font-size: 1.4em; text-align: center; font-weight: 900; margin: 10px 0; }}
                #timer {{ text-align: center; font-size: 2.2em; color: #d32f2f; margin-bottom: 20px; font-family: monospace; }}
                
                .section-header {{ background: #1a1a1a; color: #888; padding: 6px 15px; font-size: 0.7em; font-weight: bold; margin-top: 15px; display: flex; justify-content: space-between; border-left: 3px solid #d32f2f; }}
                .match-row {{ background: #141414; padding: 12px 15px; border-bottom: 1px solid #222; display: flex; align-items: center; justify-content: space-between; }}
                
                .fighter-info {{ flex: 2; }}
                .fighter-name {{ font-weight: bold; font-size: 0.95em; color: #eee; }}
                .record {{ font-size: 0.75em; color: #666; }}
                .weight-class {{ font-size: 0.65em; color: #d32f2f; text-transform: uppercase; letter-spacing: 1px; margin-top: 2px; }}
                
                .odds-container {{ flex: 1; display: flex; justify-content: flex-end; gap: 8px; text-align: center; }}
                .odds-box {{ width: 65px; }}
                .price {{ background: #222; padding: 4px; border-radius: 4px; font-weight: bold; color: #ffcc00; display: block; font-size: 0.85em; }}
                .prob {{ font-size: 0.65em; color: #444; font-weight: bold; }}
                
                .rank {{ color: #d32f2f; font-size: 0.8em; margin-right: 3px; font-weight: bold; }}
                .debut-badge {{ color: #ffd700; font-weight: bold; font-size: 0.85em; text-shadow: 0 0 5px rgba(255,215,0,0.5); }}
                .vs {{ color: #444; font-size: 0.8em; margin: 0 5px; }}
            </style>
        </head>
        <body>
            <div class="wrapper">
                <h1>UFC Fight Night: London</h1>
                <div class="main-event-title">EVLOEV <span style="color:#444">vs</span> MURPHY</div>
                <div id="timer">00d 00h 00m 00s</div>

                <div class="section-header"><span>Main Card</span><span>Odds / Implied %</span></div>

                <div class="match-row">
                    <div class="fighter-info">
                        <div class="fighter-name"><span class="rank">#1</span>Evloev <span class="vs">vs</span> <span class="rank">#3</span>Murphy</div>
                        <div class="record">19-0 <span class="vs">|</span> 17-0-1</div>
                        <div class="weight-class">Featherweight</div>
                    </div>
                    <div class="odds-container"><div class="odds-box"><span class="price">-218</span><span class="prob">68.6%</span></div><div class="odds-box"><span class="price">+180</span><span class="prob">35.7%</span></div></div>
                </div>

                <div class="match-row">
                    <div class="fighter-info">
                        <div class="fighter-name">Luke Riley <span class="debut-badge">[D]</span> <span class="vs">vs</span> Aswell Jr.</div>
                        <div class="record">10-0 <span class="vs">|</span> 13-1</div>
                        <div class="weight-class">Featherweight</div>
                    </div>
                    <div class="odds-container"><div class="odds-box"><span class="price">-350</span><span class="prob">77.8%</span></div><div class="odds-box"><span class="price">+275</span><span class="prob">26.7%</span></div></div>
                </div>

                <div class="match-row">
                    <div class="fighter-info">
                        <div class="fighter-name"><span class="rank">#14</span>Page <span class="vs">vs</span> Patterson</div>
                        <div class="record">22-3 <span class="vs">|</span> 11-2-1</div>
                        <div class="weight-class">Welterweight</div>
                    </div>
                    <div class="odds-container"><div class="odds-box"><span class="price">-110</span><span class="prob">52.4%</span></div><div class="odds-box"><span class="price">-110</span><span class="prob">52.4%</span></div></div>
                </div>

                <div class="match-row">
                    <div class="fighter-info">
                        <div class="fighter-name">Baraniewski <span class="debut-badge">[D]</span> <span class="vs">vs</span> Lane</div>
                        <div class="record">14-0 <span class="vs">|</span> 13-5</div>
                        <div class="weight-class">Heavyweight</div>
                    </div>
                    <div class="odds-container"><div class="odds-box"><span class="price">-250</span><span class="prob">71.4%</span></div><div class="odds-box"><span class="price">+200</span><span class="prob">33.3%</span></div></div>
                </div>

                <div class="match-row">
                    <div class="fighter-info">
                        <div class="fighter-name"><span class="rank">#11</span>Dolidze <span class="vs">vs</span> Duncan</div>
                        <div class="record">13-3 <span class="vs">|</span> 11-1</div>
                        <div class="weight-class">Middleweight</div>
                    </div>
                    <div class="odds-container"><div class="odds-box"><span class="price">+145</span><span class="prob">40.8%</span></div><div class="odds-box"><span class="price">-175</span><span class="prob">63.6%</span></div></div>
                </div>

                <div class="section-header"><span>Prelims</span><span>Odds / Implied %</span></div>

                <div class="match-row">
                    <div class="fighter-info">
                        <div class="fighter-name">Wood <span class="vs">vs</span> Keita <span class="debut-badge">[D]</span></div>
                        <div class="record">20-6 <span class="vs">|</span> 13-1</div>
                        <div class="weight-class">Featherweight</div>
                    </div>
                    <div class="odds-container"><div class="odds-box"><span class="price">-120</span><span class="prob">54.5%</span></div><div class="odds-box"><span class="price">+100</span><span class="prob">50.0%</span></div></div>
                </div>

                <div class="match-row">
                    <div class="fighter-info">
                        <div class="fighter-name">Kondratavičius <span class="debut-badge">[D]</span> <span class="vs">vs</span> Trocoli</div>
                        <div class="record">6-0 <span class="vs">|</span> 12-4</div>
                        <div class="weight-class">Middleweight</div>
                    </div>
                    <div class="odds-container"><div class="odds-box"><span class="price">-225</span><span class="prob">69.2%</span></div><div class="odds-box"><span class="price">+185</span><span class="prob">35.1%</span></div></div>
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
                }}, 1000);
            </script>
        </body>
    </html>
    """

if __name__ == "__main__":
    # Get the port from Render's environment, or use 5000 as a backup
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)