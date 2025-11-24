# Algorithm Repository

A comprehensive collection of algorithms and data structures implemented in Python. This repository serves as a learning resource and reference for common algorithmic problems and their solutions.

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Algorithms Implemented](#algorithms-implemented)
  - [Searching Algorithms](#searching-algorithms)
  - [Dynamic Programming](#dynamic-programming)
  - [Greedy Algorithms](#greedy-algorithms)
  - [Bit Manipulation](#bit-manipulation)
  - [Mathematical Algorithms](#mathematical-algorithms)
  - [String Algorithms](#string-algorithms)
- [Data Structures](#data-structures)
  - [Linear Data Structures](#linear-data-structures)
- [Games and Applications](#games-and-applications)
- [Getting Started](#getting-started)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains implementations of various algorithms and data structures commonly used in computer science and software engineering. Each implementation includes comments explaining the logic and approach, making it suitable for both learning and reference purposes.

## Repository Structure

```
Algorithm/
├── DataStructure/          # Data structure implementations
│   ├── linkedList.py      # Linked list implementation
│   └── stack.py           # Stack implementation
├── Binary_serach.py       # Binary and linear search algorithms
├── kadane's.py            # Kadane's algorithm for maximum subarray
├── GreedyAlgorithm.py     # Greedy algorithm examples (Knapsack)
├── bitmask.py             # Bit manipulation operations
├── Errichoto.py           # Fast exponentiation and modular arithmetic
├── Count_consonants.py    # String processing algorithm
├── tic-tak-toe.py         # Tic-tac-toe game implementation
└── README.md              # This file
```

## Algorithms Implemented

### Searching Algorithms

#### Binary Search (`Binary_serach.py`)

Binary search is an efficient algorithm for finding an element in a sorted list with O(log n) time complexity.

**Features:**
- Linear search implementation (O(n) complexity) for comparison
- Binary search implementation (O(log n) complexity)
- Performance comparison between both approaches
- Works only on sorted lists

**Key Concepts:**
- Divide and conquer approach
- Requires sorted input data
- Significantly faster than linear search for large datasets

**Time Complexity:** O(log n)  
**Space Complexity:** O(1)

### Dynamic Programming

#### Kadane's Algorithm (`kadane's.py`)

Kadane's algorithm finds the maximum sum of a contiguous subarray within a one-dimensional array of numbers.

**Features:**
- Efficient O(n) solution to the maximum subarray problem
- Handles negative numbers correctly
- Single pass through the array

**Use Cases:**
- Finding the best time to buy and sell stocks
- Maximum profit problems
- Analyzing time-series data

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

**Example:**
```python
Input: [-2, -3, 4, -1, -2, 5, 1, -3]
Output: 7  # Subarray [4, -1, -2, 5, 1]
```

### Greedy Algorithms

#### Fractional Knapsack (`GreedyAlgorithm.py`)

The fractional knapsack problem implementation using a greedy approach.

**Features:**
- Calculates value-to-weight ratio for optimal selection
- Allows taking fractions of items
- Maximizes total value within weight constraint

**Approach:**
1. Calculate value per unit weight for each item
2. Sort items by this ratio in descending order
3. Greedily select items with highest ratio first
4. Take fractions if necessary to fill remaining capacity

**Time Complexity:** O(n log n) due to sorting  
**Space Complexity:** O(n)

### Bit Manipulation

#### Bit Operations (`bitmask.py`)

Comprehensive guide to bit manipulation operations and techniques.

**Features:**
- Left shift operations (multiplication by powers of 2)
- Right shift operations (division by powers of 2)
- Checking if a specific bit is set
- Efficient bitwise operations

**Operations Covered:**
- **Left Shift (`<<`):** `x << k` equals `x * 2^k`
- **Right Shift (`>>`):** `x >> k` equals `x // 2^k`
- **Bit Checking:** Verify if the i-th bit is set using bitwise AND

**Use Cases:**
- Performance optimization
- Flag management
- Low-level programming
- Competitive programming

### Mathematical Algorithms

#### Fast Exponentiation (`Errichoto.py`)

Efficient algorithms for exponentiation and modular arithmetic operations.

**Features:**
- Fast exponentiation using binary method (O(log n))
- Modular arithmetic operations (addition, multiplication, subtraction)
- Performance comparison with built-in functions
- Optimization techniques for competitive programming

**Key Algorithms:**
1. **Binary Exponentiation:** Computes m^n in O(log n) time
2. **Modular Addition:** `(a + b) % m`
3. **Modular Multiplication:** `(a * b) % m`
4. **Modular Subtraction:** `(a - b) % m` with negative handling

**Time Complexity:** O(log n) for exponentiation  
**Space Complexity:** O(1)

### String Algorithms

#### Count Consonants and Vowels (`Count_consonants.py`)

Simple string processing algorithm to count vowels and consonants in a string.

**Features:**
- Case-insensitive counting
- Returns tuple with both counts
- Handles mixed case input

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## Data Structures

### Linear Data Structures

#### Linked List (`DataStructure/linkedList.py`)

A singly linked list implementation with common operations.

**Features:**
- Node-based structure
- Dynamic size
- Efficient insertion at beginning (prepend)
- Append operation to add at end
- Print functionality to display list

**Operations:**
- `append(data)`: Add element at the end - O(n)
- `prepend(data)`: Add element at the beginning - O(1)
- `printList()`: Display all elements - O(n)

**Use Cases:**
- Dynamic memory allocation
- Implementation of stacks and queues
- Undo functionality in applications

#### Stack (`DataStructure/stack.py`)

A stack implementation using Python lists with LIFO (Last In First Out) principle.

**Features:**
- Push operation to add elements
- Pop operation to remove elements
- Peek operation to view top element
- Check if stack is empty
- Get number of elements

**Operations:**
- `push(item)`: Add element to top - O(1)
- `pop()`: Remove and return top element - O(1)
- `showMeTheTop()`: View top element without removing - O(1)
- `isEmpty()`: Check if stack is empty - O(1)
- `numberOfElements()`: Get stack size - O(1)

**Use Cases:**
- Function call management
- Expression evaluation
- Backtracking algorithms
- Undo/Redo functionality

## Games and Applications

### Tic-Tac-Toe (`tic-tak-toe.py`)

A complete implementation of the classic Tic-Tac-Toe game for two players.

**Features:**
- Two-player gameplay
- Input validation
- Win condition checking (horizontal, vertical, diagonal)
- Interactive command-line interface
- Turn-based system

**Game Flow:**
1. Players enter their names
2. Players take turns selecting slots (1-9)
3. Board updates after each move
4. Game checks for win conditions after each turn
5. Winner is announced when conditions are met

**Win Conditions:**
- Three in a row horizontally
- Three in a row vertically
- Three in a row diagonally

## Getting Started

### Prerequisites

- Python 3.x installed on your system
- Basic understanding of Python programming
- Command line/terminal access

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Aman-Verma-28/Algorithm.git
```

2. Navigate to the repository:
```bash
cd Algorithm
```

3. Run any algorithm file:
```bash
python3 Binary_serach.py
python3 kadane's.py
python3 DataStructure/stack.py
```

## Usage Examples

### Binary Search Example

```python
from Binary_serach import bin_search

data = [1, 2, 3, 5, 6, 7, 8, 32, 45, 54, 75, 94]
target = 32

result = bin_search(data, target)
print(f"Element found: {result}")  # Output: True
```

### Kadane's Algorithm Example

```python
from kadane's import kadane

array = [-2, -3, 4, -1, -2, 5, 1, -3]
max_sum = kadane(array)
print(f"Maximum subarray sum: {max_sum}")  # Output: 7
```

### Stack Example

```python
from DataStructure.stack import Stack

s = Stack()
s.push("First")
s.push("Second")
s.push("Third")

print(f"Top element: {s.showMeTheTop()}")  # Output: Third
s.pop()
print(f"After pop: {s.showMeTheTop()}")    # Output: Second
```

### Linked List Example

```python
from DataStructure.linkedList import LinkedList

ll = LinkedList()
ll.append("Node1")
ll.append("Node2")
ll.prepend("Node0")
ll.printList()
# Output:
# Node0
# Node1
# Node2
```

### Bit Manipulation Example

```python
# Check if 3rd bit is set in number 13 (binary: 1101)
n = 13
i = 3
flag = 1 << i  # Left shift to create mask

if flag & n == flag:
    print("Bit is set")  # This will print
else:
    print("Bit is not set")
```

## Contributing

Contributions are welcome! If you'd like to add new algorithms or improve existing ones:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-algorithm`)
3. Make your changes
4. Add comments explaining your algorithm
5. Test your implementation
6. Commit your changes (`git commit -am 'Add new algorithm'`)
7. Push to the branch (`git push origin feature/new-algorithm`)
8. Create a Pull Request

### Guidelines

- Write clean, readable code
- Add comments explaining the logic
- Include time and space complexity analysis
- Provide usage examples
- Follow Python PEP 8 style guidelines
- Test your code thoroughly

## Learning Resources

To better understand the algorithms in this repository:

- **Binary Search:** [GeeksforGeeks Binary Search](https://www.geeksforgeeks.org/binary-search/)
- **Kadane's Algorithm:** [Maximum Subarray Problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
- **Greedy Algorithms:** [Introduction to Greedy Algorithms](https://www.geeksforgeeks.org/greedy-algorithms/)
- **Bit Manipulation:** [Bit Manipulation Tricks](https://www.geeksforgeeks.org/bits-manipulation-important-tactics/)
- **Data Structures:** [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

## Performance Considerations

When choosing an algorithm, consider:

1. **Time Complexity:** How the runtime scales with input size
2. **Space Complexity:** Memory requirements
3. **Input Characteristics:** Sorted vs unsorted, size, data type
4. **Use Case:** One-time operation vs repeated queries

## Future Enhancements

Planned additions to this repository:

- [ ] Sorting algorithms (Quick Sort, Merge Sort, Heap Sort)
- [ ] Graph algorithms (BFS, DFS, Dijkstra's)
- [ ] Tree data structures (Binary Tree, BST, AVL Tree)
- [ ] Advanced dynamic programming problems
- [ ] Hashing implementations
- [ ] More string algorithms (KMP, Rabin-Karp)
- [ ] Backtracking algorithms
- [ ] Unit tests for all implementations

## License

This project is open source and available for educational purposes. Feel free to use, modify, and distribute the code with proper attribution.

## Author

**Aman Verma** - [@Aman-Verma-28](https://github.com/Aman-Verma-28)

## Acknowledgments

- Thanks to the computer science community for algorithm documentation
- Inspired by classic algorithm textbooks and online resources
- Built for learning and educational purposes

---

**Note:** This repository is actively maintained and updated with new algorithms. Star ⭐ the repository to stay updated with new additions!

For questions, suggestions, or issues, please open an issue on GitHub.

---

*This README documentation is authored by Aman Verma.*
