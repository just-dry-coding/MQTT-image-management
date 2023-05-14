# MQTT-image-management
Take images with android device, store them in a database and manage them via a html gui frontend.

## Basic Components
![basic design](./resources/basic_design.svg)
1. MQTT-image-publisher: android app which allows taking images and sending them to MQTT broker (publisher)
2. MQTT-image-database-server: receives images and stores them in database(subscriber)
3. database: MongoDB stores images using GridFS 
4. image-management-server: API server that allows fetching the images from the database as well as deleting and editing them
5. image_management_ui: frontend for managing and displaying stored images

## Assignments/Workflows
1. user takes photo and saves image to database using mqtt client
2. user views, gets, modifies and deltes the images in the database using a web frontend

## How to setup and run
1. follow instructions to build and run android app [instructions]([MQTT-image-publisher/README.md](https://github.com/just-dry-coding/MQTT-image-publisher/blob/main/README.md))
2. run `npm install` in image_management_ui directory
3. setup venv
   1. `python -m venv venv`
   2. `./venv/Scripts/activate`
   3. `pip install -r requirements.txt`
4. add MongoDB connection string to environment
   1. setup MongoDB or use free online provider: https://www.mongodb.com/docs/atlas/getting-started/
   2. set TEST_DATABASE_CONNECTION_STRING=<your-mongo-connection-string> environment variable on your platform
5. start all the servers with right attributes
   1. adapt config inside `./src/server_runner.py` to match your setup (or keep default)
   2. run `python ./src/server_runner.py`