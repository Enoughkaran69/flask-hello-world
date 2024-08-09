from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'king'
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Process the webhook data here
    return "Webhook received", 200
if __name__ == "__main__":
    app.run()
