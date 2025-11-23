a = [144,150,139,145,165,120,139,91,160,93,167,70]
for i in range(-50,50):
    flag = ''
    for j in a:
        flag += chr(i+j)
    if 'flag' in flag:
        print(flag)