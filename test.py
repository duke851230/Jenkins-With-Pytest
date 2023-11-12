import pytest
import sys

if __name__ == "__main__":
    exit_code: int = pytest.main(args=['pytests'])  # 相當於執行 pytest pytests
    print(f"exit_code: {exit_code}")
    # 要用 pytest 測試的 exit code 退出 python 腳本，不然每次退出碼都是 0（沒發生異常）
    sys.exit(exit_code)