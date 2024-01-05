from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, ReplyKeyboardMarkup, ReplyKeyboardRemove
from main import Bot
from aiogram import Router,F,types
from utils.states import Add_category,Add_color,Add_memory
from models import add_category,get_idcategory,add_product2,add_color_and_link,get_name_product,add_memory,get_namecategory,delete_product,delete_category
import keyboards.keyboard as kb
from dotenv import load_dotenv
from aiogram.fsm.context import FSMContext 
import os


class Admin_settings:
    def __init__(self):
        self.categories_name = None
        self.name_product = None
        self.price_product = None
        self.description_product = None
        self.city = None
        self.adress = None
        self.telefon_number = None
        self.email = None
        self.color = None
        self.link = None
        self.memory = None
        self.price_memory = None

    def set_memory(self,value):
        self.memory = value

    def set_price_memory(self,value):
        self.price_memory = value

    def set_categories_name(self,value):
        self.categories_name = value

    def set_name_product(self,value):
        self.name_product = value

    def set_price_product(self,value):
        self.price_product = value

    def set_description_product(self,value):
        self.description_product = value
    
    def set_email(self,value):
        self.email = value

    def set_model(self,value):
        self.model = value

    def set_color(self,value):
        self.color = value

    def set_link(self,value):
        self.link = value

    def set_memory(self,value):
        self.memory = value

    def get_settings(self):
        return {
            'categories_name': self.categories_name,
            'name_product': self.name_product,
            'price_product': self.price_product,
            'description_product' : self.description_product,
            'adress' : self.adress,
            'telefon_number' : self.telefon_number,
            'email' : self.email,
            'color' : self.color,
            'link' : self.link,
            'memory' : self.memory,
            'price_memory' : self.price_memory

        }
    def set_data(self, data):
        if 'categories_name' in data:
            self.set_categories_name(data['categories_name'])
        if 'name_product' in data:
            self.set_name_product(data['name_product'])
        if 'price_product' in data:
            self.set_price_product(data['price_product'])
        if 'description_product' in data:
            self.set_description_product(data['description_product'])
        if 'name_color' in data:
            self.set_color(data['name_color'])
        if 'link' in data:
            self.set_link(data['link'])
        if 'memory' in data:
            self.set_memory(data['memory'])
        if 'price_memory' in data:
            self.set_price_memory(data['price_memory'])


admin_settings = Admin_settings()

add_product = '➕ Добавить товар'
delete_category = '🗑️ Удалить категорию'

load_dotenv('.env')
Admins =  os.getenv("ADMINS")


router = Router()

@router.message(F.text =='Настройка каталога')
async def process_settings(message:Message):
    await message.delete()
    user_id = message.from_user.id
    if str(user_id) in Admins:
        await message.answer('Выбери пункт', reply_markup=kb.admin_main)


@router.message(F.text =='Добавить товар в католог')
async def process_add(message:Message):
    await message.delete()
    user_id = message.from_user.id
    if str(user_id) in Admins:
        await message.answer('Выбери действия', reply_markup=kb.select_add_category)


@router.message(F.text =='Удалить товар с католога')
async def process_delate(message:Message):
    await message.delete()
    user_id = message.from_user.id
    if str(user_id) in Admins:
        await message.answer('Выбери действия', reply_markup=kb.kb_delete_db)


@router.callback_query(F.data.startswith('kb_'))
async def add_selected(callback: CallbackQuery,state: FSMContext): 
    await callback.message.delete()
    
    action = callback.data.split('_')[1]
    if action == 'delate':
        await callback.message.answer('Выберите категорию для удаления', reply_markup= await kb.for_admin_fulldelatecategories())
    elif action == 'delateproduct':
        await callback.message.answer('Выберите категорию', reply_markup= await kb.for_admin_delatecategories())
    elif action == 'exit':
        await callback.message.answer('Выбирите дествия', reply_markup= await kb.main)


@router.callback_query(F.data.startswith('delatecatfull_'))
async def add_selected(callback: CallbackQuery,state: FSMContext): 
    await callback.message.delete()
    
    action = callback.data.split('_')[1]
    res = await get_namecategory(action)
    await delete_category(res)

@router.callback_query(F.data.startswith('delatecat_'))
async def add_selected(callback: CallbackQuery,state: FSMContext): 
    await callback.message.delete()
    
    action = callback.data.split('_')[1]
    await callback.message.answer('Выберите категорию', reply_markup= await kb.for_admin_models(action))


@router.callback_query(F.data.startswith('delatemodel_'))
async def add_selected(callback: CallbackQuery,state: FSMContext): 
    await callback.message.delete()
    
    action = callback.data.split('_')[1]
    await delete_product(action)
    await callback.message.answer('Успешно удален продукт', reply_markup= kb.main)


@router.callback_query(F.data.startswith('add_'))
async def add_selected(callback: CallbackQuery,state: FSMContext): 
    await callback.message.delete()
    
    action = callback.data.split('_')[1]
    if action == 'newcategory':
        await state.set_state(Add_category.categories_name)
        await callback.message.answer('Введи названия категории')
    elif action == 'yetcategory':
        await callback.message.answer('Выбирите категорию для редактирования', reply_markup= await kb.for_admin_categories())



@router.callback_query(F.data.startswith('cat_'))
async def category_selected(callback: CallbackQuery, state: FSMContext): 
    await callback.message.delete() 
    category_id = callback.data.split('_')[1]
    name_category = await get_namecategory(category_id)  
    admin_settings.set_categories_name(name_category.name)
    await state.update_data(categories_name=name_category.name)
    await state.set_state(Add_category.name_product)
    await callback.message.answer('Отлично, введи названия продукта')



# @router.callback_query(F.data.startswith('variant_'))
# async def category_selected(callback: CallbackQuery,bot: Bot): 
#     await callback.message.delete()
    
#     action = callback.data.split('_')[1]
#     if action == 'yes':



@router.message(Add_category.categories_name)
async def form_city(message: Message, state: FSMContext):
    await state.update_data(categories_name=message.text)
    await state.set_state(Add_category.name_product)
    await message.answer('Отлично, введи названия продукта')


@router.message(Add_category.name_product)
async def form_city(message: Message, state: FSMContext):
    await state.update_data(name_product=message.text)
    await state.set_state(Add_category.price_product)
    await message.answer('Отлично, введи цену продукта')


@router.message(Add_category.price_product)
async def form_index_city(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(price_product = message.text)
        await state.set_state(Add_category.description_product)  
        await message.answer('Теперь введи  описания товара')
    else: 
        await message.answer('Введите еще раз цену корректно')


@router.message(Add_category.description_product)
async def form_city(message: Message, state: FSMContext):
    await state.update_data(description_product=message.text)
    data = await state.get_data()
    await state.clear()
                
    admin_settings.set_data(data)
    formated = []
    [
        formated.append(f'{key}: {value}')
        for key, value in data.items()
    ]
    await message.answer('\n'.join(formated),reply_markup=kb.kb_result_add)



@router.message(Add_color.name_color)
async def form_city(message: Message, state: FSMContext):
    await state.update_data(name_color=message.text)
    await state.set_state(Add_color.link)
    await message.answer('Отлично, введи ссылку на фото продукта')

@router.message(Add_color.link)
async def form_city(message: Message, state: FSMContext):
    await state.update_data(link=message.text)
    data = await state.get_data()
    await state.clear()
    admin_settings.set_data(data)
    formated = []
    [
        formated.append(f'{key}: {value}')
        for key, value in data.items()
    ]
    color = admin_settings.get_settings()['color']
    link = admin_settings.get_settings()['link']
    name_product = admin_settings.get_settings()['name_product']
        
    result = await get_name_product(name_product)

    await add_color_and_link(color,link,result.id)
    await message.answer('\n'.join(formated),reply_markup=kb.kb_result_add_color)


@router.message(Add_memory.memory)
async def form_city(message: Message, state: FSMContext):
    await state.update_data(memory=message.text)
    await state.set_state(Add_memory.price_memory)
    await message.answer('Отлично, введи цену')


@router.message(Add_memory.price_memory)
async def form_city(message: Message, state: FSMContext):
    await state.update_data(price_memory=message.text)
    data = await state.get_data()
    await state.clear()
    admin_settings.set_data(data)
    formated = []
    [
        formated.append(f'{key}: {value}')
        for key, value in data.items()
    ]
    memory = admin_settings.get_settings()['memory']
    price_memory = admin_settings.get_settings()['price_memory']
    name_product = admin_settings.get_settings()['name_product']
        
    result = await get_name_product(name_product)

    await add_memory(memory,price_memory,result.id)
    await message.answer('\n'.join(formated),reply_markup=kb.kb_result_add_memory)


@router.callback_query(F.data.startswith('action_'))
async def add_selected(callback: CallbackQuery,state: FSMContext): 
    await callback.message.delete()
    
    action = callback.data.split('_')[1]
    if action == 'continue':
        await state.set_state(Add_memory.memory)
        await callback.message.answer('Введите память')
    elif action == 'addcolor':
        await state.set_state(Add_color.name_color)
        await callback.message.answer('Введите цвет')
    elif action == 'addmemory':
        await state.set_state(Add_memory.memory)
        await callback.message.answer('Введите память')
    elif action == 'finish':
        await callback.message.answer('Главное меню выбирите действия', reply_markup=kb.main)
    elif action == 'corect':
        name_category = admin_settings.get_settings()['categories_name']
        name_product = admin_settings.get_settings()['name_product']
        price_product = admin_settings.get_settings()['price_product']
        description_product = admin_settings.get_settings()['description_product']
        
        
        await add_category(name_category)
        id_category = await get_idcategory(name_category)
        await add_product2(name_product,price_product,description_product,id_category.id)
        await callback.message.answer('Успешно добавлено')
       
        
        await state.set_state(Add_color.name_color)
        await callback.message.answer('Введите цвет')
    
    else:
        await callback.message.answer('Выбери действия', reply_markup=kb.select_add_category)

