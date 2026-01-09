try:
    x = (int(input("Number dalo")))
    print(10 / x)
except:
    print("Something wrong happened")
    
try:
    x = int(input())
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")


# except (ZeroDivisionError, ValueError) as e:
#     print(e)


try:
    x = int(input())
except ValueError:
    print("Error")
else: #runs only when no exception occurs
    print("Success")

age = -1

if age < 0:
    raise ValueError("Age cannot be negative")

#Exception Hierarchy:
"""
BaseException
 └─ Exception
    ├─ ValueError
    ├─ TypeError
    ├─ KeyError
"""