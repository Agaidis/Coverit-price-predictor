from flask import Blueprint, request, jsonify
from .model.estimator import predict_price
import logging

main = Blueprint('main', __name__)

@main.route('/estimate', methods=['POST'])
def estimate():
    data = request.get_json()
    logging.info(f"Prediction request: {data}")
    prediction = predict_price(data)
    return jsonify({"estimated_cost": prediction})