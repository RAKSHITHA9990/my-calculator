"""
Integration Tests - CLI + Calculator Working Together
"""

import subprocess
import sys


class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""

    def run_cli(self, *args):
        """Helper method to run CLI and capture output"""
        cmd = [sys.executable, "-m", "src.cli"] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".")
        return result

    def test_cli_add_integration(self):
        result = self.run_cli("add", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "Result: 8"

    def test_cli_subtract_integration(self):
        result = self.run_cli("subtract", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "Result: 2"

    def test_cli_subtract_missing_operand_error(self):
        result = self.run_cli("subtract", "5")
        assert result.returncode == 1
        assert "Unexpected error" in result.stdout.strip()

    def test_cli_multiply_integration(self):
        result = self.run_cli("multiply", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "Result: 15"

    def test_cli_divide_integration(self):
        result = self.run_cli("divide", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "Result: 1.67"
