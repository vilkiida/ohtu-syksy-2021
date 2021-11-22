from player_reader import PlayerReader
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.players

    def top_scorers_by_nationality(self, nat):
        chosen_nationality = []
        for player in self.players:
            if player.nationality == nat:
                chosen_nationality.append(player)
        
        chosen_nationality.sort(key=lambda x: x.points ,reverse=True)
        return chosen_nationality
