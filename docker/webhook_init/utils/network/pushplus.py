# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-10-22 10:27:20
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-10-22 14:13:06
# @github: https://github.com/longfengpili

from .brequests import BRequests
from utils.model import Message

# import logging
# pplogger = logging.getLogger(__name__)


class PushPlus(BRequests):

    def __init__(self, token: str):
        self.token = token
        self.url = 'https://www.pushplus.plus/send'
        super(PushPlus, self).__init__()

    def send(self, message: Message):
        method = 'post'
        print(f"==={method}")
        data = {
            'token': self.token,
            'title': message.title,
            'content': message.content,
            'template': message.template,
            'channel': message.channel
        }

        result = self.request_api(method, self.url, data=data)
        return result
