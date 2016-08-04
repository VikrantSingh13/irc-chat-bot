
### Connection and authentication =============================

HOST = "irc.chat.twitch.tv."
PORT = 6667
#name of the channel chat you want to spam 
CHANNEL = "loltyler1"
#OAuth key for twitch or similar api, http://twitchapps.com/tmi/
PASS = ""
#your or your bot's twitch username
USER = "" 

### Spam related constants ===================================

### Change TARGET_KEYWORD to [], if you don't want to
### reply to a specific keyword, and just want to spam links, etc. 
TARGET_KEYWORD = ["hello", "Kappa", "elo", "BibleThump", "PogChamp",
                  "alpha", "fag", "kys", "banned", "stream", "tyler"]

### TARGET_USER only takes "True" or "False" without the quotes
TARGET_USER = True

SPAM_MESSAGE = "BANNED Kappa BANNED Kappa BANNED Kappa BANNED Kappa BANNED Kappa BANNED Kappa BANNED Kappa BANNED Kappa BANNED Kappa BANNED Kappa BANNED Kappa BANNED Kappa BANNED Kappa "

### Anti Ban===================================================

#SECONDS, set it to 0 at your own risk.
DELAY_BETWEEN_SPAM = 3 
#only take "True" or "False", without the quotes. Adds a random int after spam.
ANTI_BAN_RANDOM_INT = True
