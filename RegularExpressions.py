import re

#pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
#pattern = r"([\w\.-]+)([\w]*)@([\w\.-]+)(\.[\w\.]+)"
pattern = r"^([\w]([\.-][\w])*)@([\w])(\.)([\w]([\.-][\w])*)+$"
if re.match(pattern, "--.@-.-"):
    print('Hey!')
else:
    print('No!')
    
