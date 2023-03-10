from aiogram import executor

from loader import dp, db

from utils.notify_admins import on_startup_notify



async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await on_startup_notify(dispatcher)
    try:
        await db.create_table_users()
    # Уведомляет про запуск
    except Exception as err:
        print(err)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

