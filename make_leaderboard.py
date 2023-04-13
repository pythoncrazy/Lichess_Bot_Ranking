# Imports
import berserk # I am too lazy to make the api calls directly
import csv #I need this in order to add data to the tsv, tab separated file.

#Logging into the lichess account
with open('./lichess.token') as f:
    token = f.read()
session = berserk.TokenSession(token)
client = berserk.client.users(session)

name_of_bot_accounts = list(line.strip() for line in open('bullet_bot.names')) # Maybe not the most efficient way of doing this, but it works and I want to do it this way.

with open('./Bullet.csv','w',newline='') as f_output:         # https://stackoverflow.com/a/49150147/21368519
    tsv_output = csv.writer(f_output, delimiter='\t')
    bot_information = []
    for name_of_bot in name_of_bot_accounts: # iterate over all of the bot accounts
        name = name_of_bot
        max_rating = 
        tsv_output.writerow(data)