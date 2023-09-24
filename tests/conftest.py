from hypothesis import strategies as st

from gilded_rose import Item

normal_item_names = st.sampled_from(["normal", "item", "foo"])
brie = st.just("Aged Brie")
sulfuras_strategy = st.just("Sulfuras, Hand of Ragnaros")
backstage_pass = st.just("Backstage passes to a TAFKAL80ETC concert")

normal_quality = st.integers(min_value=0, max_value=50)
sulfuras_quality = st.just(80)

sell_in = st.integers(min_value=-10, max_value=10)


def normal_item_factory():
    return st.builds(Item, normal_item_names, sell_in, normal_quality)


def aged_brie_factory():
    return st.builds(Item, brie, sell_in, normal_quality)


def sulfuras_factory():
    return st.builds(Item, sulfuras_strategy, sell_in, sulfuras_quality)


def backstage_pass_factory():
    return st.builds(Item, backstage_pass, sell_in, normal_quality)
