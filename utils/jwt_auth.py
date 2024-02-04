import jwt
import datetime
from jwt import exceptions

# 加的盐
JWT_SALT = "ds()udsjo@jlsdosjf)wjd_#(#)$"


def create_token(payload, timeout=20):
    # 声明类型，声明加密算法
    headers = {
        "type": "jwt",
        "alg": "HS256"
    }
    # 设置过期时间
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=20)
    result = jwt.encode(payload=payload, key=JWT_SALT, algorithm="HS256", headers=headers).decode("utf-8")
    # 返回加密结果
    return result


def parse_payload(token):
    """
    用于解密
    :param token:
    :return:
    """
    result = {"status": False, "data": None, "error": None}
    try:
        # 进行解密
        verified_payload = jwt.decode(token, JWT_SALT, True)
        result["status"] = True
        result['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        result['error'] = 'token已失效'
    except jwt.DecodeError:
        result['error'] = 'token认证失败'
    except jwt.InvalidTokenError:
        result['error'] = '非法的token'
    return result
