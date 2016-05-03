import ccsyspath
import unittest


class TestPaths(unittest.TestCase):
    def test_c_compiler(self):
        lines = ccsyspath.system_include_paths('clang', cpp=False)
        self.assertEquals(list, type(lines))
        self.assertTrue(len(lines) > 0)

    def test_cpp_compiler(self):
        lines = ccsyspath.system_include_paths('clang++', cpp=True)
        self.assertEquals(list, type(lines))
        self.assertTrue(len(lines) > 0)
