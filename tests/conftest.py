"""Tests to ensure that the gilded rose requirements are met."""

import pytest
from hypothesis import strategies as st

from gilded_rose import Item

normal_item_names = st.sampled_from(["normal", "item", "foo"])
brie = st.just("Aged Brie")
sulfuras_strategy = st.just("Sulfuras, Hand of Ragnaros")
backstage_pass = st.just("Backstage passes to a TAFKAL80ETC concert")
conjured = st.just("Conjured Mana Cake")

normal_quality = st.integers(min_value=0, max_value=50)
sulfuras_quality = st.just(80)
sell_in = st.integers(min_value=-10, max_value=10)


@pytest.fixture
def normal_item():
    return Item("normal", 5, 10)


@pytest.fixture
def aged_brie_item():
    return Item("Aged Brie", 5, 10)


@pytest.fixture
def sulfuras_item():
    return Item("Sulfuras, Hand of Ragnaros", 5, 80)


@pytest.fixture
def backstage_pass_item():
    return Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)


@pytest.fixture
def conjured_item():
    return Item("Conjured Mana Cake", 5, 10)
