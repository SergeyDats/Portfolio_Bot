from aiogram import Bot, Dispatcher, types, executor
import logging
from config import Token
from Keyboards import kb_sections, create_football_keyboard, create_school_keyboard, create_swim_keyboard, \
    create_programming_keyboard, kb_help_sections
from aiogram.utils import exceptions

logging.basicConfig(level=logging.INFO)
bot = Bot(token=Token)
dp = Dispatcher(bot=bot)


async def set_start_command(bot: Bot, chat_id):
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Перезапуск Бота + Возможные Обновления"),
        types.BotCommand(command="help", description="Помощь с Ботом"),
    ], scope=types.BotCommandScopeChat(chat_id), language_code="ru")
    # Scope-Область, пространство(чат, где нужно установить команды)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await set_start_command(bot, message.from_user.id)
    photo = types.InputFile("photo_menu vchera.jpg")  # Открываем Картинку
    await message.answer_photo(photo=photo, caption=F"Привет, {message.from_user.full_name}!\n"
                                                    F"Выберите интересующий вас раздел ниже ⬇",
                               reply_markup=kb_sections)


@dp.callback_query_handler(text="football")
async def football(call: types.CallbackQuery):
    await call.answer()  # Отвечаем на callback, убираем часики
    photo = types.InputMediaPhoto(
        open("photo_football_allteam.jpg", "rb"))  # rb-Открытие картинки в виде двоичного Кода
    await call.message.edit_media(media=photo)
    await call.message.edit_caption(caption="Вы попали в раздел ⚽Футбола⚽, выберите Год ⬇",
                                    reply_markup=create_football_keyboard())


@dp.callback_query_handler(text="back")
async def back(call: types.CallbackQuery):
    photo = types.InputMediaPhoto(open("photo_menu vchera.jpg", "rb"))
    await call.message.edit_media(media=photo)
    await call.message.edit_caption(caption=F"Привет, {call.from_user.full_name}!\n"
                                            "Выберите интересующий вас раздел ниже ⬇", reply_markup=kb_sections)


@dp.callback_query_handler(text="studying")
async def studying(call: types.CallbackQuery):
    await call.answer()  # Отвечаем на callback, убираем часики
    photo = types.InputMediaPhoto(open("photo_2023-08-25_12-18-49 studying.jpg", "rb"))
    await call.message.edit_media(media=photo)
    await call.message.edit_caption(caption="Вы попали в раздел 🎓Обучения🎓, выберите Класс ⬇",
                                    reply_markup=create_school_keyboard())


@dp.callback_query_handler(text="swimming")
async def swimming(call: types.CallbackQuery):
    await call.answer()  # Отвечаем на callback, убираем часики
    photo = types.InputMediaPhoto(open("photo_pul_1.jpg", "rb"))
    await call.message.edit_media(media=photo)
    await call.message.edit_caption(caption="Вы попали в раздел 🏊‍Плаванье🏊, выберите интересующую Вас статью ⬇",
                                    reply_markup=create_swim_keyboard())


@dp.callback_query_handler(text="programming")
async def programming(call: types.CallbackQuery):
    await call.answer()  # Отвечаем на callback, убираем часики
    photo = types.InputMediaPhoto(open("photo_it_sevodnya.jpg", "rb"))
    await call.message.edit_media(media=photo)
    await call.message.edit_caption(caption="Вы попали в раздел 💻Программирование💻, выберите интересующий Вас Курс ⬇",
                                    reply_markup=create_programming_keyboard())


@dp.message_handler(commands="help")
async def help(message: types.Message):
    photo = types.InputFile("help.jpg")
    await message.answer_photo(photo=photo, caption=F"Привет, {message.from_user.full_name}, чем могу помочь?\n"
                                                    F"Выберите интересующий вас раздел ниже ⬇",
                               reply_markup=kb_help_sections())


@dp.callback_query_handler(text="help_delete")
async def delete(call: types.CallbackQuery):
    await call.answer()  # Отвечаем на callback, убираем часики
    await call.message.delete()
    try:
        # Блок кода, который может быть с ошибкой
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    except exceptions.MessageToDeleteNotFound:
        pass


executor.start_polling(dp)
