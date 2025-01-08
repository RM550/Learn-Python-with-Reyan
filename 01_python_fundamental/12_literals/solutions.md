# Python Practice Tasks with Solutions ✨📚🚀

Welcome to the **Python Practice Tasks** repository! Here, you will find a list of exciting and challenging tasks along with their solutions to help you improve your Python programming skills. 😄✨

## Instructions ℹ️✨
1. Read each task carefully. 🔍
2. Understand the solution and the explanation provided. 🤔
3. Experiment with modifying the solutions to explore new ideas. 🔧
4. Practice consistently to strengthen your skills. 🏆❤️

---

## Beginner Tasks 🌱✨

### Task 1: Print Your Name Repeatedly
**Task:** Write a program to print your name 5 times using a `for` loop. 🌐

**Solution:**
```python
for i in range(5):
    print("Your Name")  # Replace "Your Name" with your actual name.
```
**Explanation:** The `for` loop iterates 5 times, printing the name during each iteration. 🔄

---

### Task 2: Even Numbers Finder
**Task:** Print all the even numbers from 1 to 50 using a `while` loop. 🔢

**Solution:**
```python
num = 1
while num <= 50:
    if num % 2 == 0:
        print(num)
    num += 1
```
**Explanation:** The `while` loop checks each number from 1 to 50, printing it if it is divisible by 2. 🔄

---

### Task 3: Create a Shopping List
**Task:** Take input from the user to create a shopping list with 5 items. Print the list using a loop. 🍒🍲

**Solution:**
```python
shopping_list = []
for i in range(5):
    item = input("Enter an item for your shopping list: ")
    shopping_list.append(item)
print("Your shopping list:")
for item in shopping_list:
    print(item)
```
**Explanation:** The `for` loop collects 5 inputs from the user, appending them to a list, which is then printed item by item. 🎨

---

## Intermediate Tasks 🌌✨

### Task 4: Multiplication Table Generator
**Task:** Ask the user for a number and generate its multiplication table up to 10 using a `for` loop. 🔢📚

**Solution:**
```python
number = int(input("Enter a number: "))
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```
**Explanation:** The `for` loop iterates from 1 to 10, multiplying the input number with each value to generate the table. 🔄

---

### Task 5: Pattern Printer
**Task:** Print the following pattern using nested loops:
```
*
**
***
****
*****
```
🌈⭐

**Solution:**
```python
rows = 5
for i in range(1, rows + 1):
    print("*" * i)
```
**Explanation:** The outer loop determines the number of rows, and the string multiplication (`"*" * i`) generates the stars for each row. 🎨

---

### Task 6: Sum of Natural Numbers
**Task:** Write a program to calculate the sum of the first 20 natural numbers using a `while` loop. 📊➕

**Solution:**
```python
n = 20
sum = 0
count = 1
while count <= n:
    sum += count
    count += 1
print("Sum of the first 20 natural numbers:", sum)
```
**Explanation:** The `while` loop iterates through numbers from 1 to 20, adding each to the total sum. 📊

---

## Advanced Tasks 💡✨

### Task 7: Pyramid Generator
**Task:** Take an input number from the user and create a pyramid pattern of stars with that height using nested loops. 🌈⬆

**Solution:**
```python
rows = int(input("Enter the number of rows for the pyramid: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
```
**Explanation:** The outer loop determines the number of rows, while the inner expressions handle spacing and star generation. 🌟

---

### Task 8: Palindrome Checker
**Task:** Write a program that takes a string input from the user and checks if it is a palindrome. Use a `for` loop to reverse the string. ⟠⭐️

**Solution:**
```python
word = input("Enter a word: ")
reversed_word = "".join([word[i] for i in range(len(word) - 1, -1, -1)])
if word == reversed_word:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
```
**Explanation:** A list comprehension is used to reverse the string, and it is compared with the original string to check for palindrome status. 🌐

---

### Task 9: Fibonacci Sequence Generator
**Task:** Generate the first `n` numbers of the Fibonacci sequence where `n` is provided by the user. Use a `while` loop to solve this. 💡♻️

**Solution:**
```python
n = int(input("Enter the number of Fibonacci numbers to generate: "))
a, b = 0, 1
fibonacci = []
while len(fibonacci) < n:
    fibonacci.append(a)
    a, b = b, a + b
print("Fibonacci Sequence:", fibonacci)
```
**Explanation:** The `while` loop runs until the list contains `n` elements, updating Fibonacci numbers in each iteration. 🔄

---

### Task 10: Create a Dynamic Dictionary
**Task:** Take two lists of equal length from the user (keys and values). Use a loop to create a dictionary that maps keys to values. 📂✨

**Solution:**
```python
keys = input("Enter keys separated by commas: ").split(",")
values = input("Enter values separated by commas: ").split(",")
if len(keys) != len(values):
    print("Error: Keys and values must have the same length.")
else:
    data = {keys[i]: values[i] for i in range(len(keys))}
    print("Dynamic Dictionary:", data)
```
**Explanation:** The program uses a dictionary comprehension to map keys to values based on their indices. 🔖

---

## Bonus Challenge Tasks 🏆✨

### Task 11: Prime Number Finder
**Task:** Write a program that finds and prints all prime numbers between 1 and 100 using nested loops. 🔢🔮

**Solution:**
```python
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number.")
```
**Explanation:** The nested loop checks divisibility for each number, marking it as prime if no divisors are found. 🔮

---

### Task 12: Multiples of a Number
**Task:** Take two inputs: a number and a range limit. Print all multiples of the number up to the range limit using a loop. 🌢➕

**Solution:**
```python
num = int(input("Enter the number: "))
limit = int(input("Enter the range limit: "))
for i in range(1, limit + 1):
    if i % num == 0:
        print(i)
```
**Explanation:** The `for` loop iterates through the range, printing numbers divisible by the input number. 🔄

---

Happy coding🐍✨ 
---
