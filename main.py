# main.py

# Import method 1
import math_utils

# Import method 2
from math_utils import square

import string_utils

# Import from package
from shop_package.discount import apply_discount
from shop_package.billing import calculate_total


# ---- Testing math_utils ----
print("Add:", math_utils.add(5, 3))
print("Subtract:", math_utils.subtract(10, 4))
print("Square:", square(6))


# ---- Testing string_utils ----
print("Upper:", string_utils.to_upper("hello"))
print("Lower:", string_utils.to_lower("WORLD"))
print("Length:", string_utils.get_length("Python"))


# ---- Testing package functions ----
prices = [100, 200, 300]

print("Total:", calculate_total(prices))
print("Discounted Price:", apply_discount(1000, 10))