class BoardTile:
    def __init__(self, position, total_dividend_multiple, required_players_count, required_players, possible_players):
        self.position = position
        self.total_dividend_multiple = total_dividend_multiple
        self.required_players_count = required_players_count
        self.required_players = required_players
        self.possible_players = possible_players

    def __repr__(self):
        return (f"Tile(position={self.position}, required_players={self.required_players}, "
                f"deal_amount={self.total_dividend_multiple}, required_player_types={self.required_players}, "
                f"possible_player_types={self.possible_players})")

    def init_deal(self):
        pass
