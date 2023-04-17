'''st="Kratika Agarwal"

length=len(st)
print("length of string is: ",length)

st1=st[1:10]
st2=st[11:13]
print("new sub string: ",st1)
print("concatenated sub strings: ",st1+st2)
for i in range(len(st1)):
    print(st1[i])

    
st="naman"
rev=st[::-1]
print(rev)
if rev==st:
    print("string is palindrome")
else:
    print("string is not palindrome")'''

st="21bcon@711"
'''cd=0
cl=0
cs=0
for i in range(len(st)):
    if(st[i].isalpha()):
        cl+=1
    elif(st[i].isdigit()):
        cd+=1
    else:
        cs+=1
print("no. of digits: ",cd)
print("no. of letters: ",cl)
print("no. of special characters: ",cs)'''


total=0
avg=0
cd=0
for i in range(len(st)):
    if(st[i].isdigit()):
        cd+=1
        total+=int(st[i])
print("sum of digits: ",total)
avg=total/cd
print("average of digits: ",avg)
    






