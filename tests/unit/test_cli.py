import subprocess
import sys


def test_cli_add():
    result = subprocess.run(
        [sys.executable, "-m", "src.cli", "add", "5", "3"],
        capture_output=True,
        text=True,
    )
    assert "Result: 8" in result.stdout
