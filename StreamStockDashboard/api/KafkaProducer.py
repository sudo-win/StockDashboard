import finnhub
from confluent_kafka import Producer
import socket

from confluent_kafka.admin import AdminClient, ClusterMetadata

finnhub_client = finnhub.Client(api_key="")

# print(finnhub_client.quote('AAPL'))

conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}

producer = Producer(conf)
# print(producer.__bool__())
adminClient = AdminClient({'bootstrap.servers': "localhost:9092"})
print('before admin')

x = adminClient.list_topics(timeout=10).topics.keys()


print(x)

# y = adminClient.describe_configs()
# print(y)


