from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"message": "Hello from Vercel!"}

# Vercel requires the app to be callable from the main module
def handler(event, context):
    return app(event, context)
