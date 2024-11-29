from model import load_prices, register_user, get_menu, generate_receipt, is_user_adult, load_users
from view import display_message, show_main_menu, register_user_view, pizza_selection_view

def run_main_loop():
    users = load_users()

    while True:
        show_main_menu()
        choice = input("Выберите действие: ")

        if choice == '1':
            name, password, birth_year = register_user_view()
            success, message = register_user(name, password, birth_year)
            display_message(message)
            if success:
                users[name] = {'password': password, 'birth_year': birth_year}

        elif choice == '2':
            name = input("Введите ваше имя для заказа: ")
            if name not in users:
                display_message("Сначала необходимо зарегистрироваться.")
                continue
                
            password = input("Введите пароль: ")
            if password != users[name]['password']:
                display_message("Неверный пароль. Попробуйте снова.")
                continue
            
            # Проверка возраста
            is_adult = is_user_adult(users[name]['birth_year'])
            menu = get_menu(is_adult)

            # Вывод сообщения о доступном меню
            if is_adult:
                display_message("Выберите пиццу или напиток:")
            else:
                display_message("Выберите пиццу:")

            # Выбор пиццы и напитков
            orders = pizza_selection_view(menu)

            if orders:
                receipt = generate_receipt(name, orders)
                print(receipt)
                break  # Завершение программы после вывода чека

        elif choice == '3':
            print("Выход из программы.")
            break

        else:
            display_message("Неверный выбор, попробуйте снова.")
