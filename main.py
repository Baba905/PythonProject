from internet_speed_bot import InternetTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "bdiop8683@gmail.com"
TWITTER_PASSWORD = "loveTKD99++"

bot = InternetTwitterBot()
# bot.get_internet_speed()
# print(f"Down : {bot.down}\nUp : {bot.up}")

bot.tweet_at_provider()

