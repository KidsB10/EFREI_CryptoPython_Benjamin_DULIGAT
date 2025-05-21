from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')  # Page d'accueil

# Chiffrement avec clé utilisateur
@app.route('/encrypt/<key>/<valeur>')
def encryptage(key, valeur):
    try:
        f = Fernet(key.encode())
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur lors du chiffrement : {str(e)}"

# Déchiffrement avec clé utilisateur
@app.route('/decrypt/<key>/<valeur>')
def decryptage(key, valeur):
    try:
        f = Fernet(key.encode())
        valeur_bytes = valeur.encode()
        valeur_decryptee = f.decrypt(valeur_bytes)
        return f"Valeur décryptée : {valeur_decryptee.decode()}"
    except InvalidToken:
        return "Clé incorrecte ou token invalide !"
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
