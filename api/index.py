from flask import Flask
from app import bot



@app.route('/')
def hello_world():
    return 'king'


if __name__ == "__main__":
    bot.run()
