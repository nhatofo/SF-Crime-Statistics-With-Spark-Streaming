import producer_server

TOPIC_NAME = 'com.udacity.dep.police.service'
SERVER_URL = 'localhost:9092'
CLIENT_ID = 'com.udacity.dep.police.broker'

def run_kafka_server():
    
    input_file = "./police-department-calls-for-service.json"

    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic=TOPIC_NAME,
        bootstrap_servers=SERVER_URL,
        client_id = CLIENT_ID
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()