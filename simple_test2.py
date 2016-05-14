import unittest
import requests
from yaml import load



class TestDeleteIssue(unittest.TestCase):

    def setUp(self):
        self.settings = load(open('fake_creds.yml').read())
        self.base_url = self.settings['base_url']
        login = self.settings['credentials']['login']
        password = self.settings['credentials']['password']
        self.creds = (login, password)

    def test_delete_issue(self):
        url = self.base_url + '/issue/' + 'API-10'

        r = requests.delete(url, auth = self.creds)
        self.assertEquals(r.status_code, 404)

    def test_delete_unexisted_issue(self):
        
        url = self.base_url + '/issue/' + 'ZZZZ'
        r = requests.delete(url, auth=self.creds)

        self.assertEquals(r.status_code, 404)

if __name__ == '__main__':
    unittest.main()
