from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.message import ContentType
import logging
from config import TOKEN, PAYMENT_TOKEN
from markups_for_payment import ikb_pay

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)

PRICE = types.LabeledPrice(label='Подписка на 1 месяц в копейках - ', amount=500*100)   # в копейках


@dp.message_handler(commands=['buy'])
async def cmd_buy(message: types.Message):
    if PAYMENT_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.from_user.id, text='This is TEST!')
    # send_invoice -
    await bot.send_invoice(title='Подписка на бота!',
                           description='Еже месячная оплата\nВ размере 500 рублей',
                           provider_token=PAYMENT_TOKEN,
                           currency='rub',
                           photo_url='https://avatars.mds.yandex.net/i?id=e665ce9a6cb3c54ba459bcfa9c52366e-3861166-images-thumbs&n=13',
                           photo_size=416,
                           photo_width=416,
                           photo_height=234,
                           is_flexible=False,   # True только когда конечная цена зависит от доставки
                           prices=[PRICE],
                           start_parameter='one-mouth-subscription',
                           payload='test-invoice-payload',
                           chat_id=message.from_user.id)


@dp.pre_checkout_query_handler(lambda query: True)   # Обрабатывается после 1 запроса user`a
async def pre_check(pre_c_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_c_q.id, ok=True)   # Нужно ответить за 10 сек или платёж будет остановлен


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def success_payment(message: types.Message):
    print('SUCCESSFUL PAY:')
    payment_into = message.successful_payment.to_python()
    for f, v in payment_into.items():
        print(f'{f} = {v}')
    await bot.send_message(message.chat.id,
                           f'Платёж на:{message.successful_payment.total_amount // 100} {message.successful_payment.currency} ПРОШОЛ УСПЕШНО, ПРЕДОСТАВЛЕН НОВЫЙ КОНТЕНТ!',
                           reply_markup=ikb_pay)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)   # ЧТО БЫ НЕ ПРОПУСТИТЬ НИ ОДНОГО СООБЩЕНИЯ!!!