from typing import List

from pyrogram.types import Chat

from .. import admins


async def get_administrators(chat: Chat) -> List[int]:
    get = admins.get(chat.id)
    if get:
        return get
    administrators = await chat.get_members(filter='administrators')
    to_set = [
        administrator.user.id
        for administrator in administrators
        if administrator.can_manage_voice_chats
    ]


    admins.set(chat.id, to_set)
    return await get_administrators(chat)
