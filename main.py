from testcase import TestCase, TestResult
from wasrun import WasRun
from testsuite import TestSuite
class BrokenSetUpTestCase(TestCase):
    def setUp(self):
        raise Exception

class BrokenTearDownTestCase(TestCase):
    def tearDown(self):
        raise Exception
    def testMethod(self):
        pass

class DummyTestCase(TestCase):
    def setUp(self):
        self.log = "setUp "

    def test1(self):
        self.log += "test1 "
    def test2(self):
        self.log += "test2 "
    def test3(self):
        self.log += "test3 "
    def test4(self):
        self.log += "test4 "

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

    def testTearDownInvokedWhenTestFails(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("setUp tearDown " == test.log)

    def testFailOnTearDown(self):
        test = BrokenTearDownTestCase("testMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testSuiteFromTestClass(self):
        suite = TestSuite()
        suite.fromClass(DummyTestCase)
        suite.run(self.result)
        assert("4 run, 0 failed" == self.result.summary())
        
        

suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailOnSetUp"))
suite.add(TestCaseTest("testSuite"))
suite.add(TestCaseTest("testTearDownInvokedWhenTestFails"))
suite.add(TestCaseTest("testFailOnTearDown"))
suite.add(TestCaseTest("testSuiteFromTestClass"))

result = TestResult()
suite.run(result)
print(result.summary())