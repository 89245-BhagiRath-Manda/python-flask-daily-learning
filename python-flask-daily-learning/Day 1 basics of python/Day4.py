# List Revise  +> mutable h ye

nums = [1, 5, 3, 4]
names = ["Ram", "Shyam"]
mixed = [1, "Hi", 2.5]

print(mixed)

nums.append(2)
print(nums)

nums.insert(3, 6)

print(nums)

nums.remove(6)
print(nums)

nums.pop()
print(nums)

nums.sort()
print(nums)

nums.reverse()

squares = [x*x for x in range(5)]

print(squares)

even = [x for x in range(10) if x%2 == 0]

print(even)

# Matrix Nested List

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(matrix)
print(matrix[0][1])

print(len(matrix), len(matrix[0]))

b = [1, 2, 3]
print(b)
# a = b #never do this, because it will copy only reference part
# print(a)

a = b.copy()
print(a)

c = b[:]
print(c)


print("Here")
for x in b:
    print(x)
    
for i, v in enumerate(b):
    print(i, v)
    
    
    
    
    
    
    
    
    # Tuple  IMMUTABLE ds
    
t = (1, 2, 3)
t1 = 10, 20

print(t.count)

x, y = (10, 20)
print(x, y)
print(y)

def get_point():
    return (3, 4)

y, z = get_point()
print(z)



# tuple Methods
# .conunt() .index()



# Set :- stores unique value, is unordered, is mutable


nums = {1, 2, 5, 3, 4, 4}
print(nums)

#we can create list to set


s = {1, 2}

s.add(3)
s.remove(2)
s.discard(5)   # no error if missing



# we can create frozen set

fs = frozenset([1, 2, 3])



#Dictionary :- very important, flask k point of view se bahut important h


user = {
    "id": 1,
    "name": "Ram",
    "Age":24,
    "active": True
}

print(user)

print(user["name"])
print(user.get("Age"))
