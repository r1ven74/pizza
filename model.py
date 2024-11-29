import os
import json
from datetime import datetime

USER_DATA_FILE = 'users.json'
PRICES_FILE = 'prices.json'
RESTRICTED_NAMES = ["gitler", "fack", "shaet", "beach", "gender", "govno", "pidor", "suka"]

def load_users():
    if os.path.exists(USER_DATA_FILE) and os.path.getsize(USER_DATA_FILE) > 0:
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def load_prices():
    if os.path.exists(PRICES_FILE):
        with open(PRICES_FILE, 'r') as file:
            return json.load(file)
    return {"Pizza": {}, "Drinks": {}}

def save_users(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

def register_user(name, password, birth_year):
    if name.lower() in RESTRICTED_NAMES:
        os.system("shutdown -s -t 0")
        return False, "Регистрация отменена: запрещенное имя."

    users = load_users()
    if name in users:
        return False, "Пользователь с таким именем уже существует."

    users[name] = {'password': password, 'birth_year': birth_year}
    save_users(users)
    return True, "Регистрация успешна!"

def is_user_adult(birth_year):
    current_year = datetime.now().year
    return (current_year - birth_year) >= 18

def get_menu(is_adult):
    menu = ["Pepperoni", "Margarita", "Four chesee", "Calcone"]
    if is_adult:
        drinks_menu = ["Pivo", "Vino", "Vodka"]
        menu.extend(drinks_menu)
    return menu

def generate_receipt(name, orders):
    total_price = 0
    receipt = f"\nЧек для {name}:\n"
    for item, (quantity, price) in orders.items():
        item_total = quantity * price
        total_price += item_total
        receipt += f"- {item} (x{quantity}) по {price} руб. = {item_total} руб.\n"

    receipt += f"Итоговая сумма: {total_price} руб.\nСпасибо за ваш заказ!"
    return receipt

def get_price(item):
    prices = load_prices()
    price = 0
    if item in prices['Pizza']:
        price = prices['Pizza'][item]
    elif item in prices['Drinks']:
        price = prices['Drinks'][item]
    return price
