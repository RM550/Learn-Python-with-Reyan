
# 🧩 **Python Operators Tasks** 🚀

Dive into the fascinating world of Python operators with these challenging problems! Each question is followed by a detailed explanation to help you understand the concepts better. 🌟✨

---

## 🔢 Problem 1: Checking Odd or Even 🔄

Write a program to check if a given number is odd or even using the modulo operator. 🤔🔢

### **Hint:**
Use the `%` operator with the number `2`. If the result is `0`, the number is even; otherwise, it's odd. 🎲

### **Solution:**
```python
number = 5  # Change this to test other numbers
if number % 2 == 0:
    print("Even Number ✅")
else:
    print("Odd Number ❌")
```
### **Explanation:**
The modulo operator `%` gives the remainder when one number is divided by another. Checking against `0` helps determine if the number is even. 🌟🎉

---

## 🎭 Problem 2: Calculate Power Using Exponentiation 🔋

Write a function to calculate the power of a number using the `**` operator. 🛠️⚡

### **Hint:**
Use `base ** exponent` to compute the power directly. 🚀

### **Solution:**
```python
def power(base, exponent):
    return base ** exponent

base = 2
exponent = 3
result = power(base, exponent)
print(f"{base} raised to the power {exponent} is {result} ✨")
```
### **Explanation:**
The exponentiation operator `**` simplifies power calculations without needing loops or extra logic. 💡🔥

---

## 🔒 Problem 3: Calculate Quotient and Remainder 🔑

Write a program to calculate the quotient and remainder of a division. 🔐📊

### **Hint:**
Use the `//` operator for quotient and `%` for remainder. 💪

### **Solution:**
```python
numerator = 10
denominator = 3
quotient = numerator // denominator
remainder = numerator % denominator
print(f"Quotient: {quotient} 🔹, Remainder: {remainder} 🔸")
```
### **Explanation:**
The floor division operator `//` gives the integer quotient, while `%` provides the remainder. Essential for division problems! ✨📈

---

## 🌐 Problem 4: Find Average 🌍

Given a list of numbers, calculate their average using arithmetic operators. 📡📉

### **Hint:**
Sum all the numbers and divide by the count. 💡

### **Solution:**
```python
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(f"Average: {average} 📊")
```
### **Explanation:**
The `+` operator adds numbers, and `/` divides the sum by the total count. Simple and effective for averages! 🌟💻

---

## 📊 Problem 5: Check Relational Operators 🔢

Write a program to compare two numbers using relational operators. 🧮🔍

### **Hint:**
Use `==`, `!=`, `>`, `<`, `>=`, and `<=` for comparisons. 💬

### **Solution:**
```python
a = 10
b = 20
print(a == b)  # False ❌
print(a != b)  # True ✅
print(a > b)   # False ❌
print(a < b)   # True ✅
print(a >= b)  # False ❌
print(a <= b)  # True ✅
```
### **Explanation:**
Relational operators help compare values and return `True` or `False` based on the condition. Great for decision-making! 💡💥

---

## 🕹️ Problem 6: Logical Operator Challenge 🚩

Write a program to check if a number lies within a range using logical operators. 🎯🧠

### **Hint:**
Combine conditions using `and`, `or`, and `not`. 🔄💥

### **Solution:**
```python
number = 15
if number > 10 and number < 20:
    print("Number is in the range 10-20 ✅")
else:
    print("Number is out of range ❌")
```
### **Explanation:**
Logical operators combine multiple conditions to form complex logical expressions. Perfect for range checks! 🚀🎉

---

## 🎉 Conclusion

Operators are the building blocks of Python programming. By solving these challenges, you've sharpened your understanding of arithmetic, relational, and logical operators. Keep exploring and coding! 💻✨🚀

---
