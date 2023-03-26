# Подключение библиотек
from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

# Создание переменной токена бота и создание экземпляров классов Bot и Dispatcher
token = 'TOKEN'  # Сюда вместо TOKEN нужно вставлять токен бота
bot = Bot(token)
dp = Dispatcher(bot)


# Функция, объявляющая запуск бота
async def on_startup(_):
    print('Я запустился!')




@dp.message_handler(commands=['start'])  # Обработчик команды /start
async def start(message: types.Message):  # Функция start
    ikb = InlineKeyboardMarkup(row_width=2)  # Создание инлайн клавиатуры и кнопки с текстом и ссылкой
    ikb.add(InlineKeyboardButton('Zegich', url='https://t.me/+imjtN9g5PFdhMzZi'))
    ikb.add(InlineKeyboardButton('Я подписался!✅', callback_data='prov')) #Здесь вместо ссылки прикрепляю callback данные
    #Отправка сообщения с начальным текстом
    await message.answer('''
    Привет🖐, тебя приветствует бот, созданный разработчиком Zegich🐸.
Чтобы продолжить общение с ботом, подпишись на его Telegram канал✅.
    ''', reply_markup=ikb)


#Обработчик callback запросов
@dp.callback_query_handler()
async def proverka(callback: types.CallbackQuery): #Функция proverka
    if callback.data == 'prov': #Если callback данные совпадают, то бот делает проверку
        user_channel_status = await bot.get_chat_member(chat_id=-1001930581929, user_id = callback.from_user.id) #Сюда записывается строка с информацией из чата
        if user_channel_status["status"] != 'left':  #Если кусок предыдущей строки не равен left, то бот отправляет сообщение
            await callback.message.answer('Ты подписался на канал!🥳')
        else: #Если же равно, то выводится табличка
            await callback.answer('Ты ещё не подписался!❌', show_alert=True)



if __name__ == "__main__":  # Условие, если код выполняется самостоятельно, то бот стартует
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
