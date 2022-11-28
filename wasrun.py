from testcase import TestCase

class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "

    def tearDown(self):
        self.log += "tearDown "

    def testMethod(self):
        self.log += "testMethod "

    def testBrokenMethod(self):
        raise Exception
