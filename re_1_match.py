import re

def readEmail(email):
    re_email = re.compile(r'([\w.]+)@([\w.]+)')
    m = re_email.match(email)
    if m:
        print('Right\n', m.groups())
    else:
        print('Wrong')
        
if __name__ == '__main__':
    email = input()
    readEmail(email)