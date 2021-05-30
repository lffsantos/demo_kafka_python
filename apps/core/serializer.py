import json

from apps.core.message import Message


class MessageSerializer:

    @staticmethod
    def serialize(msg):
        content = {
            'payload': msg.payload.serialize(),
            'correlationId': msg.id.__dict__,
            'type': 'payload.ge'
        }
        return json.dumps(content).encode()

    @staticmethod
    def deserialize(msg):
        msg = json.loads(msg.decode())
        return Message(msg['correlationId'], msg['payload'])
