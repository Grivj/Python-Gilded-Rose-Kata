from dataclasses import dataclass, field

from .item import Item


@dataclass
class NormalItem(Item):
    name: str = field(default="Normal Item", init=False)

    def update(self):
        self.sell_in -= 1
        self.quality = max(0, self.quality - (2 if self.sell_in < 0 else 1))
