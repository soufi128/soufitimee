from flask import render_template
from app import app
from flask import request
from .scripts.calculs import *
from .scripts.imagenes import *

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/calculs', methods=['POST'])
def calc():
    Algebra_240011=request.form['AL']
    Info_240015=request.form['FI']
    Quimica1_240014=request.form['Q1']
    Calcul1_240012=request.form['C1']
    Mecfon_240013=request.form['MF']
    Expre_240025=request.form['EG']
    Termo_240023=request.form['TF']
    Quimica2_240024=request.form['Q2']
    Calcul2_240022=request.form['C2']
    Geo_240021=request.form['GEO']
    d = {'240011': [float(Algebra_240011)],'240012':[float(Calcul1_240012)],'240013':[float(Mecfon_240013)],'240014':[float(Quimica1_240014)],'240015':[float(Info_240015)],'240021':[float(Geo_240021)],'240022':[float(Calcul2_240022)],'240023':[float(Termo_240023)],'240024':[float(Quimica2_240024)],'240025':[float(Expre_240025)]}
    print(d)
    s = calcular(d)
    print(s) 
    v=imatges(s)
    return render_template('calculs.html',title='quatris total',resultat=str(s),imatge=str(v))