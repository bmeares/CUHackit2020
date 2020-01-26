from flask import Flask, session, redirect, url_for, escape, request
import pandas as pd
import sqlalchemy 

app = Flask(__name__)
engine = sqlalchemy.create_engine('mysql://cuhackit2020:gurgle@inscribe.productions/hackbox_db')

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

return trivia.stages[trivia.currentState](stuff)

class Game:
  def __init__(self, engine):
    self.stages = {}
    self.players = {}
    self.max_players = 8
    self.data = {}
    self.engine = engine
    self.currentStage = 0

    self.start()

  @property
  def game_state(self):
    return {
      "players": len(self.players),
    }

  def add_player(self, request):
    if self.currentStage == 0 and len(self.players) < self.max_players:
      self.players[request["player"]] = True
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
    }


class Trivia(Game):
  def start(self):
    self.stages = {
      1: self.getVotes,
      2: self.end
    }
  
    questions = pd.read_sql("SELECT TOP 3 * FROM TRIVIA_ALL ORDER_BY_RAND()", self.engine)

    self.data["questions"] = map(
      lambda q : {
        "question": q[1]["Question"],
        "correct": q[1]["Correct Answer"],
        "incorrect": q[1]["Incorrect Answer"].split(";"),
      },
      questions.iterrows()
    )
    self.data["question_num"] = 0

  def get_info(self, request):
    d = game_state
    if self.currentStage == 0:
      return game_state
    if len(self.data["votes"]) >= len(self.players):
      self.update_scores()
      self.data["votes"] = []
      self.currentStage += 1
    d.update(self.stages[self.currentStage](request))
    return d

  def post_info(self, request):
    if self.currentStage == 0:
      self.currentStage += 1
      return True
    if request["player"] not in self.data["votes"]:
      self.data["votes"][request["player"]] = request["body"]["vote"]
      return True
    return False

  def update_scores(self):
    for player, answer in self.data["votes"].items():
      if answer == self.data["questions"][self.data["question_num"]]["correct"]:
        self.data["score"][player] = self.data["score"].get(player, 0) + self.data["question_num"] + 1
    return None

  def getVotes(self, request):
    d = {
      "message": self.data["questions"][self.data["question_num"]]["question"],
      "buttons": (
        [self.data["questions"][self.data["question_num"]]["correct"]] +
        self.data["questions"][self.data["question_num"]]["incorrect"]
      ),
    }
    return d

  def end(self, request):
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
    
  def generateQuestions(self):
     return

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
      pass
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
