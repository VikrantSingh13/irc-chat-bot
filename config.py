
### Connection and authentication =============================
HOST = "irc.chat.twitch.tv."
PORT = 6667
CHANNEL = "" #name of the channel chat you want to spam 
PASS = "" #OAuth key for twitch or similar api, http://twitchapps.com/tmi/
USER = "" #your or your bot's twitch username

### Spam related constants ===================================

### Change TARGET_KEYWORD to [], if you don't want to
### reply to a specific keyword, and just want to spam links, etc. 
TARGET_KEYWORD = ["hello", "Kappa"]

### TARGET_USER only takes "True" or "False" without the quotes
TARGET_USER = True

SPAM_MESSAGE = "Hello! Kappa"
DELAY_BETWEEN_SPAM = 5 #SECONDS, set it to 0 at your own risk.
