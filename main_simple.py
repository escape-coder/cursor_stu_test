import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import sys

def bubble_sort_animation_simple(arr):
    """
    简化版冒泡排序动画
    添加错误处理和调试信息
    """
    try:
        print(f"开始处理数组: {arr}")
        
        # 设置matplotlib后端
        plt.switch_backend('TkAgg')  # 使用TkAgg后端
        
        # 创建图形
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # 初始化数据
        data = arr.copy()
        n = len(data)
        
        # 设置图表
        ax.set_xlim(0, n)
        ax.set_ylim(0, max(data) * 1.1)
        ax.set_title('冒泡排序动画演示', fontsize=14, fontweight='bold')
        ax.set_xlabel('数组索引')
        ax.set_ylabel('数值')
        ax.grid(True, alpha=0.3)
        
        # 创建初始柱状图
        bars = ax.bar(range(n), data, color='skyblue', edgecolor='navy')
        
        # 添加数值标签
        for i, bar in enumerate(bars):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}', ha='center', va='bottom', fontweight='bold')
        
        def update(frame):
            """动画更新函数"""
            nonlocal data
            
            # 清除之前的图形
            ax.clear()
            ax.set_xlim(0, n)
            ax.set_ylim(0, max(arr) * 1.1)
            ax.set_title(f'冒泡排序动画演示 - 第{frame//n + 1}轮', fontsize=14, fontweight='bold')
            ax.set_xlabel('数组索引')
            ax.set_ylabel('数值')
            ax.grid(True, alpha=0.3)
            
            # 执行一步排序
            if frame < n * (n - 1) // 2:  # 限制最大帧数
                i = frame // (n - 1)
                j = frame % (n - 1)
                
                if j < n - i - 1 and data[j] > data[j + 1]:
                    # 交换元素
                    data[j], data[j + 1] = data[j + 1], data[j]
                    print(f"第{i+1}轮第{j+1}步: 交换 {data[j+1]} 和 {data[j]}")
            
            # 绘制柱状图
            colors = ['skyblue'] * n
            if frame < n * (n - 1) // 2:
                i = frame // (n - 1)
                j = frame % (n - 1)
                if j < n - i - 1:
                    colors[j] = 'red'
                    colors[j + 1] = 'orange'
            
            # 标记已排序的部分
            for k in range(n - i, n):
                colors[k] = 'lightgreen'
            
            bars = ax.bar(range(n), data, color=colors, edgecolor='navy')
            
            # 添加数值标签
            for i, bar in enumerate(bars):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{int(height)}', ha='center', va='bottom', fontweight='bold')
            
            return bars
        
        # 创建动画
        print("创建动画...")
        anim = animation.FuncAnimation(
            fig, update, frames=min(50, n * (n - 1) // 2), 
            interval=500, repeat=False, blit=False
        )
        
        print("显示动画...")
        plt.tight_layout()
        plt.show()
        
        print("动画完成!")
        return data
        
    except Exception as e:
        print(f"动画运行出错: {e}")
        print("尝试运行静态版本...")
        return bubble_sort_static(arr)

def bubble_sort_static(arr):
    """
    静态版本的冒泡排序（无动画）
    """
    print(f"原始数组: {arr}")
    
    n = len(arr)
    arr_copy = arr.copy()
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        print(f"第 {i + 1} 轮排序后: {arr_copy}")
        
        if not swapped:
            break
    
    print(f"排序后数组: {arr_copy}")
    return arr_copy

def create_simple_visualization(arr):
    """
    创建简单的静态可视化
    """
    try:
        plt.switch_backend('TkAgg')
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # 原始数组
        ax1.bar(range(len(arr)), arr, color='skyblue', edgecolor='navy')
        ax1.set_title('排序前', fontsize=12, fontweight='bold')
        ax1.set_xlabel('索引')
        ax1.set_ylabel('数值')
        ax1.grid(True, alpha=0.3)
        
        for i, v in enumerate(arr):
            ax1.text(i, v, str(v), ha='center', va='bottom', fontweight='bold')
        
        # 排序后数组
        sorted_arr = sorted(arr)
        ax2.bar(range(len(sorted_arr)), sorted_arr, color='lightgreen', edgecolor='darkgreen')
        ax2.set_title('排序后', fontsize=12, fontweight='bold')
        ax2.set_xlabel('索引')
        ax2.set_ylabel('数值')
        ax2.grid(True, alpha=0.3)
        
        for i, v in enumerate(sorted_arr):
            ax2.text(i, v, str(v), ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"静态可视化出错: {e}")

if __name__ == "__main__":
    print("=== 冒泡排序动画演示（简化版）===")
    print("正在初始化...")
    
    # 测试用例
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]
    
    for i, test_array in enumerate(test_cases, 1):
        print(f"\n测试用例 {i}: {test_array}")
        print("-" * 50)
        
        try:
            # 显示静态对比图
            print("显示静态对比图...")
            create_simple_visualization(test_array)
            
            # 执行带动画的排序
            print("开始动画排序...")
            sorted_result = bubble_sort_animation_simple(test_array)
            
            print(f"排序结果: {sorted_result}")
            
        except Exception as e:
            print(f"处理测试用例 {i} 时出错: {e}")
            # 如果动画失败，至少运行静态版本
            sorted_result = bubble_sort_static(test_array)
        
        print("\n" + "="*60)
        
        # 等待用户确认继续
        if i < len(test_cases):
            try:
                input("按回车键继续下一个测试用例...")
            except KeyboardInterrupt:
                print("\n程序被用户中断")
                break
