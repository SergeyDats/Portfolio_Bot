from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_sections = InlineKeyboardMarkup()
btn_football = InlineKeyboardButton(text="⚽Футбол⚽", callback_data="football")
btn_swimming = InlineKeyboardButton(text="🏊‍Плаванье🏊", callback_data="swimming")
btn_studying = InlineKeyboardButton(text="🎓‍Обучение🎓", callback_data="studying")
btn_programming = InlineKeyboardButton(text="💻Программирование💻", callback_data="programming")
btn_back = InlineKeyboardButton(text="🔙Назад🔙", callback_data="back")
kb_sections.add(btn_football)
kb_sections.add(btn_studying)
kb_sections.add(btn_swimming)
kb_sections.add(btn_programming)


# kb_sections.add(btn_programming, btn_studying)
# kb_sections.add(btn_football, btn_swimming)
def create_football_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text="2018: НАЧАЛО МОЕЙ ФУТБОЛЬНОЙ ИСТОРИИ", callback_data="btn_football_2018"),
        InlineKeyboardButton(text="2019 ТУРНИР: ВЕСЕНННИЙ КУБОК СМЕНЫ", callback_data="btn_football_2019"),
        InlineKeyboardButton(text="2021: ФИНАЛ КУБКА РОССИИ", callback_data="btn_football_2021_1"),
        InlineKeyboardButton(text="2021 ТУРНИР: КУБОК ДРУЖБЫ НАРОДОВ", callback_data="btn_football_2021_2"),
        InlineKeyboardButton(text="2022: ОСОБАЯ НОВОГОДНЯЯ ТРЕНИРОВКА", callback_data="btn_football_2022_1"),
        InlineKeyboardButton(text="2022 ТУРНИР: Football Events", callback_data="btn_football_2022_2"),
    ]
    keyboard.add(*buttons)
    keyboard.add(btn_back)  # Предполагается, что у вас уже есть кнопка btn_back

    return keyboard


def create_school_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text="1 Класс", callback_data="btn_school_1"),
        InlineKeyboardButton(text="2 Класс", callback_data="btn_school_2"),
        InlineKeyboardButton(text="3 Класс", callback_data="btn_school_3"),
        InlineKeyboardButton(text="4 Класс", callback_data="btn_school_4"),
        InlineKeyboardButton(text="5 Класс", callback_data="btn_school_5"),
        InlineKeyboardButton(text="6 Класс", callback_data="btn_school_6"),
        InlineKeyboardButton(text="7 Класс", callback_data="btn_school_7"),
    ]
    keyboard.add(*buttons)
    keyboard.add(btn_back)  # Предполагается, что у вас уже есть кнопка btn_back

    return keyboard


def create_swim_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text="Тренировки в маленьком бассейне", callback_data="btn_swimming_tsp"),
        InlineKeyboardButton(text="Тренировки в большом бассейне", callback_data="btn_swimming_tbp"),
        InlineKeyboardButton(text="Тренировки от родных по плаванью", callback_data="btn_swimming_slf"),
        InlineKeyboardButton(text="Успехи по плаванью в различных водоёмах", callback_data="btn_swimming_ssvwb"),
    ]
    keyboard.add(*buttons)
    keyboard.add(btn_back)  # Предполагается, что у вас уже есть кнопка btn_back

    return keyboard


def create_programming_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text="1-я часть Курса", callback_data="btn_programming_1"),
        InlineKeyboardButton(text="2-я часть Курса", callback_data="btn_programming_2"),
        InlineKeyboardButton(text="3-я часть Курса", callback_data="btn_programming_3"),
        InlineKeyboardButton(text="4-я часть Курса", callback_data="btn_programming_4"),
        InlineKeyboardButton(text="Работы", callback_data="btn_programming_w"),
    ]
    keyboard.add(*buttons)
    keyboard.add(btn_back)  # Предполагается, что у вас уже есть кнопка btn_back

    return keyboard


def kb_help_sections():
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text="Помощь с ботом", callback_data="help_1"),
        InlineKeyboardButton(text="Помощь с обновлениями бота", callback_data="help_2"),
        InlineKeyboardButton(text="Отправить сообщение администратору бота с помощью", callback_data="help_3"),
        InlineKeyboardButton(text="❌Удалить данное сообщение❌", callback_data="help_delete"),
    ]
    keyboard.add(*buttons)
    return keyboard


def football_events():
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text="Помощь с ботом", callback_data="help_1"),
        InlineKeyboardButton(text="Помощь с обновлениями бота", callback_data="help_2"),
        InlineKeyboardButton(text="Отправить сообщение администратору бота с помощью", callback_data="help_3"),
        InlineKeyboardButton(text="❌Удалить данное сообщение❌", callback_data="help_delete"),
    ]
    keyboard.add(*buttons)
    return keyboard
