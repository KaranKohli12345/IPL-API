from flask import Flask, jsonify, request
import IPL
from jugaad import teamAPI, batsmanAPI, bowlerAPI

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hi'

# API # 1
@app.route('/api/teams')
def teams():
    teams = IPL.teamsAPI()
    return jsonify(teams)

# API # 2
@app.route('/api/teamVsTeam')
def teamVsTeam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = IPL.teamVsTeamFunction(team1, team2)
    return jsonify(response)

# API # 3
@app.route('/api/team-record')
def team_record():
    team = request.args.get('team')
    response = teamAPI(team)
    return response

# API # 4
@app.route('/api/batter-record')
def batter_record():
    batsman = request.args.get('batsman')
    response = batsmanAPI(batsman)
    return response

# API # 5
@app.route('/api/bowler-record')
def bowler_record():
    bowler = request.args.get('bowler')
    response = bowlerAPI(bowler)
    return response

# API # 6
# @app.route('')
# def team

app.run(debug=True)
