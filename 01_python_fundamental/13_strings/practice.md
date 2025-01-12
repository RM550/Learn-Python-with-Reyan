# String Problems and Solutions in Python 🐍✨

This README contains a list of string-related problems, their solutions, and explanations to help you sharpen your Python skills! 🎉 Each problem is paired with a code example and step-by-step explanation. Let's dive in! 🚀✨

---

## 1. Reverse a String 🔄✨

**Problem**: Write a function to reverse a string.

```python
# Solution ✨
def reverse_string(s):
    return s[::-1]  # Slice to reverse string 🌀

# Example Usage 🌟
text = "Python"
result = reverse_string(text)
print(result)  # Output: nohtyP 🐍
```

**Explanation**: We use Python slicing with `[::-1]` to reverse the string in one step. ✂️✨

---

## 2. Check for Palindrome 🪞✨

**Problem**: Check if a given string is a palindrome.

```python
# Solution ✨
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize string 🔤
    return s == s[::-1]  # Compare with reversed string 🌀

# Example Usage 🌟
text = "Racecar"
print(is_palindrome(text))  # Output: True ✅
```

**Explanation**: We normalize the string by converting it to lowercase and removing spaces. Then we check if the string is the same when reversed. 🎯✨

---

## 3. Count Vowels and Consonants 🔡✨

**Problem**: Write a function to count the vowels and consonants in a string.

```python
# Solution ✨
def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"  # Define vowels 🌟
    vowel_count = sum(1 for char in s if char in vowels)  # Count vowels 🔢
    consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)  # Count consonants 📊
    return vowel_count, consonant_count

# Example Usage 🌟
text = "Hello World"
print(count_vowels_and_consonants(text))  # Output: (3, 7) ✅
```

**Explanation**: Using list comprehensions, we count vowels and consonants separately. 🎯✨

---

## 4. Find the Longest Word 🌟✨

**Problem**: Find the longest word in a sentence.

```python
# Solution ✨
def longest_word(sentence):
    words = sentence.split()  # Split into words 📂
    return max(words, key=len)  # Find longest word 🌟

# Example Usage 🌟
text = "I love programming in Python"
print(longest_word(text))  # Output: programming 🏆
```

**Explanation**: We split the sentence into words and use `max()` with `key=len` to find the longest word. ✂️✨

---

## 5. Remove Duplicates from String 🎭✨

**Problem**: Remove duplicate characters from a string.

```python
# Solution ✨
def remove_duplicates(s):
    return "".join(dict.fromkeys(s))  # Use dictionary to keep order and remove duplicates 🎭

# Example Usage 🌟
text = "programming"
print(remove_duplicates(text))  # Output: programin ✅
```

**Explanation**: Using `dict.fromkeys()`, we preserve the order while eliminating duplicates. 🛠️✨

---

## 6. Anagram Checker 🔀✨

**Problem**: Check if two strings are anagrams.

```python
# Solution ✨
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)  # Compare sorted strings 🌀

# Example Usage 🌟
print(are_anagrams("listen", "silent"))  # Output: True ✅
```

**Explanation**: By sorting both strings, we can easily compare if they contain the same characters. 🎯✨

---

## 7. Capitalize Each Word 📝✨

**Problem**: Capitalize the first letter of each word in a string.

```python
# Solution ✨
def capitalize_words(s):
    return " ".join(word.capitalize() for word in s.split())  # Capitalize each word 🔤

# Example Usage 🌟
text = "hello world"
print(capitalize_words(text))  # Output: Hello World 🖋️
```

**Explanation**: We split the string into words, capitalize each word, and join them back. 🎯✨

---

## 8. Count Word Frequency 📊✨

**Problem**: Count the frequency of each word in a string.

```python
# Solution ✨
def word_frequency(s):
    words = s.split()  # Split into words 📂
    return {word: words.count(word) for word in set(words)}  # Count occurrences 🧮

# Example Usage 🌟
text = "apple banana apple orange banana apple"
print(word_frequency(text))  # Output: {'orange': 1, 'banana': 2, 'apple': 3} ✅
```

**Explanation**: Using a dictionary and `set`, we count unique word occurrences. 🎯✨

---

## 9. Find Unique Characters 🌈✨

**Problem**: Find all unique characters in a string.

```python
# Solution ✨
def unique_characters(s):
    return "".join(sorted(set(s)))  # Get unique characters and sort them 🔡

# Example Usage 🌟
text = "hello"
print(unique_characters(text))  # Output: ehlo ✅
```

**Explanation**: We use `set()` to get unique characters and sort them alphabetically. 🎯✨

---

## 10. Replace a Substring 🔄✨

**Problem**: Replace all occurrences of a substring with another.

```python
# Solution ✨
def replace_substring(s, old, new):
    return s.replace(old, new)  # Replace substring 🎭

# Example Usage 🌟
text = "I love Java"
print(replace_substring(text, "Java", "Python"))  # Output: I love Python ✅
```

**Explanation**: Using `.replace()`, we substitute one substring with another. 🛠️✨

---

Feel free to try these problems and level up your Python string skills! 🐍✨
