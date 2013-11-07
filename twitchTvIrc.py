"""
TwitchTv IRC Library written by aphoriste.
License: GPLv3
"""

import socket
import threading
import requests
import simplejson as json

class TwitchTvIrcApi:
	def __init__(self, silence=False):
		self.silence = False
		self.ircSocket = socket.socket()
		def logger(socket=self.ircSocket):
			while True:
				try:
					data = socket.recv(1024)
					if ' ' in data:
						splitData = data.split()

						if 'PING' in splitData[0]:
							self.ircSocket.send('PONG %s' % splitData[1])
							print('Received PING, sent PONG')
						
						elif 'PRIVMSG' in splitData[1]:
							self.messageReceived(splitData, data)
						
 						else: print(data)
					else:
						print(data)		
				except:
					pass
		logging = threading.Thread(target=logger).start()

	def connect(self):
		self.ircSocket.connect(('irc.twitch.tv', 6667))
		return True

	def authenticate(self, username, oauth):
		"""
		Log into TwitchTV IRC
		"""
		self.ircSocket.send('PASS oauth:%s\n' % oauth)
		self.ircSocket.send('NICK %s\n' % username)
		self.ircSocket.send('USER %s %s %s :%s\n' % (username, username, username, username))
		return True

	def join(self, channel):
		"""
		Join a channel
		"""
		self.ircSocket.send('JOIN %s\n' % channel.lower())
		return True

	def privmsg(self, channel, message):
		"""
		Send a message to a channel, must be in the channel first :)
		"""
		self.ircSocket.send('PRIVMSG %s :%s\n' % (channel.lower(), message))
		return True

	def messageReceived(self, splitData, data):
		"""
		Do this when receive a message in a channel
		"""
		username = splitData[0].split('@')[0].split('!')[1]
		message = data.split(':')[2]
		channel = data.split('#')[1].split()[0]
		print('<%s to #%s>: %s' % (username, channel, message))
		return True

	def generateOAuth(self, client_id, client_secret, username, password):
		"""
		To use this you must have been granted access by twitchtv staff.
		"""
		payload = {
		
		'grant_type': 'password',
		'client_id': client_id,
		'client_secret': client_secret,
		'username': username,
		'password': password,
		'scope': 'chat_login'

		}
		jsonData = json.loads(requests.post('https://api.twitch.tv/kraken/oauth2/token', \
		params=payload).text)
		return jsonData['access_token']

	def print(self, data):
		if self.silence != False:
			print(data)
