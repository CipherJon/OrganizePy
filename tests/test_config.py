import unittest
from file_organizer.config import BASE_DIR, FILE_TYPES

class TestConfig(unittest.TestCase):
    def test_base_dir(self):
        self.assertTrue(isinstance(BASE_DIR, str))

    def test_file_types(self):
        self.assertTrue(isinstance(FILE_TYPES, dict))
        self.assertTrue(all(isinstance(k, str) for k in FILE_TYPES.keys()))
        self.assertTrue(all(isinstance(v, list) for v in FILE_TYPES.values()))