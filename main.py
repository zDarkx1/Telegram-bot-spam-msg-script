import asyncio
from telegram import Bot
from telegram.error import TelegramError
from getpass import getpass

async def send_message(token, chat_id, message, number_of_messages, delay):
    bot = Bot(token)
    for _ in range(number_of_messages):
        try:
            response = await bot.send_message(chat_id=chat_id, text=message)
            print("Sukses terkirim ✅")
            print("Response:", response)
        except TelegramError as e:
            print(f"Telegram error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        await asyncio.sleep(delay)

async def main():
    # mintak pass
    correct_password = "@P0xaca"  
    password = getpass("Masukkan password: ")
    if password != correct_password:
        print("Password salah!")
        return

    # Input user untuk Token Bot
    token = getpass("Masukkan Token Bot: ")

    # Input user lainnya setelah memasukkan password yang benar
    chat_id = input("Masukkan Chat ID: ")
    message = input("Masukkan pesan yang ingin dikirim: ")
    number_of_messages = int(input("Berapa banyak pesan yang ingin dikirim: "))
    delay = float(input("Masukkan delay antar pesan (detik): "))

    # Mengirim pesan
    await send_message(token, chat_id, message, number_of_messages, delay)

# loop
if __name__ == '__main__':
    asyncio.run(main())
