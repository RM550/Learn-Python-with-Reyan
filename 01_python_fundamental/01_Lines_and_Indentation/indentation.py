# good indentation

# ✅ 4 spaces for indentation
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Name is missing.")

  -----------------------------------------

# bad indentation


# ❌ Improper indentation will raise an error
def greet(name):
if name:
print(f"Hello, {name}!")
else:
print("Name is missing.")
