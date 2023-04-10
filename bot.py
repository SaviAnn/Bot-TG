import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

logging.basicConfig(level=logging.INFO)
#TOKEN=os.getenv('TOKEN')
bot=Bot(token=TOKEN)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name=message.from_user.first_name
    user_id=message.from_user.id
    text=f"Hello, {user_name}!"
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await message.reply(text)


@dp.message_handler()
async def send_translit(message: types.Message):
    user_name=message.from_user.first_name
    
    user_id=message.from_user.id
    text=(message.text).lower()
    rus=["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о",
            "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я", " ", "-"]
    eng=["a","b","v","g","d","e","e","zh","z","i","i","k","l","m","n","o",
            "p","r","s","t","u","f","kh","ts","ch","sh","shch","y","ie","","e","iu","ia", " ", "-"]
    rus_eng=dict(zip(rus,eng))
    trans=[]
    for i in text:
        trans.append(rus_eng.get(i))
    trans=str(''.join(trans)).title()
    logging.info(f"{user_name=} {user_id=} sent message: {text}")
    await bot.send_message(user_id,trans)

if __name__=='__main__':
    executor.start_polling(dp)