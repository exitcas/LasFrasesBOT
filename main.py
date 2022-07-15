import os, frases
from markupsafe import escape
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
print("Funcionando")


async def frase(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  x = frases.frase()
  if x["autor"] == False:
    x["autor"] = "Anónimo"
  await update.message.reply_html(f'<b>"{escape(x["frase"])}"</b>\n--{escape(x["autor"])}')


app = ApplicationBuilder().token(os.getenv("token")).build()
app.add_handler(CommandHandler("frase", frase))
app.run_polling()
