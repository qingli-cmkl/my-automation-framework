import pytest
import os

if __name__ == "__main__":
    # 测试用例路径、报告输出路径
    # case_path = "./testcases"
    report_path = "./report/report.html"
    # 执行命令：失败重跑2次，生成html报告
    pytest.main([
        # case_path,
        "-v", "-s",
        "--reruns=2",
        f"--html={report_path}",
        "--self-contained-html"
    ])
    print(f"测试执行完成，报告路径：{os.path.abspath(report_path)}")