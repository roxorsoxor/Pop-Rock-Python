import json

with open('data/AliceCooperBand_021519.json', 'r') as f:
    data = f.read()

artist2 = json.loads(data)


def openData(rockdata):
    with open(rockdata, 'r') as f:
        data = f.read()
    artist3 = json.loads(data)
    return artist3
