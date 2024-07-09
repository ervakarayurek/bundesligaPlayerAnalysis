# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 00:27:43 2024

@author: ekara
"""

#BAYERN MUNIH'S DEFENCE PLAYERS VS BAYER LEVERKUSEN

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mplsoccer import Pitch, Sbopen, VerticalPitch
from statsbombpy import sb

#create an object

parser = Sbopen()

# get a list of available statsbomb competitions
competitions = sb.competitions()

#Bundesliga/23-24 season values

df_match = parser.match(competition_id = 9, season_id = 281)
df_match.columns

df_match[["match_id", "match_date", "home_team_name", "home_score", "away_score",
          "away_team_name", "home_team_managers_name", "away_team_managers_name",
          "competition_name", "competition_stage_name", "stadium_name", "stadium_country_name"]]

# The match_id for the Bayer Leverkusen match is 3895232. I'll parse this to get event data for this match

df_event, df_related, df_freeze, df_tactics = parser.event(3895232)

passes = df_event.loc[df_event["type_name"] == "Pass"].loc[df_event["sub_type_name"] != "Throw-in"].set_index("id")
passes.head()

#Boolean mask for filtering the Kim Min Jae Passes

player_1 = "Min Jae Kim"
mask_kim1 = (df_event["type_name"] == "Pass") & (df_event["player_name"] == "Min Jae Kim")

df_kim1 = df_event[mask_kim1]
df_kim1["outcome_name"].value_counts()


df_pass = df_event.loc[mask_kim1,
                       ['x', 'y', 'end_x', 'end_y',
                       'outcome_name']]
kim_pass = df_pass.outcome_name.isnull()

df_pass.head()


#Setup the pitch for Kim Min Jae

pitch = Pitch(pitch_color="grass",
              line_color="white",
              stripe=True)
fig, ax = pitch.draw(figsize=(16, 11),
                     constrained_layout=False,
                     tight_layout = True)
fig.set_facecolor("#FFFFFF")

#Plot the completed passes

lc1 = pitch.lines(df_pass[kim_pass].x,
                  df_pass[kim_pass].y,
                  df_pass[kim_pass].end_x,
                  df_pass[kim_pass].end_y,
                  lw=5, transparent=True,
                  comet=True, label="Completed Passes",
                  color = "#ad993c", ax=ax)

#Plot the other passes

lc2 = pitch.lines(df_pass[~kim_pass].x,
                  df_pass[~kim_pass].y,
                  df_pass[~kim_pass].end_x,
                  df_pass[~kim_pass].end_y,
                  lw=5, transparent=True,
                  comet = True, label ="Other Passes",
                  color = "#ba4f45", ax=ax)

#Create the heatmap

pitch.kdeplot(
    x=df_pass["x"],
    y=df_pass["y"],
    shade=True,
    shade_lowest=False,
    alpha=0.5,
    n_levels=10,
    cmap="plasma",
    ax=ax)

#Plot the legend

ax.legend(facecolor="#22312b",
          edgecolor="None",
          fontsize=20,
          loc="upper left",
          handlelength=4)

#Set the title

ax_title = ax.set_title(f'{player_1} passes and Pass Heatmap vs Bayer Leverkusen', fontsize=30)
















