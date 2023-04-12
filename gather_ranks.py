# Imports
import berserk
import json
import supabase

#Logging into the lichess account
with open('./lichess.token') as f:
    token = f.read()
session = berserk.TokenSession(token)
client = berserk.clients.Bots(session)

#get the list of all 2000000000000 bots accounts online
# I do realize that there could one day be more than 200000000000 bot accounts online, but it is very unlikely
online_bots = client.get_online(nb=20000000000)
for i in online_bots:
    i = i['id']
    print(i)
