import unittest
import time
from collections import defaultdict


class Test(unittest.TestCase):
    test_cases = [
        #("abcd", True),
    ]
    test_functions = [
    ]

    def test_implementations(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        if not (self.test_functions and self.test_cases):
            return

        for _ in range(num_runs):
            for args, expected in self.test_cases:
                for implementation in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        implementation(*args) == expected
                    ), f"{implementation.__name__} failed for args: {args}"
                    function_runtimes[implementation.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")
