from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hi kya hal chal hai aapke aasa hai aap thik thak hi honge. Mai hu ❦︎𝗗𝗮𝘆𝗻𝗮𝗺𝗶𝗰 𝖝 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁.\n\n ❗️ Niyam:\n   - Bat chit mat karo plzz\n   - Spam to bilkul nhi \n\n 👉 **Kisi group me agar mai join nhi ho pa rha hu to us grp ka link idhar send kar dena.**\n\n")
  return                        
