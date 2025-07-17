# slack_listener.py
from flask import Flask, request, Response
import os, json
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier
from dotenv import load_dotenv

from agents.document_parser import run_document_parser
from agents.market_researcher import run_market_research
from agents.content_writer import run_content_writer
from agents.validator import validate_article

load_dotenv()
app = Flask(__name__)

slack_token = os.getenv("SLACK_BOT_TOKEN")
signing_secret = os.getenv("SLACK_SIGNING_SECRET")
client = WebClient(token=slack_token)
verifier = SignatureVerifier(signing_secret)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    if not verifier.is_valid_request(request.get_data(), request.headers):
        return Response("Invalid signature", status=403)

    payload = json.loads(request.data)
    if "event" in payload:
        event = payload["event"]

        if event.get("type") == "app_mention":
            text = event.get("text", "")
            channel = event.get("channel")
            thread_ts = event.get("ts")

            if "analyze:" in text:
                topic = text.split("analyze:")[1].strip()
                respond_to_topic(topic, channel, thread_ts)
            else:
                client.chat_postMessage(channel=channel, thread_ts=thread_ts,
                                        text="🧠 Please use `analyze: <topic>` to trigger analysis.")

    return Response(status=200)

def respond_to_topic(topic, channel, thread_ts):
    client.chat_postMessage(channel=channel, thread_ts=thread_ts, text=f"🔍 Analyzing topic: *{topic}*...")

    research = run_market_research(topic)
    summary = run_document_parser(research)
    article = run_content_writer(summary, research)
    is_valid, feedback = validate_article(article)

    reply = f"""*Summary:*\n{summary}\n\n*Article:*\n{article}\n\n*Validation:* {feedback}"""
    client.chat_postMessage(channel=channel, thread_ts=thread_ts, text=reply)

if __name__ == "__main__":
    app.run(port=5000)
