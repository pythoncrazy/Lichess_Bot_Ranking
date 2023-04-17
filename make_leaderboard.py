# Imports
import berserk # I am too lazy to make the api calls directly
import csv #I need this in order to add data to the tsv, tab separated file.

#Logging into the lichess account
with open('./lichess.token') as f:
    token = f.read()
session = berserk.TokenSession(token)
client = berserk.Client(session)

name_of_bot_accounts = list(line.strip() for line in open('bullet_bot.names')) # Maybe not the most efficient way of doing this, but it works and I want to do it this way.

i=0
with open('./Bullet.csv','a',newline='') as f_output:         # https://stackoverflow.com/a/49150147/21368519
    csv_output = csv.writer(f_output)
    for name_of_bot in name_of_bot_accounts: # iterate over all of the bot accounts
        print(name_of_bot,i)
        i+=1
        #rating information
        rating_stats = client.users.get_performance_statistics(name_of_bot,"bullet") #for some reason, the pypi berserk package does not have this function. I have manually added it from their GitHub repo: https://github.com/rhgrant10/berserk/blob/master/berserk/clients.py#L329
        max_rating = rating_stats["stat"]["highest"]["int"]
        current_rating = rating_stats["perf"]["glicko"]["rating"]
        games_played = rating_stats["stat"]["count"]["rated"] #For leaderboard purposes, we only want to have rated games played. If there is a reason to change this, I will change it
        rating_progress = rating_stats["perf"]["progress"]
        #Playing time information
        playing_stats = client.users.get_public_data(name_of_bot)
        if("playTime" in playing_stats.keys()):
            total_play_time = playing_stats["playTime"]["total"]
            tv_play_time = playing_stats["playTime"]["tv"]
        else:
            total_play_time = 0
            tv_play_time = 0
        
        data = [name_of_bot,current_rating,max_rating, games_played, rating_progress, total_play_time,tv_play_time]
        
        csv_output.writerow(data)