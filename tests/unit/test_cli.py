import subprocess

def test_cli_add():
    result = subprocess.run(
        ["python", "src/cli.py", "add", "5", "3"], capture_output=True, text=True
    )
    assert "Result: 8" in result.stdout

