import importlib.util
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "get.py"


class MainFlowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("get_cli", SCRIPT)
        cls.get_cli = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(cls.get_cli)

    def test_main_calls_download_for_valid_mp3_flag(self):
        with (
            patch.object(sys, "argv", ["get", "-mp3", "https://example.com"]),
            patch.object(self.get_cli, "check_deps") as check_deps,
            patch.object(self.get_cli, "download") as download,
        ):
            self.get_cli.main()
            check_deps.assert_called_once_with()
            download.assert_called_once_with("mp3", "https://example.com")


if __name__ == "__main__":
    unittest.main()
