from flask import Flask, request
import hashlib

app = Flask(__name__)

# Store the mapping from hash to original message
message_map = {}


@app.route('/helloWorld')
def intro():
    return "Ahmet Burak"


@app.route('/messages', methods=['POST'])
def post_message():
    # Read the message from the POST request
    message = request.form['message']

    # Compute the SHA256 hash of the message
    message_hash = hashlib.sha256(message.encode()).hexdigest()

    # Store the original message with its hash in the message_map dictionary
    message_map[message_hash] = message

    # Return the hash of the message
    return message_hash


@app.route('/messages/<hash>', methods=['GET'])
def get_message(hash):
    # Look up the original message for the given hash
    if hash in message_map:
        return message_map[hash]
    else:
        # Return a 404 error if the hash is not found
        return "Error: Message not found", 404


if __name__ == '__main__':
    app.run()
