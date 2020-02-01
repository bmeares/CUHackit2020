import pandas as pd
from random import choice

from games.GameHandler import GameHandler

class HackerFall(GameHandler):
  adjectives = [
    "web",
    "command line",
    "native"
  ]
  fors = [
    "cats",
    "hackers",
    "banks"
  ]
  power = [
    "blockchain",
    "deep learning",
    "VR"
  ]

  def start(self):
    self.stages = {
      1: self.getVotes,
      2: self.end
    }
  
    self.data["idea"] = (
      f"a {choice(self.adjectives)} app "
      f"for {choice(self.fors)} "
      f"powered by {choice(self.power)}"
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
          f"You are the hacker. The idea is a  "
          f"{self.adjectives} app for {self.fors} that uses the power of {self.power}."
        ),
        "hostMessage": f"We build a {self.adjectives} app for {self.fors} that uses the power of {self.power}",
        "quit":True
      }
    else:
      d = {
        "phoneMessage": f"The idea is {self.data['idea']}.",
        "hostMessage": f"We build a {self.adjectives} app for {self.fors} that uses the power of {self.power}",
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
    
