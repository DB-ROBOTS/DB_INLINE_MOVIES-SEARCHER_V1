#Kanged From @TroJanZheX
from info import AUTH_CHANNEL, AUTH_USERS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
import re
from pyrogram.errors import UserNotParticipant
from utils import get_filter_results, get_file_details, is_subscribed
BUTTONS = {}

@Client.on_message(filters.text & filters.private & filters.incoming & filters.user(AUTH_USERS) if AUTH_USERS else None)
async def filter(client, message):
    if message.text.startswith("/"):
        return
    if AUTH_CHANNEL:
        invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        try:
            user = await client.get_chat_member(int(AUTH_CHANNEL), message.from_user.id)
            if user.status == "kicked":
                await client.send_message(
                    chat_id=message.from_user.id,
                    text="Sorry Sir, You are Banned to use me.",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await client.send_message(
                chat_id=message.from_user.id,
                text="**Please Join My Updates Channel to use this Bot!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url=invite_link.invite_link)
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await client.send_message(
                chat_id=message.from_user.id,
                text="Something went Wrong.",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 100:    
        btn = []
        search = message.text
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                file_id = file.file_id
                filename = f"💽❰{get_size(file.file_size)}❱➤🎬{file.file_name}"
                btn.append(
                    [InlineKeyboardButton(text=f"{filename}",callback_data=f"subinps#{file_id}")]
                    )
        else:
            await client.send_sticker(chat_id=message.from_user.id, sticker='CAADBQADMwIAAtbcmFelnLaGAZhgBwI')
            return

        if not btn:
            return

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="🎬🆄🅼🆁 🔰 ᴘᴀɢᴇs 1/1 🔰 🆄🅼🆁🎬",callback_data="pages")]
            )
            await message.reply_text(
                f"<b>[𝚄𝚁𝚂 𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙼𝙾𝚅𝙸𝙴 𝙵𝙸𝙻𝙴 𝚁𝙴𝙰𝙳𝚈 𝚃𝙾 𝙶𝙴𝚃 🤹].\n💡ᴛᴏ ᴊᴏɪɴ ᴏᴜʀs ᴀʟʟ ᴄʜᴀɴɴᴇʟs ɢᴏ ᴛʜʀᴏᴜɢʜ..\n☞ ❱❱❱ ❴ @UNI_MOVIES_BOX ❵ \n\n🎬𝐌𝐨𝐯𝐢𝐞 𝐍𝐚𝐦𝐞 ❱»<code>{search}</code>.\n\n🕵️ᴍᴀᴄᴛᴄʜᴇᴅ ᴛᴏ ɢɪᴠᴇ ᴏᴘᴛɪᴏɴs ᴄʟɪᴄᴋ ᴛʜᴛ ʙᴜᴛᴛᴀɴs ᴀɴᴅ ɢᴇᴛ ᴜʀsғɪʟᴇ🔎</b>",

                
                reply_markup=InlineKeyboardMarkup(buttons)
            )
            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="ɢᴏ ɴᴇxᴛ ᴘᴀɢᴇ ❯❯",callback_data=f"next_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"🎬🆄🅼🆁 🔰 ᴘᴀɢᴇs 1/{data['total']} 🔰 🆄🅼🆁🎬",callback_data="pages")]
        )

        await message.reply_text("<b>[𝚄𝚁𝚂 𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙼𝙾𝚅𝙸𝙴 𝙵𝙸𝙻𝙴 𝚁𝙴𝙰𝙳𝚈 𝚃𝙾 𝙶𝙴𝚃 🤹].\n💡ᴛᴏ ᴊᴏɪɴ ᴏᴜʀs ᴀʟʟ ᴄʜᴀɴɴᴇʟs ɢᴏ ᴛʜʀᴏᴜɢʜ..\n☞ ❱❱❱ ❴ @UNI_MOVIES_BOX ❵ \n\n🎬𝐌𝐨𝐯𝐢𝐞 𝐍𝐚𝐦𝐞 ❱»<code>{search}</code>.\n\n🕵️ᴍᴀᴄᴛᴄʜᴇᴅ ᴛᴏ ɢɪᴠᴇ ᴏᴘᴛɪᴏɴs ᴄʟɪᴄᴋ ᴛʜᴛ ʙᴜᴛᴛᴀɴs ᴀɴᴅ ɢᴇᴛ ᴜʀsғɪʟᴇ🔎</b>",
                reply_markup=InlineKeyboardMarkup(buttons)
            )    

@Client.on_message(filters.group & filters.text & filters.incoming)
async def group(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 50:    
        btn = []
        search = message.text
        botusername=await client.get_me()
        nyva=botusername.username
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                file_id = file.file_id
                filename = f"[{get_size(file.file_size)}] {file.file_name}"
                btn.append(
                    [InlineKeyboardButton(text=f"{filename}", url=f"https://telegram.dog/{nyva}?start=subinps_-_-_-_{file_id}")]
                )
        else:
            return
        if not btn:
            return

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="🎬🆄🅼🆁 🔰 ᴘᴀɢᴇs 1/1 🔰 🆄🅼🆁🎬",callback_data="pages")]
            )
            await message.reply_text(
                f"<b>[𝚄𝚁𝚂 𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙼𝙾𝚅𝙸𝙴 𝙵𝙸𝙻𝙴 𝚁𝙴𝙰𝙳𝚈 𝚃𝙾 𝙶𝙴𝚃 🤹].\n💡ᴛᴏ ᴊᴏɪɴ ᴏᴜʀs ᴀʟʟ ᴄʜᴀɴɴᴇʟs ɢᴏ ᴛʜʀᴏᴜɢʜ..\n☞ ❱❱❱ ❴ @UNI_MOVIES_BOX ❵ \n\n🎬𝐌𝐨𝐯𝐢𝐞 𝐍𝐚𝐦𝐞 ❱»<code>{search}</code>.\n\n🕵️ᴍᴀᴄᴛᴄʜᴇᴅ ᴛᴏ ɢɪᴠᴇ ᴏᴘᴛɪᴏɴs ᴄʟɪᴄᴋ ᴛʜᴛ ʙᴜᴛᴛᴀɴs ᴀɴᴅ ɢᴇᴛ ᴜʀsғɪʟᴇ🔎</b>",

                
                reply_markup=InlineKeyboardMarkup(buttons)
            )
            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="ɢᴏ ɴᴇxᴛ ᴘᴀɢᴇ ❯❯",callback_data=f"next_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"🎬🆄🅼🆁 🔰 ᴘᴀɢᴇs 1/{data['total']} 🔰 🆄🅼🆁🎬",callback_data="pages")]
        )

        await message.reply_text(
                f"<b>[𝚄𝚁𝚂 𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙼𝙾𝚅𝙸𝙴 𝙵𝙸𝙻𝙴 𝚃𝙾 𝙶𝙴𝚃 🤹].\n💡ᴛᴏ ᴊᴏɪɴ ᴏᴜʀs ᴀʟʟ ᴄʜᴀɴɴᴇʟs ɢᴏ ᴛʜʀᴏᴜɢʜ..\n☞ ❱❱❱ ❴ @UNI_MOVIES_BOX ❵ \n\n🎬𝐌𝐨𝐯𝐢𝐞 𝐍𝐚𝐦𝐞 ❱»<code>{search}</code>.\n\n🕵️ᴍᴀᴄᴛᴄʜᴇᴅ ᴛᴏ ɢɪᴠᴇ ᴏᴘᴛɪᴏɴs ᴄʟɪᴄᴋ ᴛʜᴛ ʙᴜᴛᴛᴀɴs ᴀɴᴅ ɢᴇᴛ ᴜʀsғɪʟᴇ🔎</b>",
                reply_markup=InlineKeyboardMarkup(buttons)
            )

    
def get_size(size):
    """Get size in readable format"""

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]          






@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    clicked = query.from_user.id
    try:
        typed = query.message.reply_to_message.from_user.id
    except:
        typed = query.from_user.id
        pass
    if (clicked == typed):

        if query.data.startswith("next"):
            await query.answer()
            ident, index, keyword = query.data.split("_")
            data = BUTTONS[keyword]

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("❮❮ ɢᴏ back ᴘᴀɢᴇ", callback_data=f"back_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎬🆄🅼🆁 🔰 ᴘᴀɢᴇs {int(index)+2}/{data['total']} 🔰 🆄🅼🆁🎬", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("❮❮ ɢᴏ back ᴘᴀɢᴇ", callback_data=f"back_{int(index)+1}_{keyword}"),InlineKeyboardButton("ɢᴏ ɴᴇxᴛ ᴘᴀɢᴇ ❯❯", callback_data=f"next_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎬🆄🅼🆁 🔰 ᴘᴀɢᴇs {int(index)+2}/{data['total']} 🔰 🆄🅼🆁🎬", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return


        elif query.data.startswith("back"):
            await query.answer()
            ident, index, keyword = query.data.split("_")
            data = BUTTONS[keyword] 

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("ɢᴏ ɴᴇxᴛ ᴘᴀɢᴇ ❯❯", callback_data=f"next_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎬🆄🅼🆁 🔰 ᴘᴀɢᴇs {int(index)}/{data['total']} 🔰 🆄🅼🆁🎬", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("❮❮ ɢᴏ back ᴘᴀɢᴇ", callback_data=f"back_{int(index)-1}_{keyword}"),InlineKeyboardButton("ɢᴏ ɴᴇxᴛ ᴘᴀɢᴇ ❯❯", callback_data=f"next_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"🎬🆄🅼🆁 🔰 ᴘᴀɢᴇs {int(index)}/{data['total']} 🔰 🆄🅼🆁🎬", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
        elif query.data == "about":
            buttons = [
                [ InlineKeyboardButton('🔎Sᴇᴀʀᴄʜ Mᴏᴠɪᴇs..', switch_inline_query_current_chat=query)],
                 [   InlineKeyboardButton('𝙱𝙾𝚃𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url='https://t.me/db_robots'),
                    InlineKeyboardButton('𝙱𝙾𝚃𝚂 𝙶𝚁𝙾𝚄𝙿', url='https://t.me/db_helper')
                ],[InlineKeyboardButton('💡JOIN OUR ALL CHANNELs💡', url='https://t.me/uni_movies_box')]
                ]
            await query.message.edit(text="<b>Dev</b>", reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)



        elif query.data.startswith("subinps"):
            ident, file_id = query.data.split("#")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                file_caption = files.file_name
                size=files.file_size
                caption = files.caption
                buttons = [
                    [
                        InlineKeyboardButton('🔎Sᴇᴀʀᴄʜ Mᴏᴠɪᴇs..', switch_inline_query_current_chat=query)],
                    [    InlineKeyboardButton('🃏𝙱𝙾𝚃𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻🃏', url='https://t.me/DB_ROBOTS'),
                        InlineKeyboardButton('🎲𝙱𝙾𝚃𝚂 𝙶𝚁𝙾𝚄𝙿🎲', url='https://t.me/DB_HELPER')
                    ],[InlineKeyboardButton('💡JOIN OUR ALL CHANNELs💡', url='https://t.me/uni_movies_box')]
                    ]
                
                await query.answer()
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )
        elif query.data.startswith("checksub"):
            if AUTH_CHANNEL and not await is_subscribed(client, query):
                await query.answer("I Like Your Smartness, But Don't Be Oversmart 😒",show_alert=True)
                return
            ident, file_id = query.data.split("#")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                file_caption = files.file_name
                size=files.file_size
                caption = files.caption
                buttons = [
                    [ InlineKeyboardButton('🔎Sᴇᴀʀᴄʜ Mᴏᴠɪᴇs..', switch_inline_query_current_chat=query)],
                    [    InlineKeyboardButton('🃏𝙱𝙾𝚃𝚜 𝙲𝙷𝙰𝙽𝙽𝙴𝙻🃏', url='https://t.me/db_robots'),
                        InlineKeyboardButton('🎲𝙱𝙾𝚃𝚜 𝙶𝚁𝙾𝚄𝙿🎲', url='https://t.me/db_helper')
                    ],[  InlineKeyboardButton('📑𝐉𝐎𝐈𝐍 𝐎𝐔𝐑 𝐀𝐋𝐋 𝐂𝐇𝐀𝐍𝐍𝐄𝐋𝐒📑', url='https://t.me/uni_movies_box')]
                    ]
                
                await query.answer()
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )


        elif query.data == "pages":
            await query.answer()
    else:
        await query.answer("🤔𝙏𝙃𝙄𝙎 𝙄𝙎 𝙉𝙊𝙏 𝙁𝙊𝙍 𝙐 𝙈𝘼𝙉,𝙇𝙊𝙇🤩",show_alert=True)
