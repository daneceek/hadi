import random

class Game :
    snakes = {16: 6, 49:11, 46:25, 62:19, 64:60, 89:68, 74:53, 99:80, 95:75, 92:88}
    ladders = {2:38, 7:14, 8:31, 15:26, 21:42, 36:44, 51:67, 78:98, 71:91, 87:94, 28:84}
    
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
                hod = random.randint(1, 6)
                while (hod % 6 == 0):
                    print("hráč č."+ str(active_player) +" hodil číslo 6. Hází tedy ještě jednou. Zmáčkněte enter.")
                    input()
                    bonus_hod = random.randint(1, 6)
                    hod += bonus_hod
                    print("hráč č." + str(active_player) + " hodil " +str(bonus_hod)+"." )
                    if bonus_hod == 6:
                        print("Nyní již nahrál " + str(hod))
                        continue
                
                self.player_dict["player" + str(active_player)] += hod
                print("hráč č." + str(active_player) + " celkově hodil " + str(hod)+"." )
                self.check_field(active_player)
                self.check_player_win(active_player, hod)
                print("nyní je na políčku č." + str(self.player_dict["player" + str(active_player)])+"\n")
                
                print(self.player_dict)
                
    def check_field(self, active_player):
        
        active_field = self.player_dict["player"+str(active_player)]
        if active_field in self.snakes:
            snake = Snake()
            snake.go_back(active_player, self.snakes[active_field])
        elif active_field in self.ladders:
            ladder = Ladder()
            ladder.go_up(active_player, self.ladders[active_field])   
            
        for index in range (1, self.number_of_players + 1):
            if (self.player_dict["player" + str(index)] == self.player_dict["player" + str(active_player)]) and (index != active_player):
                self.player_dict["player" + str(active_player)] -= 1
                if self.player_dict["player" + str(active_player)] < 0:
                    self.player_dict["player" + str(active_player)] -= 1
                print("Na políčku č." + str(self.player_dict["player" + str(index)]) + " již stojí hráč č." + str(index)+", a tedy je hráč č." + str(active_player) + " posunut na políčko č." + str(self.player_dict["player" + str(active_player)]))
                self.check_field(active_player)
                
    def check_player_win(self, active_player, hod):
        if self.player_dict["player" + str(active_player)] == 100:
            print("nyní je na políčku č.100 \n")
            exit("Hráč č." + str(active_player) + " vyhrál hru.")
        elif self.player_dict["player" + str(active_player)] > 100:
            print("hráč č." + str(active_player) + " se netrefil do cíle, zůstává tedy stát na původním políčku")
            self.player_dict["player" + str(active_player)] -= hod
             
        


class Snake():
    def go_back(self, active_player, goto_field):
        print("na tomto políčku se nachází had, který hráče č." +str(active_player) + " vrací na políčko č." + str(goto_field)+"!")
        game.player_dict["player"+str(active_player)] = goto_field
        
class Ladder():
    def go_up(self, active_player, goto_field):
        print("na tomto políčku se nachází žebřík, který hráče č." +str(active_player) + " vyzdvihne na políčko č." + str(goto_field)+"!")
        game.player_dict["player"+str(active_player)] = goto_field
        
game = Game()
game.main()