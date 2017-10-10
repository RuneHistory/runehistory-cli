import requests


def get(player):
    # http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player=Hess
    response = requests.get('http://services.runescape.com/m=hiscore_oldschool/index_lite.ws', {
        'player': player
    })
    return parse_response(response.content)


def parse_response(response):
    return response
