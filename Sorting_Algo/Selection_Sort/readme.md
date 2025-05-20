# 🚀 Selection Sort Algorithm

> A simple, easy-to-understand algorithm to introduce the concept of sorting.

![Language](https://img.shields.io/badge/language-C++%2FJavaScript-blue.svg)
![Difficulty](https://img.shields.io/badge/difficulty-Easy-brightgreen)
![Stability](https://img.shields.io/badge/stability-Unstable-red)
![Space](https://img.shields.io/badge/space-O(1)-lightgrey)
![Time](https://img.shields.io/badge/time-O(n²)-orange)

---

## 📌 What is Selection Sort?

Selection Sort is a **comparison-based sorting algorithm** that sorts an array by repeatedly selecting the **smallest (or largest)** element from the unsorted portion and swapping it with the first unsorted element. This continues until the entire array is sorted.

---

## 🧠 Working Principle

<details>
<summary>📖 Click to expand step-by-step explanation</summary>

1. Start with the first index.
2. Find the smallest element from the unsorted part of the array.
3. Swap it with the element at the current index.
4. Move to the next index and repeat the process.
5. Continue until the array is completely sorted.
</details>

---

## 💡 Visual Example

- Initial Array: [64, 25, 12, 22, 11]

- Step 1 (Find min): [11, 25, 12, 22, 64]
- Step 2 (Find next): [11, 12, 25, 22, 64]
- Step 3: [11, 12, 22, 25, 64]
- Step 4: [11, 12, 22, 25, 64] ✅ Sorted


---

## 🧮 Time & Space Complexity

| Scenario       | Time Complexity |
|----------------|-----------------|
| Best Case      | O(n²)           |
| Average Case   | O(n²)           |
| Worst Case     | O(n²)           |

- 🔁 **Number of Comparisons**: Always `(n-1) + (n-2) + ... + 1 = O(n²)`
- 🧠 **Space Complexity**: `O(1)` (in-place sorting)
- ✍️ **Swaps**: At most `(n - 1)` swaps (minimal writes)

---

## ✅ Advantages

- ✅ Simple to understand and implement.
- 💾 Uses only constant `O(1)` extra memory.
- 🧾 Performs the minimum number of writes — ideal when memory writes are costly.

---

## ❌ Disadvantages

- 🐢 Slow for large datasets due to `O(n²)` time complexity.
- ⚠️ Not stable — equal elements may lose their original order.

---

## 📦 Real-Life Applications

| Application                                | Reason                                                                 |
|--------------------------------------------|------------------------------------------------------------------------|
| Teaching Algorithm Concepts                | Simple logic, easy to visualize.                                       |
| Small Lists                                | Overhead of complex algorithms isn't justified.                        |
| Embedded Systems                           | Memory writes are costly; Selection Sort minimizes them.              |
| Base for Advanced Algorithms (like Heap Sort)| Heap Sort builds upon selection technique.                           |

---

## 🧑‍💻 Python Implementation

```python
def selection_sort(ar):
    n=len(ar)
    for i in range(n-1):
        m_index = i
        for j in range(i+1,n):
            if ar[j] < ar[m_index]:
                m_index = j

        ar[i], ar[m_index] = ar[m_index], ar[i]

    return ar

def main():
    ar = list(map(int,input().split()))
    print(selection_sort(ar))

if __name__ == "__main__":
    main() 
```

