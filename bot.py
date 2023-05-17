
import os
import logging

import aioredis
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

redis = aioredis.from_url("redis://localhost")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"User {update.effective_user.first_name} - Chat ID {update.effective_chat.id}")
    await redis.lpush("chats", update.effective_chat.id)
    await update.message.reply_text(f"Hello, {update.effective_user.first_name}")


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
