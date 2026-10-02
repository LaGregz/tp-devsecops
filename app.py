import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def accueil():
    return "Hello, TP DevSecOps !"

# Route volontairement vulnerable (injection de commande) - pour le TP
@app.route("/ping")
def ping():
    hote = request.args.get("host", "")
    # FAILLE : l'entree utilisateur est collee directement dans une commande shell
    resultat = os.popen("ping -c 1 " + hote).read()
    return resultat

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
