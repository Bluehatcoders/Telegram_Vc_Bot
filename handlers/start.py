from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME


@Client.on_message(filters.command(["start", "start@dynamicxmusicbot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hei 👋🏻 {}!**\n\nDekh bhai **mai koi devta nhi hu mai bas VC me songs bja sakta hu** Ha lekin kuch features hai **jisse mai aapko Amaze kar sakta hu hue hue!**\n\n**Click /cmdlist For More Help or contact @iamsatyanchal / @SHubHam_XD*".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Add To Your Group ➕", url="https://t.me/dynamicxmusicbot?startgroup=true")
            ],[
            InlineKeyboardButton("💬 Group", url="https://t.me/@PROLABS_127_0_0_1"),
            InlineKeyboardButton("🤖 Contact Owner", url="https://t.me/@PROLABS_127_0_0_1")
            ],[
            InlineKeyboardButton("🙁 Found error", url="https://t.me/@PROLABS_127_0_0_1")
            ]]
        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@dynamicxmusicbot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**Mai jinda hu itni jaldi thori marunga :(**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="🎙️ Owner Group 🎙️", url="https://t.me/@PROLABS_127_0_0_1")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@dynamicxmusicbot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**❦︎𝗗𝗮𝘆𝗻𝗮𝗺𝗶𝗰  𝖝 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁: Aapki seva me**

__× Sabse pahle mujhe apne group me add karo..
× Uske bad mujhe admin bna de with all permissions..__

** ⚙ Commands**

• `/play` - Song Name : __Plays Via Youtube__
• `/dplay` - Song Name : __Play Via Deezer__
• `/splay` - Song Name : __Play Via Jio Saavn__
• `/playlist` - __Show now playing list__
• `/current` - __Show now playing__

• `/song` - Song Name : __Get The Song From YouTube__
• `/vid` - Video Name : __Get The Video From YouTube__
• `/deezer` - song name : __download songs you want quickly via deezer__
• `/saavn` - song name : __download songs you want quickly via saavn__
• `/search` - YouTube Title : __(Get YouTube Search Query)__

** Commands for group Admins**

• `/skip` : __Skips Music__
• `/pause` : __Pause Playing Music__
• `/resume` : __Resume Playing Music__
• `/end` : __Stops playing Music__
• `/reload` : __Reloads Admin List__
• `/userbotjoin` : __Assistant Joins The Group__
• `/userbotleave` : __Assistant Leaves From The Group.__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/@PROLABS_127_0_0_1")
              ]]
          )
      )
