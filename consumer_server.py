import asyncio

from confluent_kafka import Consumer
from confluent_kafka.admin import AdminClient, NewTopic

BROKER_URL = 'PLAINTEXT://localhost:9092'
N_MESSAGE = 5
TIMEOUT = 1.0
TOPIC_NAME = 'com.udacity.dep.police.service'
GROUP_ID = '0'

async def consume(topic_name):
    consumer = Consumer({
        'bootstrap.servers': BROKER_URL,
        'group.id': GROUP_ID,
    })
    
    consumer.subscribe([topic_name])
    
    while True:
        messages = consumer.consume(N_MESSAGE, timeout=TIMEOUT)
        
        for message in messages:
            if message is None:
                print('Message not found')
            elif message.error() is not None:
                print(f'Error: {message.error()}')
            else:
                print(f'{message.value()}\n')
                
        await asyncio.sleep(TIMEOUT)
                
def run_consumer():
    try:
        asyncio.run(consume(TOPIC_NAME))
        
    except KeyboardInterrupt as e:
        print("Shutting down...")
        
if __name__ == '__main__':
    run_consumer()