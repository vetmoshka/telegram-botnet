import asyncio
from client import BotClient
import json

class Swarm:
    def __init__(self, config_path="bots.json"):
        with open(config_path, 'r') as f:
            self.bots = json.load(f)
        self.clients = []

    async def deploy(self):
        for bot in self.bots:
            client = BotClient(bot['api_id'], bot['api_hash'], bot['session'], bot.get('proxy'))
            self.clients.append(await client.start())

    async def raid(self, chat_link, message_list, repeats=5):
        for _ in range(repeats):
            tasks = []
            for client in self.clients:
                tasks.append(client.send_message(chat_link, random.choice(message_list)))
            await asyncio.gather(*tasks)
            await asyncio.sleep(10)

    async def mass_join(self, links):
        tasks = []
        for link in links:
            for client in self.clients:
                tasks.append(client.join_chat(link))
        await asyncio.gather(*tasks)

    async def scan_and_report(self, target_chat):
        for client in self.clients:
            chats = await client.get_chats()
            print(f"{client.client.session.filename} сидит в: {chats}")
