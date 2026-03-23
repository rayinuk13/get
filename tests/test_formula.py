import unittest
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
FORMULA = REPO_ROOT / "Formula" / "get.rb"


class FormulaTests(unittest.TestCase):
    def test_formula_has_install_and_test(self):
        content = FORMULA.read_text(encoding="utf-8")
        self.assertIn("class Get < Formula", content)
        self.assertIn("bin.install", content)
        self.assertIn("get.py", content)
        self.assertIn("=> \"get\"", content)
        self.assertIn("depends_on \"ffmpeg\"", content)
        self.assertIn("depends_on \"yt-dlp\"", content)
        self.assertIn("archive/refs/tags/v", content)
        self.assertIn(".tar.gz", content)
        self.assertIn("sha256", content)
        self.assertIn(r"assert_match(/get v\d+\.\d+\.\d+/", content)
        self.assertIn("test do", content)

    def test_formula_url_uses_semver_tag(self):
        content = FORMULA.read_text(encoding="utf-8")
        match = re.search(r'url\s+"[^"]*/v(\d+\.\d+\.\d+)\.tar\.gz"', content)
        self.assertIsNotNone(match)


if __name__ == "__main__":
    unittest.main()
