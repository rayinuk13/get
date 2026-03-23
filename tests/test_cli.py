import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "get.py"


class GetCliTests(unittest.TestCase):
    def run_get(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_help_flag_succeeds(self):
        result = self.run_get("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Usage:", result.stdout)
        self.assertIn("get -mp3 <url>", result.stdout)

    def test_unknown_flag_fails(self):
        result = self.run_get("-nope", "https://example.com")
        self.assertEqual(result.returncode, 1)
        self.assertIn("[get] unknown flag: -nope", result.stdout)


if __name__ == "__main__":
    unittest.main()
