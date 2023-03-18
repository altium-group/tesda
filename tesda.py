import json

def Opens(user):
    users = datas()
    if str(user.id) in users:
        return
    else:
        users[str(user.id)] = {
            "bank": 150,
            "msg": 0,
            "xp": 0,
            "lvl": 0,
            "warn": 0,
            "power": 0,
            "bounty": 0,
            "gold": 0,
            "copper": 0,
            "steel": 0,
            "tin": 0,
            "food": 0,
            "trash": 0,
        }
        saves(users)


def datas():
    with open("tesda.json", "r") as f:
        users = json.load(f)
    return users


def saves(users):
    with open("tesda.json", "w") as f:
        json.dump(users, f)


def cooldConvert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%dh %02dm %02ds" % (hour, minutes, seconds)


def isOwner(ctx):
    return ctx.message.author.id == 439743312413458432
