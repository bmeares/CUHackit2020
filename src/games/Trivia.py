import pandas as pd
import pandasql as psql
from urllib.parse import unquote
from random import shuffle

from .GameHandler import GameHandler


class Trivia(GameHandler):
  def start(self):
    self.stages = {}
    for i in range(int(self.data["numRounds"])):
      self.stages[i + 1] = self.getVotes

    self.stages[len(self.stages) + 1] = self.end

    self.data["votes"]  = {}
    self.data["scores"]  = {}
    #  self.all_questions = pd.read_csv('questions.csv')
    query = f"""
        SELECT question, correct_answer, incorrect_answers
        FROM Trivia_questions
        ORDER BY RAND() LIMIT {self.data['numRounds']}"""
    
    questions = pd.read_sql(query, self.engine)

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
    #  print(self.data)
    
  def get_info(self, username):
    d = self.game_state
    if self.currentStage == 0:
      d.update({'waiting_for_players':True})
      return d
    #  print('votes:',self.data["votes"])
    if len(self.data["votes"]) >= len(self.players):
      self.update_scores()
      self.data["votes"] = {}
      self.currentStage += 1
      self.data['question_num'] += 1
      #  del self.data['all_buttons']
      #  print('next stage')
    d.update(self.stages[self.currentStage](username))
    return d

  def post_info(self, data : dict, username):
    #  print('self.data:',self.data)
    #  print('data:',data)
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
