import pytest
import sys

if __name__ == "__main__":
    exit_code: int = pytest.main(args=['pytests'])  # 相當於執行 pytest pytests
    print(f"exit_code: {exit_code}")
    sys.exit(exit_code)