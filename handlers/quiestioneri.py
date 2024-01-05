# from aiogram import F,Router
# from aiogram.types import Message,CallbackQuery
# from aiogram.filters import Command 
# from aiogram.fsm.context import FSMContext 
# from main import Bot
# from utils.states import Form
# from keyboards.keyboard import kb_fsm


# router = Router()


# @router.callback_query(F.data.startswith('select2_buy'))
# async def buy_or_exit_selected(callback: CallbackQuery,state: FSMContext): 
#     await callback.message.delete()
#     await state.set_state(Form.city)
#     await callback.message.answer(
#         'Введите город куда отправится товар',
#     )

# @router.message(Form.city)
# async def form_city(message: Message, state: FSMContext):
#     await state.update_data(city=message.text)
#     await state.set_state(Form.index_city)
#     await message.answer('Отлично, введите индекс города')



# @router.message(Form.index_city)
# async def form_index_city(message: Message, state: FSMContext):
#     if message.text.isdigit():
#         await state.update_data(index_city = message.text)
#         await state.set_state(Form.adress)  
#         await message.answer('Теперь введите адрес')
#     else: 
#         await message.answer('Введите еще раз индекс города корректно')


# @router.message(Form.adress)
# async def form_adress(message: Message, state: FSMContext):
#     await state.update_data(adress=message.text)
#     await state.set_state(Form.email)
#     await message.answer('Теперь введите  электронный адрес')


# @router.message(Form.email)
# async def form_email(message: Message, state: FSMContext):
#     await state.update_data(email=message.text)
#     await state.set_state(Form.telefon_number)
#     await message.answer('Теперь введите  номер телефона')

# @router.message(Form.email)
# async def form_email(message: Message, state: FSMContext):
#     await state.update_data(email=message.text)
#     await state.set_state(Form.telefon_number)
#     await message.answer('Теперь введите  номер телефона')


# @router.message(Form.telefon_number)
# async def form_index_city(message: Message, state: FSMContext):
#     if message.text.isdigit():
#         await state.update_data(telefon_number = message.text)
#         data = await state.get_data()
#         await state.clear()
#         formated = []
#         [
#             formated.append(f'{key}: {value}')
#             for key, value in data.items()
#         ]
#         await message.answer('\n'.join(formated),reply_markup=kb_fsm)

#     else: 
#         await message.answer('Введите еще раз номер телфона') 


