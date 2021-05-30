# https://kafka-python.readthedocs.io/en/master/usage.html
import logging
import uuid

from kafka import KafkaProducer

from apps.core.correlation_id import CorrelationId
from apps.core.message import Message
from apps.core.serializer import MessageSerializer


class KafkaDispatcher:
    producer = None

    def __init__(self):
        self.producer = KafkaProducer(**self.properties())

    def send(self, topic: str, key: str, correlation_id: CorrelationId, payload):
        self.sendAsync(topic, key, correlation_id, payload)
        self.producer.flush()

    def sendAsync(self, topic: str, key: str, correlation_id: CorrelationId, payload):
        def on_send_success(record_metadata):
            print(
                f'topic={record_metadata.topic}'
                f':: partition={record_metadata.partition}'
                f':: offset={record_metadata.offset}')

        def on_send_error(excp):
            logging.error('I am an errback', exc_info=excp)
            # handle exception

        value = Message(correlation_id.continue_with(f"_{topic}"), payload)
        self.producer.send(topic, key=key, value=value).add_callback(
            on_send_success).add_errback(
            on_send_error)

    @staticmethod
    def properties():
        conf = {
            'bootstrap_servers': "127.0.0.1:9092",
            'key_serializer': str.encode,
            'value_serializer': lambda v: MessageSerializer.serialize(v),
            'client_id': str(uuid.uuid4()),
            'acks': 'all'

        }
        return conf


# teste
if __name__ == '__main__':
    dispatcher = KafkaDispatcher()
    dispatcher.send('meu-tpoicssp', b'testwqqdsdsqqe', {})
