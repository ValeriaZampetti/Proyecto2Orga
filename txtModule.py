import json


def writeDatabase(db: list):
    with open("database.json", "w") as file:
        json.dump(db, file, indent=4)
        print("Database saved")


def readDatabase() -> list:
    with open("database.json") as file:
        if file.read() == "":
            return []
        db = json.loads(file)
        print(db)
    return db
