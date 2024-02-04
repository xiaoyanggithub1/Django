import hashlib

from flask import request
import json
from django.http import HttpResponse


def success(data, code=200, msg='请求成功', errno=0):
    return HttpResponse(json.dumps(
        {
            'code': code,
            'errno': errno,
            'msg': msg,
            'data': data,
        }
    ))


def fail(data=None, code=400, errno=1, msg='请求失败！'):
    return HttpResponse(json.dumps(
        {
            'code': code,
            'errno': errno,
            'msg': msg,
            'data': data,
        }
    ))

def encrypt_password(password):
    # 生成MD5哈希值,加密密码
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

