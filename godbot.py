#!/usr/bin/env python
import argparse, ConfigParser, json, random, webutil, slackutils, time
from slackclient import SlackClient
from time import sleep
from datetime import datetime

tools = webutil.webmethods()
utils = slackutils.slackUtils()

class Converser:
    topics = {}
    business = {}
    images = {}
    client = None
    debug = False
    my_user_name = ''

    def connect(self, token):
        self.client = SlackClient(token)
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
                            self.process_message(action, start)


                else:
                    sleep(1)
            except Exception as e:
                print("Exception: ", e.message)

    def process_message(self, message, start):

        # General Trigger words
        for topic in self.topics.keys():

            # All topics
            if topic.lower() in message['text'].lower():
                response = self.topics[topic].format(**message)

                # Responses that require other class level functions

                if response == 'help':
                    response = "Commands:`<pugme>`,`<catme>`,`<gifme search>`,`<quoteme>`,`<montyme>`,`<insultme>`,`<drunkme>`"

                if response == 'pug':
                    response = tools.pugme()

                if response == 'cat':
                    response = tools.catme()

                if response == 'gif':
                    response = tools.gifme(message['text'])

                if response == 'quote':
                    r = tools.quoteme()
                    r = r.strip('\n')
                    response = "`" + r + "`"
                    
                if response == 'insult':
                    r = tools.insultme()
                    response = "`" + r + "`"

                if response == 'me':
                    users = utils.getUsers()
                    r = users[message['user']]
                    r = "`" + r + "`"
                    response = r

                if response == 'ts':
                    current = time.time() - start
                    dt_obj = datetime.utcfromtimestamp(current)
                    r = str(dt_obj).strip('1970-01-01').split(".")[0]
                    response = "`" + r + "`"

                if response == "drunk":
                    response = utils.postImage()

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
    start = time.time()
    conv.listen()
