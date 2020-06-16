from functools import partial
from pytest_bdd import scenarios, parsers, given, when, then

from cucumbers import CucumberBasket


scenarios('../features/cucumbers.feature')

EXTRA_TYPES = {
    'Number': int,
}

parser = partial(parsers.cfparse, extra_types=EXTRA_TYPES)

@given(parser('the basket has "{initial:Number}" cucumbers'))
def basket(initial):
    return CucumberBasket(initial_count=initial)

@when(parser('"{some:Number}" cucumbers are added to the basket'))
def add_cucumbers(basket, some):
    return basket.add(some)

@when(parser('"{some:Number}" cucumbers are removed from the basket'))
def remove_cucumbers(basket, some):
    return basket.remove(some)

@then(parser('the basket contains "{total:Number}" cucumbers'))
def basket_has_total(basket, total):
    assert basket.count == total