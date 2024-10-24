# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-10-22 10:27:20
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-10-23 18:14:11
# @github: https://github.com/longfengpili

import json

from .brequests import BRequests
from utils.model import Message, OneOf


class PushPlus(BRequests):
    channel = OneOf('wechat', 'webhook', 'cp', 'mail', 'sms')

    def __init__(self, token: str, channel: str = 'wechat'):
        self.token = token
        self.channel = channel
        self.url = "https://www.pushplus.plus/send"

    def send(self, message: Message):
        method = 'post'
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'token': self.token,
            'title': message.title,
            'content': message.content,
            'template': message.template,
            'channel': self.channel
        }

        result = self.request_api(method, self.url, headers=headers, data=json.dumps(data))
        return result
