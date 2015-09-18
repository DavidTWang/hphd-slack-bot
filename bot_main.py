import time
import tokens
from slackclient import SlackClient

def main():
	token = tokens.token
	client = SlackClient(token)
	if client.rtm_connect():
		channel = raw_input("Channel name: ")
		while True:
			message = raw_input("Message: ")
			client.rtm_send_message(channel, message)
	else:
		print "Connection Failed."

if __name__ == '__main__':
	main()