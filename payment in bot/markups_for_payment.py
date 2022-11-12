from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb_pay = InlineKeyboardMarkup(row_width=2)
ib_pay1 = InlineKeyboardButton(text='Секретный документ!', callback_data='%secret_dock%')
ib_pay2 = InlineKeyboardButton(text='Секретный пароль!', callback_data='@secret_password@')
ib_pay3 = InlineKeyboardButton(text='Какой-то номер', callback_data='#number_of_phone#')
ib_pay4 = InlineKeyboardButton(text='Какой-то контент', callback_data='$content$')
ikb_pay.add(ib_pay3, ib_pay4).row(ib_pay1, ib_pay2)