from dataclasses import dataclass


@dataclass
class Item:
    name: str
    sell_in: int
    quality: int

    def update(self) -> None:
        raise NotImplementedError
