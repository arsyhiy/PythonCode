import asyncio
import telegram


async def main():
    bot = telegram.Bot("7551740409:AAHAFH_unaEd1HZHKygeBpUlh_ychnJDxHI")
    async with bot:
        await bot.send_message(text="hi arsen!", chat_id=893877652)


if __name__ == "__main__":
    asyncio.run(main())
