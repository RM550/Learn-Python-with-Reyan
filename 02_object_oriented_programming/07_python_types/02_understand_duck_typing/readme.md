

## 🔥 **Introduction to Duck Typing**  

*"If it looks like a duck and quacks like a duck, then it must be a duck!"* 🦆  

**Duck Typing** means Python doesn’t care about an object's type—**only its behavior**. If an object implements the required method(s), it works!  

📌 **Example Concept:** A **USB drive, an external HDD, and a cloud storage service** can all be used for storage. We don’t care **what** they are; we only care **that they support file storage operations**.  

---

## 🏗 **1️⃣ What is Duck Typing?**  

### 🔹 **Definition:**  
- Python does **not** require explicit type declarations.  
- As long as an object **has the expected methods**, it can be used.  

🔍 **Key Benefits:**  
✔ More **flexible** code  
✔ Less **boilerplate**  
✔ More **reusable** components  

---

## 🚀 **2️⃣ Duck Typing in Action**  

### 📌 **Example 1: Storage System (USB, HDD, Cloud, etc.)**  
Let’s say we have different storage solutions. Each one implements a `.save()` method differently:  

```python
class USBDrive:
    def save(self, data):
        print(f"Saving '{data}' to USB Drive 💾")

class ExternalHDD:
    def save(self, data):
        print(f"Saving '{data}' to External HDD 📀")

class CloudStorage:
    def save(self, data):
        print(f"Uploading '{data}' to Cloud ☁️")

def backup_data(storage_device, data):
    storage_device.save(data)

# Using Duck Typing—any storage with a save() method works!
backup_data(USBDrive(), "Project Files")      # Saving 'Project Files' to USB Drive 💾
backup_data(ExternalHDD(), "Backup Data")     # Saving 'Backup Data' to External HDD 📀
backup_data(CloudStorage(), "Photos")         # Uploading 'Photos' to Cloud ☁️
```

✅ **Why It Works?**  
- `backup_data()` doesn’t care **what type** `storage_device` is.  
- It **only checks if `.save()` exists** and calls it.  

---

### 📌 **Example 2: Notification System (Email, SMS, Push Notifications, etc.)**  

Let's build a notification system that supports **Email, SMS, and Push Notifications**, all using Duck Typing.  

```python
class EmailNotifier:
    def send(self, message):
        print(f"📧 Sending Email: {message}")

class SMSNotifier:
    def send(self, message):
        print(f"📱 Sending SMS: {message}")

class PushNotifier:
    def send(self, message):
        print(f"🔔 Sending Push Notification: {message}")

def notify_users(notifier, message):
    notifier.send(message)

# Using different notification methods
notify_users(EmailNotifier(), "Your OTP is 1234")  # 📧 Sending Email: Your OTP is 1234
notify_users(SMSNotifier(), "Payment received!")   # 📱 Sending SMS: Payment received!
notify_users(PushNotifier(), "New message!")       # 🔔 Sending Push Notification: New message!
```

✅ **Why It Works?**  
- `notify_users()` doesn’t check if the input is `EmailNotifier`, `SMSNotifier`, or `PushNotifier`.  
- As long as `.send()` exists, it works!  

---

### 📌 **Example 3: Payment Processing (Credit Card, PayPal, Bitcoin, etc.)**  

Let’s implement a **payment gateway** that supports different payment methods.  

```python
class CreditCard:
    def process_payment(self, amount):
        print(f"💳 Processing Credit Card payment of ${amount}")

class PayPal:
    def process_payment(self, amount):
        print(f"🅿️ Processing PayPal payment of ${amount}")

class Bitcoin:
    def process_payment(self, amount):
        print(f"₿ Processing Bitcoin payment of ${amount}")

def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

# Making payments using different methods
make_payment(CreditCard(), 100)  # 💳 Processing Credit Card payment of $100
make_payment(PayPal(), 250)      # 🅿️ Processing PayPal payment of $250
make_payment(Bitcoin(), 500)     # ₿ Processing Bitcoin payment of $500
```

✅ **Why It Works?**  
- `make_payment()` only expects the object to have `process_payment()`.  
- **Any payment method** can be used as long as it follows the contract.  

---

### 📌 **Example 4: Data Serialization (JSON, XML, CSV)**  

Let's serialize data into different formats **(JSON, XML, CSV)** using Duck Typing.  

```python
import json

class JSONSerializer:
    def serialize(self, data):
        return json.dumps(data)

class XMLSerializer:
    def serialize(self, data):
        return f"<data>{data}</data>"

class CSVSerializer:
    def serialize(self, data):
        return ",".join(str(value) for value in data)

def convert_data(serializer, data):
    print(serializer.serialize(data))

# Serialize data into different formats
convert_data(JSONSerializer(), {"name": "Reyan", "age": 16})  # {"name": "Reyan", "age": 16}
convert_data(XMLSerializer(), "Hello World")                 # <data>Hello World</data>
convert_data(CSVSerializer(), [1, 2, 3, 4, 5])               # 1,2,3,4,5
```

✅ **Why It Works?**  
- `convert_data()` doesn’t check **what kind of serializer** is passed.  
- As long as `.serialize()` exists, it works!  

---

## 🛑 **3️⃣ When Duck Typing Might Not Be Ideal**  

While Duck Typing is powerful, **sometimes explicit type checking is necessary**:  

✔ **When working with external APIs** that expect a specific type.  
✔ **For security-sensitive code**, like validating user inputs.  
✔ **When performance is critical**, and you want **faster type enforcement**.  

---

## 🏆 **4️⃣ Best Practices for Duck Typing in Python**  

### ✅ **DOs**  
✔ Rely on **behavior** instead of explicit type checks.  
✔ Use **try-except blocks** instead of `isinstance()`.  
✔ Follow **Python’s “EAFP” principle**: *Easier to Ask for Forgiveness than Permission*.  

### ❌ **DON’Ts**  
🚫 Avoid excessive `isinstance()` checks.  
🚫 Don’t assume an object’s type—**assume it has the required behavior**.  

---

## 🎯 **Conclusion**  

✅ **Duck Typing makes Python flexible and powerful!**  

🚀 It allows **dynamic, reusable, and scalable code**.  
🐍 Python doesn’t care **what an object is**—only **how it behaves**.  
🔥 Use **Duck Typing when possible**, but **explicit checks when necessary**.  

💡 **"Don't ask what an object is—ask what it can do!"** 💡  

**Happy Coding!** 🚀🐍
