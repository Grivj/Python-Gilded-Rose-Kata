from conftest import sulfuras_factory
from hypothesis import given
from hypothesis import strategies as st

from gilded_rose import GildedRose
from items import SulfurasItem


@given(item=sulfuras_factory(), days=st.integers(min_value=1, max_value=20))
def test_sulfuras_never_decreases_quality(item: SulfurasItem, days: int):
    gilded_rose = GildedRose([item])
    for _ in range(days):
        gilded_rose.update_quality()
    assert item.quality == 80
