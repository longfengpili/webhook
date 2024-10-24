# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-10-22 10:06:03
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-10-24 10:14:08
# @github: https://github.com/longfengpili


import time
from .validator import OneOf, Number


class Message:
    template = OneOf('html', 'txt', 'json')

    def __init__(self, title: str, content: any, template: str = 'html', **kwargs):
        self.title = title
        self.content = content
        self.template = template
        self.kwargs = kwargs

    def __repr__(self):
        content = self.content
        content = content if len(content) <= 20 else content[:20]
        return f"Message({self.title}:{content})::{self.template}"

    def __getattr__(self, item):
        '''
        当你使用属性访问时（例如 `obj.attr`），Python会首先查找对象的实例字典（`obj.__dict__`）来查找属性。
        '''
        if item in self.kwargs:
            return self.kwargs.get(item)
        return object.__getattribute__(self, item)  # 避免递归

    def __getitem__(self, item):
        '''
        当你使用索引访问时（例如 `obj[key]`），Python会首先尝试调用 `__getitem__` 方法。
        如果对象没有定义 `__getitem__` 方法，或者 `__getitem__` 方法抛出了一个 `KeyError`，
        那么Python会引发一个 `TypeError`，表明对象不支持索引访问。
        '''

        if item in self.attrs:
            return self.attrs[item]
        return getattr(self, item)

    def get(self, item, default=None):
        return getattr(self, item, default)
