import time         # For delay
import collections  # For deque
import random       # For computer
import typing       # For documentation
import copy

class Robot :
    id : int
    name : str
    health : int
    power : int
    
    def __init__(self, id: int, name: str, health: int, power: int) :
        self.id = id
        self.name = name
        self.health = health
        self.power = power
    
    def takeDamage(self, damage: int) :
        self.health -= damage

    def attack(self, enemy: "Robot") :
            print(f"{self.name} attacks {enemy.name} for {self.power} damages!")
            time.sleep(0.5)
            enemy.takeDamage(self.power)
            print(f"{enemy.name}'s remaining health: {enemy.health}")
            time.sleep(1.0)

Robots = [
    Robot(1, "Alpha",   1, 10),
    Robot(2, "Beta",    5, 6),
    Robot(3, "Gamma",   4, 7),
    Robot(4, "Delta",   3, 8),
    Robot(5, "Epsilon", 8, 3),
    Robot(6, "Zeta",    9, 2),
    Robot(7, "Eta",    10, 1),
    Robot(8, "Theta",   6, 5),
    Robot(9, "Iota",    7, 4),
    Robot(10, "Kappa",  2, 9)
]

class Player : 
    name : str
    team : typing.Deque[Robot] = collections.deque()
    score : int

    def __init__(self, name: str) :
        if name == "Computer" : 
            self.name = name
        else :
            while True :
                self.name = input("Enter your name: ").strip() 
                if self.name : 
                    break
                else :
                    print("Name cannot be empty. Please try again.")
            print(f"Welcome, {self.name}!")
        self.team = collections.deque()
        self.score = 0
    
    def update(self) :
        if self.team and self.team[0].health <= 0 :
            self.team.popleft()
            if self.team :
                return True
            else :
                return False
        else :
            return False


    def showTime(self) :
        print(f"\n{self.name}'s Team:")
        time.sleep(0.5)
        for robot in self.team :
            print(f"{robot.name}: H = {robot.health}, P = {robot.power}")
            time.sleep(0.25)
        time.sleep(1.0)
        print("")

class Battle :
    robot1 : Robot
    robot2 : Robot

    def __init__(self, r1: Robot, r2: Robot) :
        self.robot1 = r1
        self.robot2 = r2

    def fight(self) :
        time.sleep(0.5)
        print(f"\nStart Battle {self.robot1.name} vs {self.robot2.name}!")
        time.sleep(0.25)
        while (self.robot1.health > 0 and self.robot2.health > 0) :
            self.robot1.attack(self.robot2)
            self.robot2.attack(self.robot1)
            if (self.robot1.health <= 0 and self.robot2.health > 0) :
                print(f"{self.robot1.name} has been defeated!")    
                return [True, False]
            elif (self.robot2.health <= 0 and self.robot1.health > 0) :
                print(f"{self.robot2.name} has been defeated!")
                return [False, True]
        else :
                print(f"Both {self.robot1.name} and {self.robot2.name} have been defeated!")
                return [True, True]

class Game :
    mode : str

    def __init__(self):
        print("\n--------------------------------")
        time.sleep(0.5)
        print("Welcome to the Battle of Robots!")
        time.sleep(0.5)
        print("--------------------------------\n")
        time.sleep(1.5)

        print("Select Mode:")
        time.sleep(0.25)
        print("[P] Player vs Player")
        time.sleep(0.25)
        print("[C] Play Against Computer")
        time.sleep(0.25)

        gameMode = input("Select: ")
        while(True) :
            if (gameMode == "P" or gameMode == "C") :
                self.mode = gameMode
                if (gameMode == "P") :
                    print("You chose PvP Mode!\n")
                else :
                    print("You chose to Play Against Computer!\n")

                break
            else :
                gameMode = input("Invalid Input! Try again: ")
        time.sleep(1.0)

    def showOptions(self) :
        print("\nAvailable Robots:")
        time.sleep(0.5)
        for i in range(10) :
            print(f"[{i+1}] {Robots[i].name}: Health = {Robots[i].health} | Power = {Robots[i].power}")
            time.sleep(0.25)
        print("")
    
    def choose(self, user: Player) :
        selected = set()
        print("Choose 4 different robots!")
        for i in range(4) :
            while True :
                try :
                    choice = int(input(f"Robot {i+1}: "))
                    if ((0 < choice < 11) and (choice not in selected)) :
                        user.team.append(copy.deepcopy(Robots[choice - 1]))
                        selected.add(choice)
                        break
                    else : 
                        print("Invalid input! Either out of range or already selected. Please select again.")
                except ValueError :
                    print("Invalid input! Please enter a number.")

    def startBattle(self, p1: Player, p2: Player) :
        while p1.team and p2.team :
            currentBattle = Battle(p1.team[0], p2.team[0])
            result = currentBattle.fight()
            p1.score += int(result[0])
            p2.score += int(result[1])
            p1.update()
            p2.update()

        self.checkWinner(p1, p2)
    
    def checkWinner(self, p1: Player, p2: Player) :
        time.sleep(1.0)
        print("\n+--------------+")
        print(  "|  GAME OVER!  |")
        print(  "+--------------+\n")
        time.sleep(1.0)
        if (not len(p1.team) and len(p2.team)) :
            print(f"{p2.name} WINS WITH SCORE: {p2.score*100}\n")
        elif (len(p1.team) and not len(p2.team)) :
            print(f"{p1.name} WINS WITH SCORE: {p2.score*100}\n")
        else :
            print("IT'S A DRAW\n")
        time.sleep(1.0)
        print("+------------------------+")
        print("| Thank you for playing! |")
        print("+------------------------+\n")

### End of Classes Definiton

newGame = Game()
if (newGame.mode == "P") :
    print("Initializing Player 1...")

player1 = Player("")
newGame.showOptions()
newGame.choose(player1)
player1.showTime()

if (newGame.mode == "P") :
    print("Initializing Player 2...")
    player2 = Player("")
    newGame.showOptions()
    newGame.choose(player2)
    player2.showTime()
else :
    player2 = Player("Computer")
    setRobot = set()
    while (len(player2.team) < 4) :
        rand = random.randint(0, 9)
        if (rand not in setRobot) :
            player2.team.append(Robots[rand])
            setRobot.add(rand)
    player2.showTime()

newGame.startBattle(player1, player2)

exit()