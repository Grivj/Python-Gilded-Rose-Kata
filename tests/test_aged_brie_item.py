from conftest import aged_brie_factory
from hypothesis import given
from hypothesis import strategies as st

from gilded_rose import GildedRose, Item


def test_aged_brie_item_quality_increases():
    item = Item("Aged Brie", 5, 10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 11


@given(item=aged_brie_factory(), days=st.integers(min_value=1, max_value=41))
def test_quality_never_more_than_50(item: Item, days: int):
    gilded_rose = GildedRose([item])
    for _ in range(days):
        gilded_rose.update_quality()
    assert item.quality <= 50
