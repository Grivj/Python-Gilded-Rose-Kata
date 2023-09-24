from hypothesis import strategies as st

from items import AgedBrieItem, BackstagePassItem, NormalItem, SulfurasItem

normal_quality = st.integers(min_value=0, max_value=50)
sulfuras_quality = st.just(80)

sell_in = st.integers(min_value=-10, max_value=10)


def normal_item_factory():
    return st.builds(NormalItem, sell_in=sell_in, quality=normal_quality)


def aged_brie_factory():
    return st.builds(AgedBrieItem, sell_in=sell_in, quality=normal_quality)


def backstage_pass_factory():
    return st.builds(BackstagePassItem, sell_in=sell_in, quality=normal_quality)


def sulfuras_factory():
    return st.builds(SulfurasItem)
