from app import app
from app.controllers.area_controller import AreaController 

@app.route('/areas',methods=['GET'])
def areasALL():
    #validaciones
    #obtener datos del QueryParams/PathParam o BodyRequest
    controller = AreaController()
    return controller.all()