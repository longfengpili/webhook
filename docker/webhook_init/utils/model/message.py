# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-10-22 10:06:03
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-10-22 14:17:13
# @github: https://github.com/longfengpili


import time
from abc import ABC, abstractmethod


class Validator(ABC):
    """验证器抽象基类"""
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner=None):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class OneOf(Validator):
    """字符串单选验证器"""
    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f'Expected {value!r} to be one of {self.options!r}')


class Number(Validator):
    """数值类型验证器"""
    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value!r} to be an int or float')


class Message:
    channel = OneOf('wechat', 'webhook', 'cp', 'mail', 'sms')
    template = OneOf('html', 'txt', 'json')

    def __init__(self, title: str, content: str, channel: str = 'wechat', template: str = 'html', **kwargs):
        self.title = title
        self.content = content
        self.channel = channel
        self.template = template
        self.kwargs = kwargs

    def __repr__(self):
        content = self.content
        content = content if len(content) <= 20 else content[:20]
        return f"Message({self.title}:{content})::{self.channel}"

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
