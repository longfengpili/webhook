# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-10-23 11:15:27
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-10-24 10:24:31
# @github: https://github.com/longfengpili

import json

from .message import Message


class OpenMetaDataMessage(Message):

    @classmethod
    def load_message(cls, message: str):
        keys = ['fullyQualifiedName', 'testDefinition', 'entityFQN', 'testCaseResult', 'owners', 
                'updatedAt', 'updatedBy', 'deleted', 'computePassedFailedRowCount', 'useDynamicAssertion']
        message = json.loads(message)
        entity = json.loads(message.get('entity'))
        entity = {key: entity[key] for key in keys}
        title = entity.get('fullyQualifiedName')
        return cls(title, content=entity, template='json')
