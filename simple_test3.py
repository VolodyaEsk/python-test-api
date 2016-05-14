from base_test import BaseTestAPI
import requests


class TestCreateIssue(BaseTestAPI):

    def test_create_issue(self):
        url = self.base_url + '/issue/'
        params = {
          'project': 'API',
          'summary': 'test summary',
          'description': 'test descr',
        }

        r = requests.put(url, params, cookies=self.cookies)
        issue_id = r.headers['Location'].split('/')[-1]
        self.assertEquals(r.status_code, 201)

        url = self.base_url + '/issue/' + issue_id
        r = requests.get(url, cookies=self.cookies)
        self.assertEquals(r.status_code, 200)
