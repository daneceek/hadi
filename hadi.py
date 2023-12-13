import random

class Game :
    snakes = {16: 6, 49:11, 46:25, 62:19, 64:60, 89:68, 74:53, 99:80, 95:75, 92:88}
    
    
    def set_number_of_players(self):
        self.number_of_players = int(input("Zadejte počet hráčů: "))
        self.player_dict = dict()
        for player in range(1, self.number_of_players + 1):
            self.player_dict["player" + str(player)]  = 0
        
    def main(self):
        self.set_number_of_players()
        while True:
            for active_player in range(1, self.number_of_players + 1):
                print("nyní hází kostkou hráč č." + str(active_player) + ". Stiskněte enter pro hod kostkou.\n")
                input()
                hod = random.randint(1, 7)
                while (hod % 6 == 0):
                    print("hráč č."+ str(active_player) +" hodil číslo 6. Hází tedy ještě jednou. Zmáčkněte enter.")
                    input()
                    bonus_hod = random.randint(1, 7)
                    print("hráč č." + str(active_player) + " hodil " + str(bonus_hod)+" | 6 + "+ str(bonus_hod)+f" = {6 + int(bonus_hod)}" )
                    hod += bonus_hod
                self.player_dict["player" + str(active_player)] += hod
                self.check_field(active_player)
                print("hráč č." + str(active_player) + " hodil " + str(hod)+".")
                print("nyní je na políčku č." + str(self.player_dict["player" + str(active_player)])+"\n")
            
    def check_field(self, active_player):
        active_field = self.player_dict["player"+str(active_player)]
        
        if active_field in self.snakes:
            snake = Snake()
            snake.go_back(active_player, self.snakes[active_field])


class Snake(Game):
    
    def go_back(self, active_player, goto_field):
        game.player_dict["player"+str(active_player)] = goto_field
        

game = Game()
game.main()