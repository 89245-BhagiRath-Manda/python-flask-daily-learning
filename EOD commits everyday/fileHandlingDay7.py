# import os
# print("CWD:", os.getcwd())


# with open("data.txt", "r") as f:
#     content = f.read()

# print(content)

# with open("data.txt", "w") as f:
#     f.write("Hello\n")

import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "data.txt")

with open(file_path, "r") as f:
    content = f.read()

print(content)

