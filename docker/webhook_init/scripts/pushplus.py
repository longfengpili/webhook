#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-10-21 19:03:55
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-10-24 10:18:58
# @github: https://github.com/longfengpili

import os

from utils.model import OpenMetaDataMessage
from utils.network import PushPlus

token = os.getenv('PUSHPLUS_TOKEN')
message = os.getenv('MESSAGE')

message = OpenMetaDataMessage.load_message(message)
pushplus = PushPlus(token=token)
result = pushplus.send(message)
print(result)
