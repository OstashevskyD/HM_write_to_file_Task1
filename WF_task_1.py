with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredient_count = int(file.readline())
        ingredients = []
        for i in range(ingredient_count):
            ing = file.readline().strip()
            ingredient_name, quantity, measure = ing.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingredients
print(cook_book)
