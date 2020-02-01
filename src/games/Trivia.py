import pandas as pd
from urllib.parse import unquote
from random import shuffle

from games.GameHandler import GameHandler


class Trivia(GameHandler):
  def start(self):
    self.stages = {}
    for i in range(int(self.data["numRounds"])):
      self.stages[i + 1] = self.getVotes

    self.stages[len(self.stages) + 1] = self.end

    self.data["votes"]  = {}
    self.data["scores"]  = {}

    self.get_questions()

    self.data["question_num"] = 0
    
  def get_info(self, username):
    d = self.game_state
    if self.currentStage == 0:
      d.update({'waiting_for_players':True})
      return d
    if len(self.data["votes"]) >= len(self.players):
      self.update_scores()
      self.data["votes"] = {}
      self.currentStage += 1
      self.data['question_num'] += 1
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

  def get_questions(self):
    q_dict = requests.get(
      "https://opentdb.com/api.php?amount=3&difficulty=medium"
    ).json()["results"]

    self.data["questions"] = list(map(
      lambda q : {
        "question": unquote(
          q["question"]
        ),
        "correct": unquote(q["correct_answer"]),
        "answer_choices": (
          [unquote(q["correct_answer"])] + [unquote(j) for j in q["incorrect_answers"]]
        )
      },
      q_dict
    ))
    for x in self.data["questions"]:
      shuffle(x["answer_choices"])
    return None
