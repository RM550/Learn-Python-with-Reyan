### 🐍 Python Decision Statements Practice Tasks 🚦  

Welcome to the **Decision Statements Practice** section! 🎉 Below are solutions and detailed explanations for the tasks. 🧠✨  

---

## 📝 Practice Problems with Solutions  

---

### 1️⃣ **Odd or Even Number Checker**  

#### Problem:  
Check whether a number is odd or even.  

#### Solution:  

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even! ✅")
else:
    print("The number is odd! 🔢")
```  

#### Explanation:  
- The `%` operator gives the remainder of a division.  
- If the remainder when dividing the number by 2 is `0`, the number is even; otherwise, it's odd.  

---

### 2️⃣ **Eligibility for Driving License** 🚗  

#### Problem:  
Check if a person is eligible for a driving license based on age.  

#### Solution:  

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to apply for a driving license! 🚗")
else:
    print("You are not eligible yet. 🕒")
```  

#### Explanation:  
- The program compares the user's age to 18 using `>=`.  
- If the condition is true, it prints a positive message; otherwise, it advises waiting.  

---

### 3️⃣ **Fruit in Stock** 🍎🍌  

#### Problem:  
Check if a fruit is available in the inventory.  

#### Solution:  

```python
fruits = ["apple", "banana", "mango", "orange"]
fruit = input("Enter the fruit name: ").lower()

if fruit in fruits:
    print(f"{fruit.capitalize()} is available! 🍎")
else:
    print(f"{fruit.capitalize()} is not available! 🚫")
```  

#### Explanation:  
- The program checks if the entered fruit exists in the `fruits` list using the `in` keyword.  
- If true, it confirms availability; otherwise, it informs the user.  

---

### 4️⃣ **Grade Calculator** 🎓  

#### Problem:  
Determine a student's grade based on their marks.  

#### Solution:  

```python
marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Your grade is: {grade} 🎉")
```  

#### Explanation:  
- The program evaluates the marks in descending order using `if-elif-else`.  
- Based on the first condition that matches, it assigns a grade.  

---

### 5️⃣ **Restaurant Menu Selector** 🍔🍕  

#### Problem:  
Check if a food item is on the menu.  

#### Solution:  

```python
menu = ["pizza", "burger", "salad", "pasta"]
order = input("What would you like to order? ").lower()

if order in menu:
    print(f"{order.capitalize()} is available! 🍽️")
else:
    print(f"Sorry, {order.capitalize()} is not on the menu. 🙁")
```  

#### Explanation:  
- The program checks if the `order` exists in the `menu` list.  
- If true, it confirms availability; otherwise, it informs the user.  

---

### 6️⃣ **Number Comparer** 🔢  

#### Problem:  
Compare two numbers and find which is greater or if they're equal.  

#### Solution:  

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print("The first number is greater! 🔺")
elif num1 < num2:
    print("The second number is greater! 🔻")
else:
    print("Both numbers are equal! ➗")
```  

#### Explanation:  
- The program compares two numbers using `>`, `<`, and `==`.  
- It prints the result based on the matching condition.  

---

### 7️⃣ **Weather Activity Suggestion** 🌦️  

#### Problem:  
Suggest an activity based on the weather condition.  

#### Solution:  

```python
weather = input("Enter the weather condition (sunny, rainy, snowy, cloudy): ").lower()

if weather == "sunny":
    print("Go for a walk! 🌞")
elif weather == "rainy":
    print("Stay indoors and read a book! 🌂")
elif weather == "snowy":
    print("Build a snowman! ⛄")
elif weather == "cloudy":
    print("Take a drive! 🌥️")
else:
    print("Sorry, I don't have suggestions for that weather. 🤔")
```  

#### Explanation:  
- The program evaluates the weather condition using `if-elif-else`.  
- Based on the input, it prints the corresponding activity suggestion.  

---

### 8️⃣ **Movie Ticket Price** 🎥  

#### Problem:  
Determine the ticket price based on the age of the customer.  

#### Solution:  

```python
age = int(input("Enter your age: "))

if age < 12:
    price = 10
elif age <= 18:
    price = 15
else:
    price = 20

print(f"Your ticket price is ${price}. 🎟️")
```  

#### Explanation:  
- The program checks the age and assigns a ticket price based on the conditions.  
- If the user's age falls into a specific range, the corresponding price is displayed.  

---

### 9️⃣ **Password Validator** 🔑  

#### Problem:  
Validate if a password meets certain criteria.  

#### Solution:  

```python
password = input("Enter your password: ")

if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
    print("Password is strong! 🔐")
else:
    print("Password is weak! ⚠️")
```  

#### Explanation:  
- The program checks:  
  1. The password is at least 8 characters long.  
  2. It contains at least one digit (`isdigit`).  
  3. It contains at least one letter (`isalpha`).  
- If all conditions are true, the password is strong.  

---

### 🔟 **Eligibility for Scholarship** 🏅  

#### Problem:  
Check if a student qualifies for a scholarship based on criteria.  

#### Solution:  

```python
marks = int(input("Enter your marks: "))
extra_curricular = input("Do you participate in extracurricular activities? (yes/no): ").lower() == "yes"

if marks >= 85 and extra_curricular:
    print("You are eligible for the scholarship! 🎉")
else:
    print("You are not eligible for the scholarship. 📚")
```  

#### Explanation:  
- The program checks if the marks are at least 85 and the student participates in extracurricular activities.  
- If both conditions are true, it declares eligibility; otherwise, it denies eligibility.  

---

### 🎉Happy coding  

---
