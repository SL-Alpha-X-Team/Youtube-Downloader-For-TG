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
    await message.reply_photo(thumbnail_url, caption=f"**🙂 Hi <b>{message.from_user.first_name}**</b>\n\n<br>__😇 I Can Download YT Videos For You ✨️__</br>\n\n<b>• **🗂️ Instructions for use...**</b>\n• **⚙ Type /help to get instructins...**\n \n───── ❝ **Lets Play** ❞ ─────\n ", reply_markup=Alpha)
    raise StopPropagation
