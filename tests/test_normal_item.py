from conftest import normal_item_factory
from hypothesis import given
from hypothesis import strategies as st

from gilded_rose import GildedRose
from items import NormalItem


def test_normal_item_quality_degrades():
    item = NormalItem(5, 10)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 9


@given(item=normal_item_factory(), days=st.integers(min_value=1, max_value=20))
def test_quality_never_negative(item: NormalItem, days: int):
    gilded_rose = GildedRose([item])
    for _ in range(days):
        gilded_rose.update_quality()
    assert item.quality >= 0
