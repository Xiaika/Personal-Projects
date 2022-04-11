from collections import defaultdict, Counter, OrderedDict
from typing import Dict, DefaultDict, Set, List
Ingredient = str
Allergen = str
Ingredients = Set[Ingredient]

counter = Counter()

def find_allergens(dic: Dict[Allergen, Ingredients]) -> Dict[Allergen, Ingredient]:
    """Reduce the possible allergens dict to a dictionary with
    key: allergen, value: ingredient"""
    new_dic = dict()
    for key, value in dic.items():
        values = list()
        for string in value:
            values.append(string)
        new_dic[key] = values

    actual_allergens = dict()
    # Check every value against every other value
    found = 0
    while found < len(new_dic):
        found = 0
        for key, value in new_dic.items():
            if len(value) == 1:
                actual_allergens[key] = list(value)[0]
                found += 1
        temp_dic = new_dic.copy()
        for key2, value2 in temp_dic.items():
            if len(value2) > 1:
                edited = [item for item in value2 if item not in actual_allergens.values()]
                new_dic[key2] = edited

    return actual_allergens




def find_clean_ingredients() -> list:
    """Check every set of ingredients for intersections
       with respect to the allergen"""
    clean_ingredients = list()
    for key, list_of_sets in foods.items():
        # compute the intersection of all sets per key
        intersect = set.intersection(*list_of_sets)
        for _set in list_of_sets:
            # compute the set difference of each set and the intersection
            set_difference = _set ^ intersect
            if len(set_difference) != 0:
                for ingredient in set_difference:
                    if ingredient not in clean_ingredients:
                        # Add unique ingredients to a list
                        clean_ingredients.append(ingredient)
        possible_allergies[key] = intersect

    # flatten possible allergies dict into a set of strings of the values
    temp = [string for set_ in possible_allergies.values() for string in set_]
    temp = set(temp)
    # print('Foods: ', dict(foods))
    # print('Temp: ', temp)
    # remove all occurrences of the allergenic ingredients from clean ingredients
    return [item for item in clean_ingredients if item not in temp]

def add_to_dict(ingredients, allergens):
    """Takes in a list of ingredients and a list of allergens and
       adds to a dictionary of {allergens: list of sets of ingredients}"""
    # Count how many times every ingredient occurs in the file
    for ingredient in ingredients:
        counter[ingredient] += 1
    ingredients = set(ingredients)  # Remove duplicates after counting

    # Make a dictionary of allergens to a list of sets of ingredients
    for allergen in allergens:
        foods[allergen].append(ingredients)

def parse(data):
    """Parse the data into a usable form"""
    for line in data:
        # Parse the data into usable form
        line = line.replace('contains ', '')
        line = line.replace('(', ': ')
        line = line.replace(')', '')
        line = line.replace(',', '')
        left = line.split(' : ')[0]
        right = line.split(' : ')[1]

        # Capture the ingredients and allergens separately
        ingredients = left.split()
        allergens = right.split()
        add_to_dict(ingredients, allergens)


with open('Problem21.txt') as infile:
    data = infile.read().splitlines()
    foods = defaultdict(list)

parse(data)
possible_allergies = defaultdict(set)
clean_ingredients = find_clean_ingredients()
allergens = find_allergens(possible_allergies)

# sum the count of all clean ingredients
result = sum((counter[ingredient]) for ingredient in clean_ingredients)
print('Part 1 answer: ', result)

# Alphabetize allergenic ingredients and print comma delimited list
allergens = OrderedDict(allergens)
allergens = sorted(allergens.items())
string = ''
i = 1
for key, value in allergens:
    string += value
    if i < len(allergens):
        string += ','
    i += 1
print('Part 2 answer: ', string)


