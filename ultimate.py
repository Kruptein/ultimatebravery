import json
import random
import shutil

import rawpi

__author__ = 'Kruptein'


def update_items():
    with open('config', 'r') as f:
        key = json.load(f)['key']

    shutil.copy('items.txt', 'items.txt.old')
    with open("items.txt", 'w') as f:
        json.dump(rawpi.get_item_list(key, 'euw', itemListData='all').json(), f, indent=4)


def load_items(path="items.txt"):
    with open(path) as f:
        items = json.load(f)
    return items["data"]


def filter_items(_i):
    items = []

    for item in _i:
        if not _i[item]["maps"]['11']:
            continue
        if not _i[item]["gold"]["purchasable"]:
            continue
        if _i[item]["gold"]["total"] < 1000:
            continue
        items.append(_i[item]["name"])
    return items


ITEMS = filter_items(load_items())
#  ITEMS = load_items()
SUMMONERS = [
    "heal",
    "ghost",
    "exhaust",
    "barrier",
    "cleanse",
    "teleport",
    "flash",
    "ignite",
    "smite"
]


def get_item():
    return random.choice(list(ITEMS))


def get_skills(count=18):
    skills = []
    while len(skills) != count:
        skill = get_skill()
        if skills.count(skill) >= 5:
            continue
        if skills.count(skill) >= 3 and skill == "r":
            continue
        if len(skills) == 1 and skill == skills[0]:
            continue
        if skills.count('r') == 0 and len(skills) < 5 and skill == "r":
            continue
        if skills.count('r') == 1 and len(skills) < 10 and skill == "r":
            continue
        if skills.count('r') == 2 and len(skills) < 15 and skill == "r":
            continue
        skills.append(skill)
    return {i+1: skills[i] for i in range(count)}


def get_skill():
    return random.choice(["q", "w", "e", "r"])


def get_summoner():
    return random.choice(SUMMONERS)
