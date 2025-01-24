from aiogram import F
from aiogram.types import Message
from loader import router

@router.message(F.text == 'Lets go gambling!')
async def fun_text(message: Message):
    dice_mess = await message.answer_dice(emoji='🎰')
    value_dice = dice_mess.dice.value
    if value_dice < 32:
        await message.answer(text="You lose!")
    else:
        await message.answer(text=f'You won {value_dice}$')