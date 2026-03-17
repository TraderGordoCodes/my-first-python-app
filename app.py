from flask import Flask, render_template
from scraper import get_ufc_data

app = Flask(__name__)

@app.route("/")
def home():
    fights = get_ufc_data()
    
    # If the scraper finds 14 fights, we take the top 6 as the Main Card
    # If it fails, we provide a fallback so the page isn't blank
    if not fights:
        return "<h1>Data temporarily unavailable. Please refresh in a moment.</h1>"

    main_card = fights[:6]
    prelims = fights[6:]

    return render_template("index.html", main_card=main_card, prelims=prelims)

if __name__ == "__main__":
    # Get the port from Render's environment, or use 5000 as a backup
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)