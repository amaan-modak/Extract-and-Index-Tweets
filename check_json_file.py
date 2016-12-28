import json
with open ('USElection-en.json') as f:
	for line in f:
		data = json.loads(line)