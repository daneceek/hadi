import random

class Game :
    fields = [1, "zebrik", 3, 4, 5, 6, "zebrik", 8, 9, 10, 11, 12, 13, 14, "zebrik", "had", 17, 18, 19]
    
    
    def set_number_of_players(self):
        self.number_of_players = int(input("Zadejte počet hráčů: "))
        self.player_dict = dict()
        for player in range(1, self.number_of_players + 1):
            self.player_dict["player" + str(player)]  = 0
        
    def main(self):
        self.set_number_of_players()
        # while True:
        for active_player in range(1, self.number_of_players + 1):
            print("nyní hází kostkou hráč č." + str(active_player) + ". Stiskněte enter pro hod kostkou.\n")
            input()
            self.hod = random.randint(1, 7)
            while (self.hod % 6 == 0):
                print("hráč č."+ str(active_player) +" hodil číslo 6. Hází tedy ještě jednou. Zmáčkněte enter.\n")
                self.hod += random.randint(1, 7)
            self.player_dict["player" + str(active_player)] += self.hod
            self.check_field(active_player)
            print("hráč č." + str(active_player) + " hodil " + str(self.hod)+".")
          
    def check_field(self, active_player):
        active_field = self.player_dict["player"+str(active_player)]
        
        if self.fields[active_field - 1] == "had":
            pass


class Snake:
    def __init__(self, goto_field):
        self.goto_field = goto_field


game = Game()
game.main()