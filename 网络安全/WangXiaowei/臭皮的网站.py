import random
import string

mac_int = 0x00163e102d87
random.seed(mac_int)
password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
print(f"密码: {password}")