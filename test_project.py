from project.project import BOARD, SOLD, Player, check, dice, buy, winner
import pytest

def test_board():
    assert len(BOARD) == 36

def test_player():
    player = Player("John")
    assert isinstance(player, Player)
    assert player.name == "John"
    assert player.money == 1500
    assert player.property == []
    assert player.position == 0
    assert player.total == 0
    assert player.jail == 0
    assert player.worth == 0

def test_check():
    player = Player("John")
    assert check(player, "Old Kent Road") == "Noone"
    SOLD["John"] = ["Old Kent Road"]
    assert check(player, "Old Kent Road") == "John"

def test_dice():
    assert 1 <= dice() <= 6

def test_buy():
    player = Player("John")
    board = BOARD[1]
    buy(player, board, board["price"])
    assert board in player.property
    assert player.money == 1440
    assert player.worth == 60

def test_winner():
    player = Player("John")
    player.money = 1000
    player.worth = 500
    winner(player)
    assert player.total == 1500
