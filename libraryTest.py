#!/usr/bin/env python2
import twitchTvIrc

irc = twitchTvIrc.TwitchTvIrcApi()

irc.connect()
irc.authenticate('aphoriste', 'OAUTH TOKEN, DONT INCLUDE oauth:')
irc.join("aphoriste")
irc.privmsg('#aphoriste', 'HELLO WORLD!')
