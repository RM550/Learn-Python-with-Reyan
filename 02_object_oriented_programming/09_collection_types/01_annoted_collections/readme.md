# Annotated Collections in Python

## Introduction 📌

Annotated collections in Python leverage **type hints** from the `typing` module to enhance code readability, maintainability, and correctness. By explicitly specifying the expected data types in collections, we make the code more robust and easier to understand.

Python provides various ways to annotate collections, including:

- **Lists** (`list` or `List[T]`)
- **Tuples** (`tuple` or `Tuple[T, ...]`)
- **Sets** (`set` or `Set[T]`)
- **Dictionaries** (`dict` or `Dict[K, V]`)
- **Frozen Sets** (`frozenset` or `FrozenSet[T]`)
- **Typed Deques** (`Deque[T]`)
- **Typed Named Tuples** (`NamedTuple`)
- **Typed Default Dictionaries** (`DefaultDict[K, V]`)
- **Typed Ordered Dictionaries** (`OrderedDict[K, V]`)
- **Typed Counters** (`Counter[T]`)

This document explores each annotation in detail. 🚀

---

## 1. Annotating Lists 📋

A **list** is an ordered, mutable collection. Type annotations ensure consistency in data types.

```python
from typing import List

def get_names() -> List[str]:
    return ["Alice", "Bob", "Charlie"]
```

Here, `List[str]` indicates that the function returns a list of strings.

---

## 2. Annotating Tuples 🔗

A **tuple** is an immutable, ordered collection. Tuples can be of fixed length with specific types or variable-length.

### Fixed-length Tuple Annotation
```python
from typing import Tuple

def get_person() -> Tuple[str, int]:
    return ("Alice", 30)
```

Here, `Tuple[str, int]` ensures the first element is a string and the second is an integer.

### Variable-length Tuple Annotation
```python
from typing import Tuple

def get_coordinates() -> Tuple[int, ...]:
    return (10, 20, 30, 40)
```

`Tuple[int, ...]` allows an arbitrary number of integers.

---

## 3. Annotating Sets 🎯

A **set** is an unordered collection of unique elements.

```python
from typing import Set

def get_unique_numbers() -> Set[int]:
    return {1, 2, 3, 4, 5}
```

Here, `Set[int]` ensures the set contains only integers.

---

## 4. Annotating Dictionaries 🗂️

A **dictionary** is a key-value collection.

```python
from typing import Dict

def get_student_scores() -> Dict[str, int]:
    return {"Alice": 90, "Bob": 85}
```

Here, `Dict[str, int]` ensures that keys are strings and values are integers.

---

## 5. Annotating Frozen Sets ❄️

A **frozen set** is an immutable version of a set.

```python
from typing import FrozenSet

def get_constants() -> FrozenSet[str]:
    return frozenset({"PI", "E"})
```

Here, `FrozenSet[str]` ensures all elements are strings.

---

## 6. Annotating Deques 🌀

A **deque** is a double-ended queue optimized for fast appends and pops.

```python
from typing import Deque
from collections import deque

def get_recent_logs() -> Deque[str]:
    return deque(["Log1", "Log2", "Log3"])
```

Here, `Deque[str]` ensures the deque contains only strings.

---

## 7. Annotating Named Tuples 🏷️

A **named tuple** provides named fields for tuple-like objects.

```python
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    age: int

def get_person() -> Person:
    return Person(name="Alice", age=30)
```

This ensures `Person` objects always contain a `name` (str) and an `age` (int).

---

## 8. Annotating Default Dictionaries 🏛️

A **defaultdict** provides default values for missing keys.

```python
from typing import DefaultDict
from collections import defaultdict

def get_default_scores() -> DefaultDict[str, int]:
    return defaultdict(int, {"Alice": 90})
```

Here, `DefaultDict[str, int]` ensures keys are strings and values are integers.

---

## 9. Annotating Ordered Dictionaries 📜

An **OrderedDict** maintains insertion order.

```python
from typing import OrderedDict
from collections import OrderedDict

def get_ordered_items() -> OrderedDict[str, int]:
    return OrderedDict({"apple": 5, "banana": 3})
```

This ensures keys are strings and values are integers.

---

## 10. Annotating Counters 🔢

A **Counter** counts occurrences of elements.

```python
from typing import Counter
from collections import Counter

def get_char_counts() -> Counter[str]:
    return Counter("banana")
```

Here, `Counter[str]` ensures elements being counted are strings.

---

## Summary 📌

| Collection Type | Annotation Syntax | Example |
|---------------|----------------|---------|
| List | `List[T]` | `List[int]` |
| Tuple (fixed) | `Tuple[T1, T2]` | `Tuple[str, int]` |
| Tuple (variable) | `Tuple[T, ...]` | `Tuple[int, ...]` |
| Set | `Set[T]` | `Set[str]` |
| Frozen Set | `FrozenSet[T]` | `FrozenSet[int]` |
| Dictionary | `Dict[K, V]` | `Dict[str, int]` |
| Deque | `Deque[T]` | `Deque[float]` |
| Named Tuple | `NamedTuple` | `NamedTuple("Person", [("name", str), ("age", int)])` |
| Default Dict | `DefaultDict[K, V]` | `DefaultDict[str, int]` |
| Ordered Dict | `OrderedDict[K, V]` | `OrderedDict[str, int]` |
| Counter | `Counter[T]` | `Counter[str]` |

---

## Conclusion 🎯

Using **annotated collections** improves code clarity, enforces type safety, and makes debugging easier. By utilizing the `typing` module, we ensure our collections hold consistent data types, leading to more maintainable and error-free code. 🚀🐍

🚀 **Happy Coding!** 🚀

