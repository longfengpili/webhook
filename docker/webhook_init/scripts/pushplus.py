#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-10-21 19:03:55
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-10-22 14:19:49
# @github: https://github.com/longfengpili

import os

from utils.model import Message
from utils.network import PushPlus

token = os.getenv('PUSHPLUS_TOKEN')

message = Message(title='test1', content='content', channel='wechat', template='txt')
pushplus = PushPlus(token=token)
pushplus.send(message)
