import pytest
import allure

class TestDisplay:
    @allure.step(title="登录")
    def test_mobile_display_input(self):
        print("hello")
        assert 1

    @allure.step(title="用户名")
    def test_mobile_display_input1(self):
        print("hello")
        assert 1

    @allure.step(title="密码")
    def test_mobile_display_input2(self):
        print("hello")
        assert 1

