# Changing the Search Module in Python 🔍

This guide will help you understand how to modify and enhance the search functionality in Python. We’ll be exploring built-in modules, customizing search behavior, and creating your own search functions. Let’s dive into the details! 💻🔧

---

### Table of Contents 📚
1. [Introduction to Search in Python](#introduction-to-search-in-python)
2. [Using Built-in Search Modules](#using-built-in-search-modules)
   - `find()`
   - `index()`
   - `in` Keyword
3. [Customizing Search Logic](#customizing-search-logic)
   - Case Insensitivity 🅰️🅾️
   - Searching in Lists and Dictionaries 📜🔍
4. [Regular Expressions in Search 🔎](#regular-expressions-in-search)
5. [Creating Your Own Search Function 🛠️](#creating-your-own-search-function)
6. [Conclusion](#conclusion)

---

## Introduction to Search in Python 🎯

Python provides various ways to search for elements within strings, lists, or other data structures. You can use built-in methods or even create your own search functions. In Python, searching means looking for a pattern, value, or condition inside an iterable like strings, lists, or dictionaries.

When dealing with text, searching can mean finding substrings in a string or looking for specific words or patterns. For lists and dictionaries, it’s about searching for a value or key.

---

## Using Built-in Search Modules 🛠️

### `find()` Method 🔎

The `find()` method allows you to search for a substring in a string. It returns the index of the first occurrence of the substring. If not found, it returns `-1`.

```python
text = "Hello, welcome to Python!"
result = text.find("Python")
print(result)  # Output: 18
```

#### Explanation:
- It searches for the substring `"Python"` within the string `text`.
- Returns `18`, which is the starting index of `"Python"`.

### `index()` Method 📌

Similar to `find()`, but `index()` raises an exception (`ValueError`) if the substring is not found.

```python
text = "Hello, welcome to Python!"
result = text.index("Python")
print(result)  # Output: 18
```

#### Explanation:
- `index()` will return the position of the substring just like `find()`.
- If the substring is not found, it raises an exception: `ValueError`.

### `in` Keyword 🔍

This is the simplest way to check if a substring exists in a string or a value exists in a list. It returns a boolean value: `True` or `False`.

```python
text = "Hello, welcome to Python!"
result = "Python" in text
print(result)  # Output: True
```

#### Explanation:
- This method returns `True` if the substring `"Python"` exists in `text`, otherwise `False`.

---

## Customizing Search Logic 🧠

### Case Insensitivity 🅰️🅾️

If you want to make the search case-insensitive, you can convert both the search term and the string to lower case (or upper case) before searching.

```python
text = "Hello, Welcome to Python!"
search_term = "hello"

result = search_term.lower() in text.lower()
print(result)  # Output: True
```

#### Explanation:
- Converting both the `text` and `search_term` to lowercase ensures that the search works regardless of case.

### Searching in Lists and Dictionaries 📜🔍

For **lists**, you can use the `in` operator to search for a specific element:

```python
my_list = [1, 2, 3, 4, 5]
search_value = 3

result = search_value in my_list
print(result)  # Output: True
```

#### Explanation:
- It checks if `3` is in the list `my_list`. Returns `True` if found, `False` otherwise.

For **dictionaries**, you search for a key:

```python
my_dict = {"name": "John", "age": 30}
search_key = "age"

result = search_key in my_dict
print(result)  # Output: True
```

#### Explanation:
- This checks if the key `"age"` exists in the dictionary `my_dict`.

---

## Regular Expressions in Search 🔎

For more advanced search patterns, Python provides the `re` module, which allows you to search for complex patterns.

Example of searching for any word starting with 'p' in a string:

```python
import re

text = "Python is powerful and fun"
pattern = r"\bp\w*"

matches = re.findall(pattern, text, flags=re.IGNORECASE)
print(matches)  # Output: ['Python', 'powerful']
```

#### Explanation:
- `\b` is a word boundary.
- `p\w*` matches any word starting with 'p'.
- `re.IGNORECASE` makes the search case-insensitive.

---

## Creating Your Own Search Function 🛠️

If you need to customize the search functionality further, you can create your own function. For example, let’s write a function that searches for a value and returns the index or `-1` if not found.

```python
def custom_search(sequence, search_item):
    for i, item in enumerate(sequence):
        if item == search_item:
            return i
    return -1

# Test with a list
my_list = [10, 20, 30, 40]
result = custom_search(my_list, 30)
print(result)  # Output: 2
```

#### Explanation:
- The function `custom_search()` searches for the `search_item` in the `sequence`.
- It returns the index of the first occurrence of the item, or `-1` if not found.

---

## Conclusion 🎉

In this guide, we covered different ways to perform searches in Python using built-in methods like `find()`, `index()`, and the `in` keyword. We also discussed how to customize searches for case insensitivity, search lists, and dictionaries, and introduced regular expressions for more complex patterns.

With this knowledge, you can now create efficient and tailored search functionality for your Python applications! 🚀

---

Happy coding! 😎
