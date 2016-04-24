import requests, sys, re
import xml.etree.ElementTree as et

DEBUG = 0

class apiutil:
    def __init__(self):
        """
        Instantiation of hostname, authentication, and api version
        :return: None
        """
        if DEBUG > 0: print self.__module__ + ' init Called'
        self.hostname = ''
        self.auth_handler = ''
        self.version = ''

    def setHostname(self, hostname):
        """
        Set host of webservice
        :param hostname: String for hostname
        :return: None
        """
        if DEBUG > 0: print self.__module__ + ' setHostname Called'
        self.hostname = hostname
        return hostname

    def setVersion(self, version):
        """
        Set API version used
        :param version: string for API version
        :return: None
        """
        self.version = version
        return version

    def authHandler(self, user, password):
        """
        Sets authentication for target webservice
        :param user: string of username
        :param password: string of password
        :return: tuple of (user, name) for request authentication
        """
        if DEBUG > 0: print self.__module__ + ' authHandler Called'
        self.user = user
        self.password = password
        self.auth_handler = (user, password)
        return self.auth_handler

    def getRequest(self, url, payload):
        if DEBUG > 0: print self.__module__ + ' getRequest Called'
        self.url = url
        self.payload = payload
        r = requests.get(url, auth=self.auth_handler, data=payload)
        return r.content


