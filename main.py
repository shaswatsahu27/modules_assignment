# main.py

import math_utils
from math_utils import square

import string_utils

# Correct import style (VERY IMPORTANT)
import shop_package.discount as disc
import shop_package.billing as bill


# ---- math_utils ----
print("Add:", math_utils.add(2, 3))
print("Square:", square(5))


# ---- string_utils ----
text = "hello world"
print("Capitalize:", string_utils.capitalize_words(text))
print("Reverse:", string_utils.reverse_string(text))
print("Word Count:", string_utils.word_count(text))


# ---- package functions ----
price = 1000

print("Percentage Discount:", disc.apply_discount(price, 10))
print("Flat Discount:", disc.flat_discount(price, 100))

print("Total:", bill.calculate_total([100, 200, 300]))
print("Price with Tax:", bill.apply_tax(price, 18))
