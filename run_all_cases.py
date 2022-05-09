import time
import unittest2
from lib.HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    # 1.找到所有需要执行的测试用例
    # 通过默认的测试用例加载器, 发现要执行的测试用例
    suite = unittest2.defaultTestLoader.discover("./test_case", "*Test.py")

    # 2.生成测试报告
    # 指定测试报告位置
    now = time.strftime("%Y%m%d %H%M%S")
    path = "report/TestReport.html"
    file = open('./report/' + now + '.html', 'wb')  # w表示写，b表示二进制方式写,description表示正文描述信息, tester测试人员名字
    HTMLTestRunner(stream=file, verbosity=1, title="自动化测试报告", description="测试环境：Chrome",tester="威廉").run(suite)




