class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        self.wasSetUp = 1
    def run(self):
            self.setUp()
            method = getattr(self, self.name)
            method()
class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setUp(self):
        self.log = "setUp "
        self.wasRun= None
        
    def testMethod(self):
        self.log = self.log + "testMethod "
    
class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert("setUp testMethod " == self.test.log)


TestCaseTest("testTemplateMethod").run()