
# Set Practice Problems with Solutions and Explanations 📝✨

Welcome to the Set Practice Problems repository! This README contains 10 interesting problems related to sets in Python, along with their solutions and detailed explanations. Let's dive in! 🚀

## Table of Contents 📖
1. [Problem 1: Creating a Set from a List](#problem-1-creating-a-set-from-a-list)
2. [Problem 2: Removing Duplicates from a List](#problem-2-removing-duplicates-from-a-list)
3. [Problem 3: Finding Common Elements in Two Lists](#problem-3-finding-common-elements-in-two-lists)
4. [Problem 4: Elements Unique to Each List](#problem-4-elements-unique-to-each-list)
5. [Problem 5: Checking for Supersets](#problem-5-checking-for-supersets)
6. [Problem 6: Difference of Sets](#problem-6-difference-of-sets)
7. [Problem 7: Symmetric Difference of Sets](#problem-7-symmetric-difference-of-sets)
8. [Problem 8: Checking Subsets](#problem-8-checking-subsets)
9. [Problem 9: Set Comprehensions](#problem-9-set-comprehensions)
10. [Problem 10: Frozensets](#problem-10-frozensets)

## Problem 1: Creating a Set from a List 🛠️
**Problem:** Convert a list of integers `[1, 2, 3, 4, 5, 1, 2]` to a set.

**Solution:**
```python
my_list = [1, 2, 3, 4, 5, 1, 2]
my_set = set(my_list)
print(my_set)
```
**Explanation:** Converting a list to a set removes any duplicate elements. This is useful for eliminating duplicates from a list. 📚

## Problem 2: Removing Duplicates from a List ➕
**Problem:** Given a list of integers with duplicates, return a new list with duplicates removed.

**Solution:**
```python
def remove_duplicates(input_list):
    return list(set(input_list))

input_list = [1, 2, 2, 3, 4, 4, 5]
output_list = remove_duplicates(input_list)
print(output_list)
```
**Explanation:** By converting the list to a set and back to a list, we remove any duplicate elements. This is a common way to ensure all elements in a list are unique. 🔄

## Problem 3: Finding Common Elements in Two Lists 🔍
**Problem:** Find common elements between two lists `[1, 2, 3, 4]` and `[3, 4, 5, 6]`.

**Solution:**
```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = set(list1).intersection(set(list2))
print(common_elements)
```
**Explanation:** The `intersection()` method returns a set of elements that are common to both input sets. This is useful for finding shared items between two collections. 🎯

## Problem 4: Elements Unique to Each List 🔄
**Problem:** Find elements that are unique to each of the lists `[1, 2, 3, 4]` and `[3, 4, 5, 6]`.

**Solution:**
```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
unique_elements = set(list1).symmetric_difference(set(list2))
print(unique_elements)
```
**Explanation:** The `symmetric_difference()` method returns a set of elements that are in either of the sets but not in both. This is useful for finding differences between two collections. 🌀

## Problem 5: Checking for Supersets ✅
**Problem:** Check if the set `{1, 2, 3}` is a superset of `{1, 2}`.

**Solution:**
```python
set1 = {1, 2, 3}
set2 = {1, 2}
is_superset = set1.issuperset(set2)
print(is_superset)
```
**Explanation:** The `issuperset()` method returns `True` if the first set contains all elements of the second set. This is useful for verifying hierarchical relationships between sets. 💎

## Problem 6: Difference of Sets ↔️
**Problem:** Find the difference between sets `{1, 2, 3}` and `{2, 3, 4}`.

**Solution:**
```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
difference_set = set1.difference(set2)
print(difference_set)
```
**Explanation:** The `difference()` method returns a new set with elements that are in the first set but not in the second set. ➖

## Problem 7: Symmetric Difference of Sets 🔄
**Problem:** Find the symmetric difference between sets `{1, 2, 3}` and `{2, 3, 4}`.

**Solution:**
```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)
```
**Explanation:** The `symmetric_difference()` method returns a new set with elements that are in either of the sets, but not in both. 🔄

## Problem 8: Checking Subsets ✅
**Problem:** Check if `{1, 2}` is a subset of `{1, 2, 3}`.

**Solution:**
```python
set1 = {1, 2}
set2 = {1, 2, 3}
is_subset = set1.issubset(set2)
print(is_subset)
```
**Explanation:** The `issubset()` method returns `True` if all elements of the first set are in the second set. ✅

## Problem 9: Set Comprehensions 🧠
**Problem:** Create a set of squares of numbers from 1 to 5.

**Solution:**
```python
squares_set = {x**2 for x in range(1, 6)}
print(squares_set)
```
**Explanation:** Set comprehensions allow for creating sets using a concise syntax. This example creates a set of squares of numbers from 1 to 5. 🔢

## Problem 10: Frozensets ❄️
**Problem:** Create a frozenset with the elements 1, 2, and 3.

**Solution:**
```python
frozen_set = frozenset([1, 2, 3])
print(frozen_set)
```
**Explanation:** A frozenset is an immutable version of a set. Once created, elements cannot be added or removed. ❄️

---

I hope these problems and solutions help you understand and practice working with sets in Python! Happy coding! 😃👩‍💻👨‍💻
