# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-10-23 18:07:44
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-10-23 18:07:53
# @github: https://github.com/longfengpili


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
