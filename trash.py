def Open(user):
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
            "trash": 0

        }
    saves(users)