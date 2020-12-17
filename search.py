#!/usr/bin/env python3

import re
import operator
import sys

def search_name(file):

    for line in file:
      match = re.search(r"^[B].* ", line)
      if match is not None:
        print (match)

def search_error(file):
    err = {}
    users = {}
    
    for line in file:
      info = re.findall(r"ticky: (?P<logtype>INFO|ERROR): (?P<logmessage>[\w].*)? \((?P<username>[\w]*)\)$", line, re.MULTILINE)
    
      for logtype, logmessage, username in info:
        if username not in users:
          users[username]={"INFO": 0, "ERROR": 0}
      
        users[username][logtype] +=1
        
        if logtype == "ERROR":
          if logmessage not in err:
            err[logmessage] = 1
          else:
            err[logmessage] +=1

    sortedErr = sorted(err.items(), key=lambda x: x[1], reverse=True)
    sortedUsers = sorted(users.items(), key=lambda x: x[0], reverse=False)     
    
    print(sortedErr)
    print(sortedUsers)

def main():
    f=open("errors.txt")
    search_error(f)
    f.close()

if __name__=='__main__':
    main()
