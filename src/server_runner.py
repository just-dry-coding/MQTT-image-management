# quick and dirty solution fix later
import sys  # noqa
from os import environ, path  # noqa

current_dir = path.dirname(path.abspath(__file__))  # noqa
sys.path.append(path.join(current_dir, '../MQTT-image-database-server/src'))  # noqa

import json
from os import environ
from image_database_server import ImageDataBaseServer


connection_string = environ.get('TEST_DATABASE_CONNECTION_STRING')

config = '{ \
            "mqtt_subscriber":{ \
                "broker_url": "broker.hivemq.com", \
                "broker_port": 1883, \
                "topic": "one/unique/nice/test/topic" \
            }, \
            "mongo_handler":{ \
                "connection_string": "", \
                "database": "test", \
                "collection": "test" \
            } \
        }'


json_config = json.loads(config)
json_config['mongo_handler']['connection_string'] = connection_string
img_database_server = ImageDataBaseServer(json_config)
img_database_server.run()
while True:
    try:
        pass
    except KeyboardInterrupt:
        break
