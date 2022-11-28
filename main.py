class TestCase:
    def __init__(self, name):
        self.name = name
    
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def run(self):
            result = TestResult()
            result.testStarted()
            try:
                self.setUp()
                method = getattr(self, self.name)
                method()
            except:
                result.testFailed()
            self.tearDown()
            return result

class TestResult:
    def __init__(self) -> None:
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.errorCount +=1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)
class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "

    def tearDown(self):
        self.log += "tearDown "

    def testMethod(self):
        self.log += "testMethod "

    def testBrokenMethod(self):
        raise Exception

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)
    
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())
    
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

class FailingSetUpTestCaseTest(TestCase):
    def setUp(self):
        raise Exception
    def testFailOnSetUp(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResultFormatting").run()
TestCaseTest("testFailedResult").run()
FailingSetUpTestCaseTest("testFailOnSetUp").run()