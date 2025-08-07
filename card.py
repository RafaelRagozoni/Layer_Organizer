

class Card:
    def __init__(self, title):
        self.title = title
        self.card_ids_behind = []
        self.card_ids_ahead = []
        self.cards_blocking = []
        self.tasks = {} #{task_id: True, task_id: False}
        self.completion = 0