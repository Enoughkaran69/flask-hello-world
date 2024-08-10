import requests
import logging
from pyrogram import Client, filters
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Enable logging
logging.basicConfig(level=logging.ERROR)

# Replace with your own API ID, API hash, and bot token
api_id = "15122558"
api_hash = "43042882a789e5c2e8526d2da740b9c1"
bot_token = "6401987505:AAHe1Tm28KiEa51lM-RBzVtpq4v7DeAe9yI"

app = Client("sesss", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Google Drive API credentials
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'path/to/service_account_key.json'

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, SCOPES)
drive_service = build('drive', 'v3', credentials=creds)

@app.on_message(filters.text)
async def echo(client, message):
    """Reply to text messages"""
    await message.reply_text(f"You said: {message.text}")

@app.on_message(filters.video)
async def video_size(client, message):
    """Reply with video size"""
    
    try:
        video = message.video
        file_id = video.file_id
        
        size_in_mb = video.file_size / (1024 * 1024)  # Convert size to MB
        await message.reply_text(f"The size of the video is {size_in_mb:.2f} MB")
        
        
        
        # Download the video from Telegram
        video_file = await client.download_media(message)

        with open(video_file, 'rb') as f:
            # Upload the video to GoFile API
             # Upload the video to Google Drive
        file_metadata = {'name': video.file_name}
        media = MediaFileUpload(f, mimetype='video/mp4')
        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        file_id = file.get('id')
        
        # Get the file link
        file_link = f"https://drive.google.com/uc?id={file_id}"
        await message.reply_text(f"Uploaded to Google Drive: {file_link}")

        

    except Exception as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    print("Bot is starting...")
    app.run()

