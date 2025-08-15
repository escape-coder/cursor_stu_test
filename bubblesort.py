def bubble_sort(arr):
    """
    冒泡排序算法实现
    
    算法原理：
    1. 重复遍历要排序的数组
    2. 每次比较相邻的两个元素，如果顺序错误就交换它们
    3. 每一轮遍历后，最大的元素会"冒泡"到数组末尾
    4. 重复这个过程直到没有需要交换的元素
    
    时间复杂度：O(n²)
    空间复杂度：O(1)
    稳定性：稳定排序
    
    Args:
        arr: 要排序的数组
        
    Returns:
        排序后的数组（原地排序，会修改原数组）
    """
    n = len(arr)  # 获取数组长度
    
    # 外层循环：控制排序轮数
    # 每轮排序会将当前最大的元素移动到正确位置
    for i in range(n):
        # 内层循环：比较相邻元素
        # 每轮只需要比较到 n-i-1，因为后面的 i 个元素已经排好序
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换它们
            if arr[j] > arr[j + 1]:
                # Python的多重赋值语法，同时交换两个元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        # 打印每轮排序后的结果，便于观察排序过程
        print(f"第 {i + 1} 轮排序后: {arr}")
    
    return arr  # 返回排序后的数组


if __name__ == "__main__":
    """
    主程序入口
    测试冒泡排序算法在不同情况下的表现
    """
    
    # 测试用例1：普通数组
    test_array1 = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array1)
    # 使用.copy()方法创建数组副本，避免修改原数组
    sorted_array1 = bubble_sort(test_array1.copy())
    print("排序后数组:", sorted_array1)
    print()  # 空行分隔
    
    # 测试用例2：已经排序的数组（最好情况）
    test_array2 = [1, 2, 3, 4, 5]
    print("原始数组:", test_array2)
    sorted_array2 = bubble_sort(test_array2.copy())
    print("排序后数组:", sorted_array2)
    print()
    
    # 测试用例3：逆序数组（最坏情况）
    test_array3 = [5, 4, 3, 2, 1]
    print("原始数组:", test_array3)
    sorted_array3 = bubble_sort(test_array3.copy())
    print("排序后数组:", sorted_array3)
    print()
    
    # 测试用例4：包含重复元素的数组
    test_array4 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("原始数组:", test_array4)
    sorted_array4 = bubble_sort(test_array4.copy())
    print("排序后数组:", sorted_array4)
