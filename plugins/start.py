from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
import config

@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Alpha = InlineKeyboardMarkup([
        
        [InlineKeyboardButton(config.G1N, url=config.G1L)],
        [InlineKeyboardButton(config.G2N, url=config.G2L)]

    ])
    thumbnail_url = config.SPIC
    await message.reply_photo(thumbnail_url, caption=f"**š Hi <b>{message.from_user.first_name}**</b>\n\n<br>__š I Can Download YT Videos For You āØļø__</br>\n\n<b>ā¢ **šļø Instructions for use...**</b>\nā¢ **ā Type /help to get instructins...**\n \nāāāāā ā **Lets Play** ā āāāāā\n ", reply_markup=Alpha)
    raise StopPropagation
