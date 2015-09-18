import time
import tokens
from slackclient import SlackClient

def main():
	token = tokens.token
	client = SlackClient(token)
	if client.rtm_connect():
		client.rtm_send_message("testbed", ":dank_horse:")
	else:
		print "Connection Failed."

if __name__ == '__main__':
	main()