from twitch_bot.twitch import TChannel
import re


def on_message(message):
    pass


def main():
    channel = TChannel(on_message, channel=["shroud", "summit1g"])
    channel.join()


if __name__ == "__main__":
    main()