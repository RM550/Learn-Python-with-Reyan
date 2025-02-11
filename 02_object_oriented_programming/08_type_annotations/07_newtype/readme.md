# NewType Annotations

## Introduction 📌

The `NewType` feature in Python was introduced in **PEP 484** and is available from **Python 3.5+**. It allows developers to create **distinct types** based on existing ones, enabling stricter type checking without introducing runtime overhead.

## Why Use `NewType`? 🤔

- **Enhances type safety**: Prevents accidental mixing of different types.
- **Provides better documentation**: Clearly distinguishes between logically different entities.
- **Zero runtime overhead**: Acts as a simple wrapper without additional performance cost.
- **Improves code readability**: Makes function signatures clearer.

## Importing `NewType` 📝

The `NewType` function is imported from the `typing` module:

```python
from typing import NewType
```

## Basic Example 🎯

```python
from typing import NewType

UserId = NewType('UserId', int)

def get_user(user_id: UserId) -> None:
    print(f"Fetching user with ID: {user_id}")

user = UserId(123)  # ✅ Valid
get_user(user)  # ✅ Valid

invalid_user = 456  # ❌ Type checker will raise an error
get_user(invalid_user)  # ❌ Type error
```

## How `NewType` Works 🔍

- `NewType('Alias', OriginalType)` creates a **new distinct type** based on `OriginalType`.
- It prevents **accidental misuse** by ensuring only the correct type is passed.
- It does **not** create a new class; it behaves like the original type at runtime but is **treated as a separate type** during static analysis.

## Example: Using `NewType` for Stronger Typing ✅

```python
from typing import NewType

EmployeeId = NewType('EmployeeId', int)
ProjectId = NewType('ProjectId', int)

def assign_project(employee: EmployeeId, project: ProjectId) -> None:
    print(f"Assigning employee {employee} to project {project}")

e_id = EmployeeId(101)
p_id = ProjectId(2001)

assign_project(e_id, p_id)  # ✅ Valid
assign_project(p_id, e_id)  # ❌ Type checker error
```

## Difference Between `NewType` and Type Alias 🔄

`NewType` is **not the same** as a regular type alias.

```python
UserIdAlias = int  # This is just an alias, not a distinct type
UserIdNewType = NewType('UserIdNewType', int)

def process_user(user: UserIdNewType) -> None:
    print(f"Processing user {user}")

uid_alias: UserIdAlias = 123  # ✅ Works fine
process_user(uid_alias)  # ❌ Type checker error
```

- `UserIdAlias = int` is simply a **shorthand** for `int` (no extra type safety).
- `NewType('UserIdNewType', int)` creates a **distinct type** that prevents mixing with `int`.

## Nesting `NewType` in Function Scope 🏗️

`NewType` can be **defined inside functions** to limit its scope.

```python
from typing import NewType

def process_transaction():
    TransactionId = NewType('TransactionId', int)
    t_id = TransactionId(500)
    print(f"Processing transaction {t_id}")

process_transaction()  # ✅ Works fine
```

## `NewType` and Subclassing 🚨

`NewType` **does not support subclassing**.

```python
from typing import NewType

UserId = NewType('UserId', int)

class ExtendedUserId(UserId):  # ❌ This will raise an error
    pass
```

## Using `NewType` with `isinstance()` 🧐

Since `NewType` is just an alias at runtime, `isinstance()` treats it as the original type.

```python
from typing import NewType

OrderId = NewType('OrderId', int)
order = OrderId(789)

print(isinstance(order, int))  # ✅ True (NewType behaves like int at runtime)
```

## When to Use `NewType`? 🎯

✅ Use `NewType` when:
- You want to **prevent unintended type mixing**.
- You need **static type checking** for distinct entities.
- You require **better code clarity and documentation**.
- You want **zero runtime performance cost**.

🚫 Avoid `NewType` if:
- You **need runtime enforcement** (use classes instead).
- You require **custom methods and behavior** (use a class instead).
- You are working with **simple type aliases** (use `type Alias = OriginalType`).

## Summary 📌

| Feature | Supported? |
|---------|------------|
| Type safety | ✅ |
| Runtime overhead | ❌ (No overhead) |
| Works with `isinstance()` | ✅ |
| Prevents accidental mixing | ✅ |
| Supports subclassing | ❌ |
| Allows runtime validation | ❌ |

## Conclusion 🎯

The `NewType` feature in Python provides a **lightweight way to enforce stronger typing** without introducing runtime overhead. It helps distinguish logically different types and prevents accidental misuse, making your code **safer, clearer, and more maintainable**.

🚀 **Happy Coding!** 🚀

