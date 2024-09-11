import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

rand_num = random.randint(lower_bound, upper_bound)

print(f"Your random number is {rand_num}")