from aiogram import Bot
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from utils.config import TOKEN


storage = MemoryStorage()


bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)
