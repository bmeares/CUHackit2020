import pandas as pd
import sqlalchemy

from Trivia import Game
from random import choice


class HackerFall(Game):
  adjectives = [
    "greedy",
    "hacky",
    "poorly-made"
  ]
  nouns = [
    "machine learning algorithm",
    "social network",
    "video game"
  ]
  fors = [
    "cats",
    "programmers",
    "children"
  ]

  def start(self):
    self.stages = {
      1: self.getVotes,
      2: self.end
    }
  
    self.data["idea"] = (
      f"A {choice(self.adjectives)} {choice(self.nouns)} "
      f"for {choice(self.fors)}"
    )
    self.data["votes"] = {}

  def get_info(self, username):
    d = self.game_state
    if self.currentStage == 0:
      d.update({'waiting_for_players':True})
      return d
    if self.currentStage == 1:
      d.update(self.getVotes(username))
      return d
    if self.currentStage == 2:
      if len(self.data["votes"]) >= len(self.players) - 1:
        self.data["votes"] = []
        self.currentStage += 1
        return d
    return d

  def post_info(self, data : dict, username):
    if self.currentStage == 0:
      self.currentStage += 1
      self.data["hacker"] = choice(
        list(self.players.keys())
      )

      return True
    #  if username not in self.data["votes"]:
      #  self.data["votes"][username] = data["buttonText"]
      #  return True
    return False

  def getVotes(self, username):
    if username == self.data["hacker"]:
      d = {
        "phoneMessage": (
          f"You are the hacker. The idea could be "
          f"{self.adjectives} {self.nouns} for {self.fors}."
        ),
        "hostMessage" : "HOME MESSAGE",
        "quit":True
      }
    else:
      d = {
        "phoneMessage": f"The idea is {self.data['idea']}.",
        "hostMessage": f"A {self.adjectives} {self.nouns} for {self.fors}",
        "buttons": [],
        "quit":True
      }
      for player in self.players:
        if player != username:
          d["buttons"].append(player)
    return d

  def end(self):
    ratio = (
      len([vote for user, vote in self.data["votes"].items() if vote == self.data["hacker"]]) /
      (len(self.players) - 1)
    )
    if ratio > .5:
      mess = f"Hacker {self.data['hacker']} wins!"
    else:
      mess = f"Team wins!"
    d = {
      "hostMessage": mess,
      "phoneMessage": mess,
      "currentStage": self.currentStage,
    }
    return d
    
