from pytest_bdd import scenarios, parsers, given, when, then

from cucumbers import CucumberBasket

CONVERTERS = {
    'initial': int,
    'some': int,
    'total': int,
}

EXTRA_TYPES = {
    'Number': int,
}

scenarios('../features/cucumbers.feature', example_converters = CONVERTERS)

@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=EXTRA_TYPES))
@given('the basket has "<initial>" cucumbers')
def basket(initial):
    return CucumberBasket(initial_count=initial)

@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=EXTRA_TYPES))
@when('"<some>" cucumbers are added to the basket')
def add_cucumbers(basket, some):
    return basket.add(some)

@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', extra_types=EXTRA_TYPES))
def remove_cucumbers(basket, some):
    return basket.remove(some)

@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=EXTRA_TYPES))
@then('the basket contains "<total>" cucumbers')
def basket_has_total(basket, total):
    assert basket.count == total