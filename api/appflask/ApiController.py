'''
Created on 9 nov. 2020

@author: Amalio
'''
from modelo.recomender.recommendQuerys import Recomendations
class ApiController(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def recommend(self, idCliente, limit=10):
        
        recs=Recomendations()
        out=recs.descubrirArticulos(idCliente, limit)
        
        o2=out['articuloR']
        str = [s.strip().replace('\ufffd', " ") for s in o2]
        
        return str
        
    def home(self):
        salida="<h1>Bienvenido al sistema recomendador</h1>"
        salida=salida+"<p>Escriba en la URL -> http://127.0.0.1:5000/recommend?id=1248 para recomendar</p>"
        return salida
if __name__ == '__main__':
    controller=ApiController()
    controller.recommend('1248')
    pass        