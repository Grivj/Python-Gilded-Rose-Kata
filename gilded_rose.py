from dataclasses import dataclass
from typing import Sequence

from items import Item


@dataclass
class GildedRose:
    items: Sequence[Item]

    def update_quality(self):
        for item in self.items:
            item.update()
