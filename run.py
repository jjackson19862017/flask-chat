import os
from datetime import datetime
from flask import Flask, redirect, render_template

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """Add messages to the 'messages' list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}
    messages.append(messages_dict)

@app.route('/')
def index():
    """Main page with instructions """
    return render_template("index.html")

@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return "<h1>Welcome, {0}</h1>{1} ".format(username, messages)

@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(os.getenv('IP'), port=os.getenv('PORT'), debug=True)