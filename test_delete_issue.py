import requests
from base_test import BaseTestAPI


class TestDeleteIssue(BaseTestAPI):

    def setUp(self):
        super(TestDeleteIssue, self).setUp()
        self.url = self.base_url + '/issue/'

    def test_delete_issue(self):
        issue_id = self.create_issue()

        url = self.url + issue_id
        print url
        r = requests.delete(url, cookies=self.cookies)

        self.assertEquals(r.status_code, 200)
        
        r = requests.get(url, cookies=self.cookies)
        self.assertEquals(r.status_code, 404)


    def test_delete_unexisted_issue(self):
        url = self.url + 'zzzz'
        r = requests.delete(url, cookies=self.cookies)
        self.assertEquals(r.status_code, 404)
