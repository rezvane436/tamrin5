n=input(('enter string plz'))
s='q0'
for i in range(len(n)):
    if s=='q0' and n[i]=='a':
        s='q1'  
if s=='q0':
    print('accept')
else:
    print('reject')
