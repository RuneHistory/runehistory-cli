import requests


def get(player):
    # http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player=Hess
    response = requests.get('http://services.runescape.com/m=hiscore_oldschool/index_lite.ws', {
        'player': player
    })
    return parse_response(response.content.decode('utf-8'))


def parse_response(response):
    skills_order = ['overall', 'attack', 'defence', 'strength', 'hitpoints', 'ranged'
              'prayer', 'magic', 'cooking', 'woodcutting', 'fletching',
              'fishing', 'firemaking', 'crafting', 'smithing', 'mining',
              'herblore', 'agility', 'theiving', 'slayer', 'farming', 'hunter']
    split_skills = response.split('\n')
    skill_objects = []
    for index, skill in enumerate(skills_order):
        rank, level, experience = split_skills[index].split(',')
        skill_objects.append(Skill(skill, rank, level, experience))
    return dict(zip(skills_order, skill_objects))


class Skill:
    def __init__(self, name, rank, level, experience):
        self.name = name
        self.rank = rank
        self.level = level
        self.experience = experience

    def __repr__(self):
        return str(self.__dict__)
