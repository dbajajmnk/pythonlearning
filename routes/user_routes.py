from flask import Blueprint, request, jsonify
from models.user import User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['POST'])
def add_user():
    data = request.json
    User.create(data)
    return jsonify({"message": "User added successfully"}), 201

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = User.get_all()
    return jsonify(users), 200

@user_routes.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    result = User.update(user_id, data)
    if result.modified_count:
        return jsonify({"message": "User updated successfully"}), 200
    return jsonify({"message": "User not found"}), 404

@user_routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = User.delete(user_id)
    if result.deleted_count:
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "User not found"}), 404
