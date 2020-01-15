import os
from flask import Flask

app = Flask(__name__)
messages = []

def add_messages(username, message):
    messages.append("{}: {}".format(username, message))
    print(messages)

@app.route('/')
def index():
    """Main page with instructions """
    return "To send a message use /USERNAME/MESSAGE"

@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return "Welcome, {0} ".format(username, messages)

@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    return "{0}: {1}".format(username, message)


app.run(os.getenv('IP'), port=os.getenv('PORT'), debug=True)