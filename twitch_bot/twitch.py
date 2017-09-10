import socket
import threading
from random import randint
import json


class TChannel(threading.Thread):
    def __init__(self, callback, channel=[], length=50):
        super(TChannel, self).__init__()
        self.host = "irc.chat.twitch.tv"
        self.port = 6667
        self.buffer = MessageBuffer(length)
        self.nick = "justinfan" + "".join("%s" % randint(0, 9) for i in range(0, 10))
        self.PASS = "doesnotmatter"
        self.channel = channel[:20]
        self.callback = callback
        self.start()

    def run(self):
        s = socket.socket()
        s.connect((self.host, self.port))
        s.send(("PASS %s\r\n" % self.PASS).encode())
        s.send(("NICK %s\r\n" % self.nick).encode())
        self.join_channel(s)

    def join_channel(self, s):
        for i in self.channel:
            s.send(("JOIN #%s\r\n" % i).encode())
        self.populate_buffer(s)

    def populate_buffer(self, s):
        while True:
            message = s.recv(1024)
            self.on_message(message)

    def on_message(self, message):
        self.callback(self, message)


class MessageBuffer(object):
    def __init__(self, size):
        self.buffer_content = []
        self.size = size

    def push(self, message):
        if len(self.buffer_content) >= self.size:
            self.buffer_content.pop(0)
            self.buffer_content.append(message)
        else:
            self.buffer_content.append(message)

    def __str__(self):
        return json.dumps({"buffer": self.buffer_content})
