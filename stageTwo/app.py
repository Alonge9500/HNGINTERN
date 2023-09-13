from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///details.db'

db = SQLAlchemy(app)
migrate = Migrate(app,db)


class Person(db.Model):
    
    id =db.Column(db.Integer, primary_key = True)
    name =db.Column(db.String(100), nullable=False)
    age =db.Column(db.Integer)
    gender =db.Column(db.String(6))
    
@app.route('/person', methods=['POST'])
def create():
    details = request.get_json()
    if details:
        with app.app_context():
            new = Person(name=details['name'], age=details['age'], gender=details['gender'])
            db.session.add(new)
            db.session.commit()
        
        return jsonify({
            'report': 'Successful'
        })
    else:
        return jsonify({
            'report': 'Unsuccessful'
        })

@app.route('/person/<name>', methods=['PUT'])
def update(name):
    details = request.get_json()
    with app.app_context():
        per = Person.query.filter_by(name=name).first()
        person = Person.query.filter_by(id = per.id).first()
        
    if person:
        if 'name' in details and details['name'] != name:
            person.name = details['name']

        person.age = details['age']
        person.gender = details['gender']

        db.session.commit()
        return jsonify({
            'report': 'Update successful',
            'code': 200,
            'updated_person': {
                'name': person.name,
                'age': person.age,
                'gender': person.gender
            }
            })
       
    else:
        return jsonify({
            'report': 'User Not Found',
            'code': 404
        })


@app.route('/person/<name>', methods=['GET'])
def read(name):
    with app.app_context():
        person = Person.query.filter_by(name=name).first()
    if person:
        
        return jsonify({
            'name':person.name,
            'age':person.age,
            'gender':person.gender
        
        })
    else:
        return jsonify({
            'report':'User Not Found'
            })
    
        
@app.route('/person/<name>', methods=['DELETE'])
def delete(name):
    with app.app_context():
        person = Person.query.filter_by(name=name).first()
    if person:
        db.session.delete(person)
        db.session.commit()
        
        return jsonify({
            'report':'Delete successful',
            'code':200
        })
    else:
        return jsonify({
            'report':'User Not Found',
            'code':404
            })
        
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
    