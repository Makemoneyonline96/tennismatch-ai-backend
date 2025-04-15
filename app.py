from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze")
def analyze():
    match = request.args.get("match", "").lower()

    if "bautista" in match and "zandschulp" in match:
        prediction = "Bautista Agut 55% - van de Zandschulp 45%"
        analysis = (
            "Bautista Agut zeigt eine stabile Sandform, van de Zandschulp ist gefährlich – "
            "aber inkonstant. Leichter Vorteil für den Spanier."
        )
    else:
        prediction = "Matchdaten nicht verfügbar"
        analysis = "Bitte gib ein bekanntes Match ein."

    return jsonify({
        "prediction": prediction,
        "analysis": analysis
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
