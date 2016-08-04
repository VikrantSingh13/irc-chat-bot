from Socket import open_socket, send_message
from Initialize import *
import config, random, time

s = open_socket()
join_room(s)


#main loop
while(True):
  read_buffer = s.recv(1024).decode('UTF-8')
  reply_to_user = get_user(read_buffer)
  reply_to_message = get_message(read_buffer).lower()
  
	
  if (config.TARGET_KEYWORD != []):
    for keyword in config.TARGET_KEYWORD:
      if (keyword.lower() in reply_to_message):
        if(not config.TARGET_USER):
          send_message(s, config.SPAM_MESSAGE)
        else:
          send_message(s,  "@" + reply_to_user + " " + config.SPAM_MESSAGE)
        break
  else:
    if(not config.TARGET_USER):
        send_message(s, config.SPAM_MESSAGE)
    else:
        send_message(s,  "@" + reply_to_user + " " + config.SPAM_MESSAGE)
    
  time.sleep(config.DELAY_BETWEEN_SPAM)	
