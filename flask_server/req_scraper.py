from bs4 import BeautifulSoup
import os
import requests

class ReqScraper:

    def __init__(self, url, classification):
        self.url = url
        self.classification = classification
        self.keywords = []

        keywordsFile = os.getcwd()
        if classification == 'Engineering and Technology':
            path = self.buildFilePathByOS('eng_tech_keywords.txt')
            keywordsFile += path

        with open(keywordsFile, 'r') as f:
             for keyword in f:
                 if keyword != '' and keyword != '\n' and not keyword.startswith('#'):
                     self.keywords.append(keyword.rstrip())

    def buildFilePathByOS(self, file):
        if os.name == 'nt':
            return '\\flask_server\\static\\keywords\\{}'.format(file)
        else:
            return '/flask_server/static/keywords/{}'.format(file)

    def scrape(self):
        #TODO: This section needs to be properly filled out
        print(self.url)
        print(self.classification)
        print(self.keywords)
