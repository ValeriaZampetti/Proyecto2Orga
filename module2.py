def searchByModel(db: list, model: str) -> dict:
    for game in db:
        if game["modelo"] == model:
            return game
    return {}


def searchByTitle(db: list, title: str) -> dict:
    for game in db:
        if game["titulo"] == title:
            return game
    return {}
