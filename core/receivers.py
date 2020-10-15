from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from core import models, actions, tasks


@receiver(post_save, sender=models.Product, dispatch_uid="update_detail_decription_by_product", weak=False)
def update_detail_decription_by_product(**kwargs):
    tasks.populate_test.apply_async([], countdown=1)


@receiver(pre_save, sender=models.Product, dispatch_uid="pre_save_product", weak=False)
def pre_save_product(**kwargs):
    instance = kwargs.get('instance')
    actions.ProductActions.update_detail_decription(product=instance)
    actions.ProductActions.calculate_sale_price(product=instance)
