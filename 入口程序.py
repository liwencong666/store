import unittest
from HTMLTestRunner import HTMLTestRunner

#创建测试集
suite = unittest.TestSuite()
#让测试加载器自己加载所有用例
tests = unittest.defaultTestLoader.discover("C:\\Users\\ThinkPad\\PycharmProjects\\day16",pattern="*Test.py")
#将所用例放入测试集
suite.addTests(tests)
#创建测试运行器
f = open(file="银行系统测试报告.html",mode="w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    title = "这是一个银行系统的测试报告",
    verbosity = 2,
    description="测试用例"
)
#让运行器生成测试报告
runner.run(suite)






