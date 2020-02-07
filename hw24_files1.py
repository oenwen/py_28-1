
def create_cookbook():
    global cookbook
    cookbook = dict()
    dish_list = list()
    ingredient_list = list()
    with open('recipes.txt', encoding='utf8') as recipes:
        while True:
            dish = recipes.readline().strip()
            if not dish:
                break
            dish_list.append(dish)
            quantity = int(recipes.readline().strip())
            for i in range(quantity):
                ingredient_list.append(recipes.readline().strip())
            recipes.readline().strip() # чтение пустой строки
            # превращение списка строк ingredient_list в список словарей
            book_values = list()
            for ingredient in ingredient_list:
                ingredient_name = ingredient.split(' | ')[0]
                ingredient_quantity = int(ingredient.split(' | ')[1])
                ingredient_unit = ingredient.split(' | ')[2]
                ingredient_dict = {'ingredient_name':ingredient_name,
                                   'quantity':ingredient_quantity,
                                   'measure':ingredient_unit}
                book_values.append(ingredient_dict)
            cookbook[dish] = book_values
            ingredient_list = list()
        from pprint import pprint
        pprint(cookbook)

def get_shop_list_by_dishes(dishes, person_count):
    print(f'\nМеню: {cookbook.keys()}')
    order = input('Введите порядковые номера нужных блюд через запятую ')
    order_list = (order.split(sep = ','))














    # person_count = int(input('Введите количество персон'))
    pass



def main():
    create_cookbook()
    get_shop_list_by_dishes(dishes = [], person_count=0)
main()




