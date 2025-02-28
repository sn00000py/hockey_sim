class team:
    def __init__(self, points):
        self.points = points

    def game(self, result):
        outcomes = ['win', 'loss', 'tie', 'ot_loss']
        if result not in outcomes:
            print('result not a possible outcome')
            exit()
        
        if result == 'win':
            self.points += 2
        elif result == 'tie' or result == 'ot_loss':
            self.points += 1
    
class init_sim:
    def __init__(self, teams, schedule):
        self.teams = teams
        self.schedule = schedule

    