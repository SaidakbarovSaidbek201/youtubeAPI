from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from database import get_all_categories, get_all_products


start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboards.add(KeyboardButton('Course'))
start_keyboards.add(KeyboardButton('Lessons'))
start_keyboards.add(KeyboardButton('Registr'), KeyboardButton('Enrollment'))

admin_start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, 
    keyboard=[
        [KeyboardButton('Course')],
        [KeyboardButton('Course ✏️/➕'), KeyboardButton('Lesson ✏️/➕')],
        [KeyboardButton('Course ochirish ❌'), KeyboardButton('Lesson ochirish ❌')],
])

contact = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Telefon raqam jonatish', request_contact=True))


def menu_keyboards():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    categories = get_all_categories()
    for category in categories:
        keyboard.add(KeyboardButton(category['name']))
    return keyboard.add(KeyboardButton('🔙 Orqaga'))


def product_keyboards_by_category(category_id):
    keyboard = InlineKeyboardMarkup()
    products = get_all_products()
    for product in products:
        if product['category_id'] == category_id:
            keyboard.add(InlineKeyboardButton(product['name'], callback_data=product['id']))
    return keyboard


def product_keyboards_by_id(product_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('🛒 Savatchaga qo\'shish', callback_data=f'add_to_cart_{product_id}'))
    keyboard.add(InlineKeyboardButton('🔙 Orqaga', callback_data='back'))
    return keyboard