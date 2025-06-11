shopping_list = []

def shopping_add(*name):
    for item in name:
        shopping_list.append(item)


def shopping_remove(*name):
    for item in name:
        if item in  shopping_list:
            shopping_list.remove(item)
        else:
            print(f"{item} not present in shopping list")

shopping_add("apple", "banana", "orange", "sour")

shopping_remove("ball", "sour")

print(shopping_list)


