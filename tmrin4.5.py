n=input(('enter string plz'))
s='q0'
for i in range(len(n)):
    if(n[i]=='a' and s=='q0'):
        s='q1'
    elif(n[i]=='b' and s=='q0'):
        s='q1'
    elif(n[i]=='a' and s=='q1'):
        s='q2'
    elif(n[i]=='b' and s=='q1'):
        s='q2'
    elif(n[i]=='a' or n[i]=='b' and s=='q2'):
        s='q1'
    
if(s=='q1'):
    print("accept")
else:
    print("reject")

