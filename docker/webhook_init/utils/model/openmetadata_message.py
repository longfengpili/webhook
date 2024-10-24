# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-10-23 11:15:27
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-10-24 14:09:07
# @github: https://github.com/longfengpili

import json

from .message import Message


class OpenMetaDataMessage(Message):

    @classmethod
    def load_message(cls, message: str):
        keys = ['fullyQualifiedName', 'entityFQN', 'testCaseResult', 'owners', 
                'updatedAt', 'updatedBy', 'deleted', 'computePassedFailedRowCount', 'useDynamicAssertion']
        message = json.loads(message)
        message = {key: message[key] for key in keys}
        title = message.get('fullyQualifiedName')
        return cls(title, content=message, template='json')
