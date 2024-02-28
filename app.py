from flask import abort, Flask, request
import requests

from constant import CHATGPT_SYSTEM_QUERY, CHATGPT_USER_QUERY


app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return {
        "message": "hello, world!"
    }


@app.route("/chatgpt", methods=["GET"])
def call_chatgpt():
    theme = request.args.get("theme")

    if not theme:
        abort(400)

    response = requests.post(
        url="https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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"
        },
        json={
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": CHATGPT_SYSTEM_QUERY,
                },
                {
                    "role": "user",
                    "content": CHATGPT_USER_QUERY.format(theme=theme)
                },
            ]
        }
    )

    # response.raise_for_status()

    return response.json()

@app.route("/kakaomap", methods=["GET"])
def call_kakaomap():
    return {
        "message": "kakaomap"
    }


if __name__ == "__main__":
    app.run()