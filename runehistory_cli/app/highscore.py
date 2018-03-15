import typing
from datetime import datetime
import requests

from pyrunehistory.domain.models.account import Account

from runehistory_cli.domain.models.highscore import HighScore, Skill, SKILLS


def get_raw_highscores(player: str) -> str:
    response = requests.get(
        'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws', {
            'player': player
        })
    response.raise_for_status()
    return response.content.decode('utf-8')


def get(account: Account) -> HighScore:
    raw_skills = get_raw_highscores(account.nickname)
    skills = parse_response(raw_skills)
    highscore = HighScore(account.id, datetime.utcnow(), skills)
    return highscore


def parse_response(data: str) -> typing.Dict[str, Skill]:
    split_skills = data.split('\n')
    skills = {}
    for index, skill_name in enumerate(SKILLS):
        rank, level, experience = split_skills[index].split(',')
        skill = Skill(rank, level, experience)
        skills[skill_name] = skill
    return skills
