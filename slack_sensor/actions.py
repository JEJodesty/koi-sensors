from rid_lib.types import SlackMessage
from slack_sdk.errors import SlackApiError
from .core import slack_app


async def dereference(message: SlackMessage):
    try:
        response = await slack_app.client.conversations_replies(
            channel=message.channel_id,
            ts=message.ts
        )
        return response["messages"][0]
    except SlackApiError:
        return None