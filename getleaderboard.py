import requests
import constants

s = requests.Session()
cookie = constants.sessionCookie
resp = s.get('https://adventofcode.com/2022/leaderboard/private/view/2306847.json',cookies={'session': cookie}, headers={'User-Agent': 'https://github.com/jnchaba/'})

data = resp.json()

members = data['members'].items()
array = []
for key, value in members:
	array.append({ 'name': value['name'], 'score': value['local_score']})

sortedScores = sorted(array, key = lambda x : x['score'], reverse=True)
output = dict()
for i in range(len(sortedScores)):
	print(sortedScores[i])
	output[str(i+1)] = sortedScores[i]