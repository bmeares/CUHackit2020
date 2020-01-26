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
    self.data = {}
    self.engine = engine
    self.currentStage = 0

    start()

  def 

  def start(self):
    return None

  def end(self):
    return None

class TriviaLiesGame(Game):
  def start(self):
    self.stages = {
      0: self.,
      1: self.getAnswers,
      2: self.getVotes,
      3: self.end 
  
      questions = pd.read_sql("SELECT TOP 3 * FROM TRIVIA_ALL ORDER_BY_RAND()", self.engine)

      self.data["questions"] = map(lambda q : {
        "question": q[1]["Question"],
        "correct": q[1]["Correct Answer"],
        "incorrect": q[1]["Incorrect Answer"].split(";")
      }, questions.iterrows()) 
     }
    
  def generateQuestions(self):
     

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
