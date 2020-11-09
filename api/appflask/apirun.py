'''
Created on 9 nov. 2020

@author: Amalio
'''

import flaskfrom . import ApiController
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
controller=None

@app.route('/', methods=['GET'])
def api_home():
    return controller.home()

@app.route('/recommend', methods=['GET'])
def api_recommend():
    if 'id' in request.args:
        id = int(request.args['id'])
        out= jsonify(controller.recommend(id))
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