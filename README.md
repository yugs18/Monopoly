# Monopoly
    #### Video Demo:  <URL HERE>
    #### Description:

## Introduction ##
    Welcome to the world of Monopoly! In this game, players take on the role of business and try to acquire all the properties and build houses and hotel.

    This is a text-base version of "Monopoly". This is a basic version of actual game, not all the functionalities are there.
    The game can  be played by one or more players. Each player gets 1500 at the start. 
    Players roll one dice to determine how many spaces they move on the board, and then another die to land on a property. 
    If they land on a ownerless property, they can buy that property.
    If the land already have an owner, they have to pay the rent to the owner.

    There are many more things... 



### Code Explanation ###
        Modules I imported are:
        sys
        time
        random

        Global variable:
        BOARD: It contains the design of the monopoly board. It is a list of dictionary where each dictionary have five keys, namely, 'name', 'color', 'price', 'group' 'rent'.
        They store the information about the properties and other things according to monopoly board.

        SOLD: It will store the sold properties. It is dictionary which will have name of the player as a key and that key will be a list which will store the name of the properties that player bought.

        BOARD_LENGTH: It stores the lenght of the board which is 36.

        COLOR_GROUPS: It is a list of turples. Each tuple has two elements, first, the name of the color and second, the group number of that color. [I have not use this global variable at this moment but if I want to implement more functions and all, this will be very helpful]

        COMMUNITY_CHEST: It is a list of cards. Each card have a description saying to the player what to do. [At this moment, there are only 3 cards.]

        CHANCE: It also same as COMMUNITY_CHEST. It is a list of cards where each card says what to do to the player. [At this moment, there are 2 cards]

        DICE: It is list number from one to six, just like the dice in real life game.

        
        Classes:
        There are two classes, Board and Player.
        Board: It's main function is to moniter the flow of the game. There is a class method "play" which takes two arguments, player's information and the number that the player got after rolling the dice. It moves the player that many steps and depending on where player landed, it calls certain function or do some workings.

        Player: It's job is to store the players informations and return it.


        Functions:
        main: Here, we creates an object and starts the game. 
            1- We create a player using Player class.
            2- Then we roll the dice for each player until all players pass GO or bankruptcy.
            3- If any player passes GO then he/she collects $200.
            4- After that, each player can buy property if he has enough money.
                   - He buys the first available property on his turn.
            5- Whenever a player lands on a property owned by someone else, he pays the rent to the owner.
               (If he doesn't have enough money, he goes bankrupt)
            6- The game continues until first player goes bankrupt or game is interrupted.

            If any player lands on jail or go to jail, either he have to pay 500 or have to skip his turn up to 3 times.

        player_input: Takes the name of the player and yield to Player class.

        dice: returns a random choice from the DICE list.

        check: It checks if the property is already owned by someone or not.

        chest: It checks the cards of COMMUNITY_CHEST and CHANCE and takes action accordingly.

        corner: Takes care of corner cases of the board, GO and GO TO JAIL.

        buy: Complete the transaction between bank and buyer.

        winner: returns the total of a player.