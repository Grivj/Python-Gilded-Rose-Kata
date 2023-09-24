from conftest import backstage_pass_factory
from hypothesis import given

from gilded_rose import GildedRose, Item


def assert_quality_increase(sell_in: int, quality: int, item: Item):
    if sell_in > 10:
        assert item.quality == min(50, quality + 1)
    elif 6 <= sell_in <= 10:
        assert item.quality == min(50, quality + 2)
    elif 1 <= sell_in <= 5:
        assert item.quality == min(50, quality + 3)
    else:
        assert item.quality == 0


@given(item=backstage_pass_factory())
def test_backstage_pass_quality_increases_by_2(item: Item):
    gilded_rose = GildedRose([item])
    initial_quality = item.quality
    initial_sell_in = item.sell_in
    gilded_rose.update_quality()

    assert_quality_increase(initial_sell_in, initial_quality, item)


@given(item=backstage_pass_factory())
def test_backstage_pass_quality_drops_to_0(item: Item):
    item.sell_in = 0
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert item.quality == 0
