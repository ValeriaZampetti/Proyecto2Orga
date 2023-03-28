from main import *

# Create a txt file
def createDataBase():
    with open("database.txt", "w") as file:
        file.write("")
        print("File created")

# Read the txt file and return a list
def readDataBase():
    with open("database.txt", "r") as file:
        data = file.readlines()
        return data 
