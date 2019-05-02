import os
import json
from kafka import KafkaConsumer, KafkaProducer
from arragodb import ArrangoStorage

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
TRANSACTIONS_TOPIC = os.environ.get('TRANSACTIONS_TOPIC')
LEGIT_TOPIC = os.environ.get('LEGIT_TOPIC')
FRAUD_TOPIC = os.environ.get('FRAUD_TOPIC')
ARRANGO_IP = os.environ.get('ARRANGO_IP')
ARRANGO_USER = os.environ.get('ARRANGO_USER')
ARRANGO_PASSWORD = os.environ.get('ARRANGO_ROOT_PASSWORD')
ARRANGO_PORT = os.environ.get('ARRANGO_PORT')
ARRANGO_DB = os.environ.get('ARRANGO_DB')
ARRANGO_COLLECTION = os.environ.get('ARRANGO_COLLECTION')
ARRANGO_PROTOCOL = os.environ.get('ARRANGO_PROTOCOL')


def is_suspicious(transaction: dict) -> bool:
    """Determine whether a transaction is suspicious."""
    return transaction['amount'] >= 901


if __name__ == '__main__':
    #  longtermStorage = ArrangoStorage(ARRANGO_PROTOCOL, ARRANGO_IP, ARRANGO_PORT, ARRANGO_USER, ARRANGO_PASSWORD,
    #                                  ARRANGO_DB, ARRANGO_COLLECTION)
    # database = longtermStorage.connect()
    consumer = KafkaConsumer(
        TRANSACTIONS_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        value_deserializer=lambda value: json.loads(value),
    )
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    for message in consumer:
        transaction: dict = message.value
        topic = FRAUD_TOPIC if is_suspicious(transaction) else LEGIT_TOPIC
        producer.send(topic, value=transaction)

        # longtermStorage.store(database, message)

        print(topic, transaction)  # DEBUG
