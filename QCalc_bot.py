# QCalc_bot
import model
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Вычислить выражение", callback_data="1")],
        [
            InlineKeyboardButton("Просмотр лога", callback_data="2"),
            InlineKeyboardButton("Выход", callback_data="3"),
        ],
    ]
    await update.message.reply_text("Калькулятор:", reply_markup=InlineKeyboardMarkup(keyboard))


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "1":
        await query.message.edit_text("Введите выражение:")   
    elif query.data == "2":
        await query.message.edit_text(model.get_log())
    elif query.data == "3":
        await query.message.edit_text("До новой встречи!")
       

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text
    result = model.calculator(user_input)
    if result:
        await update.message.reply_text(result)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Используйте /start, чтобы протестировать этого бота.")


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Неизвестная команда")