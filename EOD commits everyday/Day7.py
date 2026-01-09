# ===============================================================
# Lambda, map, filter, reduce
# =================================================================

add = lambda a, b: a+b
print(add(2,3))


"""When to Use Lambda

Use when:

    Function is small

    Used once

    Improves readability


    Don’t use for complex logic."""
    


nums = [1, 2, 3]
squares = list(map(lambda x: x*x, nums))
print(squares)



even = list(filter(lambda x: x%2 == 0, nums))
print(even)

from functools import reduce

total = reduce(lambda x, y: x+y, nums)
print(total)

nu = reduce(lambda a,b : a if a>b else b, nums)
print(nu)

# map
[x*x for x in nums]

# filter
[x for x in nums if x % 2 == 0]

import math
print(math.sqrt(16))

"""
__init__.py (Important Concept)

Marks a directory as a package.

services/
 ├─ __init__.py
 ├─ user_service.py


Inside __init__.py:

from .user_service import get_user


Now:

from services import get_user


👉 Used heavily in Flask apps.

Keyword arguments:
argument -- description
Return: return_description
"""


