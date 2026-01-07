# Dictionary :- very important, flask k point of view se bahut important h


user = {
    "id": 1,
    "name": "Ram",
    "Age": 24,
    "active": True,
    "class": {
       "section": "Cs",
       "degree": "MCA"
    }
}
print(user)
print(user)

print(user["name"])
print(user.get("Age"))

user["age"] = 25
user["name"] = "Bhagirath Manda"


print(user)



customer = {
    1: {
        "name": "Bhagirath",
        "class": "Mca",
        "Age": 23
    },
    2: {
        "name": "Abhimanyu",
        "Class": "BE",
        "Age": 30
    }
}

customer[3] = {
    "name": "Arjun",
    "Class": "BCA",
    "Age": 28
}

print(customer)





# =========================
# SET PRACTICE
# =========================

# Create set
roles = {"USER", "ADMIN"}
print("Initial roles:", roles)

# add()
roles.add("MANAGER")
print("After add:", roles)

# update() - add multiple
roles.update(["HR", "ADMIN"])  # ADMIN ignored (duplicate)
print("After update:", roles)

# remove() - error if not exists
roles.remove("HR")
print("After remove:", roles)

# discard() - no error if missing
roles.discard("GUEST")
print("After discard:", roles)

# pop() - removes random element
removed = roles.pop()
print("Popped element:", removed)
print("After pop:", roles)

# Membership check
print("Is ADMIN present?", "ADMIN" in roles)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("\nSet A:", a)
print("Set B:", b)

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference A-B:", a - b)
print("Symmetric Difference:", a ^ b)

# issubset / issuperset
print("Is A subset of B?", a.issubset(b))
print("Is A superset of B?", a.issuperset(b))

# copy()
a_copy = a.copy()
print("Copy of A:", a_copy)

# clear()
a_copy.clear()
print("After clear copy:", a_copy)

# Looping
print("\nLooping set:")
for item in a:
    print(item)
