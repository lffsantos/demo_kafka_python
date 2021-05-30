import json
import logging

from kafka import KafkaConsumer

consumer = KafkaConsumer('my-topic', group_id='my-group',  group_id='my-group',  group_id='my-group', bootstrap_servers=['localhost:9092'])

print("starting the consumer")
for msg in consumer:
    logging.info("read msg = {}".format(json.loads(msg.value)))
    print("read msg = {}".format(json.loads(msg.value)))
