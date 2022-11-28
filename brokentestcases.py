from testcase import TestCase

class BrokenSetUpTestCase(TestCase):
    def setUp(self):
        raise Exception

class BrokenTearDownTestCase(TestCase):
    def tearDown(self):
        raise Exception
    def testMethod(self):
        pass