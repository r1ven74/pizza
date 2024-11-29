from model import get_price

def display_message(message):
    print(message)

def show_main_menu():
    print("Главное меню:")
    print("1. Регистрация")
    print("2. Заказать пиццу")
    print("3. Выход")

def register_user_view():
    name = input("Введите ваше имя: ")
    password = input("Введите пароль: ")
    birth_year = int(input("Введите год рождения: "))
    return name, password, birth_year

def pizza_selection_view(menu):
    orders = {}
    while True:
        for index, item in enumerate(menu, start=1):
            print(f"{index}. {item}")

        choice = input("Выберите пункт (или введите 'готово' для завершения заказа): ")
        if choice.lower() == 'готово':
            break

        if choice.isdigit() and 1 <= int(choice) <= len(menu):
            item = menu[int(choice) - 1]
            quantity = int(input(f"Сколько {item} вы хотите заказать? "))
            price = get_price(item)
            if price > 0:
                orders[item] = (quantity, price)
            else:
                print(f"Цена для {item} не найдена.")
        else:
            print("Неверный выбор, попробуйте еще раз.")

    return orders
