import re
def valida_email(email):
   padrao = '[\w]{3,50}(@)(globo|gmail|hotmail|yahoo)(.com)(.br)?'
   if re.match(padrao, email):
      return True
   return False
