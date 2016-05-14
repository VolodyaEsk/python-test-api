import unittest



class TestGetIssue(unittest.TestCase):
    

    def setUp(self):
        self.base_url = 'http://codespace-api.myjetbrains.com/youtrack/rest'
        self.creds = ('root', 'c11desp@ce')

    def test_get_issue(self):
        self.assertEquals(1, 1)



if __name__ == '__main__':
    unittest.main()

    
