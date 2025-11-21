import asyncio
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import re

API_ID = 26652570         # change
API_HASH = "1dcbd158e145479b1599a49259ab84b3" # change
MASTER_GROUP_LINK = "https://t.me/zhueheu"  # change

app = Client("forwarder", api_id=API_ID, api_hash=API_HASH)

# Convert group link → username
def extract_username(link):
    return link.replace("https://t.me/", "").replace("joinchat/", "").strip()

async def join_groups():
    print("Joining target groups...")
    with open("groups.txt", "r") as f:
        links = f.read().splitlines()

    for link in links:
        if not link.strip():
            continue

        username = extract_username(link)

        try:
            await app.join_chat(username)
            print(f"Joined: {username}")
        except UserAlreadyParticipant:
            print(f"Already in: {username}")
        except Exception as e:
            print(f"Failed to join {username} → {e}")


@app.on_message(filters.chat(MASTER_GROUP_LINK))
async def forward(client, message):
    print("New message in master group. Forwarding...")

    with open("groups.txt", "r") as f:
        links = f.read().splitlines()

    for link in links:
        username = extract_username(link)
        try:
            await message.copy(username)
            print(f"Sent to {username}")
        except Exception as e:
            print(f"Failed to send to {username} → {e}")


async def main():
    await join_groups()
    print("Bot running...")
    await app.start()
    await idle()
    await app.stop()

if __name__ == "__main__":
    app.run()
