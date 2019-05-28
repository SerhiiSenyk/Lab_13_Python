from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://serhii:pass@localhost/lab13'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class StationeryKnife(db.Model):

    __tablename__ = 'StationeryKnife'

    id = db.Column(db.Integer, primary_key=True)
    price =  db.Column(db.Integer)
    weight = db.Column(db.Integer)
    producer = db.Column(db.String(80))
    material = db.Column(db.String(80))
    width_of_blade =  db.Column(db.Integer)
    def __init__(self, price = 0, weight = 0, producer =  None, material = None, width_of_blade = 0):
        self.price = price
        self.weight = weight
        self.producer = producer
        self.material = material
        self.width_of_blade = width_of_blade

    def __str__(self):
        return "\tPrice :\t" + str(self.price) + "\n" +\
            "\tWeight :\t" + str(self.weight) + "\n" +\
            "\tProducer :\t" + str(self.producer) + "\n" +\
            "\tMaterial :\t" + str(self.material) + "\n" +\
            "\twidth_of_blade:\t" + str(self.width_of_blade)

class StationeryKnifeSchema(ma.Schema):
    class Meta:
        fields = ('price', 'weight', 'producer', 'material', 'width_of_blade') 

stationery_knife_schema = StationeryKnifeSchema()
stationery_knifes_schema = StationeryKnifeSchema(many = True)
db.create_all()

#POST
@app.route("/knife", methods = ['POST'])
def add_stationery_knife():
    price = request.get_json()['price']
    weight = request.get_json()['weight']
    producer = request.get_json()['producer']
    material = request.get_json()['material']
    width_of_blade = request.get_json()['width_of_blade']

    new_stationery_knife = StationeryKnife(price,
                                           weight,
                                           producer,
                                           material,
                                           width_of_blade)
    db.session.add(new_stationery_knife)
    db.session.commit()
    return stationery_knife_schema.jsonify(new_stationery_knife)

#GET
@app.route("/knife", methods = ["GET"])# +
def get_stationery_knifes():
    all_stationery_knifes = StationeryKnife.query.all()
    result = stationery_knifes_schema.dump(all_stationery_knifes)
    return jsonify(result)

#GET
@app.route("/knife/<id>", methods = ["GET"])# +
def get_stationery_knifes_by_id(id):
    stationery_knife = StationeryKnife.query.get(id)
    return stationery_knife_schema.jsonify(stationery_knife)

@app.route("/knife/<id>", methods = ["PUT"])# +
def stationery_knife_update(id):
    stationery_knife = StationeryKnife.query.get(id)

    stationery_knife.price = request.json['price']
    stationery_knife.weight = request.json['weight']
    stationery_knife.producer = request.json['producer']
    stationery_knife.material = request.json['material']
    stationery_knife.width_of_blade = request.json['width_of_blade']
    db.session.commit()
    return stationery_knife_schema.jsonify(stationery_knife)


@app.route("/knife/<id>", methods = ["DELETE"])# +
def stationery_knife_delete(id):
    stationery_knife = StationeryKnife.query.get(id)
    db.session.delete(stationery_knife)
    db.session.commit()

    return stationery_knife_schema.jsonify(stationery_knife)

if __name__ == '__main__':
    app.run(debug = True)

