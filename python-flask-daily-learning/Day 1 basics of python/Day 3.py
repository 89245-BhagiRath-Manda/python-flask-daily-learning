# today is 31st december continuing with remaining python basics

#boolean
#always use snake_case also remember for boolean we should use capital T and F for true and false
is_active = True;
is_admin = False;

print(is_active)


#Type Casting 
a = "10"
#a = "abc" #it will give error while converting like :- intvalid literal for int ()
print(a)
b = int(a) #similar to java where i was using int b = Integer.parseInt(a);

print(a)


#User Input
# name = input("Enter name : ")
# #convert bhi kr sakte h :-
# age = int(input("Enter age: "))

# print(name, age)

#Arithmatic op

a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3  (floor division)
print(a % b)   # 1
print(a ** b)  # 1000 (power)


#Assignment Operators
x = 10
x += 5 
print(x)  # 15
x -= 2
print(x)   # 13
x *= 2 
print(x)  # 26
x /= 2 
print(x)  # 13.0
x %= 3


#Comparison(Relational) Operator

a = 10
b = 20

print(a==b)   # False
print(a != b)   # True
a > b
a < b
a >= b
a <= b



#logical operator

x = True
y = True

print(x and y)
print(x or y)
print(not y)

#Bitwise Operator  :- Revisit krna h

a = 5   # 0101
b = 3   # 0011

print(a & b)   # 1
print(a | b)   # 7
a ^ b   # 6
a << 1
a >> 1


# Membership Operators

nums = [1, 3, 2]

x = 2 in nums
print(x)

#identity Operators

a = 10
b = 10.0

print(a == b)   # True (value)
print(a is b )  # True (same object, small int cache)


# formatted output

name = "Ram"
age = 25

print("Name: {}, Age: {}".format(name, age))


#fstring :- Most important

name = "Ram"
age = 25
print(f"Name: {name}, age: {age}")

print("Hello \n world \t Hi\"")

print("Hello", end=" ")
print("World")


# 0, 0.0, "", [], {}, None, False   these are false

for i in [1, 2, 3]:
    print(i, end = " ")
    
for i in range(1, 10, 2):
    print(i, end = " ")

for i in range(3):
    for j in range(2):
        print(i, j)

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        pass
    else: 
        print(i)
        

s = "Python"
print(s[0])   # P
print(s[3])   # h
print(s[-1])  # n*** imp


#string slicing
print(s[0:4])
print(s[::-2])

# string are immutable but but.......
s = "H"+s[1:]
print(s)


u = "python Programming  "

print(u.upper())
k = u.lower()
print(k)
j = u.strip()
print(j)# removes spaces
m = u.replace("python", "Java")
print(m)
e = u.split()
print(e)# returns list
print(u.startswith("py"))
print(u.endswith("ing"))


print("Hello\nWorld")
print("Path: C:\\Users\\Ram")


for ch in "Python":
    print(ch)


nums = [1, 2, 3, 4]
names = ["Ram", "Shyam"]
mixed = [1, "Hi", 2.5]

print(nums, names, mixed)

nums = [1, 3, 2]
nums.append(4)