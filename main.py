import controller
from telegram.ext import CallbackQueryHandler, filters, MessageHandler, ApplicationBuilder, CommandHandler
from QCalc_bot import *


def main():
    controller.run_app()


if __name__ == "__main__":
    # main()

    application = ApplicationBuilder().token("6250061300:AAFDRLTXQum_wrrgRV_QkdLRHgxzTR8xTxk").build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calc))
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    application.run_polling()