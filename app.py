import re
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def accueil():
    return "Hello, TP DevSecOps !"

@app.route("/ping")
def ping():
    hote = request.args.get("host", "")
    # 1) On VALIDE l'entree : uniquement lettres, chiffres, points et tirets
    if not re.fullmatch(r"[A-Za-z0-9.-]+", hote):
        return "Hote invalide", 400
    # 2) subprocess.run avec une LISTE d'arguments, sans shell -> injection impossible
    resultat = subprocess.run(
        ["ping", "-c", "1", hote],
        capture_output=True, text=True, timeout=5
    )
    return resultat.stdout

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
