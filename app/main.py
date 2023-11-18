from .media import get_media_info
from .config import DISCORD_ID, ALLOW_EXTERNAL_APPS
from pypresence import AioPresence
import asyncio

discord_rpc = AioPresence(client_id=DISCORD_ID)

async def amain():
    await discord_rpc.connect()

    while True:
        await asyncio.sleep(2)

        info = await get_media_info()

        if not info:
            await discord_rpc.clear()
            continue

        is_yandex = info["app"] == "Yandex.Music"
        await discord_rpc.update(
            state=info["app"] if ALLOW_EXTERNAL_APPS else None,
            details=f"{info['artist']} - {info['title']}",
            large_text=f"{info['artist']} - {info['title']}",
            large_image="https://github.com/maj0roff/YandexMusicDiscordRPC/raw/main/fallback-black_2.gif",
            small_image="https://github.com/maj0roff/YandexMusicDiscordRPC/blob/main/logo.png?raw=true" if is_yandex else None,
        )
