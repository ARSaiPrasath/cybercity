
class NextRound():
    def __init__(self):
        self.round_counter = 0


    def get_num_rounds(self):
        return self.round_counter

    def next_round(self):
        self.round_counter += 1
