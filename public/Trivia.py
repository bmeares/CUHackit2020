import pandas as pd
import sqlalchemy 
from urllib.parse import unquote
from random import shuffle

class Game:
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


class Trivia(Game):
  def start(self):
    self.stages = {}
    for i in range(int(self.data["numRounds"])):
      self.stages[i + 1] = self.getVotes

    self.stages[len(self.stages) + 1] = self.end

    self.data["votes"]  = {}
    self.data["scores"]  = {}
    questions = pd.read_sql(f"""
        SELECT question, correct_answer, incorrect_answers
        FROM Trivia_questions
        ORDER BY RAND() LIMIT {self.data['numRounds']}""",
        self.engine)

    self.data["questions"] = list(map(
      lambda q : {
        "question": unquote(q[1]["question"]),
        "correct": unquote(q[1]["correct_answer"]),
        "answer_choices": ([q[1]["correct_answer"]] + q[1]["incorrect_answers"].split(';'))
      },
      questions.iterrows()
    ))
    for rnd in self.data["questions"]:
        shuffle(rnd["answer_choices"])
    self.data["question_num"] = 0
    print(self.data)
    
  def get_info(self, username):
    d = self.game_state
    if self.currentStage == 0:
      d.update({'waiting_for_players':True})
      return d
    print('votes:',self.data["votes"])
    if len(self.data["votes"]) >= len(self.players):
      self.update_scores()
      self.data["votes"] = {}
      self.currentStage += 1
      self.data['question_num'] += 1
      #  del self.data['all_buttons']
      print('next stage')
    d.update(self.stages[self.currentStage](username))
    return d

  def post_info(self, data : dict, username):
    print('self.data:',self.data)
    print('data:',data)
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
        self.data["scores"][player] = self.data["scores"].get(player, 0) + 1
    return None

  def getVotes(self, username):
    d = {
      "phoneMessage": self.data["questions"][self.data["question_num"]]["question"],
      "hostMessage": self.data["questions"][self.data["question_num"]]["question"],
      "buttons": self.data["questions"][self.data["question_num"]]["answer_choices"],
      "currentStage": self.currentStage,
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
