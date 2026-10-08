# -*- coding: utf-8 -*-
# langchain1.3_tutorial - 项目名称
# test_my_add - 文件名称
# by 深秋 - 当前用户
# 2026/9/30 - 当前日期

from my_add import add

def test_add():
    """测试加法功能"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(10, -5) == 5