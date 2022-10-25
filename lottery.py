from random import randint

selection = [
    [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    ['A', 'R', 'I', 'S', 'T']
]

class Lottery:
    def __init__(self, selection):
        self.selection = selection
        self.winner = []
    
    def make_winner(self):
        winner = []
        
        for i in range(4):
            x = randint(0, len(self.selection) - 1)
            y = randint(0, len(self.selection[x]) - 1)
            winner.append(self.selection[x][y])
            
        self.winner = winner    
        return winner
            
            
sample_lottery = Lottery(selection)
print(sample_lottery.make_winner())

my_ticket = ['S', 'T', 25, 30]

count = 0
while sample_lottery.winner != my_ticket:
    sample_lottery.make_winner()
    count += 1
    print("It took {count} tries before I won".format(count = count))