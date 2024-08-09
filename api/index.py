from flask import Flask, request
from pyrogram import Client
import asyncio

app = Flask(__name__)

# Initialize the bot client
api_id = "15122558"
api_hash = "43042882a789e5c2e8526d2da740b9c1"
bot_token = "6401987505:AAHe1Tm28KiEa51lM-RBzVtpq4v7DeAe9yI"
bot_client = Client("sesss", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.route('/')
def hello_world():
    return 'king'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    async def process_update(data):
        async with bot_client:
            await bot_client.process_update(data)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(process_update(data))

    return "Webhook received", 200

if __name__ == "__main__":
    app.run()
