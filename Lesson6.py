# Задание 1

with open('nginx_logs.txt') as f:
    data = []
    for line in f:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
print(data)

# Задание 3

from itertools import zip_longest
import json

out_dict = {}
with open("users.csv", encoding='utf-8') as users:
    with open("hobby.csv", encoding='utf-8') as hobby:
        lines_users = sum(1 for line in users)
        lines_hobby = sum(1 for line in hobby)

        if lines_users < lines_hobby:
            exit(1)

            users.seek(0)
            hobby.seek(0)
            for line_user, lines_us_hob in zip_longest(users, hobby):
                out_dict[line_user.strip()] = lines_us_hob.strip() if lines_us_hob is not None else lines_us_hob

with open('task.json', 'w', encoding='utf-8') as f:
    json.dump(out_dict, f, ensure_ascii=False)
print(out_dict)

# Задание 6

import sys

nums = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as f:
    if len(nums) > 1:
        start_idx = int(nums[0])
        end_idx = int(nums[1])
    elif len(nums) == 0:
        start_idx = 0
        end_idx = sum(1 for line in f)
        f.seek(0)
    else:
        start_idx = int(nums[0])
        end_idx = sum(1 for line in f)
        f.seek(0)

    for idx, line in enumerate(f):
        if start_idx <= idx + 1 <= end_idx:
            print(line.strip())
