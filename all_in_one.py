# importing flask
from flask import Flask, render_template
import csv
import runpy
import time
# importing pandas
import pandas as pd

app = Flask(__name__)

# Imports
import berserk  # I am too lazy to make the api calls directly

#Logging into the lichess account
with open('./lichess.token') as f:
  token = f.read()
session = berserk.TokenSession(token)

variants = ["bullet", "blitz", "rapid"]


def create_bot_txt(variant):
  client = berserk.clients.Bots(session)
  #get the list of all 2000000000000 bots accounts online
  # I do realize that there could one day be more than 200000000000 bot accounts online, but it is very unlikely
  online_bots = client.get_online(nb=20000000000)

  name_of_bot_accounts = set(
    line.strip() for line in open(variant + "/" + variant + '_bot.names')
  )  # Read in all of the previous bot accounts into a set. This allows for any bots I manually add to be kept, but not have duplicates.

  for i in online_bots:
    name_of_bot = i['id']
    #print(name_of_bot,i.keys())
    if (
        i["perfs"][variant]["rd"] < 100
    ):  # filter out the bot accounts that are inactive in bullet. I choose 100 because I feel that most active bots can reach sub 100 rd. I did not choose 75, since some bots don't always get to play other bots at their rating. I feel very strongly on this, but will most likely change it at some future point in time.
      try:
        if (
            i["tosViolation"]
        ):  #exclude bots that have a TOS Violation, since they shouldn't be on the list anyways
          continue
      except:
        name_of_bot_accounts.add(name_of_bot)
  name_of_bot_accounts = list(name_of_bot_accounts)
  name_of_bot_accounts.sort(
  )  #I want it sorted because it looks better. It has a minimal impact on performance, but it feels better and cleaner. Just like washing your hands.
  with open(variant + "/" + variant + '_bot.names', 'w') as f:
    for i in name_of_bot_accounts:
      f.write(i + "\n")
  print(" Made list of bots: done!")


def make_leaderboard_txt(variant):
  client = berserk.Client(session)
  name_of_bot_accounts = list(
    line.strip() for line in open(variant + "/" + variant + '_bot.names')
  )  # Maybe not the most efficient way of doing this, but it works and I want to do it this way.

  i = 0
  with open(
      variant + "/" + variant + ".csv", 'w',
      newline='') as f_output:  # https://stackoverflow.com/a/49150147/21368519
    csv_output = csv.writer(f_output)
    csv_output.writerow([
      "Name", "Current Rating", "Maximum Rating", "Total Games Played",
      "Rating Progression", "Total Playing Time", "Total Time on TV"
    ])
    for name_of_bot in name_of_bot_accounts:  # iterate over all of the bot accounts
      if (i % 10 == 0):
        print(i, "done!")
      i += 1
      #rating information
      rating_stats = client.users.get_performance_statistics(
        name_of_bot, variant
      )  #for some reason, the pypi berserk package does not have this function. I have manually added it from their GitHub repo: https://github.com/rhgrant10/berserk/blob/master/berserk/clients.py#L329
      max_rating = rating_stats["stat"]["highest"]["int"]
      current_rating = rating_stats["perf"]["glicko"]["rating"]
      games_played = rating_stats["stat"]["count"][
        "rated"]  #For leaderboard purposes, we only want to have rated games played. If there is a reason to change this, I will change it
      rating_progress = rating_stats["perf"]["progress"]
      #Playing time information
      playing_stats = client.users.get_public_data(name_of_bot)
      if ("playTime" in playing_stats.keys()):
        total_play_time = playing_stats["playTime"]["total"]
        tv_play_time = playing_stats["playTime"]["tv"]
      else:
        total_play_time = 0
        tv_play_time = 0

      data = [
        name_of_bot, current_rating, max_rating, games_played, rating_progress,
        total_play_time, tv_play_time
      ]

      csv_output.writerow(data)
  print("Made Leaderboard csv file: done!")


def sort_to_csv(variant):
  # making data frame from csv file
  data = pd.read_csv(variant + "/" + variant + ".csv")
  data.sort_values("Maximum Rating",
                   axis=0,
                   ascending=False,
                   inplace=True,
                   na_position='first')
  print(data)
  data.to_csv(variant + "/" + variant + '_sorted_by_max_rating.csv',
              index=False)

  data = pd.read_csv(variant + "/" + variant + ".csv")
  data.sort_values("Current Rating",
                   axis=0,
                   ascending=False,
                   inplace=True,
                   na_position='first')
  print(data)
  data.to_csv(variant + "/" + variant + '_sorted_by_current_rating.csv',
              index=False)



def get_data():
  for variant in variants:
    print("Doing ", variant, " currently!")
    create_bot_txt(variant)
    make_leaderboard_txt(variant)
    make_leaderboard_txt(variant)
    print("finished", variant)
  time.sleep(3600)

x=0
mult= 1.2
while True:
    try:
        get_data()
        x=0
    except Exception as e:
        x+=1
        print(e)
        print("backing off")
        time.sleep(3600+(mult)**x)