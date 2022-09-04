from flask import render_template , jsonify
from app.models.area_model import AreaModel


class AreaController:
    #Si deseas usar un template
    # def all(self):
    #     records=AreaModel.query.all()#SELECT*FROM area
    #     # return records
    #     return render_template('areas.html', areas=records)

      def all(self):
        records=AreaModel.query.all()#SELECT*FROM area
        return jsonify(records),200
