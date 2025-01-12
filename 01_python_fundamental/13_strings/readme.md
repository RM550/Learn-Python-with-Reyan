# Python Strings 🐍✨

Strings in Python are sequences of characters enclosed in single quotes `'...'`, double quotes `"..."`, or triple quotes `'''...'''` / `"""..."""`. Strings are one of the most commonly used data types in Python. Let's explore! 🚀✨

---

## What are Strings? 🤔✨

A **string** is a collection of characters. It can include letters, numbers, and symbols. For example: ✨🐍

```python
name = "Reyan Mumtaz"  # A simple string ✍️✨
quote = 'Never give up!'  # Another example 💪🔥
multiline = '''This is 
a multiline 
string.'''  # Multiline string 📜✨
```

---

## Types of Strings 📝✨

1. **Single-quoted Strings**: `'Hello'` 🖋️✨
2. **Double-quoted Strings**: `"Hello"` ✍️✨
3. **Triple-quoted Strings**: `'''Hello'''` or `"""Hello"""` (for multiline strings) 📜✨

Example:

```python
# Single-quoted string 🖋️
single = 'Single Quote' ✨

# Double-quoted string ✍️
double = "Double Quote" ✨

# Multiline string 📜
multiline = '''This is 
multiline!''' ✨

print(single, double, multiline)  # Output example 🖨️
```

---

## Common String Operations 🛠️✨

### 1. String Concatenation ➕✨
Combine two or more strings using `+`. 🎉

```python
first = "Hello"  # First word 🌟
second = "World"  # Second word 🌍
result = first + " " + second  # Combining with a space ✨
print(result)  # Output: Hello World 🖨️
```

### 2. String Repetition ✨✨✨
Repeat strings using `*`. 🎢

```python
repeat = "Python " * 3  # Repeating three times 🌀
print(repeat)  # Output: Python Python Python 🎉
```

### 3. String Indexing 🔢✨
Access individual characters using their index. 🎯

```python
text = "Python"  # A string example 🐍
print(text[0])  # Output: P 🅿️
print(text[-1])  # Output: n (last character) ✨
```

### 4. String Slicing 🍰✨
Extract parts of a string using slices. 🔪✨

```python
text = "Python Programming"  # Another example ✍️
print(text[0:6])  # Output: Python 🐍
print(text[7:])  # Output: Programming 🖋️
```

---

## String Methods 🧰✨

Here are some common methods with examples: 🛠️✨

1. **`.lower()`**: Converts to lowercase. 🔡✨

    ```python
    print("HELLO".lower())  # Output: hello 🌟
    ```

2. **`.upper()`**: Converts to uppercase. 🔠✨

    ```python
    print("hello".upper())  # Output: HELLO 🌟
    ```

3. **`.strip()`**: Removes leading and trailing spaces. 🧹✨

    ```python
    print("  Python  ".strip())  # Output: Python 🖨️
    ```

4. **`.replace()`**: Replaces a substring with another. 🔄✨

    ```python
    print("I love Java".replace("Java", "Python"))  # Output: I love Python 🐍✨
    ```

5. **`.find()`**: Finds the first occurrence of a substring. 🔍✨

    ```python
    print("Hello World".find("World"))  # Output: 6 📍
    ```

6. **`.split()`**: Splits the string into a list based on a delimiter. 📂✨

    ```python
    print("a,b,c".split(","))  # Output: ['a', 'b', 'c'] 📄
    ```

7. **`.join()`**: Joins elements of a list into a string. 🔗✨

    ```python
    print("-".join(["a", "b", "c"]))  # Output: a-b-c 🧩
    ```

---

## Formatting Strings 🎨✨

You can format strings using **f-strings**, `.format()`, or `%` formatting. 🖌️✨

### 1. F-strings 🖋️✨

```python
name = "Reyan"  # Example name ✨
age = 16  # Example age 🔢
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Reyan and I am 16 years old. 🎉
```

### 2. `.format()` Method ✍️✨

```python
text = "My name is {} and I am {} years old.".format("Reyan", 16)  # Placeholder replacement ✨
print(text)  # Output: My name is Reyan and I am 16 years old. 🎉
```

### 3. `%` Formatting 🌀✨

```python
name = "Reyan"  # Placeholder example 📋
age = 16  # Placeholder example 🔢
print("My name is %s and I am %d years old." % (name, age))  # Output: My name is Reyan and I am 16 years old. 🎊
```

---

## Escape Sequences 🚪✨

Escape sequences allow you to include special characters in strings. ✨🎭

| Escape Sequence | Description                   | Example Output    |
|-----------------|-------------------------------|-------------------|
| `\n`           | Newline                      | Hello\nWorld       |
| `\t`           | Tab                          | Hello\tWorld       |
| `\\`           | Backslash                    | Hello\\World       |
| `\'`           | Single Quote                 | It\'s Python!     |
| `\"`           | Double Quote                 | He said \"Hello\". |

Example:

```python
print("Hello\nWorld")  # Newline example ✨
print("Hello\tWorld")  # Tab example ✨
print("It\'s Python!")  # Single quote example ✨
print("He said \"Hello\".")  # Double quote example ✨
```

---

## Examples 🌟✨

### Example 1: Palindrome Checker 🔄✨

```python
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")  # Cleanup text ✨
    return cleaned == cleaned[::-1]  # Check if reversed is the same ✨

print(is_palindrome("Racecar"))  # Output: True 🎉
```

### Example 2: Word Frequency Counter 🖋️✨

```python
text = "apple banana apple orange banana apple"  # Example string ✨
words = text.split()  # Split into words 📂
frequency = {word: words.count(word) for word in set(words)}  # Count occurrences ✨
print(frequency)  # Output: {'orange': 1, 'banana': 2, 'apple': 3} 📊
```

### Example 3: Count Vowels 🔡✨

```python
def count_vowels(text):
    vowels = "aeiou"  # Define vowels 🌀
    return sum(1 for char in text.lower() if char in vowels)  # Count matches ✨

print(count_vowels("Hello World"))  # Output: 3 🎉
```

---

Feel free to experiment with these examples and become a string wizard! 🧙‍♂️✨✨✨
