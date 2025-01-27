# Regular Expressions in Python 🎯

Regular Expressions (regex or regexp) are sequences of characters that define a search pattern. Python provides a built-in module, `re`, to work with regular expressions effectively. Regular expressions are widely used for string searching, validation, parsing, and text manipulation. 🧩

## Importing the `re` Module 🚀
To use regex in Python, first import the `re` module:

```python
import re
```

## Basic Syntax 📜
Here are some common regex elements:

| Pattern | Description |
|---------|-------------|
| `.`     | Matches any character except a newline. |
| `^`     | Matches the start of a string. |
| `$`     | Matches the end of a string. |
| `*`     | Matches 0 or more repetitions of the preceding pattern. |
| `+`     | Matches 1 or more repetitions of the preceding pattern. |
| `?`     | Matches 0 or 1 repetition of the preceding pattern. |
| `{n}`   | Matches exactly `n` repetitions. |
| `{n,}`  | Matches `n` or more repetitions. |
| `{n,m}` | Matches between `n` and `m` repetitions. |
| `\`    | Escapes special characters. |

## Common Regex Functions in Python 🛠️

### 1. `re.match()` 🔍
Checks for a match only at the beginning of the string.

```python
import re
pattern = r"hello"
result = re.match(pattern, "hello world")
print(result)  # Output: <re.Match object>
```

### 2. `re.search()` 🌟
Searches for a match anywhere in the string.

```python
result = re.search(r"world", "hello world")
print(result)  # Output: <re.Match object>
```

### 3. `re.findall()` 🗂️
Finds all occurrences of a pattern in a string.

```python
result = re.findall(r"\d", "There are 123 numbers")
print(result)  # Output: ['1', '2', '3']
```

### 4. `re.finditer()` 🔄
Returns an iterator yielding match objects for all matches.

```python
for match in re.finditer(r"\d", "There are 123 numbers"):
    print(match.group())
```

### 5. `re.sub()` ✂️
Replaces occurrences of the pattern with a replacement string.

```python
result = re.sub(r"world", "Python", "hello world")
print(result)  # Output: hello Python
```

### 6. `re.split()` 🧹
Splits a string by the occurrences of the pattern.

```python
result = re.split(r"\s", "Split this string")
print(result)  # Output: ['Split', 'this', 'string']
```

## Special Sequences ✨

| Sequence | Description |
|----------|-------------|
| `\d`    | Matches any digit (0-9). |
| `\D`    | Matches any non-digit character. |
| `\w`    | Matches any word character (alphanumeric + underscore). |
| `\W`    | Matches any non-word character. |
| `\s`    | Matches any whitespace character. |
| `\S`    | Matches any non-whitespace character. |

## Flags 🚩
Flags modify the behavior of regex. Common flags:

| Flag       | Description |
|------------|-------------|
| `re.IGNORECASE` or `re.I` | Makes the pattern case-insensitive. |
| `re.MULTILINE` or `re.M`  | Allows `^` and `$` to match start and end of each line. |
| `re.DOTALL` or `re.S`     | Makes `.` match newlines as well. |

```python
result = re.search(r"hello", "Hello World", re.IGNORECASE)
print(result)  # Output: <re.Match object>
```

## Grouping and Capturing 🎯
Use parentheses `()` to group patterns and capture parts of a match.

```python
match = re.search(r"(\d+)-(\d+)", "Phone: 123-456")
if match:
    print(match.group(1))  # Output: 123
    print(match.group(2))  # Output: 456
```

## Lookahead and Lookbehind 🔎
### Lookahead
- **Positive Lookahead (`(?=...)`)**: Matches a group before a main pattern without including it in the result.
- **Negative Lookahead (`(?!...)`)**: Ensures a pattern is not matched.

### Lookbehind
- **Positive Lookbehind (`(?<=...)`)**: Matches a group that precedes a main pattern.
- **Negative Lookbehind (`(?<!...)`)**: Ensures a pattern does not precede the main one.

```python
# Positive Lookahead
result = re.search(r"Python(?= 3.10)", "Python 3.10")
print(result)  # Output: <re.Match object>

# Negative Lookbehind
result = re.search(r"(?<!Java)Script", "JavaScript")
print(result)  # Output: None
```

## Examples 📖
### Validate an Email Address ✉️
```python
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email = "example@example.com"
if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
```

### Extract URLs 🌐
```python
pattern = r"https?://(?:www\.)?\S+"
text = "Visit https://example.com or http://test.com"
urls = re.findall(pattern, text)
print(urls)  # Output: ['https://example.com', 'http://test.com']
```

### Replace Multiple Spaces 🧽
```python
text = "This  is   a    test"
result = re.sub(r"\s+", " ", text)
print(result)  # Output: This is a test
```

## Conclusion 🏁
Regular expressions are a powerful tool for text processing and manipulation in Python. Practice different patterns and functions to become proficient in using regex for solving complex string-related tasks. 🔥
