from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    index_city = State()
    city = State()
    adress = State()
    telefon_number = State()
    email = State()


class Add_category(StatesGroup):
    categories_name = State()
    name_product = State()
    price_product = State()
    description_product = State()



class Add_color(StatesGroup):
    name_color = State()
    link = State()
    

class Add_memory(StatesGroup):
    memory = State()
    price_memory =State()
