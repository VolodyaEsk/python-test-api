import unittest
import xmltodict
import requests
import yaml


class BaseTestAPI(unittest.TestCase):

    def setUp(self):
        self.settings = yaml.load(open('fake_creds.yml').read())
        self.base_url = self.settings['base_url']

        params = {
          'login': self.settings['credentials']['login'],
          'password': self.settings['credentials']['password']
        }

        url = self.base_url + '/user/login/'
        r = requests.post(url, data=params)
        self.cookies = r.cookies
        

    def create_issue(self):
        url = self.base_url + '/issue/'

        params = {
          'project': 'API',
          'summary': 'test issue by robots',
          'description': 'Hail Robots!',
        }

        r = requests.put(url, data=params, cookies=self.cookies)
        location = r.headers['Location']
        issue_id = location.split('/')[-1]

        return issue_id
