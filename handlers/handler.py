from aiogram import Router, F,types
from main import Bot
import os
from dotenv import load_dotenv
from utils.states import Form
from aiogram.filters.command import Command
from aiogram.types import Message,CallbackQuery
from aiogram.types.message import ContentType
from aiogram.fsm.context import FSMContext 
from models import get_description,add_user_and_purchases,get_color_id,get_memory_id,get_color_link,delete_product
import keyboards.keyboard as kb



load_dotenv('.env')
PAYMENTS_TOKEN = os.getenv("PAYMENTS_TOKEN")


class Settings:
    def __init__(self):
        self.model = None
        self.color = None
        self.memory = None
        self.index_city = None
        self.city = None
        self.adress = None
        self.telefon_number = None
        self.email = None

    def set_index_city(self,value):
        self.index_city = value

    def set_city(self,value):
        self.city = value

    def set_adress(self,value):
        self.adress = value

    def set_telefon_number(self,value):
        self.telefon_number = value
    
    def set_email(self,value):
        self.email = value

    def set_model(self,value):
        self.model = value

    def set_color(self,value):
        self.color = value

    def set_memory(self,value):
        self.memory = value

    def get_settings(self):
        return {
            'model': self.model,
            'color': self.color,
            'memory': self.memory,
            'city' : self.city,
            'adress' : self.adress,
            'index_city':self.index_city,
            'telefon_number' : self.telefon_number,
            'email' : self.email

        }
    def set_data(self, data):
        if 'index_city' in data:
            self.set_index_city(data['index_city'])
        if 'city' in data:
            self.set_city(data['city'])
        if 'adress' in data:
            self.set_adress(data['adress'])
        if 'telefon_number' in data:
            self.set_telefon_number(data['telefon_number'])
        if 'email' in data:
            self.set_email(data['email'])

router = Router()

settings = Settings()





photos = {
    '1': 'https://i.pinimg.com/564x/86/5b/4f/865b4ffa4d109700e22343051ae4922f.jpg',
    '2': 'https://i.pinimg.com/564x/c9/0b/73/c90b7302d866c27a7263b5ec49a82e2b.jpg',
    '3': 'https://i.pinimg.com/564x/df/10/8e/df108ea01b988b641e02e28a518c4997.jpg',
    '4': 'https://i.pinimg.com/564x/7f/dc/2f/7fdc2f00b1790eccca942115870a28e3.jpg',
    '5': 'https://media.bechtle.com/is/180712/1c4b3d4ee288fc9434f5175bf56070570/c3/gallery/dad4f22ffe8f41d1a7897e5a4ee947bc?version=0',
    '6': 'https://m.media-amazon.com/images/I/61xk5l4aXOL._AC_UF894,1000_QL80_.jpg'
}

photos_category = {
    '1': 'https://assets-global.website-files.com/60a35497ea15cf45782248b1/64ad1c67e150599b36b7b3d4_6285fcBg.webp',
    '2': 'https://ipkey.com.ua/media/k2/items/cache/36778fed172d9c8502d2d42dc025835b_XL.jpg',
    '3': '',
    '4': ''
}


@router.message(Command("start"))
async def command_start(message :types.Message):
    user_name = message.from_user.username
    greeting = f"Привет, {user_name}! Добро пожаловать в интернет магазин BossMarket!"
    await message.answer(text=greeting, reply_markup=kb.main)


@router.message(F.text == 'delete')
async def contacts(message :Message):
    await delete_product(5)



@router.message(F.text == 'Католог')
async def catalog(message :Message,bot: Bot):
    photo_url = 'https://i.pinimg.com/564x/85/c8/3d/85c83d242b73d3c52b8c4c2e7df27db7.jpg'
    await bot.send_photo(message.chat.id,caption='Выберите вариант из католога', photo=photo_url, reply_markup= await kb.categories())

@router.message(F.text == 'Контакты')
async def contacts(message :Message):
    await message.answer('Информация о магазине', reply_markup=  kb.contacts)

@router.message(F.text == 'Контактные данные')
async def catalog(message :Message):
    await message.answer('Телефоны: 🇩🇪️ +49 223 222-11-2,  🇺🇦 +380 44 222-11-2')
    
@router.message(F.text == 'График работы')
async def catalog(message :Message):
    await message.answer('Понедельник-пятница: с 9:00 до 18:00\nСуббота: с 10:00 до 16:00\nВоскресенье: выходной')

@router.message(F.text == 'Возвраты и обмены')
async def catalog(message :Message):
    await message.answer('Возврат товара в течение 14 дней\nОбмен товара в течение 7 дней')

@router.message(F.text == 'Ссылки на социальные сети')
async def catalog(message :Message):
    await message.answer('Интернет магазин сайт -> https://allo.ua/\nИнстаграм -> https://goo.su/gkJYM')

@router.message(F.text == 'Способы доставки')
async def catalog(message :Message):
    await message.answer('Доставка курьером\nДоставка почтой DHL\nСамовывоз')

@router.message(F.text == 'Назад')
async def catalog(message :Message):
    await message.answer( text='Выбирите действия',reply_markup=kb.main)



@router.callback_query(F.data.startswith('category_'))
async def category_selected(callback: CallbackQuery,bot: Bot): 
    await callback.message.delete() 
    category_id = callback.data.split('_')[1]
    if category_id == "1":
        await bot.send_photo(callback.message.chat.id,caption='Выберите вариант модели', photo=photos_category[category_id], reply_markup= await kb.models(category_id))
    elif category_id == "2":
        await bot.send_photo(callback.message.chat.id,caption='Выберите вариант модели', photo=photos_category[category_id], reply_markup= await kb.models(category_id))
    await callback.answer("Выбрано!")

    
    
@router.callback_query(F.data.startswith('model_'))
async def model_selected(callback: CallbackQuery,bot: Bot): 
    await callback.message.delete()
    model_id = callback.data.split('_')[1]
    text = await get_description(model_id)
    settings.set_model(model_id)
    photo_path = photos[model_id]
    await bot.send_photo(callback.message.chat.id, photo=photo_path, caption=f'{text.description}', reply_markup= kb.color_kb)


    
@router.callback_query(F.data.startswith('select_'))
async def select_selected(callback: CallbackQuery,bot: Bot): 
    await callback.message.delete()
    model_id = settings.get_settings()['model']
    select = callback.data.split('_')[1]
    await bot.send_photo(callback.message.chat.id, photo=photos[model_id], caption='Выбирите цвет', reply_markup= await kb.colors(model_id)) 


@router.callback_query(F.data.startswith('color_'))
async def color_selected(callback: CallbackQuery,bot: Bot): 
    await callback.message.delete()
    model_id = settings.get_settings()['model']
    select = callback.data.split('_')[1]
    settings.set_color(select)
    await bot.send_photo(callback.message.chat.id, photo=photos[model_id], caption='Выбирите память', reply_markup= await kb.memory(model_id)) 




@router.callback_query(F.data.startswith('memory_'))
async def memory_selected(callback: CallbackQuery,bot: Bot): 
    await callback.message.delete()
    model_id = settings.get_settings()['model']
    color_id = settings.get_settings()['color']
    select = callback.data.split('_')[1]
    settings.set_memory(select)
    photo_path = photos[model_id]
    text = await get_description(model_id)
    color = await get_color_id(color_id)
    memory = await get_memory_id(select)
    await bot.send_photo(callback.message.chat.id, photo=photo_path, caption=f'{text.description}\n\n цена {memory.price}\n\n цвет {color.name}\n\n память {memory.memory}', reply_markup= kb.buy_and_exit)
      
@router.callback_query(F.data.startswith('buy_exit'))
async def memory_selected(callback: CallbackQuery,bot: Bot): 
    await callback.message.delete()
    model_id = settings.get_settings()['model']
    color_id = settings.get_settings()['color']
    memory_id = settings.get_settings()['memory']
    photo_path = photos[model_id]
    text = await get_description(model_id)
    color = await get_color_id(color_id)
    memory = await get_memory_id(memory_id)
    await bot.send_photo(callback.message.chat.id, photo=photo_path, caption=f'{text.description}\n\n цена {memory.price}\n\n цвет {color.name}\n\n память {memory.memory}', reply_markup= kb.buy_and_exit)


@router.callback_query(F.data.startswith('buy_'))
async def buy_or_exit_selected(callback: CallbackQuery,bot:Bot): 
    await callback.message.delete() 
    select = callback.data.split('_')[1]
    if select == 'product':
        model = settings.get_settings()['model']
        color = settings.get_settings()['color']
        memory = settings.get_settings()['memory']
        text_id = await get_description(model)
        color_id = await get_color_id(color)
        memory_id = await get_memory_id(memory)
        photo_path = await get_color_link(color)
        user_id = callback.from_user.id
        PRICE = types.LabeledPrice(label=text_id.name,amount=memory_id.price*100)

        if PAYMENTS_TOKEN.split(':')[1] == 'TEST':
            await  callback.message.answer('Оплата товара')
            await bot.send_invoice(callback.message.chat.id,
                title=text_id.name,
                description=f'цвет {color_id.name}, память {memory_id.memory} Гб',
                provider_token=PAYMENTS_TOKEN,
                currency='EUR',
                photo_url=photo_path,
                is_flexible=False,
                prices=[PRICE], 
                start_parameter='onedwdwdwd',
                payload='test-infewif')

    elif select == 'exit':
        settings.set_color(None)
        settings.set_memory(None)   
        settings.set_model(None)
        await callback.message.answer('Выберите вариант из католога', reply_markup= await kb.categories())

@router.pre_checkout_query(lambda query:True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery,bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
    if hasattr(pre_checkout_query.order_info, 'email') and (pre_checkout_query.order_info.email == 'vasya@pupkin.com'):
        return await bot.answer_pre_checkout_query(
            pre_checkout_query.id,
            ok=False,
            error_message='Нам кажется, что указанный имейл не действителен.\nПопробуйте указать другой имейл')
    
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)



@router.message(F.content_type == types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message, bot: Bot):
    print('successful_payment:')  
    model = settings.get_settings()['model']
    color = settings.get_settings()['color']
    memory = settings.get_settings()['memory']
    phone_number = settings.get_settings()['telefon_number']
    email = settings.get_settings()['email']
    adress = settings.get_settings()['adress']
    city = settings.get_settings()['city']
    index_city = settings.get_settings()['index_city']
    user_id = message.from_user.id
    await add_user_and_purchases(user_id,model,color,memory,adress,city,index_city,phone_number,email)
    pmnt = message.successful_payment
    for key in pmnt.__fields__:
        print(f'{key} = {getattr(pmnt, key)}')
    await bot.send_message(
        message.chat.id,
        f' Успешная покупка: {pmnt.total_amount // 100} {pmnt.currency} ждите на почту дальнейшие действия',
    )
    



@router.callback_query(F.data.startswith('select2_buy'))
async def buy_or_exit_selected(callback: CallbackQuery,state: FSMContext): 
    await callback.message.delete()
    await state.set_state(Form.city)
    await callback.message.answer(
        'Введите город куда отправится товар',
    )

@router.message(Form.city)
async def form_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(Form.index_city)
    await message.answer('Отлично, введите индекс города')



@router.message(Form.index_city)
async def form_index_city(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(index_city = message.text)
        await state.set_state(Form.adress)  
        await message.answer('Теперь введите адрес')
    else: 
        await message.answer('Введите еще раз индекс города корректно')


@router.message(Form.adress)
async def form_adress(message: Message, state: FSMContext):
    await state.update_data(adress=message.text)
    await state.set_state(Form.email)
    await message.answer('Теперь введите  электронный адрес')


@router.message(Form.email)
async def form_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await state.set_state(Form.telefon_number)
    await message.answer('Теперь введите  номер телефона')

@router.message(Form.email)
async def form_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await state.set_state(Form.telefon_number)
    await message.answer('Теперь введите  номер телефона')



@router.message(Form.telefon_number)
async def form_index_city(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(telefon_number = message.text)
        data = await state.get_data()
        await state.clear()
        settings.set_data(data)
        formated = []
        [
            formated.append(f'{key}: {value}')
            for key, value in data.items()  
        ]
        await message.answer('\n'.join(formated),reply_markup=kb.kb_fsm)

    else: 
        await message.answer('Введите еще раз номер телфона') 