import typing
from datetime import datetime

from pyrunehistory.domain.models.highscore import HighScore as RHHighScore,\
    Skill as RHSkill

SKILLS = ['overall', 'attack', 'defence', 'strength', 'hitpoints',
          'ranged', 'prayer', 'magic', 'cooking', 'woodcutting',
          'fletching', 'fishing', 'firemaking', 'crafting', 'smithing',
          'mining', 'herblore', 'agility', 'theiving', 'slayer',
          'farming', 'hunter']


class Skill(RHSkill):
    pass


class HighScore(RHHighScore):
    def __init__(self, account_id: str,
                 created_at: datetime, skills: typing.Dict[str, Skill],
                 id: str = None):
        super().__init__(account_id, id, created_at, skills)


def to_skills(skills: typing.Dict[str, dict]):
    return {
        name: Skill(**skill)
        for name, skill in skills.items()
    }
