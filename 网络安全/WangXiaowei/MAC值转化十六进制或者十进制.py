import random
import string
import uuid


# 将 MAC 地址转化为整数
mac_address = "00:16:3e:38:e3:d3"
mac_int = int(mac_address.replace(":",""),16)

# 确保使用的种子是 UUID 节点
# 这里使用的是 mac_int,作为 uuid.getnode()模拟值
random.seed(mac_int)


# 生成密码
password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
print(f"MAC Adress:{mac_address}")
print(f"MAC Integer:{mac_int}")
print(f"Generated Password:{password}")


