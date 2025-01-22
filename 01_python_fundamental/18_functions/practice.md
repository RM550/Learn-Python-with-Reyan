# 🧠 **11 Advanced Python Functions: Problems, Solutions, and Explanations** 🚀  

Python offers many advanced functions to make your coding life easier! 💻 In this guide, we’ll tackle 11 key functions, solve problems, and explain how they work—complete with examples and emojis! 🐍✨  

---

## 🔢 **1. `map()` Function**  
The `map()` function applies a given function to all items in an iterable (like a list).  

### 🚨 Problem:  
You have a list of numbers, and you want to double each number.  

### ✅ Solution:  
```python  
nums = [1, 2, 3, 4]  
doubled = list(map(lambda x: x * 2, nums))  
print(doubled)  # Output: [2, 4, 6, 8]  
```  

### 💡 Explanation:  
- The `lambda` function doubles each number.  
- `map()` applies this function to every item in the list.  

---

## 🧮 **2. `filter()` Function**  
The `filter()` function filters items based on a condition.  

### 🚨 Problem:  
Filter even numbers from a list.  

### ✅ Solution:  
```python  
nums = [1, 2, 3, 4, 5, 6]  
evens = list(filter(lambda x: x % 2 == 0, nums))  
print(evens)  # Output: [2, 4, 6]  
```  

### 💡 Explanation:  
- The `lambda` checks if each number is even.  
- `filter()` includes only those items that meet the condition.  

---

## 🎯 **3. `reduce()` Function**  
The `reduce()` function (from `functools`) reduces a list to a single value.  

### 🚨 Problem:  
Find the product of all numbers in a list.  

### ✅ Solution:  
```python  
from functools import reduce  

nums = [1, 2, 3, 4]  
product = reduce(lambda x, y: x * y, nums)  
print(product)  # Output: 24  
```  

### 💡 Explanation:  
- `reduce()` applies the `lambda` to pairs of numbers until one result remains.  

---

## 📊 **4. `zip()` Function**  
The `zip()` function combines two or more iterables into tuples.  

### 🚨 Problem:  
Combine two lists of names and scores.  

### ✅ Solution:  
```python  
names = ["Alice", "Bob", "Charlie"]  
scores = [85, 92, 78]  

combined = list(zip(names, scores))  
print(combined)  # Output: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]  
```  

### 💡 Explanation:  
- `zip()` pairs items from multiple lists together.  

---

## 🧵 **5. `enumerate()` Function**  
The `enumerate()` function adds an index to an iterable.  

### 🚨 Problem:  
Print items in a list with their indexes.  

### ✅ Solution:  
```python  
fruits = ["apple", "banana", "cherry"]  
for index, fruit in enumerate(fruits):  
    print(f"{index}: {fruit}")  
```  

### 💡 Explanation:  
- `enumerate()` returns both the index and the value for each item.  

---

## 🔢 **6. `all()` and `any()` Functions**  

- `all()` returns `True` if all items in an iterable are `True`.  
- `any()` returns `True` if **at least one** item is `True`.  

### 🚨 Problem:  
Check if all or any numbers in a list are positive.  

### ✅ Solution:  
```python  
nums = [1, 2, 3, -4]  

print(all(x > 0 for x in nums))  # Output: False  
print(any(x > 0 for x in nums))  # Output: True  
```  

### 💡 Explanation:  
- `all()` checks the condition for all items.  
- `any()` checks for at least one.  

---

## 🖇️ **7. `sorted()` Function**  
The `sorted()` function sorts an iterable.  

### 🚨 Problem:  
Sort a list of dictionaries by a key.  

### ✅ Solution:  
```python  
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}]  
sorted_people = sorted(people, key=lambda x: x["age"])  
print(sorted_people)  # Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}]  
```  

### 💡 Explanation:  
- The `key` argument determines the sorting logic.  

---

## 🎛️ **8. `reversed()` Function**  
The `reversed()` function reverses an iterable.  

### 🚨 Problem:  
Reverse a list.  

### ✅ Solution:  
```python  
nums = [1, 2, 3, 4]  
reversed_nums = list(reversed(nums))  
print(reversed_nums)  # Output: [4, 3, 2, 1]  
```  

### 💡 Explanation:  
- `reversed()` creates an iterator that moves backward.  

---

## 📜 **9. `isinstance()` Function**  
The `isinstance()` function checks if an object is of a specific type.  

### 🚨 Problem:  
Check if a variable is a string.  

### ✅ Solution:  
```python  
x = "Hello"  
print(isinstance(x, str))  # Output: True  
```  

### 💡 Explanation:  
- `isinstance()` is used for type checking.  

---

## 🧑‍💻 **10. `eval()` Function**  
The `eval()` function evaluates a string as Python code.  

### 🚨 Problem:  
Calculate the result of a string expression.  

### ✅ Solution:  
```python  
expression = "2 + 3 * 4"  
result = eval(expression)  
print(result)  # Output: 14  
```  

### 💡 Explanation:  
- Use with caution, as `eval()` can execute arbitrary code.  

---

## 🔮 **11. `lambda` Functions**  
`lambda` creates small, anonymous functions.  

### 🚨 Problem:  
Sort a list of tuples by the second value.  

### ✅ Solution:  
```python  
data = [(1, 3), (2, 1), (4, 2)]  
sorted_data = sorted(data, key=lambda x: x[1])  
print(sorted_data)  # Output: [(2, 1), (4, 2), (1, 3)]  
```  

### 💡 Explanation:  
- `lambda` is a concise way to define a simple function.  

---

## 🌟 **Summary**  

Here are the 11 functions we covered:  
1. `map()` 🗺️  
2. `filter()` 🚿  
3. `reduce()` ➖  
4. `zip()` 🔗  
5. `enumerate()` 🔢  
6. `all()` and `any()` 🤔  
7. `sorted()` 🔠  
8. `reversed()` ↩️  
9. `isinstance()` 🔍  
10. `eval()` ✨  
11. `lambda` 🚀  

These functions make your Python code concise, efficient, and elegant. 🎉  

---
