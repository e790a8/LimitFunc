#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author   : lisztomania
# @Date     : 2020/12/16 19:04
# @Software : PyCharm
# @Version  : Python 3.9.1
# @Project  : LimitFunc
# @FileName : LimitFunc.py
# @Function : 限制函数
from typing import Dict, Tuple


# 检查默认值
def __check_defaults(defaults: Dict, incoming: Dict):
    for key in defaults.keys():
        try:
            incoming[key]
        except KeyError:
            incoming[key] = defaults[key]


# 检查类型
def __check_raise(checks: Dict, kwargs: Dict) -> bool:
    if checks.keys() == kwargs.keys():
        for key in checks.keys():
            checks_temp = checks.get(key)
            kwargs_temp = kwargs.get(key)
            if checks_temp.__class__ != type:
                raise Exception(f"The value of {key.__str__()} for the decorator must be type")
            if kwargs_temp.__class__ == type:
                raise Exception(f"The value of {key.__str__()} for the function cannot be type")
            if kwargs_temp.__class__ != checks_temp:
                raise Exception(f"{key} must be an {checks_temp.__name__}")
        return True
    else:
        raise Exception("The checks must be consistent with the parameters")


# 检查非关键字参数
def __check_args(checks: Dict, args: Tuple, kwargs: Dict):
    checks_keys: Tuple = tuple(checks.keys())
    for key, value in zip(checks_keys, args):
        kwargs[key] = value


# 限制装饰器
def limit_func(*, checks: Dict, defaults: Dict = None):
    """
    :param checks:type dict,The fromat of the checks is {args:type}, args is str and type is type
    :param defaults:default value dict,The fromat of the defaults is {args:value}, args is str and value not is type
    :return:None
    """
    def function(func):
        def wrapper(*args, **kwargs):
            if defaults:
                __check_defaults(defaults=defaults, incoming=kwargs)
            if args:
                __check_args(checks=checks, args=args, kwargs=kwargs)
            if __check_raise(checks=checks, kwargs=kwargs):
                return func(**kwargs)
        return wrapper
    return function
