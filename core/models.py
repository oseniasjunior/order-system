from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class ModelBase(models.Model):
    id = models.AutoField(
        db_column='id',
        null=False,
        primary_key=True,
        verbose_name=_('Code')
    )
    created_at = models.DateTimeField(
        db_column='created_at',
        null=False,
        auto_now_add=True,
        verbose_name=_('Created at')
    )
    modified_at = models.DateTimeField(
        db_column='modified_at',
        null=False,
        auto_now=True,
        verbose_name=_('Modified at')
    )
    active = models.BooleanField(
        db_column='active',
        null=False,
        default=True,
        verbose_name=_('Active')
    )

    class Meta:
        abstract = True
        managed = True


class MeansPayment(ModelBase):
    description = models.CharField(
        max_length=104,
        null=False,
        unique=True,
        verbose_name=_('Description')
    )

    class Meta:
        db_table = 'means_payment'
        verbose_name = _('Means payment')
        verbose_name_plural = _('Means payment')


class Table(ModelBase):
    class Status(models.TextChoices):
        OCUPPED = 'O', 'Occuped'
        DESOCCUPED = 'D', 'Desoccuped'

    number = models.IntegerField(
        null=False,
        unique=True
    )
    status = models.CharField(
        max_length=1,
        default=Status.DESOCCUPED,
        choices=Status.choices
    )

    class Meta:
        db_table = 'table'


class Product(ModelBase):
    name = models.CharField(
        max_length=104,
        null=False
    )
    detail_description = models.TextField(
        null=True,
        blank=True
    )
    sale_price = models.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        db_table = 'product'


class Order(ModelBase):
    class Status(models.TextChoices):
        OPENED = 'O', 'Opened'
        CLOSED = 'C', 'Closed'
        CANCELED = 'X', 'Canceled'
        PARTIAL_CLOSED = 'P', 'Partial closed'

    date = models.DateTimeField(
        null=False,
        auto_now_add=True
    )
    table = models.ForeignKey(
        to='Table',
        on_delete=models.DO_NOTHING,
        db_column='id_table',
        null=False
    )
    user = models.ForeignKey(
        to='auth.User',
        on_delete=models.DO_NOTHING,
        db_column='id_user',
        null=False
    )
    status = models.CharField(
        null=False,
        max_length=1,
        default=Status.OPENED,
        choices=Status.choices
    )

    class Meta:
        db_table = 'order'


class OrderItem(ModelBase):
    order = models.ForeignKey(
        to='Order',
        on_delete=models.DO_NOTHING,
        db_column='id_order',
        null=False
    )
    product = models.ForeignKey(
        to='Product',
        on_delete=models.DO_NOTHING,
        db_column='id_product',
        null=False
    )
    quantity = models.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=3
    )
    unit_price = models.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        db_table = 'order_item'


class MeansPaymentOrder(ModelBase):
    order = models.ForeignKey(
        to='Order',
        on_delete=models.DO_NOTHING,
        db_column='id_order',
        null=False
    )
    means_payment = models.ForeignKey(
        to='MeansPayment',
        on_delete=models.DO_NOTHING,
        db_column='id_means_payment',
        null=False
    )
    value = models.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        db_table = 'means_payment_order'
