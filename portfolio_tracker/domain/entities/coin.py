from dataclasses import dataclass


@dataclass
class Coin:
    def __init__(self, id, name, symbol):
        self.id = id
        self.name = name
        self.symbol = symbol

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'symbol': self.symbol}
    
    # def __repr__(self):
    #     return f'Coin(id={self.id}, name={self.name}, symbol={self.symbol})'