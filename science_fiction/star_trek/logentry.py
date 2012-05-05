from pyserv import Command
from time import time

class logentry(Command):
	help = "Do a Star Trek log entry!"
	def onCommand(self, uid, args):
		stardate_raw = str(time())
		stardate = stardate_raw[1:6] + "," + stardate_raw[6]
		self.msg(uid, "Captain's log, stardate " + stardate + ".")
		self.msg(uid, "We entered the Nebular in grid 476 to look for the life signs our sensors had found.")
		self.msg(uid, "We hope our response to their distress call will be in time.")

	def onFantasy(self, uid, chan, args):
		stardate_raw = str(time())
		stardate = stardate_raw[1:6] + "," + stardate_raw[6]
		ship = chan[1:].capitalize()
		account = self.auth(uid)
		nick = self.nick(uid)
		flag = self.getflag(uid, chan)
		if account != "0":
			if flag == "n":
				self.msg(chan, "Captain's log (USS " + ship + "), stardate " + stardate + ".")
				self.msg(chan, ship + " was heavily damaged in a battle with the Ascii and we're doing repairs right now.")
				self.msg(chan, "We've lost 4 of our crew members, 6 other are wounded. They died during the execution of their duties.")
				self.msg(chan, "Some of our systems are destroyed, like the shield generator. Our chief engineer is building a new one, but it could take a while.")
				self.msg(chan, "Until that, we're highly vulnerable. " + ship + " won't withstand another attack of the Ascii.")
			elif flag == "q":
				self.msg(chan, "First officer's log (USS " + ship + "), stardate " + stardate + ".")
				self.msg(chan, ship + " fought against a battalion of warships of the Ascii and was heavily damaged during the fight.")
				self.msg(chan, "The crew's moral reached a low after it. We lost 4 crew members, 6 others have been wounded.")
				self.msg(chan, "I told the counselor to speek with the ship's senior officers.")
			elif flag == "a":
				self.msg(chan, "Commander's log (USS " + ship + ", Commander " + account + "), stardate " + stardate + ".")
				self.msg(chan, ship + "'s chef is miserable. His food wasn't acceptable this week.")
				self.msg(chan, "It tasted like klingon Gagh and smelled like old muldy cheese.")
				self.msg(chan, "Next time I'll use the replicator in my quarters to \"cook\"!")
			elif flag == "o":
				self.msg(chan, "Lt. commander's log (USS " + ship + ", Lt. commander " + account + "), stardate " + stardate + ".")
				self.msg(chan, "I'm looking forward to my vacation on earth next week.")
				self.msg(chan, "But at last I don't think our journey will be without complications.")
			elif flag == "h":
				self.msg(chan, "Lietenant's log (USS " + ship + ", Lt. " + account + "), stardate " + stardate + ".")
				self.msg(chan, "My boyfriend died yesterday at " + ship + "'s battle with the Ascii.")
				self.msg(chan, "Rest in peace.")
			elif flag == "v":
				self.msg(chan, "Ensign's log (USS " + ship + ", Ensign " + account + "), stardate " + stardate + ".")
				self.msg(chan, "Our repairs of " + ship + " are nearly completed.")
				self.msg(chan, "We'll just have to adjust the new shield generator frequency.")
			else:
				self.msg(chan, "Crewman's log (USS " + ship + ", Crewman " + account + "), stardate " + stardate + ".")
				self.msg(chan, "Noone is telling me what happened yesterday at sickbay.")
				self.msg(chan, "I don't understand how humans can be so emotional.")
				self.msg(chan, "Live long and prosper.")
		else:
			self.msg(chan, "Crewman's log (USS " + ship + ", Crewman " + nick + "), stardate " + stardate + ".")
			self.msg(chan, "Noone is telling me what happened yesterday at sickbay.")
			self.msg(chan, "I don't understand how humans can be so emotional.")
			self.msg(chan, "Live long and prosper.")