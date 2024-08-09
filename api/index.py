from pyrogram import Client, filters
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

# Replace with your own API ID, API hash, and bot token
api_id = "15122558"
api_hash = "43042882a789e5c2e8526d2da740b9c1"
bot_token = "6401987505:AAHe1Tm28KiEa51lM-RBzVtpq4v7DeAe9yI"

bot = Client("sesss", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

class TelegramWebhook(BaseModel):
    update_id: int
    message: dict
@app.on_event("startup")
async def startup():
    await bot.start()

@app.on_event("shutdown")
async def shutdown():
    await bot.stop()
@app.post("/webhook")
async def webhook(webhook_data: TelegramWebhook):
    update = webhook_data.message
    if update.get("text") == "/start":
        await bot.send_message(chat_id=update["chat"]["id"], text="I'm a bot, please talk to me!")
    elif update.get("text"):
        await bot.send_message(chat_id=update["chat"]["id"], text="You sent a message!")
    elif update.get("video"):
        await bot.send_message(chat_id=update["chat"]["id"], text="You sent a video!")

@app.get("/")
def index():
    return {"message": "Hello World"}
