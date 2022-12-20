import re

total = 0
hand = open('regex_sum_1658023.txt')
for line in hand:
    numbers = re.findall('[0-9]+', line)
    new_list = [int(item) for item in numbers]
    if new_list:
        newone = sum(new_list)
        total = newone + total
print(total)
