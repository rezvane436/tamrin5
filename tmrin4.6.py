n=input(('enter string plz'))
s='q0'
for i in range(len(n)):
    if s=='q0'and n[i]=='a':
        s='q0'
    if s=='q0' and n[i]=='b':
        s='q1'
    elif s=='q1' and n[i]=='a':
        s='q1'
    elif s=='q1' and n[i]=='b':
         s='q0'
    
if s=='q0':
    print('accept')
else:
    print ('reject')
