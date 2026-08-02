import asyncio
from swarm import Swarm

async def main():
    swarm = Swarm("bots.json")
    await swarm.deploy()

    await swarm.raid("t.me/target_chat", ["FUCK YOU!", "SUCK MY DICK!", "RIP YOUR FAMILY"], repeats=100)

    await swarm.mass_join(["t.me/chat1", "t.me/chat2", "t.me/chat3"])

if __name__ == "__main__":
    asyncio.run(main())
