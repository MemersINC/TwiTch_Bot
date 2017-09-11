import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")))

from twitch_bot.twitch import TChannel
import re



def on_message(obj, message):
    print(message)


def main():
    channel = TChannel(on_message, channel=["shroud", "summit1g"])
    channel.join()


if __name__ == "__main__":
    main()