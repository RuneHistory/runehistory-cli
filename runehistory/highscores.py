import requests


SKILLS_ORDER = ['overall', 'attack', 'defence', 'strength', 'hitpoints', 'ranged',
              'prayer', 'magic', 'cooking', 'woodcutting', 'fletching',
              'fishing', 'firemaking', 'crafting', 'smithing', 'mining',
              'herblore', 'agility', 'theiving', 'slayer', 'farming', 'hunter']


def get(player):
    """
    Args:
        player (str): Player name to lookup

    Returns:
        HighScores
    """
    response = requests.get('http://services.runescape.com/m=hiscore_oldschool/index_lite.ws', {
        'player': player
    })
    return parse_response(response.content.decode('utf-8'))


def parse_response(data):
    """
    Parse the response from the API call into an object
    Args:
        data (str): Data from runescape highscores API

    Returns:
        HighScores
    """
    split_skills = data.split('\n')
    highscores = HighScores()

    for index, skill_name in enumerate(SKILLS_ORDER):
        rank, level, experience = split_skills[index].split(',')
        skill = Skill(skill_name, rank, level, experience)
        setattr(highscores, skill.name, skill)
    return highscores


class Skill:
    def __init__(self, name, rank, level, experience):
        """
        Args: Skill name
            rank (int):
            level (int):
            experience (int):
        """
        self.name = name
        self.rank = rank
        self.level = level
        self.experience = experience


class HighScores(dict):
    def __init__(self, **kwargs):
        """
        Args:
            **kwargs (dict of str: Skill):
        """
        for skill in kwargs.keys():
            if skill not in SKILLS_ORDER:
                raise AttributeError('{key} is not a valid skill'.format(key=skill))
        super(HighScores, self).__init__(**kwargs)

    def __setattr__(self, key, value):
        if key not in SKILLS_ORDER:
            raise AttributeError('{key} is not a valid skill'.format(key=key))
        self[key] = value

    def __getattr__(self, item):
        if item not in SKILLS_ORDER:
            raise AttributeError('{key} is not a valid skill'.format(key=item))
        return self[item]
