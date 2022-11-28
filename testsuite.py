from testcase import TestCase
from getmethodsfromclass import get_methods_from_class

class TestSuite:
    def __init__(self) -> None:
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def fromClass(self, target):
        tests = self.get_method_list(target)
        for test_method in tests:
            self.add(target(test_method))
    
    def get_method_list(self, target):
        return [method for method in get_methods_from_class(target)
            if not method in self.test_case_default_methods()]
    
    def test_case_default_methods(self):
        return get_methods_from_class(TestCase)

    def run(self, result):
        for test in self.tests:
            test.run(result)