## 🐍 Python Decision Statements Guide 🚦  

Welcome to this **Decision Statements** guide in Python! 📝 Decision-making is a vital skill in programming, as it lets your code respond differently based on varying inputs or conditions. Let's explore Python's decision-making tools with **real-life examples**! 🌟  

---

## 🎯 What are Decision Statements?  

Decision statements allow your program to take action based on conditions. Think of them as traffic signals 🚦 guiding your program to choose the right path.  

---

## 🛠️ Types of Decision Statements  

1. **`if` Statement**: Executes a block of code if a condition is true.  
2. **`if-else` Statement**: Chooses between two blocks of code based on a condition.  
3. **`if-elif-else` Statement**: Handles multiple conditions.  
4. **Nested `if` Statements**: Allows a decision inside another decision.  
5. **Conditional Tests**: Simple conditions used to evaluate whether a statement is `True` or `False`.  

---

## 🌍 Real-Life Examples with Explanations 🎉  

---

### 🔹 Conditional Tests: The Foundation of Decisions 🔍  

A **conditional test** is an expression that evaluates to `True` or `False`. These are the backbone of decision-making in Python.  

#### Example 1: Check if a Number is Positive or Negative ➕➖  

```python
number = 10

if number > 0:
    print("The number is positive! ✅")
else:
    print("The number is negative! ❌")
```  

💡 **Explanation**:  
- The condition `number > 0` evaluates to `True` if the number is positive.  
- If true, the program prints a positive message; otherwise, it prints a negative message.  
**Output**:  
If `number = 10`:  
`The number is positive! ✅`  

#### Example 2: Check Membership in a List 📋  

```python
fruits = ["apple", "banana", "mango"]

if "apple" in fruits:
    print("Apple is in the list! 🍎")
else:
    print("Apple is not in the list! 🚫")
```  

💡 **Explanation**:  
- The condition `"apple" in fruits` checks if `"apple"` exists in the list `fruits`.  
- Based on the result, it prints a relevant message.  
**Output**:  
If `fruits = ["apple", "banana", "mango"]`:  
`Apple is in the list! 🍎`  

---

### 1️⃣ Simple `if` Statement: Morning Routine 🌅  

```python
time = 6  # Time in hours
if time < 7:
    print("Good morning! 🌞 Time for a morning walk.")
```  

💡 **Explanation**:  
- The program checks if the current hour is less than 7.  
- If true, it prints a message about a morning walk.  
**Output**:  
If `time = 6`:  
`Good morning! 🌞 Time for a morning walk.`  

---

### 2️⃣ `if-else` Statement: Coffee or Tea? ☕🍵  

```python
preference = "coffee"

if preference == "coffee":
    print("Brewing your coffee! ☕")
else:
    print("Making some tea for you! 🍵")
```  

💡 **Explanation**:  
- The `preference` variable checks the user’s drink choice.  
- If the preference is `"coffee"`, it prints a message about coffee. Otherwise, it prints about tea.  
**Output**:  
If `preference = "coffee"`:  
`Brewing your coffee! ☕`  

---

### 3️⃣ `if-elif-else` Statement: Weather Advice 🌦️  

```python
weather = "rainy"

if weather == "sunny":
    print("Wear sunglasses! 😎")
elif weather == "rainy":
    print("Take an umbrella! 🌂")
elif weather == "cold":
    print("Wear a jacket! 🧥")
else:
    print("Enjoy the day! 🌟")
```  

💡 **Explanation**:  
- The `weather` variable holds the current condition.  
- The program uses `if`, `elif`, and `else` to decide on advice based on the condition.  
**Output**:  
If `weather = "rainy"`:  
`Take an umbrella! 🌂`  

---

### 4️⃣ Nested `if` Statement: Admission Criteria 🎓  

```python
grade = 85
extra_curricular = True

if grade > 80:
    if extra_curricular:
        print("You are eligible for admission! 🎉")
    else:
        print("Improve your extracurricular activities! 📚")
else:
    print("Work harder on academics! 💪")
```  

💡 **Explanation**:  
- The program first checks if the grade is greater than 80.  
- If true, it further checks extracurricular activity.  
- Based on both conditions, a message is displayed.  
**Output**:  
If `grade = 85` and `extra_curricular = True`:  
`You are eligible for admission! 🎉`  

---

### 🔹 Advanced Example: Conditional Tests with Logical Operators 🔗  

You can combine multiple conditions using **logical operators** like `and`, `or`, and `not`.  

#### Example: Bookstore Discounts 📚💸  

```python
is_student = True
is_first_purchase = False

if is_student and is_first_purchase:
    print("You get a 20% discount! 🎉")
elif is_student:
    print("You get a 10% discount! 🤑")
else:
    print("No discount available. 💔")
```  

💡 **Explanation**:  
- The condition `is_student and is_first_purchase` evaluates if the user is a student and it’s their first purchase.  
- If true, a 20% discount is applied.  
- If the user is only a student, a 10% discount is applied.  
**Output**:  
If `is_student = True` and `is_first_purchase = False`:  
`You get a 10% discount! 🤑`  

---  

## 🔥 Tips for Writing Better Decision Statements  

1. **Keep it clean**: Avoid deeply nested conditions by breaking logic into functions.  
2. **Use comments**: Explain your conditions for readability.  
3. **Test thoroughly**: Ensure all paths are working correctly.  

---

### 🌟 That's All for Decision Statements! 🎉  

Enjoy coding and making your programs smarter! 💻🐍 
---
