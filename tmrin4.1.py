n=input(('enter string plz'))

def DFA(strr):
    s='q0'
    for i in range(len(strr)):
        if s=='q0':
            s='q0'
    if s=='q0':
        return 'reject'
   
print(DFA(n))