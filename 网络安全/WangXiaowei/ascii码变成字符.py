# 从数字列表转换
ascii_codes = [144,150,139,145,165,120,139,91,160,93,167,70]
result = ''.join(chr(code) for code in ascii_codes)
print(result)