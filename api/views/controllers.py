from flask import Blueprint, jsonify, request
from api.models.models import Parcel
from api.validations import empty_order_fields, invalid_input_types, empty_strings_add_weight
from api.Handlers.error_handlers import InvalidUsage

parcel_blueprint = Blueprint("parcel", __name__)


@parcel_blueprint.route('/api/v1/parcel', methods=['POST'], strict_slashes=False)
def create_parcel():
    if request.content_type != "application/json":
        raise InvalidUsage("Invalid content type..--...gkjljlkjlkj.", 400)
    data = request.get_json()
    parcel_id = len(Parcel.parcel_orders) + 1
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
    Parcel.parcel_orders.append(order.to_dict() )
    return jsonify({"message": "parcel successfully added ", "data": order.to_dict()}), 201