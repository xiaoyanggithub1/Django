from cryptography.fernet import Fernet  # 导入Fernet模块

# 生成加密密钥
key = Fernet.generate_key()  # 生成加密密钥
cipher_suite = Fernet(key)  # 创建加密组件

# 加密消息
def encrypt_message(message):
    encoded_message = message.encode()  # 将消息编码
    encrypted_message = cipher_suite.encrypt(encoded_message)  # 使用加密组件加密消息
    return encrypted_message

# 解密消息
def decrypt_message(encrypted_message):
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()  # 解密消息并解码
    return decrypted_message

# 测试
message = "Hello, this is a secret message."
encrypted = encrypt_message(message)
print("Encrypted message:", encrypted)

decrypted = decrypt_message(encrypted)
print("Decrypted message:", decrypted)
