# Collection Types in Python

## Introduction 📌

Python provides several built-in collection types that allow us to store, manage, and manipulate groups of data efficiently. These collection types include:

- **Lists** (`list`)
- **Tuples** (`tuple`)
- **Sets** (`set`, `frozenset`)
- **Dictionaries** (`dict`)
- **Deque** (`collections.deque`)
- **Named Tuple** (`collections.namedtuple`)
- **Default Dictionary** (`collections.defaultdict`)
- **Ordered Dictionary** (`collections.OrderedDict`)
- **Counter** (`collections.Counter`)

This document explores each type in detail with examples. 🚀

---

## 1. Lists 📋

A **list** is a mutable, ordered collection that can store heterogeneous data.

### Creating a List
```python
my_list = [1, 2, 3, 4, 5]  # List of integers
mixed_list = ["Hello", 10, 3.14, True]  # Mixed data types
```

### List Operations
```python
my_list.append(6)  # Adds an element at the end
my_list.insert(2, 99)  # Inserts 99 at index 2
my_list.remove(3)  # Removes the first occurrence of 3
my_list.pop()  # Removes the last element
print(my_list[1])  # Access element at index 1
```

### List Slicing
```python
sub_list = my_list[1:4]  # Get elements from index 1 to 3
```

---

## 2. Tuples 🔗

A **tuple** is an immutable, ordered collection that stores heterogeneous data.

### Creating a Tuple
```python
my_tuple = (1, 2, 3, "hello")
```

### Accessing Elements
```python
print(my_tuple[0])  # Accessing the first element
```

### Immutable Property
```python
my_tuple[0] = 100  # ❌ This will raise an error (tuples are immutable)
```

---

## 3. Sets 🎯

A **set** is an unordered collection of unique elements.

### Creating a Set
```python
my_set = {1, 2, 3, 4, 5}
```

### Set Operations
```python
my_set.add(6)  # Adds element 6
my_set.remove(3)  # Removes element 3
```

### Set Operations (Union, Intersection, Difference)
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # {1, 2, 3, 4, 5}
intersection_set = set1 & set2  # {3}
difference_set = set1 - set2  # {1, 2}
```

### Frozen Sets (Immutable Sets)
```python
frozen_set = frozenset({1, 2, 3})
frozen_set.add(4)  # ❌ This will raise an error
```

---

## 4. Dictionaries 🗂️

A **dictionary** is a key-value pair collection that is mutable and unordered (Python 3.6+ maintains insertion order).

### Creating a Dictionary
```python
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
```

### Dictionary Operations
```python
print(my_dict["name"])  # Accessing value by key
my_dict["age"] = 26  # Updating value
my_dict["country"] = "USA"  # Adding a new key-value pair
del my_dict["city"]  # Deleting a key-value pair
```

---

## 5. Deque (Double-Ended Queue) 🌀

A **deque** is an optimized list-like data structure that allows fast appends and pops from both ends.

```python
from collections import deque

my_deque = deque([1, 2, 3])
my_deque.append(4)  # Adds at the end
my_deque.appendleft(0)  # Adds at the beginning
my_deque.pop()  # Removes from the end
my_deque.popleft()  # Removes from the beginning
```

---

## 6. Named Tuple 🏷️

A **named tuple** provides a lightweight way to create classes with named fields.

```python
from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])
p1 = Person(name="Alice", age=25)
print(p1.name)  # Accessing by name
```

---

## 7. Default Dictionary 🏛️

A **defaultdict** returns a default value when accessing a missing key.

```python
from collections import defaultdict

def_dict = defaultdict(int)  # Default type is int
def_dict["count"] += 1  # Instead of raising KeyError, count is initialized to 0
```

---

## 8. Ordered Dictionary 📜

An **OrderedDict** maintains the insertion order of keys (default in Python 3.7+).

```python
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["b"] = 2
ordered_dict["a"] = 1
ordered_dict["c"] = 3
print(ordered_dict)  # {'b': 2, 'a': 1, 'c': 3}
```

---

## 9. Counter 🔢

A **Counter** is a specialized dictionary used for counting elements in an iterable.

```python
from collections import Counter

counter = Counter("banana")  # Counts occurrences of each character
print(counter)  # {'b': 1, 'a': 3, 'n': 2}
```

---

## Summary 📌

| Collection Type | Ordered? | Mutable? | Unique Elements? |
|----------------|---------|---------|----------------|
| List (`list`) | ✅ | ✅ | ❌ |
| Tuple (`tuple`) | ✅ | ❌ | ❌ |
| Set (`set`) | ❌ | ✅ | ✅ |
| Frozen Set (`frozenset`) | ❌ | ❌ | ✅ |
| Dictionary (`dict`) | ✅ | ✅ | Keys: ✅, Values: ❌ |
| Deque (`deque`) | ✅ | ✅ | ❌ |
| Named Tuple (`namedtuple`) | ✅ | ❌ | ❌ |
| Default Dictionary (`defaultdict`) | ✅ | ✅ | Keys: ✅, Values: ❌ |
| Ordered Dictionary (`OrderedDict`) | ✅ | ✅ | ❌ |
| Counter (`Counter`) | ✅ | ✅ | ❌ |

---

## Conclusion 🎯

Python provides a wide variety of **collection types**, each with unique features and use cases. Choosing the right one can significantly improve code efficiency and readability.

🚀 **Happy Coding!** 🚀
---
