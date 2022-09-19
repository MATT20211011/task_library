from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class Slack:
    def __init__(self, channel: str, token: str) -> None:
        self.channel = channel
        self._slack = WebClient(token=token)

    def send(self, title: str, message: str):
        attachments = [
            {
                'title': '{}'.format(title),
                'color': '0000FF',
                'fields': [
                    {'title': 'MESSAGE', 'value': message},
                ],
                'fallback': 'Contact our data team'
            }
        ]

        try:
            # https://api.slack.com/methods/chat.postMessage/code 참고
            self._slack.chat_postMessage(channel=self.channel, attachments=attachments)
        except SlackApiError as e:
            print('Error: {}'.format(e.response['error']))