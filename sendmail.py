import smtplib 
from_addr = 'email@gmail.com' 
to_addr = ''
from_name = 'me'
to_name = 'me'
subject = 'Does this work?'
msg = 'Hey There'

message = """From: {} <{}> 
To: {} <{}>
 Subject: {} 
{} 
""" 
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg) 
# Credentials (if needed) 
username = 'r.dobson1094@gmail.com' 
password = '' 
# The actual mail send 
server = smtplib.SMTP('smtp.gmail.com:587') 
server.starttls() 
server.login(username, password) 
server.sendmail(from_addr, to_addr, message_to_send) 
server.quit()