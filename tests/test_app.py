# tests/test_app.py

import unittest
from streamlit import cli as stcli
import sys

class TestApp(unittest.TestCase):
    def test_app_runs(self):
        # This test checks if the app runs without errors
        # Since Streamlit apps are interactive, we can't test them traditionally
        # We'll simulate running the app script
        try:
            sys.argv = ["streamlit", "run", "app.py", "--headless"]
            stcli.main()
        except SystemExit as e:
            self.assertEqual(e.code, 0)  # Exit code 0 indicates success
        except Exception as e:
            self.fail(f"App failed to run: {e}")

if __name__ == '__main__':
    unittest.main()
