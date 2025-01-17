# 🐍 Python List Operators: Problems and Solutions 🎉

Welcome to a fun and challenging guide to mastering Python list operators! 🌟 This readme contains 30 problems divided into **basic**, **intermediate**, and **advanced** categories—each with solutions and tons of emojis! 🚀 Let's dive in!

---

## 🌟 Basic Problems (Level 1) 📚

### 1. Append an Item 📝
**Problem:** Add the number `10` to the list `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
my_list.append(10)
print(my_list)  # Output: [1, 2, 3, 10]
```

---

### 2. Extend a List 🌱
**Problem:** Add `[4, 5]` to the list `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

---

### 3. Insert at a Specific Index 🎯
**Problem:** Insert `100` at index `2` in `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
my_list.insert(2, 100)
print(my_list)  # Output: [1, 2, 100, 3]
```

---

### 4. Remove an Item by Value 🧹
**Problem:** Remove `2` from `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)  # Output: [1, 3]
```

---

### 5. Pop the Last Item 🎈
**Problem:** Remove and return the last item from `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
last_item = my_list.pop()
print(my_list)  # Output: [1, 2]
print(last_item)  # Output: 3
```

---

### 6. Clear All Items 🧼
**Problem:** Remove all elements from `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []
```

---

### 7. Check Membership 🧐
**Problem:** Check if `2` is in `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
print(2 in my_list)  # Output: True
```

---

### 8. Find the Length 📏
**Problem:** Get the length of `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
print(len(my_list))  # Output: 3
```

---

### 9. Count Occurrences 🔢
**Problem:** Count the occurrences of `2` in `[1, 2, 2, 3]`.
```python
my_list = [1, 2, 2, 3]
print(my_list.count(2))  # Output: 2
```

---

### 10. Reverse the List 🔄
**Problem:** Reverse the list `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]
```

---

## 🌟 Intermediate Problems (Level 2) 🛠️

### 1. Copy a List 📋
**Problem:** Create a copy of `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
copy_list = my_list.copy()
print(copy_list)  # Output: [1, 2, 3]
```

---

### 2. Sort a List Ascending 🔼
**Problem:** Sort `[3, 1, 2]` in ascending order.
```python
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]
```

---

### 3. Sort a List Descending 🔽
**Problem:** Sort `[3, 1, 2]` in descending order.
```python
my_list = [3, 1, 2]
my_list.sort(reverse=True)
print(my_list)  # Output: [3, 2, 1]
```

---

### 4. Find the Maximum Value 🌟
**Problem:** Find the largest number in `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
print(max(my_list))  # Output: 3
```

---

### 5. Find the Minimum Value 🌟
**Problem:** Find the smallest number in `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
print(min(my_list))  # Output: 1
```

---

### 6. Slice a List ✂️
**Problem:** Get the first two elements of `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
slice_list = my_list[:2]
print(slice_list)  # Output: [1, 2]
```

---

### 7. Find the Index 🧭
**Problem:** Find the index of `2` in `[1, 2, 3]`.
```python
my_list = [1, 2, 3]
print(my_list.index(2))  # Output: 1
```

---

### 8. Multiply a List 🏗️
**Problem:** Repeat the list `[1, 2]` 3 times.
```python
my_list = [1, 2]
print(my_list * 3)  # Output: [1, 2, 1, 2, 1, 2]
```

---

### 9. Combine Two Lists 🔗
**Problem:** Combine `[1, 2]` and `[3, 4]`.
```python
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)  # Output: [1, 2, 3, 4]
```

---

### 10. Remove Duplicates ❌
**Problem:** Remove duplicates from `[1, 2, 2, 3]`.
```python
my_list = [1, 2, 2, 3]
unique_list = list(set(my_list))
print(unique_list)  # Output: [1, 2, 3]
```

---

## 🌟 Advanced Problems (Level 3) 🚀

### 1. Flatten a Nested List 🛠️
**Problem:** Flatten `[[1, 2], [3, 4]]` into `[1, 2, 3, 4]`.
```python
nested_list = [[1, 2], [3, 4]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4]
```

---

### 2. Find the Intersection of Two Lists 📊
**Problem:** Find common elements between `[1, 2, 3]` and `[2, 3, 4]`.
```python
list1 = [1, 2, 3]
list2 = [2, 3, 4]
intersection = [item for item in list1 if item in list2]
print(intersection)  # Output: [2, 3]
```

---

### 3. Split a List into Chunks 🍰
**Problem:** Split `[1, 2, 3, 4, 5, 6]` into chunks of size `2`.
```python
def chunk_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

my_list = [1, 2, 3, 4, 5, 6]
print(chunk_list(my_list, 2))  # Output: [[1, 2], [3, 4], [5, 6]]
```

---

### 4. Find the Union of Two Lists 🔗
**Problem:** Find unique elements across `[1, 2, 3]` and `[3, 4, 5]`.
```python
list1 = [1, 2, 3]
list2 = [3, 4, 5]
union = list(set(list1 + list2))
print(union)  # Output: [1, 2, 3, 4, 5]
```

---

### 5. Check for a Sublist 📑
**Problem:** Check if `[2, 3]` is a sublist of `[1, 2, 3, 4]`.
```python
def is_sublist(lst, sub):
    return any(lst[i:i+len(sub)] == sub for i in range(len(lst) - len(sub) + 1))

print(is_sublist([1, 2, 3, 4], [2, 3]))  # Output: True
```

---

### 6. Remove Items by Condition 🚮
**Problem:** Remove even numbers from `[1, 2, 3, 4, 5]`.
```python
my_list = [1, 2, 3, 4, 5]
filtered_list = [x for x in my_list if x % 2 != 0]
print(filtered_list)  # Output: [1, 3, 5]
```

---

### 7. Rotate a List 🔄
**Problem:** Rotate `[1, 2, 3, 4]` by 2 positions.
```python
def rotate_list(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

my_list = [1, 2, 3, 4]
print(rotate_list(my_list, 2))  # Output: [3, 4, 1, 2]
```

---

### 8. Find the Difference of Two Lists ❓
**Problem:** Find elements in `[1, 2, 3]` not in `[2, 3, 4]`.
```python
list1 = [1, 2, 3]
list2 = [2, 3, 4]
difference = [item for item in list1 if item not in list2]
print(difference)  # Output: [1]
```

---

### 9. Find the Index of All Occurrences 🧭
**Problem:** Find indices of `2` in `[1, 2, 3, 2, 4]`.
```python
my_list = [1, 2, 3, 2, 4]
indices = [i for i, x in enumerate(my_list) if x == 2]
print(indices)  # Output: [1, 3]
```

---

### 10. Cartesian Product of Two Lists ➕
**Problem:** Compute the Cartesian product of `[1, 2]` and `["a", "b"]`.
```python
list1 = [1, 2]
list2 = ["a", "b"]
product = [(x, y) for x in list1 for y in list2]
print(product)  # Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

---

Happy Coding! 🎉🐍
