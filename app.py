from lib2to3.pgen2 import token
import os
from webbrowser import get

from slack_bolt import App


app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)



if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
