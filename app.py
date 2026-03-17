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
            <title>UFC London: Scout & Arb Tracker</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{ font-family: 'Segoe UI', sans-serif; background-color: #0a0a0a; color: #fff; margin: 0; padding: 15px; }}
                h1 {{ font-size: 0.9em; color: #666; letter-spacing: 4px; text-align: center; text-transform: uppercase; }}
                .main-event-title {{ font-size: 1.8em; text-align: center; font-weight: 900; margin: 10px 0; }}
                #timer {{ text-align: center; font-size: 2.5em; color: #d32f2f; margin-bottom: 30px; font-family: monospace; }}
                
                /* Layout Container */
                .card-container {{ display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; }}
                .card-column {{ flex: 1; min-width: 320px; max-width: 500px; }}
                
                .section-header {{ background: #1a1a1a; color: #eee; padding: 10px 15px; font-size: 0.8em; font-weight: bold; margin-top: 10px; border-left: 4px solid #d32f2f; text-transform: uppercase; }}
                .match-row {{ background: #141414; padding: 12px; border-bottom: 1px solid #222; display: flex; align-items: center; justify-content: space-between; }}
                
                .fighter-info {{ flex: 2; }}
                .fighter-name {{ font-weight: bold; font-size: 0.9em; }}
                .record {{ font-size: 0.75em; color: #666; }}
                .weight {{ font-size: 0.65em; color: #d32f2f; text-transform: uppercase; }}
                
                .odds-container {{ flex: 1; display: flex; justify-content: flex-end; gap: 5px; }}
                .price {{ background: #222; padding: 4px 6px; border-radius: 4px; font-weight: bold; color: #ffcc00; font-size: 0.8em; min-width: 45px; text-align: center; }}
                
                .rank {{ color: #d32f2f; font-weight: bold; }}
                .debut {{ color: #ffd700; font-weight: bold; text-shadow: 0 0 5px rgba(255,215,0,0.5); font-size: 0.8em; }}
                .vs {{ color: #444; margin: 0 5px; }}
            </style>
        </head>
        <body>
            <h1>UFC Fight Night: London</h1>
            <div class="main-event-title">EVLOEV <span style="color:#444">vs</span> MURPHY</div>
            <div id="timer">00d 00h 00m 00s</div>

            <div class="card-container">
                <div class="card-column">
                    <div class="section-header">Main Card</div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name"><span class="rank">#1</span> Evloev <span class="vs">vs</span> <span class="rank">#3</span> Murphy</div>
                            <div class="record">19-0 <span class="vs">|</span> 17-0-1</div>
                            <div class="weight">Featherweight</div>
                        </div>
                        <div class="odds-container"><span class="price">-218</span><span class="price">+180</span></div>
                    </div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name">Luke Riley <span class="debut">[D]</span> <span class="vs">vs</span> Aswell Jr.</div>
                            <div class="record">10-0 <span class="vs">|</span> 13-1</div>
                            <div class="weight">Featherweight</div>
                        </div>
                        <div class="odds-container"><span class="price">-350</span><span class="price">+275</span></div>
                    </div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name"><span class="rank">#14</span> Page <span class="vs">vs</span> Patterson</div>
                            <div class="record">22-3 <span class="vs">|</span> 11-2-1</div>
                            <div class="weight">Welterweight</div>
                        </div>
                        <div class="odds-container"><span class="price">-110</span><span class="price">-110</span></div>
                    </div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name">Iwo Baraniewski <span class="debut">[D]</span> <span class="vs">vs</span> Austen Lane</div>
                            <div class="record">14-0 <span class="vs">|</span> 13-5</div>
                            <div class="weight">Light Heavyweight</div>
                        </div>
                        <div class="odds-container"><span class="price">-250</span><span class="price">+200</span></div>
                    </div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name"><span class="rank">#11</span> Dolidze <span class="vs">vs</span> Duncan</div>
                            <div class="record">13-3 <span class="vs">|</span> 11-1</div>
                            <div class="weight">Middleweight</div>
                        </div>
                        <div class="odds-container"><span class="price">+145</span><span class="price">-175</span></div>
                    </div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name">Kurtis Campbell <span class="debut">[D]</span> <span class="vs">vs</span> Danny Silva</div>
                            <div class="record">8-0 <span class="vs">|</span> 11-2</div>
                            <div class="weight">Featherweight</div>
                        </div>
                        <div class="odds-container"><span class="price">-150</span><span class="price">+125</span></div>
                    </div>
                </div>

                <div class="card-column">
                    <div class="section-header">Prelims</div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name">Mason Jones <span class="vs">vs</span> Axel Sola</div>
                            <div class="record">14-2 <span class="vs">|</span> 8-0</div>
                            <div class="weight">Lightweight</div>
                        </div>
                        <div class="odds-container"><span class="price">-180</span><span class="price">+150</span></div>
                    </div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name">Wood <span class="vs">vs</span> Keita <span class="debut">[D]</span></div>
                            <div class="record">20-6 <span class="vs">|</span> 13-1</div>
                            <div class="weight">Featherweight</div>
                        </div>
                        <div class="odds-container"><span class="price">-120</span><span class="price">+100</span></div>
                    </div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name">Louie Sutherland <span class="vs">vs</span> Brando Peričić</div>
                            <div class="record">7-2 <span class="vs">|</span> 6-0</div>
                            <div class="weight">Heavyweight</div>
                        </div>
                        <div class="odds-container"><span class="price">-140</span><span class="price">+115</span></div>
                    </div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name">Kondratavičius <span class="debut">[D]</span> <span class="vs">vs</span> Trócoli</div>
                            <div class="record">6-0 <span class="vs">|</span> 12-4</div>
                            <div class="weight">Middleweight</div>
                        </div>
                        <div class="odds-container"><span class="price">-225</span><span class="price">+185</span></div>
                    </div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name"><span class="rank">#15</span> Mario Pinto <span class="vs">vs</span> Felipe Franco <span class="debut">[D]</span></div>
                            <div class="record">9-0 <span class="vs">|</span> 8-0</div>
                            <div class="weight">Heavyweight</div>
                        </div>
                        <div class="odds-container"><span class="price">-200</span><span class="price">+165</span></div>
                    </div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name">Shem Rock <span class="vs">vs</span> Al-Selwady</div>
                            <div class="record">10-1-1 <span class="vs">|</span> 15-2</div>
                            <div class="weight">Lightweight</div>
                        </div>
                        <div class="odds-container"><span class="price">+110</span><span class="price">-135</span></div>
                    </div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name">Shanelle Dyer <span class="debut">[D]</span> <span class="vs">vs</span> Oliveira</div>
                            <div class="record">5-0 <span class="vs">|</span> 7-2</div>
                            <div class="weight">Strawweight</div>
                        </div>
                        <div class="odds-container"><span class="price">-300</span><span class="price">+240</span></div>
                    </div>
                    <div class="match-row">
                        <div class="fighter-info">
                            <div class="fighter-name">Melissa Mullins <span class="vs">vs</span> Luana Carolina</div>
                            <div class="record">6-1 <span class="vs">|</span> 10-5</div>
                            <div class="weight">Bantamweight</div>
                        </div>
                        <div class="odds-container"><span class="price">-115</span><span class="price">-105</span></div>
                    </div>
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