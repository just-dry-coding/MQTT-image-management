# MQTT Publisher Android App
Simple Android App which allows publishing images taken with phone directly to MQTT Broker

## MIT APP INVENTOR Development
App developed [MIT APP INVENTOR](https://appinventor.mit.edu/)
App code can be viewed by importing .aia file into MIT APP INVENTOR

## About the App
First screen allows to specify MQTT Topic to which images will be published on hivemq broker.
Second screen allows to take and send multiple images to the specified topic

### Sent Msgs
The Msgs sent consist of a dictionary containing two entries:
{
    {"name": "<filename_with_extension>"},
    {"data": "<base64_encoded_image_data>"}
}

### Current State
The App can only be seen as a prototype which lacks functionality, style and safety!

Crashes when sending image! need to investigate 