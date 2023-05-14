# quick and dirty solution fix later
import sys
from os import environ, path

current_dir = path.dirname(path.abspath(__file__))  # noqa
parent_dir = path.dirname(current_dir)  # noqa
sys.path.append(path.join(parent_dir, 'MQTT-image-database-server/src'))  # noqa
sys.path.append(path.join(parent_dir, 'image-management-server/src'))  # noqa

import json
import uvicorn
import subprocess

from image_database_server import ImageDataBaseServer


connection_string = environ.get('TEST_DATABASE_CONNECTION_STRING')

config = json.loads(
    '{ \
            "mqtt_subscriber":{ \
                "broker_url": "broker.hivemq.com", \
                "broker_port": 1883, \
                "topic": "my/super/test/unique/topic" \
            }, \
            "mongo_handler":{ \
                "connection_string": "", \
                "database": "test", \
                "collection": "test" \
            } \
        }')


sys.argv = ['_', connection_string, config['mongo_handler']
            ['database'], config['mongo_handler']['collection']]

from image_management_server import app  # noqa


try:
    print("starting frontend")
    UIprocess = subprocess.Popen(['npm', 'run', 'start'], start_new_session=True, shell=True, cwd=path.join(
        parent_dir, 'image_management_ui'))
except subprocess.CalledProcessError as e:
    print(f"Error starting npm server: {e}")

config['mongo_handler']['connection_string'] = connection_string
img_database_server = ImageDataBaseServer(config)
print("starting database server")
img_database_server.run()
print("starting API server")
uvicorn.run(app, host="0.0.0.0", port=8000)

# todo: kill processes gracefully
while True:
    try:
        pass
    except KeyboardInterrupt:
        UIprocess.kill()
        sys.exit(0)
