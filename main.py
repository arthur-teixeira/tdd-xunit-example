from testcase import TestCase, TestResult
from wasrun import WasRun
class BrokenSetUpTestCase(TestCase):
    def setUp(self):
        raise Exception
    def testMethod(self):
        pass

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

    def testFailOnSetUp(self):
        test = BrokenSetUpTestCase("testMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

    # def testSuite(self):
    #     suite = TestSuite()
    #     suite.add(WasRun("testMethod"))
    #     suite.add(WasRun("testBrokenMethod"))
    #     result = suite.run()
    #     assert("2 run, 1 failed" == result.summary())

print(TestCaseTest("testTemplateMethod").run().summary())
print(TestCaseTest("testResult").run().summary())
print(TestCaseTest("testFailedResultFormatting").run().summary())
print(TestCaseTest("testFailedResult").run().summary())
print(TestCaseTest("testFailOnSetUp").run().summary())