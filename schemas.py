device_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "deviceModel": {"type": "string"},
        "name": {"type": "string"},
        "node": {"type": "string"},
        "serial": {"type": "string"}
    },
    "required": ["id", "deviceModel", "name", "node", "serial"]
}