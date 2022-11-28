class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def run(self):
            self.setUp()
            method = getattr(self, self.name)
            method()
            self.tearDown()
class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = "setUp "
        self.wasRun= None
        
    def testMethod(self):
        self.log += "testMethod "

    def tearDown(self):
        self.log += "tearDown "
    
class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert("setUp testMethod tearDown " == self.test.log)


TestCaseTest("testTemplateMethod").run()