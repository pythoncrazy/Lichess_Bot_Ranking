# Imports
import berserk # I am too lazy to make the api calls directly


#Logging into the lichess account
with open('./lichess.token') as f:
    token = f.read()
session = berserk.TokenSession(token)
client = berserk.clients.Bots(session)

#get the list of all 2000000000000 bots accounts online
# I do realize that there could one day be more than 200000000000 bot accounts online, but it is very unlikely
online_bots = client.get_online(nb=20000000000)

name_of_bot_accounts = set(line.strip() for line in open('bullet_bot.names')) # Read in all of the previous bot accounts into a set. This allows for any bots I manually add to be kept, but not have duplicates.

for i in online_bots:
    name_of_bot = i['id']
    if i["perfs"]["bullet"]["rd"]<100: # filter out the bot accounts that are inactive in bullet. I choose 100 because I feel that most active bots can reach sub 100 rd. I did not choose 75, since some bots don't always get to play other bots at their rating. I feel very strongly on this, but will most likely change it at some future point in time.
        name_of_bot_accounts.add(name_of_bot)
name_of_bot_accounts = list(name_of_bot_accounts)
name_of_bot_accounts.sort() #I want it sorted because it looks better. It has a minimal impact on performance, but it feels better and cleaner. Just like washing your hands. 
with open('bullet_bot.names','w') as f:
    for i in name_of_bot_accounts:
        f.write(i+"\n")
