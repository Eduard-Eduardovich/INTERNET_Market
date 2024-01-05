from aiogram.types import Message
from dotenv import load_dotenv
import os
from aiogram.filters import BaseFilter

load_dotenv('.env')
ADMINS =  os.getenv("ADMINS")

class  IsAdmin(BaseFilter):
    async def check(self,message:Message):
        return message.from_user.id in ADMINS