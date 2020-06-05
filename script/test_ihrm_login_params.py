import unittest
import logging
import requests

import app
from utils import assert_common, read_login_data
from parameterized import parameterized
from api.login_api import TestLoginApi


# 创建测试类，继承unittest.TestCase
class TestIHRMLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"
        # 导入封装的API模块
        self.login_api = TestLoginApi()  # 实例化登录API

    def tearDown(self):
        pass

    # 定义数据文件的路径
    filename = app.BASE_DIR + "/data/login_data.json"

    @parameterized.expand(read_login_data(filename))
    # 编写第一个案例，测试登录成功
    def test01_login_success(abc, case_name, jsonData, http_code, success, code, message):
        # IHRM项目可以直接发送登录请求
        headers = {"Content-Type": "application/json"}  # 定义请求头
        jsonData = jsonData
        # 发送登录请求
        response = abc.login_api.login(jsonData, headers)
        # 打印登录的结果
        result = response.json()
        logging.info("登录的结果为：{}".format(result))
        # 使用封装的通用断言函数实现优化断言
        assert_common(http_code, success, code, message, response, abc)
