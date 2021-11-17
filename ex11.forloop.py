
num_list = [23,45,54,67,32,98,25,76]
num_total = 0
num_average = 0
item_count = 0
for num in num_list:
    num_total += num  # without using sum
    item_count += 1# without using len()
print(f"Total = {num_total}")
print(f"Average = {num_total/item_count}")

sum_num = 0
for num in range(1,101):
    sum_num += num # without using sum
print(f"Sum of numbers between range = {sum_num}")


sum_num_even = 0
for num in range(2,101):
    if num % 2 == 0:
        sum_num_even += num # without using sum
print(f"Sum of even numbers between range = {sum_num_even}")

sum_num_odd = 0
for num in range(1,101):
    if num % 2 != 0:
        sum_num_odd += num
print(f"Sum of odd numbers between range = {sum_num_odd}")