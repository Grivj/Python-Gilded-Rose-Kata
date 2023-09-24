from conftest import normal_item_factory, normal_item_names, normal_quality, sell_in
from hypothesis import given
from hypothesis import strategies as st

from gilded_rose import GildedRose, Item


def test_normal_item_quality_degrades():
    item = Item("normal", 5, 10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 9


@given(item=normal_item_factory(), days=st.integers(min_value=1, max_value=20))
def test_quality_never_negative(item: Item, days: int):
    gilded_rose = GildedRose([item])
    for _ in range(days):
        gilded_rose.update_quality()
    assert item.quality >= 0


@given(item_name=normal_item_names, sell_in=sell_in, quality=normal_quality)
def test_normal_items(item_name: str, sell_in: int, quality: int):
    item = Item(item_name, sell_in, quality)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    expected_quality = max(0, quality - 1 if sell_in > 0 else quality - 2)
    assert item.quality == expected_quality
