import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class BubbleSortAnimation:
    """Bubble Sort Animation Class"""
    
    def __init__(self, data):
        self.data = data.copy()
        self.n = len(data)
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.bars = []
        self.sorting_steps = []
        
        # Setup chart
        self.ax.set_xlim(0, self.n)
        self.ax.set_ylim(0, max(self.data) * 1.1)
        self.ax.set_title('Bubble Sort Animation', fontsize=16, fontweight='bold')
        self.ax.set_xlabel('Array Index', fontsize=12)
        self.ax.set_ylabel('Value', fontsize=12)
        self.ax.grid(True, alpha=0.3)
        
        self.generate_sorting_steps()
        
    def generate_sorting_steps(self):
        """Generate sorting steps"""
        arr = self.data.copy()
        self.sorting_steps.append(arr.copy())
        
        for i in range(self.n):
            swapped = False
            for j in range(0, self.n - i - 1):
                # Record comparison state
                step_info = {
                    'array': arr.copy(),
                    'comparing': [j, j + 1],
                    'round': i + 1,
                    'step': j + 1
                }
                self.sorting_steps.append(step_info)
                
                if arr[j] > arr[j + 1]:
                    # Swap elements
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    
                    # Record state after swap
                    step_info = {
                        'array': arr.copy(),
                        'comparing': [j, j + 1],
                        'swapped': True,
                        'round': i + 1,
                        'step': j + 1
                    }
                    self.sorting_steps.append(step_info)
            
            # Record round completion state
            step_info = {
                'array': arr.copy(),
                'round_complete': True,
                'round': i + 1
            }
            self.sorting_steps.append(step_info)
            
            if not swapped:
                break
    
    def init_animation(self):
        """Initialize animation"""
        self.ax.clear()
        self.ax.set_xlim(0, self.n)
        self.ax.set_ylim(0, max(self.data) * 1.1)
        self.ax.set_title('Bubble Sort Animation', fontsize=16, fontweight='bold')
        self.ax.set_xlabel('Array Index', fontsize=12)
        self.ax.set_ylabel('Value', fontsize=12)
        self.ax.grid(True, alpha=0.3)
        
        bars = self.ax.bar(range(self.n), self.data, 
                          color='skyblue', edgecolor='navy', linewidth=1)
        
        for i, bar in enumerate(bars):
            height = bar.get_height()
            self.ax.text(bar.get_x() + bar.get_width()/2., height,
                        f'{int(height)}', ha='center', va='bottom', fontweight='bold')
        
        return bars
    
    def animate(self, frame):
        """Animation update function"""
        if frame >= len(self.sorting_steps):
            return self.bars
        
        step = self.sorting_steps[frame]
        self.ax.clear()
        self.ax.set_xlim(0, self.n)
        self.ax.set_ylim(0, max(self.data) * 1.1)
        
        # Set title
        title = 'Bubble Sort Animation'
        if 'round' in step:
            title += f' - Round {step["round"]}'
            if 'step' in step:
                title += f' Step {step["step"]}'
        self.ax.set_title(title, fontsize=16, fontweight='bold')
        self.ax.set_xlabel('Array Index', fontsize=12)
        self.ax.set_ylabel('Value', fontsize=12)
        self.ax.grid(True, alpha=0.3)
        
        current_array = step['array']
        colors = ['skyblue'] * self.n
        
        # Set colors
        if 'comparing' in step:
            i, j = step['comparing']
            colors[i] = 'red'
            colors[j] = 'orange'
            
            if step.get('swapped', False):
                colors[i] = 'lightgreen'
                colors[j] = 'lightgreen'
        
        if step.get('round_complete', False):
            round_num = step['round']
            for k in range(self.n - round_num, self.n):
                colors[k] = 'lightgreen'
        
        # Draw bar chart
        bars = self.ax.bar(range(self.n), current_array, 
                          color=colors, edgecolor='navy', linewidth=1)
        
        # Add value labels
        for i, bar in enumerate(bars):
            height = bar.get_height()
            self.ax.text(bar.get_x() + bar.get_width()/2., height,
                        f'{int(height)}', ha='center', va='bottom', fontweight='bold')
        
        # Add description text
        if 'comparing' in step:
            i, j = step['comparing']
            self.ax.text(0.02, 0.98, f'Comparing: arr[{i}]={current_array[i]} vs arr[{j}]={current_array[j]}', 
                        transform=self.ax.transAxes, fontsize=10, 
                        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
            
            if step.get('swapped', False):
                self.ax.text(0.02, 0.92, 'Swapped!', 
                            transform=self.ax.transAxes, fontsize=10, color='red',
                            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))
        
        if step.get('round_complete', False):
            self.ax.text(0.02, 0.98, f'Round {step["round"]} Complete!', 
                        transform=self.ax.transAxes, fontsize=12, color='green',
                        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
        
        self.bars = bars
        return bars
    
    def start_animation(self, interval=500):
        """Start animation"""
        self.anim = animation.FuncAnimation(
            self.fig, self.animate, init_func=self.init_animation,
            frames=len(self.sorting_steps), interval=interval, 
            repeat=False, blit=False
        )
        plt.tight_layout()
        plt.show()

def bubble_sort_with_animation(arr, show_animation=True):
    """Bubble sort with animation"""
    print(f"Original array: {arr}")
    
    if show_animation:
        animator = BubbleSortAnimation(arr)
        print("Starting bubble sort animation...")
        animator.start_animation(interval=800)
    
    # Execute sorting
    n = len(arr)
    arr_copy = arr.copy()
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        print(f"After round {i + 1}: {arr_copy}")
        
        if not swapped:
            break
    
    print(f"Sorted array: {arr_copy}")
    return arr_copy

def create_static_visualization(arr):
    """Create static visualization chart"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Original array
    ax1.bar(range(len(arr)), arr, color='skyblue', edgecolor='navy')
    ax1.set_title('Before Sorting', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Index')
    ax1.set_ylabel('Value')
    ax1.grid(True, alpha=0.3)
    
    for i, v in enumerate(arr):
        ax1.text(i, v, str(v), ha='center', va='bottom', fontweight='bold')
    
    # Sorted array
    sorted_arr = sorted(arr)
    ax2.bar(range(len(sorted_arr)), sorted_arr, color='lightgreen', edgecolor='darkgreen')
    ax2.set_title('After Sorting', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Index')
    ax2.set_ylabel('Value')
    ax2.grid(True, alpha=0.3)
    
    for i, v in enumerate(sorted_arr):
        ax2.text(i, v, str(v), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    ]
    
    print("=== Bubble Sort Animation Demo ===\n")
    
    for i, test_array in enumerate(test_cases, 1):
        print(f"Test case {i}:")
        print("-" * 50)
        
        # Show static comparison chart
        create_static_visualization(test_array)
        
        # Execute sorting with animation
        sorted_result = bubble_sort_with_animation(test_array, show_animation=True)
        
        print(f"Sorting result: {sorted_result}")
        print("\n" + "="*60 + "\n")
        
        # Wait for user confirmation to continue
        if i < len(test_cases):
            input("Press Enter to continue to next test case...")
