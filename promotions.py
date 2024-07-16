from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return product.price * full_price_items + (product.price / 2) * half_price_items


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        full_price_items = quantity - (quantity // 3)
        return product.price * full_price_items


class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent
    
    def apply_promotion(self, product, quantity) -> float:
        return product.price * quantity * (1 - self.percent / 100)
