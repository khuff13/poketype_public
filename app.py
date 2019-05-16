# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:29:55 2019

@author: krystinsteelman
"""

from flask import Flask, jsonify, request, render_template
import PokeType as PT

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

poke_input = []
realPoke = False
poketype = PT.PokeType()

@app.route('/')
def home():
    return render_template('index.html')

#POST /store data: {name:}
@app.route('/poketype', methods = ['POST'])
def get_poketype():
    request_data = request.get_json()
    poke_input = request_data['poketype'].split()
    realPoke = poketype.check_type(poke_input)
    if realPoke == True:
        return jsonify({'poketype_entered':poketype.poke_type})
    else: return jsonify({'ERROR':'not a poketype'})

@app.route('/poketype/off', methods = ['POST'])
def get_off():
    poketype.get_off()
    poketype.off_list()
    return jsonify({'poketype_entered':poketype.poke_type,
                    'off':poketype.off_list})

@app.route('/poketype/def',methods = ['POST'])
def get_def():
    poketype.get_def()
    poketype.def_list()
    return jsonify({'poketype_entered':poketype.poke_type,
                    'def':poketype.def_list})
    
@app.route('/poketype/offdef', methods = ['POST'])
def get_both():
    poketype.get_off()
    poketype.off_list()
    poketype.get_def()
    poketype.def_list()
    return jsonify({'poketype_entered':poketype.poke_type,
                    'off':poketype.off_list,
                    'def':poketype.def_list})
    
app.run(port = 5000)