# Python test based monopoly game
import sys
import random
import time


# Board Design
BOARD = [
    {
        "name": "GO", 
        "color": "Special", 
        "price": 200, 
        "group": -1, 
        "rent": 0
    },
    {
        "name": "Old Kent Road", 
        "color": "Brown", 
        "price": 60, 
        "group": 0, 
        "rent": 2
    },
    {
        "name": "Community Chest", 
        "color": "Special", 
        "price": 0, 
        "group": -1, 
        "rent": 0
    },
    {
        "name": "Whitechapel Road", 
        "color": "Brown", 
        "price": 60, 
        "group": 0, 
        "rent": 4
    },
    {
        "name": "INCOME TAX", 
        "color": "Special", 
        "price": 200, 
        "group": -1, 
        "rent": 0
    },
    {
        "name": "King's Cross Station",
        "color": "Station",
        "price": 200,
        "group": -1,
        "rent": 25,
    },
    {
        "name": "The Angel Islington",
        "color": "Light Blue",
        "price": 100,
        "group": 1,
        "rent": 6,
    },
    {
        "name": "Chance", 
        "color": "Special", 
        "price": 0, 
        "group": -1, 
        "rent": 0
    },
    {
        "name": "Euston Road", 
        "color": "Light Blue", 
        "price": 100, 
        "group": 1, 
        "rent": 6
    },
    {
        "name": "Pentonville Road",
        "color": "Light Blue",
        "price": 120,
        "group": 1,
        "rent": 8,
    },
    {
        "name": "JAIL", 
        "color": "Special", 
        "price": 0, 
        "group": -1, 
        "rent": 0
    },
    {
        "name": "Electric Company",
        "color": "Utility",
        "price": 150,
        "group": -1,
        "rent": 0,
    },
    {
        "name": "Whitehall", 
        "color": "Pink", 
        "price": 140, 
        "group": 2, 
        "rent": 10
    },
    {
        "name": "Northumberland Avenue",
        "color": "Pink",
        "price": 140,
        "group": 2,
        "rent": 10,
    },
    {
        "name": "Marylebone Station",
        "color": "Station",
        "price": 200,
        "group": -1,
        "rent": 25,
    },
    {
        "name": "Bow Street", 
        "color": "Orange", 
        "price": 180, 
        "group": 3, 
        "rent": 12
    },
    {
        "name": "Marlborough Street",
        "color": "Orange",
        "price": 180,
        "group": 3,
        "rent": 12,
    },
    {
        "name": "Vine Street", 
        "color": "Orange", 
        "price": 200, 
        "group": 3, 
        "rent": 14
    },
    {
        "name": "FREE PARKING", 
        "color": "Special", 
        "price": 0, 
        "group": -1, 
        "rent": 0
    },
    {
        "name": "The Strand", 
        "color": "Red", 
        "price": 220, 
        "group": 4, 
        "rent": 16
    },
    {
        "name": "Chance", 
        "color": "Special", 
        "price": 0, 
        "group": -1, 
        "rent": 0
    },
    {
        "name": "Fleet Street", 
        "color": "Red", 
        "price": 220, 
        "group": 4, 
        "rent": 16
    },
    {
        "name": "Trafalgar Square", 
        "color": "Red", 
        "price": 240, 
        "group": 4, 
        "rent": 18
    },
    {
        "name": "Fenchurch St Station",
        "color": "Station",
        "price": 200,
        "group": -1,
        "rent": 25,
    },
    {
        "name": "Leicester Square",
        "color": "Yellow",
        "price": 260,
        "group": 5,
        "rent": 20,
    },
    {
        "name": "Coventry Street",
        "color": "Yellow",
        "price": 260,
        "group": 5,
        "rent": 20,
    },
    {
        "name": "Piccadilly", 
        "color": "Yellow", 
        "price": 280, 
        "group": 5, 
        "rent": 22
    },
    {
        "name": "GO TO JAIL", 
        "color": "Special", 
        "price": 0, 
        "group": -1, 
        "rent": 0
    },
    {
        "name": "Regent Street", 
        "color": "Green", 
        "price": 300, 
        "group": 6, 
        "rent": 24
    },
    {
        "name": "Oxford Street", 
        "color": "Green", 
        "price": 300, 
        "group": 6, 
        "rent": 26
    },
    {
        "name": "Bond Street", 
        "color": "Green", 
        "price": 320, 
        "group": 6, 
        "rent": 28
    },
    {
        "name": "Liverpool Street Station",
        "color": "Station",
        "price": 200,
        "group": -1,
        "rent": 25,
    },
    {
        "name": "Chance", 
        "color": "Special", 
        "price": 0, 
        "group": -1, 
        "rent": 0
    },
    {
        "name": "Park Lane", 
        "color": "Dark Blue", 
        "price": 350, 
        "group": 7, 
        "rent": 35
    },
    {
        "name": "LUXURY TAX", 
        "color": "Special", 
        "price": 100, 
        "group": -1, 
        "rent": 0
    },
    {
        "name": "Mayfair", 
        "color": "Dark Blue", 
        "price": 400, 
        "group": 7, 
        "rent": 50
    },
]

# To store sold property
SOLD = {}

# Length of the board
BOARD_LENGTH = len(BOARD)

# Color group
COLOR_GROUPS = [
    ("Brown", 0),
    ("Light Blue", 1),
    ("Pink", 2),
    ("Orange", 3),
    ("Red", 4),
    ("Yellow", 5),
    ("Green", 6),
    ("Dark Blue", 7),
]

# Community chest cards
COMMUNITY_CHEST = [
    "Pay 200",
    "Collect 400",
    "Go to jail",
    # Add more community chest cards here
]

# Chance cards
CHANCE = [
    "Go back to start",
    "Receive 500 from bank",
    # Add more chance cards here
]

# Dice
DICE = [1, 2, 3, 4, 5, 6]


# Creating the board
class Board:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent

    # moving the player
    @classmethod
    def play(self, player, number):
        print(f"\n{player.name} is rolling the dice")
        time.sleep(1)
        print(f"{player.name} got {number}.")
        time.sleep(.5)

        # Changing the player's position
        print(f"{player.name} is moving...")
        time.sleep(1)
        if player.position + number > 35:
            print(f"\nPlayer {player.name} moved all the way around.")
            print("Getting 200 from bank...")
            player.money += 200
            time.sleep(1)
            print(f"Player {player.name} money: {player.money}")
            time.sleep(.5)
        player.position = (player.position + number) % BOARD_LENGTH
        print(f"{player.name} is standing on {BOARD[player.position]['name']}")
        time.sleep(.5)

        # Sending the information to Board(class)
        Board.name = BOARD[player.position]["name"]
        Board.price = BOARD[player.position]["price"]
        Board.rent = BOARD[player.position]["rent"]

        # Checking if the property is owned by someone
        if self.name.lower() in ["community chest", "chance"]:
            chest(player, self.name)
        elif self.name.upper() in ["GO", "JAIL", "FREE PARKING", "GO TO JAIL"]:
            corner(player, self.name)
        elif self.name.lower() in ["income tax", "luxury tax"]:
            if player.money < int(BOARD[player.position]["price"]):
                print(f"You don't have enough money to pay.")
                print(f"Player {player.name} is bankrupt. Game Over!")
                raise KeyboardInterrupt
            else:
                player.money -= int(BOARD[player.position]["price"])
                print(f"Player {player.name} paid to bank - {int(BOARD[player.position]['price'])}")
                time.sleep(1)
                print(f"Player {player.name} money: {player.money}")
                time.sleep(.5)
        else:
            own = check(player, self.name)

            if own == "Noone" or own == None:
                print(f"\n{player.name}'s status:{player}")
                time.sleep(1)
                print("Bank is asking, 'Do you want to buy?'")
                time.sleep(.5)
                while True:
                    ans = input(f"Property price = {self.price} [yes/no]? ").lower()
                    if ans == "yes":
                        buy(player, self.name, self.price)
                        break
                    elif ans == "no":
                        print(f"Player {player.name} refuse to buy")
                        time.sleep(.5)
                        break
                    else:
                        print("Invalid input")
            elif own == player.name:
                print("Already Owned!!")
                time.sleep(.5)
            else:
                print(f"Owned by {own}")
                print(f"Paying rent to player {own}...")
                time.sleep(1)
                if player.money < int(self.rent):
                    print(f"You don't have enough money to pay.")
                    print(f"Player {player.name} is bankrupt. Game Over!")
                    raise KeyboardInterrupt
                player.money -= int(self.rent)


# Player's informations
class Player:
    def __init__(self, name, money=1500):
        self.name = name
        self.money = money
        self.property = []
        self.position = 0
        self.total = 0
        self.jail = 0
        self.worth = 0


    def __str__(self) -> str:
        self.information()
        return f"\nName: {self.info['name']}\nMoney: {self.info['money']}\nProperty: {self.info['property']}"

    def information(self):
        self.info = {"name": self.name, "money": self.money, "property": self.property}


def main():
    players = list(map(Player, player_input()))

    # Showing players starting information and position
    for player in players:
        print(player)
        print(f"Position: {BOARD[player.position]['name']}")
        time.sleep(.7)

    # Starting the game
    print("\nGAMING IS STARTING...")
    time.sleep(2)
    try:
        while True:
            for player in players:

                # Checking if player is in jail
                if BOARD[player.position]["name"] == "JAIL":
                    while player.jail < 3:
                        print(f"\n{player.name} is in jail.")
                        time.sleep(.3)
                        ans = input(f"Pay 500 or Skip {player.jail + 1}st turn [pay/skip]? ").lower()
                        if ans == "pay":
                            player.money -= 500
                            number = dice()
                            Board.play(player, number)
                            player.jail = 0
                            break
                        elif ans == "skip":
                            if player.jail < 3:
                                player.jail += 1
                            break
                        else:
                            print("Invalid input")

                    if player.jail > 3:
                        number = dice()
                        Board.play(player, number)
                        player.jail = 0
                    elif player.jail == 3:
                        player.jail += 1

                else:
                    number = dice()
                    Board.play(player, number)
    except KeyboardInterrupt:
        print("\n\nGAME ENDED.")
        time.sleep(.5)
        print("Calculating results...")
        time.sleep(3)
        for player in players:
            print(player)
            winner(player)
            for other in players:
                if other != player:
                    if player.total > other.total:
                        win = player.name

        print(f"\nWinner: {win}")
        time.sleep(1)
        print("\nI HOPE YOU ENJOYED.")


# Taking player's input
def player_input():
    try:
        n = int(input("No. of Players: "))
        for i in range(n):
            yield input(f"Name of Player{i + 1}: ").strip()
    except ValueError:
        sys.exit("Invalid Input.")


# No. dice is rolling
def dice():
    return random.choice(DICE)


# Checking the owner of the property
def check(p, n):
    if p.name not in SOLD:
        SOLD[p.name] = []
    for sold in SOLD:
        for land in SOLD[sold]:
            if land == n:
                return sold
    return "Noone"


# Opening the chest
def chest(player, property):
    if property == "chance":
        card = random.choice(CHANCE)
        print(f"Your card: {card}")
        time.sleep(0.5)
        if "start" in card:
            player.position = 0
            print(f"Maoving player {player.name} to GO...")
            time.sleep(1)
        elif "Receive" in card:
            player.money += int((card.split(" "))[1])
            print(f"Player {player.name} receiced  {int((card.split(' '))[1])}.")
            time.sleep(1)

    else:
        card = random.choice(COMMUNITY_CHEST)
        print(f"Your card: {card}")
        time.sleep(0.5)
        if "jail" in card:
            player.position = 10
            print(f"Moving player {player.name} to JAIL...")
            time.sleep(1)
        elif "Collect" in card:
            player.money += int((card.split(" "))[1])
            print(f"Player {player.name} gets {int((card.split(' '))[1])}.")
            time.sleep(1)
        elif "Pay" in card:
            if player.money < int((card.split(" "))[1]):
                print(f"You don't have enough money to pay.")
                print(f"Player {player.name} is bankrupt. Game Over!")
                raise KeyboardInterrupt
            player.money -= int((card.split(" "))[1])
            print(f"{player.name} pays {int((card.split(' '))[1])}.")
            time.sleep(1)


# Corner case
def corner(player, property):
    if property.lower() == "go":
        player.money += 200
        print(f"Moving the player {player.name} to GO...")
        time.sleep(1)
    elif property.lower() == "go to jail":
        player.position = 10
        print(f"Moving the player {player.name} to JAIL...")
        time.sleep(1)


# Buying the property
def buy(player, p, price):
    if player.money < price:
        print("Not enough money.")
        time.sleep(.3)
    else:
        player.money -= int(price)
        player.property.append(p)
        player.worth += price
        SOLD[player.name].append(p)
        print(f"Player {player.name} bought {p}")
        time.sleep(.5)



# Winner
def winner(player):
    player.total = player.worth + player.money


if __name__ == "__main__":
    main()
