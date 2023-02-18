# QCalc_bot

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Helloooooo {update.effective_user.first_name}')


app = ApplicationBuilder().token("6250061300:AAFDRLTXQum_wrrgRV_QkdLRHgxzTR8xTxk").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()