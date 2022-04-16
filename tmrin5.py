n=input(('enter string plz'))
s='q0'
for i in range(len(n)):
    if s=='q0'and n[i]=='a':
        s='q1'
    elif s=='q0' and (n[i]=='b'or n[i]=='c'):
        s='q4'
    elif s=='q1' and n[i]=='b':
        s='q2'
    elif s=='q1' and (n[i]=='a'or n[i]=='c'):
        s='q4'
    elif s=='q2' and n[i]=='c':
        s='q3'
    elif s=='q2' and (n[i]=='a'or n[i]=='b'):
        s='q4'
    elif s=='q3' and (n[i]=='a'or n[i]=='b' or n[i]=='c'):
        s='q3'    
if s=='q3':
    print('reject')
else:
    print('accept')
