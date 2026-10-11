#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""手动测试 my_add.py 的修复结果"""

from my_add import add

def test_add():
    """测试加法功能"""
    print("Running tests...")
    
    # Test 1: 2 + 3 = 5
    result1 = add(2, 3)
    assert result1 == 5, f"Test 1 failed: add(2, 3) = {result1}, expected 5"
    print(f"✓ add(2, 3) = {result1}")
    
    # Test 2: -1 + 1 = 0
    result2 = add(-1, 1)
    assert result2 == 0, f"Test 2 failed: add(-1, 1) = {result2}, expected 0"
    print(f"✓ add(-1, 1) = {result2}")
    
    # Test 3: 0 + 0 = 0
    result3 = add(0, 0)
    assert result3 == 0, f"Test 3 failed: add(0, 0) = {result3}, expected 0"
    print(f"✓ add(0, 0) = {result3}")
    
    # Test 4: 10 + (-5) = 5
    result4 = add(10, -5)
    assert result4 == 5, f"Test 4 failed: add(10, -5) = {result4}, expected 5"
    print(f"✓ add(10, -5) = {result4}")
    
    print("\nAll tests passed! ✓")

if __name__ == "__main__":
    test_add()
