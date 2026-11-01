from collections import defaultdict

categories = {
    'rent': 40000,
    'grocery': 35000,
}

operations = {'grocery': [100, 345, 564]}

def print_categories():
    for key, value in categories.items():
        print(f'category {key}: amount {value}')
def add_categry(cat, amount):
    categories[cat] = amount

def filter_and_sort():
    temp = {}
    for key, value in categories.items():
        if value > 5000:
            temp[key] = value
    return sorted(temp)

def strip_string(string):
    return string.strip().lower()

def get_catgories_set():
    return set(categories.keys())

def get_operations_with_defaultdict(category: str):
    default = defaultdict(lambda: 'not found')
    if category not in operations.keys():
        return default[category]
    return operations[category]


def get_operations(category: str):
    return operations[category]

add_categry('restaurants', 5000)
print(filter_and_sort())
print_categories()
print(strip_string(" ToП-3, категории; БАНКА "))
print(get_catgories_set())
print(get_operations_with_defaultdict('restaurants'))
print(get_operations('grocery'))