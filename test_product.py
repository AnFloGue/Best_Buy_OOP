import pytest
from products import Product


def test_creating_normal_product():
    product = Product("MacBook Pro", price=1500, quantity=50)
    assert product.name == "MacBook Pro"
    assert product.price == 1500
    assert product.quantity == 50


def test_creating_product_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_becomes_inactive():
    product = Product("MacBook Pro", price=1500, quantity=1)
    product.product_purchased(1)
    assert not product.product_is_active()


def test_product_purchase_modifies_quantity():
    product = Product("MacBook Pro", price=1500, quantity=50)
    total_price = product.product_purchased(10)
    assert product.quantity == 40
    assert total_price == 15000


def test_buying_larger_quantity_than_exists():
    product = Product("MacBook Pro", price=1500, quantity=50)
    with pytest.raises(ValueError):
        product.product_purchased(60)
