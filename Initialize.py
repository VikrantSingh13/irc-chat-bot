from Socket import send_message
from config import INITIALIZATION_SPAM
import time

def join_room(s):
  loading = True
  while(loading):
    read_buffer = s.recv(1024).decode('UTF-8')
    temp = read_buffer.split("\n")
    read_buffer = temp.pop()
			
    for line in temp:
      #print(line) #don't uncomment this line if there's too much spam in the chat
      loading = loading_complete(line)
  send_message(s, INITIALIZATION_SPAM)
	
def loading_complete(line):
  if("End of /NAMES list" in line):
    return False
  else:
    return True

def get_user(str):
  end = str.index("!")
  return str[1:end]
		

def get_message(str):
  begin = str[1:].index(":") + 2
  return str[begin:].strip(" \n\r")
		
#todo add try catch to get_user and get_message
