from decimal import Decimal
from core import models


class ProductActions:
    @staticmethod
    def update_detail_decription(product: 'models.Product'):
        if product.detail_description is None:
            product.detail_description = product.name

    @staticmethod
    def calculate_sale_price(product: 'models.Product'):
        if product.sale_price is None:
            product.sale_price = product.cost_price + (product.cost_price * Decimal(0.3))
