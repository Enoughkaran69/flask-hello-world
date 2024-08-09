from flask import Flask, request
from pyrogram import Client
from concurrent.futures import ThreadPoolExecutor
import asyncio
import os
from pydantic import BaseModel


app = Flask(__name__)

# Initialize the bot client
api_id = "15122558"
api_hash = "43042882a789e5c2e8526d2da740b9c1"
bot_token = "6401987505:AAHe1Tm28KiEa51lM-RBzVtpq4v7DeAe9yI"
bot_client = Client("sesss", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.text)
async def echo(client, message):
    """Reply to text messages"""
    await message.reply_text(f"You said: {message.text}")
# Function to send a message on bot startup
async def send_startup_message():
    async with app:
        await app.send_message(chat_id=chat_id, text="Bot has started successfully!")

   
@app.get("/")
def index():
    return {"message": "Hello World"}


if __name__ == "__main__":
    app.run()
