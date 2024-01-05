from aiogram.types import Message
from aiogram.filters import BoundFilter
from dotenv import load_dotenv
import os

load_dotenv('.env')
ADMINS = os.getenv("ADMINS")

class IsAdmin(BoundFilter):

    async def check(self, message: Message):
        return message.from_user.id not in ADMINS