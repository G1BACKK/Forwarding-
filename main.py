from pyrogram import Client, filters
import asyncio

API_ID = 26652570
API_HASH = "1dcbd158e145479b1599a49259ab84b3"
STRING_SESSION = "BQFitqsAmpZV9EDZaF6gV3G-TAQjRVHJ0wcfuJG4swz3tQlX2CtRjJnbsUK0ym0z-Zi4eaY-2xoh_Kg2hFkl05GQ8s4QU4TKPEsO96wCaUUCn_1Bn-0ONPp8Xb_I67kathAeCh5skmAATcMv3Ya0SHFVD0O5AuBS9jCQSMjAknF-H3ai5DnxSUhpNnIvLalf_JpWVIm-PGyP7nKwrx39KjeNjiCRZtbiwRRZ0J4eV2hfg_zaUP8Ge289q-yeeBGyC1vtFEWw1gEiMVlJsIv30vr3SnsN0oywtU1qSsxPSFH_bKm_Ee3L5qAadv9ohqWn7vhlBtszUKuPlvf1HtxlY8lls8oLDwAAAAHkJjblAA"

MASTER_LINK = "https://t.me/hdjsjenejen"   # Your main group
TARGET_LINKS = [
    "https://t.me/GODlevelMAX4444x",
    "https://t.me/PIZOX_TEAM",
    "https://t.me/TASHANWINEARNINGS",
    "https://t.me/udsidhubb",
    "https://t.me/JALWA_GAME_PREDICTION_GROUP_VIP",
    # add all your links here...
]

app = Client("user", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)

MASTER_ID = None
TARGET_IDS = []


async def convert_links_to_ids():
    global MASTER_ID, TARGET_IDS

    # Convert master group link → chat ID
    try:
        chat = await app.get_chat(MASTER_LINK)
        MASTER_ID = chat.id
        print(f"MASTER ID = {MASTER_ID}")
    except Exception as e:
        print(f"Master group error: {e}")

    # Convert all target links → chat IDs
    for link in TARGET_LINKS:
        try:
            chat = await app.get_chat(link)
            TARGET_IDS.append(chat.id)
            print(f"{link} → {chat.id}")
        except Exception as e:
            print(f"Error for {link}: {e}")

    print("All group IDs loaded!")


@app.on_message(filters.chat(lambda: MASTER_ID))
async def forwarder(client, message):
    for group_id in TARGET_IDS:
        try:
            if message.text:
                await client.send_message(group_id, message.text)
            elif message.photo:
                await client.send_photo(group_id, message.photo.file_id, caption=message.caption)
            elif message.video:
                await client.send_video(group_id, message.video.file_id, caption=message.caption)
        except Exception as e:
            print(f"Error sending to {group_id}: {e}")


async def main():
    await convert_links_to_ids()
    print("Forwarder bot started!")


app.start()
asyncio.get_event_loop().run_until_complete(main())
app.run()
