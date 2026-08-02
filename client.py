from telethon import TelegramClient, events
import asyncio
import random

class BotClient:
    def __init__(self, api_id, api_hash, session_name, proxy=None):
        self.client = TelegramClient(session_name, api_id, api_hash, proxy=proxy)
        self.api_id = api_id
        self.api_hash = api_hash

    async def start(self):
        await self.client.start()
        return self.client

    async def send_message(self, chat_id, message):
        try:
            await self.client.send_message(chat_id, message)
        except Exception as e:
            print(f"Error: {e}")

    async def join_chat(self, link):
        try:
            await self.client.join_channel(link)
        except Exception as e:
            print(f"Didn't join: {e}")

    async def flood(self, chat_id, messages, delay=2):
        for msg in messages:
            await self.send_message(chat_id, msg)
            await asyncio.sleep(delay)

    async def get_chats(self):
        dialogs = await self.client.get_dialogs()
        return [dialog.entity.username for dialog in dialogs if dialog.is_channel or dialog.is_group]
