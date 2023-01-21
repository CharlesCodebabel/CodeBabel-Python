import telebot

# name : YourBot_Bot <This is user displayname>
# username : your_bot ( Changes made by @your_bot )

# Documentation : https://core.telegram.org/bots/api

# [[[ Remember ]]] to look for the BotFather bot to start creating the bot,
# generate the API KEY, name ( Which will be displayed on the bot screen ),
# username ( It is for them that you will make the name changes,
# bot profile image , among other details )
# You will need to get your bot online, use the free heruko server...

APIKEY = 'YourAPIKEYGeneratedByBotFather'
xbot = telebot.TeleBot(APIKEY)

@xbot.message_handler(commands=['Github'])
def my_github(message):
    xbot.reply_to(message, 'My GitHub\n')
    xbot.reply_to(message, 'https://github.com/YourGitProfile')

@xbot.message_handler(commands=['Youtube'])
def my_github(message):
    xbot.reply_to(message, 'Your Youtube Channel\n')
    xbot.reply_to(message, 'https://www.youtube.com/@YourChannel')

@xbot.message_handler(commands=['Twitter'])
def my_github(message):
    xbot.reply_to(message, 'Your Twitter Profile\n')
    xbot.reply_to(message, 'https://twitter.com/yourtwitter')

@xbot.message_handler(commands=['Picture'])
def my_github(message):
    xbot.reply_to(message, 'Your Profile Image\n')
    image = 'https://seeklogo.com/images/G/github-logo-5F384D0265-seeklogo.com.png'
    xbot.reply_to(message, f'{image}')


def verify(message):
    return True

#ttart___
@xbot.message_handler(func=verify)
def bot_reply(message):
    #print(message) }} return json message atributes and values 

    option = """
    Welcome, choose one of the options below:
    [ My Social Networks ]

    /Github    : Your GitHub   🦑
    /Twitter   : Your Youtube  🔥
    /Twitter   : Your Twitter  🐤
    /Picture   : Your Picture  📸    
    """
    xbot.reply_to(message, f'{option}')
    #xbot.send_message(message.chat.id, 'good!'), no mark reply...
    print('Message }} now ')

xbot.polling()


