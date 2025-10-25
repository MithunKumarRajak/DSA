# Data Structures and Algorithms Notes

------------------------Day 1 - Basic Sorting Algorithms--------------------------

## 1. Bubble Sort

**Definition:**  
Repeatedly compares adjacent elements and swaps them if they are in the wrong order. The largest element “bubbles” to its correct position in each pass.

**How it Works:**  

1. Compare adjacent elements.  
2. Swap if needed (ascending order: left > right).  
3. Repeat for n-1 passes or until no swaps occur.

**Summary:**  

- Simple and easy to understand.  
- Inefficient for large datasets (O(n²)).  

## 2. Cocktail Shaker Sort

**Definition:**  
Cocktail Shaker Sort (also called Bidirectional Bubble Sort) is a variation of Bubble Sort that sorts the array in both directions on each pass:

**How it Works:**  

1. Left → Right: push largest element to end.  
2. Right → Left: push smallest element to beginning.  
3. Repeat until no swaps occur.

**Summary:**  

- Slightly more efficient than Bubble Sort for certain arrays.  
- O(n²) time complexity.  

## 3. Insertion Sort

**Definition:**
Builds a sorted portion of the array by inserting the next element at its correct position in the sorted part.

**How it Works:**  

1. Take next element.  
2. Compare with sorted portion.  
3. Shift larger elements to the right.  
4. Insert current element at correct position.  

**Summary:**  

- In-place and stable.  
- Efficient for small or nearly sorted arrays.  
- Introduces element shifting instead of repeated swapping.  

## Key

Bubble Sort → teaches swapping & simple logic

----------------------------------------Day 2 - Advanced Sorting Algorithms ----------------------------

### Cocktail Shaker Sort (Bidirectional Bubble Sort) Summary

## 1. Definition

Cocktail Shaker Sort is an improvement over Bubble Sort that sorts an array in **both directions**:

- **Forward pass:** pushes the largest element to the right.
- **Backward pass:** moves the smallest element to the left.

Also called **Bidirectional Bubble Sort** or **Shaker Sort**.

## 2. How It Works

1. Start with `start = 0` and `end = n - 1`.
2. Repeat until no swaps occur or `start < end`:
   - **Forward pass (left → right)**:
     - Compare adjacent elements.
     - Swap if the left element is greater.
     - Largest element “bubbles” to the end.
   - **Backward pass (right → left)**:
     - Compare adjacent elements from right to left.
     - Swap if the left element is greater.
     - Smallest element “sinks” to the start.
   - Narrow the range: `start += 1`, `end -= 1`.

# Key Features :-

Forward and Backward Passes – each full pass handles two elements (largest + smallest).
Reduces Number of Passes – compared to Bubble Sort, reduces the number of passes roughly by half
Works on Small Arrays Efficiently – good for educational purposes or small datasets.
Detects Sorted Array Early – avoids unnecessary comparisons with the swapped flag.

----------------------------------------Day 3 - Selection Sort ----------------------------


