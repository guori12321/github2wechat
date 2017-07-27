#!/usr/bin/env python
# coding: utf-8

import socket
from thread import start_new_thread

from server import MyServer
from wxBot.wxbot import *
import server

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            self.send_msg_by_uid(u'hi', msg['user']['id'])
            self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            self.send_file_msg_by_uid("img/1.png", msg['user']['id'])

    def schedule(self):
        self.send_msg(u'tb', u'schedule')
        time.sleep(1)

def main():
    bot = MyWXBot()
    bot.DEBUG = True
    from sys import platform
    # Show the QR code in terminal if Ubuntu
    if platform == 'linux2':
        bot.conf['qr'] = 'tty'
    start_new_thread(bot.run, tuple())

    server.run()


if __name__ == '__main__':
    main()
