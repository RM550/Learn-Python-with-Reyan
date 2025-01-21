# Python Dictionaries 🔎

Welcome to this comprehensive guide on **Python Dictionaries**! 📚 In this document, we will dive deep into dictionaries, one of the most powerful and versatile data structures in Python. Let's get started! 🚀

---

## What is a Dictionary? 🔧

A **dictionary** in Python is an **unordered collection** of data that is stored as **key-value pairs**. It allows you to store, retrieve, and manipulate data efficiently using unique keys. Unlike lists or tuples, dictionaries do not store elements in a specific order.

### Syntax 🗒
```python
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
```

- **Keys**: Must be unique and immutable (e.g., strings, numbers, or tuples).
- **Values**: Can be of any data type and do not need to be unique.

---

## Creating a Dictionary 🌐

### Empty Dictionary
```python
empty_dict = {}
print(empty_dict)  # Output: {}
```

### With Data
```python
person = {
    "name": "Reyan",
    "age": 16,
    "hobbies": ["coding", "cricket", "reading"]
}
print(person)
```

### Using `dict()` Constructor 🏗️
```python
another_dict = dict(name="Ali", age=18, hobby="gaming")
print(another_dict)  # Output: {'name': 'Ali', 'age': 18, 'hobby': 'gaming'}
```

---

## Accessing Elements 🔐

You can access dictionary values using their keys.

### Using Brackets
```python
person = {"name": "Reyan", "age": 16}
print(person["name"])  # Output: Reyan
```

### Using `get()` Method
The `get()` method is safer because it doesn’t raise an error if the key doesn’t exist.
```python
print(person.get("age"))  # Output: 16
print(person.get("address", "Not Found"))  # Output: Not Found
```

### Checking if a Key Exists 🧐
```python
if "name" in person:
    print("Key 'name' exists!")
```

---

## Modifying a Dictionary ✏️

### Adding Items
```python
person["gender"] = "male"
print(person)  # {'name': 'Reyan', 'age': 16, 'gender': 'male'}
```

### Updating Items
```python
person["age"] = 17
print(person)  # {'name': 'Reyan', 'age': 17}
```

### Using `update()` Method 🔄
```python
person.update({"city": "Lahore", "country": "Pakistan"})
print(person)  # {'name': 'Reyan', 'age': 17, 'gender': 'male', 'city': 'Lahore', 'country': 'Pakistan'}
```

---

## Removing Items ❌

### Using `pop()`
```python
age = person.pop("age")
print(age)  # Output: 16
print(person)  # {'name': 'Reyan'}
```

### Using `del`
```python
del person["name"]
print(person)  # {}
```

### Using `popitem()`
Removes the last inserted key-value pair (in Python 3.7+).
```python
person = {"name": "Reyan", "age": 16}
person.popitem()
print(person)  # {'name': 'Reyan'}
```

### Clearing All Items 🧹
```python
person.clear()
print(person)  # Output: {}
```

---

## Looping Through a Dictionary ⏯️

### Keys Only
```python
for key in person.keys():
    print(key)
```

### Values Only
```python
for value in person.values():
    print(value)
```

### Keys and Values
```python
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")
```

---

## Dictionary Methods ⚙️

Here are some commonly used dictionary methods:

| Method            | Description                                   |
|-------------------|-----------------------------------------------|
| `clear()`         | Removes all elements.                        |
| `copy()`          | Returns a shallow copy of the dictionary.    |
| `fromkeys()`      | Creates a dictionary from a sequence.        |
| `get()`           | Returns the value of a key if it exists.     |
| `items()`         | Returns a view of key-value pairs.           |
| `keys()`          | Returns a view of dictionary keys.           |
| `pop()`           | Removes and returns an item by key.          |
| `popitem()`       | Removes the last inserted key-value pair.    |
| `setdefault()`    | Returns the value of a key and sets it if missing. |
| `update()`        | Updates the dictionary with key-value pairs. |
| `values()`        | Returns a view of dictionary values.         |

### Example
```python
person = {"name": "Reyan", "age": 16}
keys = person.keys()
print(keys)  # Output: dict_keys(['name', 'age'])
```

---

## Dictionary Comprehensions 🍄

You can create dictionaries dynamically using **dictionary comprehensions**.

### Example
```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Filtering with Comprehensions 🔍
```python
filtered = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(filtered)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

---

## Nesting Dictionaries 🌐

You can nest dictionaries to create complex data structures.

### Example
```python
users = {
    "user1": {"name": "Reyan", "age": 16},
    "user2": {"name": "Ali", "age": 18}
}
print(users["user1"]["name"])  # Output: Reyan
```

### Adding Nested Data 🏗️
```python
users["user3"] = {"name": "Sara", "age": 20}
print(users)
```

---

## Summary 🔍

- Dictionaries store data in key-value pairs.
- Keys must be unique and immutable.
- Values can be any data type.
- They are unordered, but in Python 3.7+, they maintain insertion order.
- Methods like `update()`, `get()`, and comprehensions make them powerful tools.

---

Feel free to experiment and explore dictionaries in Python. Happy coding! 🚀

