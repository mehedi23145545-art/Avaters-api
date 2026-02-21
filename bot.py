from flask import Flask, send_from_directory, request, jsonify
import os
import random

app = Flask(__name__)

AVATAR_FOLDER = "avatars"

@app.route("/avatar")
def get_avatar():
    uid = request.args.get("uid")

    if not uid:
        return jsonify({"error": "UID required"}), 400

    files = os.listdir(AVATAR_FOLDER)
    image = random.choice(files)

    return send_from_directory(AVATAR_FOLDER, image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)