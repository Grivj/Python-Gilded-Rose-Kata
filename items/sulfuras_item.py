from dataclasses import dataclass, field

from .item import Item


@dataclass
class SulfurasItem(Item):
    name: str = field(default="Sulfuras, Hand of Ragnaros", init=False)
    quality: int = field(default=80, init=False)
    sell_in: int = field(default=0, init=False)

    def update(self):
        pass
