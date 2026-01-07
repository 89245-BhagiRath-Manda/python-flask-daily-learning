# proper revison indepth

# =========================
# DICTIONARY PRACTICE: java m linked hash map jesa hota h
# =========================

# Create dictionary
user = {
    "id": 1,
    "name": "Ram",
    "age": 24,
    "active": True
}

print("Initial user:", user)

# Add / Update
user["age"] = 25
user["city"] = "Jaipur"
print("After add/update:", user)

# get() - safe access
print("Name:", user.get("name"))
print("Salary (default):", user.get("salary", "Not Available"))

print(user.get("age", "NA"))

# keys(), values(), items()
print("Keys:", user.keys())
print("Values:", user.values())
print("Items:", user.items())

# pop() - remove by key
removed_age = user.pop("age")
print("Removed age:", removed_age)
print("After pop:", user)

# popitem() - last wala item remove krega
last_item = user.popitem()
print("Pop last item:", last_item)
print("After popitem:", user)

# update() - purani wale ke sath merge kr dega,small brackets use kro
user.update({
    "age": 26,
    "email": "ram@test.com"
})

print("After update:", user)

user.update({
    "Education": {
        "Class": "Mca",
        "section": "B",
        "Grade Info": {
            "Result":"PASS",
            "CGPA" : 7.9,
            "Subject wise info": {
                "java":"pass",
                "c++": "pass"
            }
        }
    }
})
print("After 2nd update:", user)

# setdefault() - agar wo key h to add nhi krega agar nhi h to add krefa
user.setdefault("role", "USER")  #add kr dega yha p
user.setdefault("name", "Unknown")  #nhi krega already h
print("After setdefault:", user)

# in keyword
print("Is 'name' present?", "name" in user)
print("Result h kya? ", "Result" in user["Education"]["Grade Info"])

if("CGPA" in user["Education"]["Grade Info"]):
    user.update({
        "CGPA": 6.8
    })
    print("ho gya bhai") #ese nhi hota ye kewal add krta h reat update = se hota h


    
print(user)

user["Education"]["Grade Info"]["CGPA"] = 6.8

print(user)

#pr ye safe update nhi h safe ye wala h

user.get("Education", {}) \
    .get("Grade Info", {})["CGPA"] = 6.2

print(user)

# copy()
user_copy = user.copy() #Agar copy use nhi krega to kewal reference hi lega





print("Copied user:", user_copy)

# clear()
user_copy.clear()
print("After clear copy:", user_copy)

# Looping
print("\nLooping dictionary:")
for key, value in user.items():
    print(key, "=>", value)
    
#python apne aap dictionary ko json me convert kr deta h

#or ye bahut sahi h java ko jackson ki jarurat padti h

#insert, delete, and lookup tino chize o(1) me ho jata h

count = {}
for ch in "banana is real fruit king":
    count[ch] = count.setdefault(ch, 0) + 1
    
print(count)




#=========================
# Next Module : Functions
#=========================

def add(a, b):
    return a+b

result = add(5, 6)

print(result)
result1 = add("apple", "ball")
print(result1)
result2 = add(56.6, 42.1)
print(result2)
result3 = add('a', 'b')
print(result3)

# add(b=3, a=2)

def greet(name, msg="Hello"):
    print(msg, name)

greet("Ram")
greet("Ram", "Hi")


def total(*numbers):
    return sum(numbers) #similar to varchar of java

print(total(1, 2, 3))


# Keyword Variable Arguments (**kwargs)

# Accepts key–value pairs.
def print_user(**data):
    print(data)

print_user(name="Ram", age=25)

def demo(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)
    

# order matters :- positional → default → *args → **kwargs


def stats(a, b):
    return a+b, a*b

s, m = stats(3, 4)


#Docstring (important for team code)

def add(a, b):
    """Returns sum of two numbers"""
    return a + b


print(add(3, 4))


#avoide gloabal level variable in production

def add(a, b):
    return a + b

f = add
print(f(2, 3))


# lambda arguments : expression
add = lambda a, b: a + b
print(add(2, 3))

nums = [1, 2, 3]

squares = list(map(lambda x: x*x, nums))

print(squares)

nums = [1, 2, 3, 4]

even = list(filter(lambda x: x % 2 == 0, nums))

print(even)


from functools import reduce

nums = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, nums)

print(total)


# map
[x*x for x in nums]

# filter
[x for x in nums if x % 2 == 0]

