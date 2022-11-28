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
        self.wasRun= None
        self.wasSetUp= 1
        
    def testMethod(self):
        self.wasRun = 1
    
class TestCaseTest(TestCase):
    def testRunning(self):
        test= WasRun("testMethod")
        test.run()
        assert(test.wasRun)

    def testSetup(self):
        test= WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)
TestCaseTest("testRunning").run()
TestCaseTest("testSetup").run()