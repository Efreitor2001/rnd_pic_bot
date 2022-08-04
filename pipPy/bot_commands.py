import random
from dogs import doggie
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *
from random import randint


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    await update.message.reply_text(
        f'/hi - приветствие бота\n/time - текущее время\n/sum - сумма двух чисел (/sum число_1 число_2)\n'
        f'/fox - случайная картинка с лисичкой\n/cat - случайная картинка с котиком\n'
        f'/dog - случайная картинка с пёсиком\n/help - вызов подсказки')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    await update.message.reply_text(
        f'{datetime.datetime.now().time().hour}:{datetime.datetime.now().time().minute}:'
        f'{datetime.datetime.now().time().second}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    msg = update.message.text
    items = msg.split()  # / sum 123 5431
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')


async def fox_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    r = random.randint(1, 123)
    await update.message.reply_photo(f'https://randomfox.ca/images/{r}.jpg')


async def cat_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    r1 = random.randint(1, 1000)
    await update.message.reply_photo(f'https://aws.random.cat/view/{r1}')


async def dog_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await log(update, context)
    await update.message.reply_photo(f'{doggie()}')
