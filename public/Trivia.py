import pandas as pd
import sqlalchemy 
from urllib.parse import unquote
from random import shuffle

class Game:
  def __init__(self, engine, key):
    self.stages = {}
    self.players = {}
    self.max_players = 8
    self.data = {}
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


class Trivia(Game):
  def start(self):
    self.stages = {
      1: self.getVotes,
      2: self.end
    }
    self.data["votes"]  = {}
    self.data["scores"]  = {}
    questions = pd.read_sql("""
        SELECT question, correct_answer, incorrect_answers
        FROM Trivia_questions
        ORDER BY RAND() LIMIT 3""",
        self.engine)

    self.data["questions"] = list(map(
      lambda q : {
        "question": unquote(q[1]["question"]),
        "correct": unquote(q[1]["correct_answer"]),
        "incorrect": unquote(q[1]["incorrect_answers"]).split(";"),
      },
      questions.iterrows()
    ))
    self.data["question_num"] = 0

  def get_info(self, username):
    d = self.game_state
    if self.currentStage == 0:
      d.update({'waiting_for_players':True})
      return d
    if len(self.data["votes"]) >= len(self.players):
      self.update_scores()
      self.data["votes"] = []
      self.currentStage += 1
    d.update(self.stages[self.currentStage](username))
    return d

  def post_info(self, data : dict, username):
    if self.currentStage == 0:
      for player in self.players: self.data['scores'][player] = 0
      self.currentStage += 1
      return True
    if username not in self.data["votes"]:
      self.data["votes"][username] = data["buttonText"]
      return True
    return False

  def update_scores(self):
    for player, answer in self.data["votes"].items():
      if answer == self.data["questions"][self.data["question_num"]]["correct"]:
        self.data["scores"][player] = self.data["scores"].get(player, 0) + self.data["question_num"] + 1
    return None

  def getVotes(self, username):
    if "all_buttons" not in self.data:
      all_buttons = (
          [self.data["questions"][self.data["question_num"]]["correct"]] +
          self.data["questions"][self.data["question_num"]]["incorrect"]
      )
      shuffle(all_buttons)
      self.data["all_buttons"] = all_buttons

    d = {
      "message": self.data["questions"][self.data["question_num"]]["question"],
      "buttons": self.data['all_buttons'],
    }
    return d

  def end(self, username):
    d = {
      "message": "WINNER: {0}".format(
        max(
          self.data["scores"].items(),
          key=(lambda x: x[1])
        )[0]
      ),
      "table": self.data["scores"],
      "currentStage": self.currentStage,
    }
    return d
    
  def generateQuestions(self):
     return

