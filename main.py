from testcase import TestCase, TestResult
from wasrun import WasRun
class BrokenSetUpTestCase(TestCase):
    def setUp(self):
        raise Exception
    def testMethod(self):
        pass

class TestSuite:
    def __init__(self) -> None:
        self.tests = []

    def add(self, test):
        self.tests.append(test)
    
    def run(self, result):
        for test in self.tests:
            test.run(result)
class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)
    
    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())
    
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testFailOnSetUp(self):
        test = BrokenSetUpTestCase("testMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedResultFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())

suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailOnSetUp"))
suite.add(TestCaseTest("testSuite"))

result = TestResult()
suite.run(result)
print(result.summary())