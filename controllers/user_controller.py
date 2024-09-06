# controllers/user_controller.py
from flask import request, jsonify
from models.user import User, db

def create_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'error': 'Name, email, and password are required'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists'}), 409

    new_user = User(name=name, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'id': new_user.id, 'name': new_user.name, 'email': new_user.email}), 201
