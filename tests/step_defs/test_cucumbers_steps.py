from pytest_bdd import scenario, parsers, given, when, then

from cucumbers import CucumberBasket


@scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
def test_add():
    pass

@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=dict(Number=int)))
def basket():
    return CucumberBasket(initial_count=2)

@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=dict(Number=int)))
def add_cucumbers(basket):
    return basket.add(4)

@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=dict(Number=int)))
def basket_has_total(basket):
    assert basket.count == 6