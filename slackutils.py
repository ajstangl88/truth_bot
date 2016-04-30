from slacker import Slacker
import ConfigParser, json, os, random
"""
Additioanl API calls for client currently not supported by slackClient
"""

# Set-up using bots credentials
config = ConfigParser.RawConfigParser()
config.read('creds.cfg')
token = config.get("Slack", "token")
slack = Slacker(token)


class slackUtils():

    def getUsers(self):
        response = slack.users.list()
        # A list of dictionaries for users
        users = response.body['members']
        jstring = {}
        for elem in users:
             jstring.update({elem['id']:elem['name']})
        return jstring

    def postImage(self):
        path = r"C:\Users\AJ Stangl\PycharmProjects\truthbot\drunkeric"
        files = []
        filelist = os.listdir(path)
        for elem in filelist:
            files.append(os.path.join(path, elem))
        filedir = random.choice(files)

        response = slack.files.upload(filedir, channels='casual-encounters')
        print response.body

        return response

#
#
# tool = slackUtils()
# test = tool.postImage()
