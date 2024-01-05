from models import get_categories,get_models,get_colors,get_memory
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Католог')],
    [KeyboardButton(text='Контакты')],
    [KeyboardButton(text='Настройка каталога')]
], resize_keyboard=True,one_time_keyboard=True,  input_field_placeholder='Выбирите пункт ниже')

admin_main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Добавить товар в католог')],
    [KeyboardButton(text='Удалить товар с католога')]
], resize_keyboard=True,one_time_keyboard=True,  input_field_placeholder='Выбирите пункт ниже')

contacts = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Контактные данные')],
    [KeyboardButton(text='График работы')],
    [KeyboardButton(text='Возвраты и обмены')],
    [KeyboardButton(text='Способы доставки')],
    [KeyboardButton(text='Ссылки на социальные сети')],
    [KeyboardButton(text='delete')],
    [KeyboardButton(text='Назад')]
], resize_keyboard=True)

color_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Цвет', callback_data='select_color')      
        ]

    ]
    
)


select_add_category = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='добавить новую категорию', callback_data='add_newcategory')      
        ],        
        [
            InlineKeyboardButton(text='редактировать существующию категорию', callback_data='add_yetcategory')      
        ]

    ]
    
)

async def categories():
    categories_kb = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        categories_kb.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    return categories_kb.adjust(2).as_markup()

async def for_admin_categories():
    categories_kb = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        categories_kb.add(InlineKeyboardButton(text=category.name, callback_data=f'cat_{category.id}'))
    return categories_kb.adjust(2).as_markup()  


async def for_admin_fulldelatecategories():
    categories_kb = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        categories_kb.add(InlineKeyboardButton(text=category.name, callback_data=f'delatecatfull_{category.id}'))
    return categories_kb.adjust(2).as_markup() 

async def for_admin_delatecategories():
    categories_kb = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        categories_kb.add(InlineKeyboardButton(text=category.name, callback_data=f'delatecat_{category.id}'))
    return categories_kb.adjust(2).as_markup() 

async def models(category_id):
    models_kb = InlineKeyboardBuilder()
    models = await get_models(category_id)
    for model in models:
        models_kb.add(InlineKeyboardButton(text= model.name, callback_data=f'model_{model.id}'))
    return models_kb.adjust(2).as_markup()


async def for_admin_models(category_id):
    models_kb = InlineKeyboardBuilder()
    models = await get_models(category_id)
    for model in models:
        models_kb.add(InlineKeyboardButton(text= model.name, callback_data=f'delatemodel_{model.id}'))
    return models_kb.adjust(2).as_markup()

async def colors(color_product_id):
    colors_kb = InlineKeyboardBuilder()
    colors = await get_colors(color_product_id)
    for color in colors:
        colors_kb.add(InlineKeyboardButton(text= color.name, callback_data=f'color_{color.id}'))
    return colors_kb.adjust(1).as_markup() 


async def memory(memory_product_id):
    memory_kb = InlineKeyboardBuilder()
    memorys = await get_memory(memory_product_id)
    for memory in memorys:
        memory_kb.add(InlineKeyboardButton(text= memory.memory,callback_data=f'memory_{memory.id}'))
    return memory_kb.adjust(1).as_markup()


buy_and_exit = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Купить', callback_data='select2_buy')      
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='select2_exit')     
        ]  
    ]
    
)

kb_fsm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Купить', callback_data='buy_product')      
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='buy_exit')     
        ]  
    ]
    
)


kb_yes_or_not = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да', callback_data='variant_yes')      
        ],
        [
            InlineKeyboardButton(text='Нет', callback_data='variant_not')     
        ]  
    ]
    
)

kb_result_add = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Продолжить', callback_data='action_corect')      
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='action_exit')     
        ]  
    ]
    
)

kb_result_add_color = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить еще цвет', callback_data='action_addcolor')      
        ],
        [
            InlineKeyboardButton(text='Продолжить', callback_data='action_continue')     
        ]  
    ]
    
)


kb_result_add_memory = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Добавить еще память', callback_data='action_addmemory')      
        ],
        [
            InlineKeyboardButton(text='Завершить', callback_data='action_finish')     
        ]  
    ]
    
)


kb_delete_db= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Удалить категорию', callback_data='kb_delate')      
        ],
        [
            InlineKeyboardButton(text='Удалить продукт', callback_data='kb_delateproduct')     
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='kb_exit')     
        ]  
    ]
    
)



