from collections import Counter

class SortingFunctions:
    "Class with sorting algorithms and step by step debugging"

    def bubble_sort_debug(self, arr):
        n = len(arr)
        steps = []
        arr = arr.copy()

        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(f"Pass {i+1}, swap index {j} & {j+1}: {arr}")
        
        return arr, steps
    

    def insertion_sort_debug(self, arr):
        steps = []
        a = arr.copy()

        for i in range(1, len(a)):
            key = a[i]
            j = i - 1
            steps.append(f"Start pass {i}: key={key}, array={a}")

            while j >= 0 and key < a[j]:
                a[j + 1] = a[j]
                steps.append(f"Shift {a[j]} right: {a}")
                j -= 1

            a[j + 1] = key
            steps.append(f"Insert key {key} at position {j + 1}: {a}")

        return a, steps
    

    def selection_sort_debug(self, arr):
        steps = []
        a = arr.copy()

        n = len(a)

        for i in range(n):
            min_idx = i
            steps.append(f"Start pass {i+1}: {a}")
            for j in range(i+1, n):
                if a[j] < a[min_idx]:
                    min_idx = j
                    steps.append(f"New minimum found at index {j}: ({a[j]})")
            a[i], a[min_idx] = a[min_idx], a[i]
            steps.append(f"Swap index {i} with min index {min_idx}: {a}")

        return a, steps
    

    def merge_sort_debug(self, arr):
        steps = []

        def merge_sort(a):
            if len(a) > 1:
                mid = len(a) // 2
                L = a[:mid]
                R = a[mid:]

                # Record split
                steps.append(f"Split: {a} -> {L} and {R}")

                # Sort each half
                merge_sort(L)
                merge_sort(R)

                # Merge step
                merged = []
                i = j = 0
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        merged.append(L[i])
                        i += 1
                    else:
                        merged.append(R[j])
                        j += 1
                merged.extend(L[i:])
                merged.extend(R[j:])

                steps.append(f"Merge: {L} and {R} -> {merged}")

                # Update original list in place
                a[:] = merged

        arr_copy = arr.copy()
        merge_sort(arr_copy)
        return arr_copy, steps



    def counting_sort_debug(self, arr):
        steps = []
        a = arr.copy()

        if not a:
            return a, ["Array is empty"]

        max_val = max(a)
        count = [0] * (max_val + 1)

        steps.append(f"Initial count array: {count}")

        # Count each element
        for num in a:
            count[num] += 1
            steps.append(f"Count {num}: {count}")

        # Rebuild sorted array
        sorted_index = 0
        for num, freq in enumerate(count):
            for _ in range(freq):
                a[sorted_index] = num
                sorted_index += 1
                steps.append(f"Place {num}: {a}")

        return a, steps


    def quick_sort_debug(self, arr):
        steps = []

        def quick_sort(a, low, high):
            if low < high:
                p = partition(a, low, high)
                steps.append(f"Partitioned at index {p}: {a}")
                quick_sort(a, low, p - 1)
                quick_sort(a, p + 1, high)

        def partition(a, low, high):
            pivot = a[high]
            steps.append(f"Choosing pivot {pivot} from {a[low:high+1]}")
            i = low - 1
            for j in range(low, high):
                if a[j] <= pivot:
                    i += 1
                    a[i], a[j] = a[j], a[i]
            a[i + 1], a[high] = a[high], a[i + 1]
            return i + 1

        arr_copy = arr.copy()
        quick_sort(arr_copy, 0, len(arr_copy) - 1)
        return arr_copy, steps


class ArraySearch:
    """Array search algorithms."""

    def linear_search_debug(self, arr, target):
        steps = []
        for i, val in enumerate(arr):
            steps.append(f"Check index {i}: {val}")
            if val == target:
                return i, steps
        return -1, steps

    def binary_search_debug(self, arr, target):
        steps = []
        a = sorted(arr)  # Ensure array is sorted for binary search
        low, high = 0, len(a)-1
        while low <= high:
            mid = (low+high)//2
            steps.append(f"Check middle index {mid}: {a[mid]}")
            if a[mid] == target:
                return mid, steps
            elif a[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1, steps


class ArrayOperations:
    """Other array operations."""

    def sum_array(self, arr):
        return sum(arr)

    def product_array(self, arr):
        prod = 1
        for num in arr:
            prod *= num
        return prod

    def reverse_array(self, arr):
        return arr[::-1]

    def rotate_left(self, arr, k=1):
        if not arr:
            return []
        k %= len(arr)
        return arr[k:] + arr[:k]

    def rotate_right(self, arr, k=1):
        if not arr:
            return []
        k %= len(arr)
        return arr[-k:] + arr[:-k]

    def remove_duplicates(self, arr):
        seen = set()
        result = []
        for x in arr:
            if x not in seen:
                result.append(x)
                seen.add(x)
        return result

    def max_min(self, arr):
        if not arr:
            return (None, None)
        return (max(arr), min(arr))

    def mean(self, arr):
        if not arr:
            return 0
        return sum(arr) / len(arr)
    

    def median(self, arr):
        if not arr:
            return 0
        sorted_arr = sorted(arr)
        mid = len(sorted_arr) // 2
        if len(sorted_arr) % 2 == 1:
            return sorted_arr[mid]
        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    

    def mode(self, arr):
        if not arr:
            return None  # instead of []
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        max_count = max(freq.values())
        modes = [key for key, val in freq.items() if val == max_count]
        return modes if len(modes) > 1 else modes[0]
