from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

def hello(bot, update):
    update.message.reply_text(
        'Hello {}! Use the /jboss command to fetch the stars from the repository of JBoss.'.format(update.message.from_user.first_name))

def stars(bot, update):
    api = requests.get('https://api.github.com/orgs/JBossOutreach/repos')
    res = api.json()
    out = ''
    for a in range(len(res)):
        out += '\n' + res[a]['name'] + ': ' + str(res[a]['stargazers_count'])
    update.message.reply_text('Here are JBoss Repositories & their Stars. \n\n' + out + '\n\nFor a Specific Repo, type the name of the Repo.')

def repo(bot, update):
    api = requests.get('https://api.github.com/orgs/JBossOutreach/repos')
    res = api.json()
    out = ''
    for a in range(len(res)):
        if res[a]['name'] == update.message.text:
            out += res[a]['name'] + ': ' + str(res[a]['stargazers_count'])
    if out == '':
        out = 'No Repository Found'
    bot.send_message(chat_id=update.message.chat_id, text=out)

updater = Updater('TOKEN')

updater.dispatcher.add_handler(CommandHandler('start', hello))
updater.dispatcher.add_handler(CommandHandler('jboss', stars))
updater.dispatcher.add_handler(MessageHandler(Filters.text, repo))

updater.start_polling()
updater.idle()
