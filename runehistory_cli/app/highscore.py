import typing

from runehistory_core.domain.models.account import Account
from runehistory_core.domain.models.highscore import HighScore, Skill, SKILLS

from runehistory_cli.app import api


def get(account: Account) -> HighScore:
    highscore = HighScore(account.id)
    skills = parse_response(api.get_raw_highscores(account.nickname))
    for name, skill in skills.items():
        setattr(highscore, name, skill)
    return highscore


def parse_response(data: str) -> typing.Dict:
    split_skills = data.split('\n')
    skills = {}
    for index, skill_name in enumerate(SKILLS):
        rank, level, experience = split_skills[index].split(',')
        skill = Skill(rank, level, experience)
        skills[skill_name] = skill
    return skills
