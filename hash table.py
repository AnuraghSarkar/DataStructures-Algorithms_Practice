from typing import Dict

lists: Dict[str, int] = {'Ram': 1, 'Shyam': 8, "Hari": 4}
for data in lists:
    print(data)


def check_twice(list_people):
    name_dict = {}
    for i in list_people:
        if i in name_dict:
            return i
        name_dict[i] = 1
    return None


print(check_twice(['Ram', 'Hari', 'Shyam', 'Krishna']))
