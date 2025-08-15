#!/usr/bin/env python3
"""
测试脚本 - 验证冒泡排序项目的所有功能
"""

import sys
import os

def test_basic_sort():
    """测试基础冒泡排序功能"""
    print("Testing basic bubble sort...")
    
    # 导入基础排序模块
    sys.path.append('.')
    from bubblesort import bubble_sort
    
    # 测试用例
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    ]
    
    for i, test_array in enumerate(test_cases, 1):
        print(f"  Test case {i}: {test_array}")
        result = bubble_sort(test_array.copy())
        expected = sorted(test_array)
        if result == expected:
            print(f"    ✓ PASS - Result: {result}")
        else:
            print(f"    ✗ FAIL - Expected: {expected}, Got: {result}")
            return False
    
    print("  ✓ All basic sort tests passed!")
    return True

def test_imports():
    """测试所有模块的导入"""
    print("Testing module imports...")
    
    try:
        import matplotlib.pyplot as plt
        import matplotlib.animation as animation
        import numpy as np
        print("  ✓ matplotlib and numpy imported successfully")
    except ImportError as e:
        print(f"  ✗ Import failed: {e}")
        return False
    
    try:
        from bubblesort import bubble_sort
        print("  ✓ bubblesort module imported successfully")
    except ImportError as e:
        print(f"  ✗ Import failed: {e}")
        return False
    
    return True

def test_animation_class():
    """测试动画类的基本功能"""
    print("Testing animation class...")
    
    try:
        from main import BubbleSortAnimation
        
        # 创建动画对象
        test_data = [5, 2, 8, 1, 9]
        animator = BubbleSortAnimation(test_data)
        
        # 检查基本属性
        if len(animator.sorting_steps) > 0:
            print("  ✓ Animation class created successfully")
            print(f"  ✓ Generated {len(animator.sorting_steps)} animation steps")
        else:
            print("  ✗ No animation steps generated")
            return False
            
    except Exception as e:
        print(f"  ✗ Animation class test failed: {e}")
        return False
    
    return True

def main():
    """主测试函数"""
    print("=== Bubble Sort Project Test Suite ===\n")
    
    tests = [
        ("Module Imports", test_imports),
        ("Basic Sort Function", test_basic_sort),
        ("Animation Class", test_animation_class),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Running {test_name}...")
        if test_func():
            passed += 1
        print()
    
    print("=== Test Results ===")
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! The project is ready to use.")
        print("\nTo run the programs:")
        print("  python bubblesort.py    # Basic version")
        print("  python main.py          # Animation version")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
