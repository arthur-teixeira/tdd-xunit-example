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
        return [
            func for func in dir(target) 
            if callable(getattr(target, func)) and not func.startswith("__")
            and not func in ['run', 'setUp', 'tearDown']
        ]
    
    def run(self, result):
        for test in self.tests:
            test.run(result)