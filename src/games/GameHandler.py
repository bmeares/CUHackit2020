import pandas as pd
import pandasql as psql
import sqlalchemy 
from urllib.parse import unquote
from random import shuffle

class GameHandler:
  def __init__(self, engine, key, data):
    self.stages = {}
    self.players = {}
    self.max_players = 8
    self.data = data
    self.engine = engine
    self.currentStage = 0
    self.key = key

    self.start()

  def add_player(self, username):
    if self.currentStage == 0 and len(self.players) < self.max_players:
      self.players[username] = True
      return True
    return False

  def start(self):
    return None

  def end(self):
    return None

  @property
  def game_state(self):
    return {
      "players": len(self.players),
      "key": self.key,
    }
