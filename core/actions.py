from decimal import Decimal
from core import models, helpers


class ProductActions:
    @staticmethod
    def update_detail_decription(product: 'models.Product'):
        if product.detail_description is None:
            product.detail_description = product.name

    @staticmethod
    def calculate_sale_price(product: 'models.Product'):
        if product.sale_price is None:
            product.sale_price = product.cost_price + (product.cost_price * Decimal(0.3))


class TestActions:
    @staticmethod
    def populate():
        # helpers.send_channel_message('test', {'message': 'começou a importação'})

        counter = 0
        percentage = 0

        for index in range(1000 * 10):
            models.Test.objects.create(description='teste - {}'.format(index))
            counter += 1
            if counter == 1000:
                counter = 0
                percentage += 10
                helpers.send_channel_message('test', {'message': '{} %'.format(percentage)})
