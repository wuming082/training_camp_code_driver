import base64
import requests

def main():
    a = requests.session()
    b = a.get("https://eci-2zebitqp4m6u00f256g4.cloudeci1.ichunqiu.com:80/")  #访问URL并保存session
    key1 = b.headers["flag"]   #获取头部信息 flag的内容
    c = base64.b64decode(key1) #对key1的内容进行解码
    d = str(c).split(":")  #解码后吧内容通过:进行分割，并存入数组
    key = base64.b64decode(d[1]) #去数组的第二个内容即我需要的值再次进行base64解码
    body = {"ichunqiu":key} #构造http内容体
    f = a.post("https://eci-2zebitqp4m6u00f256g4.cloudeci1.ichunqiu.com:80/",data=body)
    print(f.text)
if __name__ == '__main__':
    main()