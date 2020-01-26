import pandas as pd
import sqlalchemy

from Trivia import Game
from random import choice
from datetime.datetime import now

"""
TODO: The end of the game needs changing.
"""

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
      1: self.vote,
      2: self.end
    }
  
    self.data["idea"] = (
      f"A {choice(self.adjectives)} {choice(self.nouns)} "
      f"for {choice(self.fors)}"
    )
    self.data["hacker"] = choice(
      list(self.players.keys())
    )

  def get_info(self, username):
    d = self.game_state
    if self.currentStage == 0:
      d.update({'waiting_for_players':True})
      return d
    if self.currentStage == 1:
      d.update(self.get_votes(username))
      return d
    if self.currentStage == 2:
      if len(self.data["votes"]) >= len(self.players) - 1:
        self.data["votes"] = []
        self.currentStage += 1
    d.update(self.stages[self.currentStage](username))
    return d

  def post_info(self, data : dict, username):
    if self.currentStage == 0:
      self.currentStage += 1
      return True
    if username not in self.data["votes"]:
      self.data["votes"][username] = data["vote"]
      return True
    return False

  def getVotes(self, username):
    if username == self.data["hacker"]:
      d = {
        "message": (
          f"You are the hacker. The idea could be "
          f"{self.adjectives} {self.nouns} for {self.fors}."
        )
      }
    else:
      d = {
        "message": f"The idea is {self.data['idea']}.",
        "buttons": []
      }
      for player in self.players:
        if player != username:
          d["buttons"].append(player)
    return d

  def end(self):
    d = {
      "message": "WINNER: {0}".format(
        max(
          self.data["scores"].getitems(),
          key=(lambda x: max(x[1]))
        )[0]
      ),
      "table": self.data["scores"],
      "currentStage": self.currentStage,
    }
    return d
    
