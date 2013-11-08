#!/usr/bin/env python2
import twitchTvIrc

irc = twitchTvIrc.TwitchTvIrcApi(silence=True)

irc.connect()
irc.authenticate('obnoxioustheegod', 'dx4a34a67rztbr2ybahrr7nv9zmsw53')
irc.join("#obnoxioustheegod")
irc.privmsg('#obnoxioustheegod', 'HELLO WORLD!')
