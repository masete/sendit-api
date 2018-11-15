from flask import Blueprint, jsonify, request
from api.models.models import Parcel, parcel_orders , Users, users_list
from api.validations import empty_order_fields, invalid_input_types, empty_strings_add_weight
from api.Handlers.error_handlers import InvalidUsage
import uuid


parcel_blueprint = Blueprint("parcel", __name__)
user_blueprint = Blueprint("user", __name__)


@user_blueprint.route('/api/auth/signup', methods=['POST'], strict_slashes=False)
def signup():
    data = request.get_json()
    user_id = uuid.uuid4()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    signup_data = Users(user_id, username, password, email)

    users_list.append(signup_data.to_dict())
    return jsonify({"message": "user added"})


@user_blueprint.route('/api/auth/login', methods=['POST'], strict_slashes=False)
def login():

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    for user in users_list:
        if not user['username'] == username:
            return jsonify({"message": "wrong username"})
        if not user['password'] == password:
            return jsonify({"message": "wrong password"})

    return jsonify({"message": "you are now logged in"})


@parcel_blueprint.route('/api/v1/parcel', methods=['POST'], strict_slashes=False)
def create_parcel():

    if request.content_type != "application/json":
        raise InvalidUsage("Invalid content type", 400)
    data = request.get_json()
    parcel_id = len(parcel_orders) + 1
    parcel_location = data.get('parcel_location')
    parcel_destination = data.get('parcel_destination')
    parcel_weight = data.get('parcel_weight')
    parcel_description = data.get('parcel_description')
    user_id = data.get('user_id')
    status = data.get('status')

    val = empty_order_fields(parcel_location, parcel_destination, parcel_weight, parcel_description, user_id, status)
    if val:
        raise InvalidUsage(val, 400)
    input_type = invalid_input_types(parcel_location, parcel_destination, parcel_weight, parcel_description, user_id, status)
    if input_type:
        raise InvalidUsage(input_type, 400)
    empty_strings = empty_strings_add_weight(parcel_location, parcel_destination, parcel_weight, parcel_description, user_id, status)
    if empty_strings:
        raise InvalidUsage(empty_strings, 400)

    order = Parcel(parcel_id, parcel_location, parcel_destination, parcel_weight, parcel_description, user_id, status)
    parcel_orders.append(order.to_dict() )
    return jsonify({"message": "parcel successfully added ", "parcel": order.to_dict()}), 201


@parcel_blueprint.route('/api/v1/parcel', methods=['GET'], strict_slashes=False)
def get_all_parcel():
    if not parcel_orders:
        return jsonify({"message": "List is empty first post"})
    return jsonify({"parcels": parcel_orders})


@parcel_blueprint.route('/api/v1/parcel/<int:parcel_id>', methods=['GET'], strict_slashes=False)
def get_single_parcel(parcel_id):
    for order in parcel_orders:
        if order['parcel_id'] == parcel_id:
            return jsonify({"message": "your request is successfull", "data": order}), 200
    return jsonify({"message": "there is no parcel requested for"}), 400


@parcel_blueprint.route('/api/v1/parcel/<int:parcel_id>/cancel', methods=['PUT'], strict_slashes=False)
def cancel_parcel(parcel_id):
    for order in parcel_orders:
        if order['parcel_id'] == parcel_id:
            order['status'] = 'cancelled'
            return jsonify(order), 200
    return jsonify({"message": "the parcel does not exist"}), 400


@parcel_blueprint.route('/api/v1/users/<int:user_id>/parcel', methods=['GET'], strict_slashes=False)
def get_parcel_by_user_id(user_id):
    single = []
    for order in parcel_orders:
        if order['user_id'] == user_id:
            single.append(order)

    if len(single) > 0:
        return jsonify(single), 200
    return jsonify({"message": "there is no such user"}), 400


@parcel_blueprint.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
