from dataclasses import dataclass, field

from .item import Item


@dataclass
class BackstagePassItem(Item):
    name: str = field(default="Backstage passes to a TAFKAL80ETC concert", init=False)

    def update(self):
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in < 5:
            self.quality = min(50, self.quality + 3)
        elif self.sell_in < 10:
            self.quality = min(50, self.quality + 2)
        else:
            self.quality = min(50, self.quality + 1)
