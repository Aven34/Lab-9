import datetime

def delivery_decorator(func):

    def wrapper(num_items):

        start_time = datetime.datetime.now()

        result = func(num_items)

        end_time = datetime.datetime.now()

        print(f"Время запуска функции: {start_time}")

        print(f"Количество товаров: {num_items}")

        print(f"Стоимость доставки: {result}")

        print(f"Время окончания работы функции: {end_time}")

        return result

    return wrapper

@delivery_decorator

def express_delivery(num_items):

    if num_items == 1:

        return 10.95

    elif num_items > 1:

        return 10.95 + 2.95 * (num_items - 1)

    else:

        return 0

num_items = int(input("Введите количество товаров в заказе: "))

total_delivery_cost = express_delivery(num_items)

print(f"Общая стоимость доставки: {total_delivery_cost}") 
