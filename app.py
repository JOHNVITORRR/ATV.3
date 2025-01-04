from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def primeira_pagina():
    return render_template('inicio.html')

@app.route('/imc', methods = ["get"])
def segunda_pagina():
    nome = request.args.get("nome")
    altura = float(request.args.get("altura"))
    peso = float(request.args.get("peso"))
    imc = round((peso/altura**2),2)
    return render_template("imc.html", nomeusuario = nome, imcusuario = imc)