# Step 01
# import my_calculator.addition
# import my_calculator.substraction

# result1 = my_calculator.addition.add(55 , 65)
# result2 = my_calculator.substraction.sub(75 , 65)

# print(result1)
# print(result2)

# Step 02
# from my_calculator import addition
# from my_calculator import substraction

# result1 = addition.add(55 , 65)
# result2 = substraction.sub(75 , 65)

# print(result1)
# print(result2)

# Step 03
from my_calculator.addition import add
from my_calculator.substraction import sub

result1 = add.add(55 , 65)
result2 = sub.sub(75 , 65)

print(result1)
print(result2)