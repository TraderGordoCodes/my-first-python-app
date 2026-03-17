from flask import Flask, render_template
from scraper import get_ufc_data  # Importing your new file

app = Flask(__name__)

@app.route("/")
def home():
    # 1. The Target URL (Official UFC London Event Page)
    url = "https://www.ufc.com/event/ufc-fight-night-march-21-2026"
    
    # 2. Call the scraper to get the live 14-fight card
    # We use a try/except block so the site doesn't crash if the UFC site is down
    try:
        fights = get_ufc_data(url)
    except Exception as e:
        print(f"Scraper Error: {e}")
        fights = [] # Fallback to empty list

    # 3. Split the fights for your side-by-side layout
    # Assuming 6 Main Card fights and 8 Prelims
    main_card = fights[:6]
    prelims = fights[6:]

    return render_template("index.html", main_card=main_card, prelims=prelims)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    # Get the port from Render's environment, or use 5000 as a backup
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)