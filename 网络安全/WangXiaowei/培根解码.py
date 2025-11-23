list1 = []
list2 = []
list3 = []
list4 = []
res1 = []
res2 = []
strs = "bacoN is one of aMerICa'S sWEethEartS. it's A dARlinG, SuCCulEnt fOoD tHAt PaIRs FlawLE"
for i in strs:
         if i.isupper():
                   list1.append('b')
         elif i.islower():
                   list1.append('a')
strs1 = ''.join(list1)
len1 = len(list1)
for i in range(0,len1+1,5):
         list2.append(i)
len2 = len(list2)
for i in range(len2):
         if i != len2 - 1:
                   list3.append(strs1[list2[i]:list2[i+1]])
for i in list3:
         list4.append(i.upper())
dir1 = {'A':'aaaaa','B':'aaaab','C':'aaaba','D':'aaabb','E':'aabaa','F':'aabab','G':'aabba','H':'aabbb','I':'abaaa','J':'abaab','K':'ababa','L':'ababb','M':'abbaa','N':'abbab','O':'abbba','P':'abbbb','Q':'baaaa','R':'baaab','S':'baaba','T':'baabb','U':'babaa','V':'babab','W':'babba','X':'babbb','Y':'bbaaa','Z':'bbaab'}
dir2 = {'a':'AAAAA','g':'AABBA','n':'ABBAA','t':'BAABA','b':'AAAAB','h':'AABBB','o':'ABBAB','u/v':'BAABB','c':'AAABA','i/j':'ABAAA','p':'ABBBA','w':'BABAA','d':'AAABB','k':'ABAAB','q':'ABBBB','x':'BABAB','e':'AABAA','l':'ABABA','r':'BAAAA','y':'BABBA','f':'AABAB','m':'ABABB','s':'BAAAB','z':'BABBB'}
for i in range(len(list3)):
         for j in dir1:
                   if list3[i] == dir1[j]:
                            res1.append(j)
print (''.join(res1))
for i in range(len(list4)):
         for j in dir2:
                   if list4[i] == dir2[j]:
                            res2.append(j)
print (''.join(res2))
