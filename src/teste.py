import json
import logging

from kafka import KafkaConsumer, KafkaProducer

TOPIC_NEW_ORDER = 'ECOMMERCE_NEW_ORDER'
BROKER_URL = 'localhost:9092'


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(bootstrap_servers=BROKER_URL, key_serializer=json_serializer, value_serializer=json_serializer)


class NewOrderMain:

    def execute_order(self, key, message):
        producer.send(TOPIC_NEW_ORDER, key, message).get()
        logging.info('pedido enviado com sucesso!')
        print('pedido enviado com sucesso!')
        # producer.flush()
    

class FraudeDetector:

    def run(self):
        self.consumer = KafkaConsumer(TOPIC_NEW_ORDER, bootstrap_servers=BROKER_URL, auto_offset_reset='earliest',group_id="fraude-detector1")
        print("starting the consumer")
        for msg in self.consumer:
            logging.info("read msg = {}".format(json.loads(msg.value)))
            print("read msg = {}".format(json.loads(msg.value)))



if __name__ == '__main__':
    order = NewOrderMain()
    order.execute_order('teste1x1', 'teste2xaaa1')
    fraude = FraudeDetector()
    fraude.run()
    # producer = KafkaProducer(bootstrap_servers='localhost:9092')
    # for _ in range(5):
    #     producer.send('foobar', b'some_message_bytes')
    #     producer.flush()    