'''
Created on 9 nov. 2020

@author: Amalio
'''

import flask

from flask import request, jsonify
from api.appflask.ApiController import ApiController

app = flask.Flask(__name__)
app.config["DEBUG"] = True
controller=None

@app.route('/', methods=['GET'])
def api_home():
    return controller.home()

@app.route('/recommend', methods=['GET'])
def api_recommend():
    if 'id' in request.args:
        idCliente = str(request.args['id'])
        out= jsonify(controller.recommend(idCliente))
    else:
        out= "Error: No id field provided. Please specify an id."
    
    return out



def run(c):
    controller=c
    app.run()



if __name__ == '__main__':
    controller=ApiController()
    run(controller)
    pass