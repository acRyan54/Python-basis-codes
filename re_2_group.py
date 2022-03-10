import re

def readEmail(email):
    re_addr = re.compile(r'^<?([a-zA-z\s.]+)>?')
    m = re_addr.match(email)
    if m:
        print('Right\n',m.group(1))
    else:
        print('Wrong')
        
if __name__ == '__main__':
    email = input()
    readEmail(email)