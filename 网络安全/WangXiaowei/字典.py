str_word = 'abcdefghijklmnopqrstuvwxyz'
num_word = '0123456789'

with open ('1.dic','w') as f:
    for i in str_word:
        for j in str_word:
            for k in str_word:
                for l in num_word:
                    for m in str_word:
                        f.write(i+j+k+l+m+'\n')