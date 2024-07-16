from flask import Flask, render_template, request
import random

app = Flask(__name__)

choices = ['rock', 'paper', 'scissors']
outcomes = {
    'rock': {'rock': 'tie', 'paper': 'lose', 'scissors': 'win'},
    'paper': {'rock': 'win', 'paper': 'tie', 'scissors': 'lose'},
    'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'tie'}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    computer_choice = random.choice(choices)
    outcome = outcomes[user_choice][computer_choice]
    return render_template('index.html', user_choice=user_choice, computer_choice=computer_choice, outcome=outcome)

if __name__ == '__main__':
    app.run(debug=True)
