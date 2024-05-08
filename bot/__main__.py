import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# from bot.config_reader import config
from bot.handlers import commands, callbacks
from bot.middlewares import DbSessionMiddleware
from bot.ui_commands import set_ui_commands


async def main():
    # engine = create_async_engine(url=config.db_url, echo=True)
    engine = create_async_engine(url="postgresql+psycopg://postgres:12345@localhost/worker_monitoring_bot", echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    # bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")
    bot = Bot("6809228592:AAGpfLTxGYV22gmd0-GBtlLMQoAytO5RdNs", parse_mode="HTML")

    # Setup dispatcher and bind routers to it
    dp = Dispatcher()
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))
    # Automatically reply to all callbacks
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    # Register handlers
    dp.include_router(commands.router)
    dp.include_router(callbacks.router)

    # Set bot commands in UI
    await set_ui_commands(bot)

    # Run bot
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
