from Socket import send_message

def join_room(s):
	read_buffer = ""
	loading = True
	while(loading):
		read_buffer = read_buffer + s.recv(1024).decode('UTF-8')
		temp = read_buffer.split("\n")
		read_buffer = temp.pop()
			
		for line in temp:
			print(line)
			loading = loading_complete(line)
	send_message(s, "Successfully joined chat")	

def loading_complete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True
	