from dataclasses import dataclass, field

from .item import Item


@dataclass
class AgedBrieItem(Item):
    name: str = field(default="Aged Brie", init=False)

    def update(self):
        self.sell_in -= 1
        if self.quality < 50:
            self.quality += 1
        if self.sell_in < 0 and self.quality < 50:
            self.quality += 1
