from flask import Flask, request, jsonify
from flask import app, jsonify, request
from database import read_device, write_device
import jsonschema
from jsonschema import validate

from schemas import device_schema

app = Flask(__name__)


@app.route('/devices', methods=['POST'])
def create_device():
    data = request.get_json()
    try:
        validate(instance=data, schema=device_schema)
        response = write_device(Item=data)
        return jsonify({"message": "Device created successfully"}), 201
    except jsonschema.exceptions.ValidationError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/devices/<string:id>', methods=['GET'])
def read_device(id):
    try:
        response = read_device(Key={'id': id})
        if 'Item' in response:
            return jsonify(response['Item']), 200
        else:
            return jsonify({"message": "Device not found"}), 404
    except Exception as e:
        print(str(e))
        return jsonify({"error": 'error occured'}), 500

