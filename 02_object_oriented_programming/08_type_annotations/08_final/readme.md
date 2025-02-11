# Final Annotations

## Introduction 📌

The `Final` type annotation in Python was introduced in **PEP 591** and is available from **Python 3.8+**. It allows developers to **prevent reassignment of variables, attributes, and methods**, enforcing immutability at the type level.

## Why Use `Final`? 🤔

- **Prevents accidental reassignment** of constants and attributes.
- **Enhances code clarity** by indicating values that should remain unchanged.
- **Improves static analysis** by allowing type checkers to detect reassignment errors.
- **Provides better documentation** by signaling intended immutability.

## Importing `Final` 📝

The `Final` type annotation is imported from the `typing` module:

```python
from typing import Final
```

## Basic Example 🎯

```python
from typing import Final

MAX_USERS: Final = 100

print(MAX_USERS)  # ✅ Allowed

MAX_USERS = 200  # ❌ Type checker will raise an error
```

## How `Final` Works 🔍

- `Final` is used to indicate that a **variable, attribute, or method** should not be overridden or reassigned.
- It **does not** enforce immutability at runtime, but static type checkers (like MyPy) will catch violations.
- It helps document **constants** and **fixed values** in the code.

## Using `Final` with Class Attributes 🏗️

```python
from typing import Final

class Config:
    API_KEY: Final = "abc123"

config = Config()
print(config.API_KEY)  # ✅ Allowed

config.API_KEY = "xyz456"  # ❌ Type checker error
```

## Using `Final` with Class Inheritance 🚨

`Final` can be used to prevent **method overriding** in subclasses.

```python
from typing import Final

class Base:
    def regular_method(self) -> None:
        print("This can be overridden.")
    
    @Final
    def final_method(self) -> None:
        print("This cannot be overridden!")

class Derived(Base):
    def regular_method(self) -> None:
        print("Overridden successfully!")  # ✅ Allowed
    
    def final_method(self) -> None:  # ❌ Type checker error
        print("Trying to override!")
```

## Preventing Subclassing with `@Final` 🎯

You can use `@Final` to **prevent an entire class from being subclassed**.

```python
from typing import Final

@Final
class ImmutableClass:
    pass

class AttemptedSubclass(ImmutableClass):  # ❌ Type checker error
    pass
```

## Difference Between `Final` and Constants 🔄

Although Python does not have built-in constants like other languages, `Final` helps **enforce constant-like behavior** through type checking.

```python
MAX_SPEED: Final[int] = 120  # Treated as a constant
PI: Final[float] = 3.14159  # Cannot be reassigned
```

However, `Final` **does not prevent mutation of mutable objects**:

```python
from typing import Final

NAMES: Final[list[str]] = ["Alice", "Bob"]

NAMES.append("Charlie")  # ✅ Allowed (Final does not enforce deep immutability)
NAMES = ["Dave"]  # ❌ Type checker error
```

## When to Use `Final`? 🎯

✅ Use `Final` when:
- You want to **enforce constant values**.
- You need to **prevent subclassing**.
- You want to **prohibit method overriding**.
- You require **better type checking and documentation**.

🚫 Avoid `Final` if:
- You need **runtime enforcement** (use `dataclass(frozen=True)` instead).
- You require **deep immutability** (use immutable types like `tuple` instead of `list`).

## Summary 📌

| Feature | Supported? |
|---------|------------|
| Prevents reassignment | ✅ |
| Prevents subclassing | ✅ (with `@Final` on a class) |
| Prevents method overriding | ✅ (with `@Final` on a method) |
| Enforced at runtime | ❌ (only checked by static analyzers) |
| Works with mutable objects | ❌ (only prevents reassignment, not mutation) |

## Conclusion 🎯

The `Final` type annotation in Python provides a **lightweight mechanism** to enforce immutability at the type level. It helps document constants, prevent method overriding, and restrict subclassing, making code **safer, clearer, and more maintainable**.

🚀 **Happy Coding!** 🚀

