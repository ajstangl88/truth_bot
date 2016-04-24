#!/usr/bin/env python



import argparse, ConfigParser, json, random, os
from slackclient import SlackClient
from time import sleep
import webutil

tools = webutil.webmethods()

class Converser:
    topics = {}
    business = {}
    images = {}
    client = None
    debug = False
    my_user_name = ''

    def connect(self, token):
        self.client = SlackClient(token)
        # self.client.api_call(method='file.upload')
        self.client.rtm_connect()
        self.my_user_name = self.client.server.username
        print("Connected to Slack.")

    def listen(self):
        while True:
            try:
                input = self.client.rtm_read()
                if input:
                    for action in input:
                        if self.debug:
                            print(action)
                        if 'type' in action and action['type'] == "message":
                            self.process_message(action)
                else:
                    sleep(1)
            except Exception as e:
                print("Exception: ", e.message)

    def process_message(self, message):

        # General Trigger words
        for topic in self.topics.keys():

            # All topics
            if topic.lower() in message['text'].lower():
                response = self.topics[topic].format(**message)

                if response == "help":
                    response = "Commands:" "\n`<pugme>`\n`<catme>`\n`<gifme search>`\n`<Drunk Friend>`"


                # Give one pug
                if response == 'pug':
                    response = tools.pugme()

                # Give a cat
                if response == 'cat':
                    response = tools.catme()

                # Give a gif
                if response == 'gif':
                    response = tools.gifme(message['text'])

                print("Posting to [%s]: %s" % (message['channel'], response))
                self.post(message['channel'], response)

        # Business Cat
        for topic in self.business:
            # Business triggers
            if topic.lower() in message['text'].lower():
                response = random.choice(conv.images)
                print("Posting to [%s]: %s" % (message['channel'], response))
                self.post(message['channel'], response)

    def post(self, channel, message):
        chan = self.client.server.channels.find(channel)

        if not chan:
            raise Exception("Channel %s not found." % channel)

        return chan.send_message(message)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(open('arg', 'r').read())
    parser.add_argument('-d', action='store_true', help="Print debug output.", required=False )

    args = parser.parse_args()

    # Create a new Converser
    conv = Converser()

    if args.d:
        conv.debug = True

    # Read our token and connect with it
    config = ConfigParser.RawConfigParser()
    config.read('creds.cfg')
    token = config.get("Slack", "token")

    conv.connect(token)

    # Add our topics to the converser
    with open('topics.json') as data_file_1:
        conv.topics = json.load(data_file_1)
    with open('business.json') as data_file_2:
        conv.business = json.load(data_file_2)
    with open('images.json') as image_file:
        conv.images = json.load(image_file)


    # Run our conversation loop.
    conv.listen()
