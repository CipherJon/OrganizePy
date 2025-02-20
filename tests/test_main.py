import unittest
from file_organizer.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        try:
            main()
        except Exception as e:
            self.fail(f"main() raised {e} unexpectedly!")