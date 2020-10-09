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
        verbose_name=_('Description'),
        error_messages={'unique': _('Means payment already exists')}
    )

    class Meta:
        db_table = 'means_payment'
        verbose_name = _('Means payment')
        verbose_name_plural = _('Means payments')

    def __str__(self):
        return self.description


class Table(ModelBase):
    class Status(models.TextChoices):
        OCUPPED = 'O', _('Occuped')
        DESOCCUPED = 'D', _('Desoccuped')

    number = models.IntegerField(
        null=False,
        unique=True,
        verbose_name=_('Number')
    )
    status = models.CharField(
        max_length=1,
        default=Status.DESOCCUPED,
        choices=Status.choices,
        verbose_name=_('Status')
    )

    class Meta:
        db_table = 'table'
        verbose_name = _('Table')
        verbose_name_plural = _('Tables')

    def __str__(self):
        return str(self.number)


class Product(ModelBase):
    name = models.CharField(
        max_length=104,
        null=False,
        verbose_name=_('Name')
    )
    detail_description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Detail description')
    )
    sale_price = models.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Sale price')
    )

    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class Order(ModelBase):
    class Status(models.TextChoices):
        OPENED = 'O', _('Opened')
        CLOSED = 'C', _('Closed')
        CANCELED = 'X', _('Canceled')
        PARTIAL_CLOSED = 'P', _('Partial closed')

    date = models.DateTimeField(
        null=False,
        auto_now_add=True,
        verbose_name=_('Date')
    )
    table = models.ForeignKey(
        to='Table',
        on_delete=models.DO_NOTHING,
        db_column='id_table',
        null=False,
        verbose_name=_('Table')
    )
    user = models.ForeignKey(
        to='auth.User',
        on_delete=models.DO_NOTHING,
        db_column='id_user',
        null=False,
        verbose_name=_('User')
    )
    status = models.CharField(
        null=False,
        max_length=1,
        default=Status.OPENED,
        choices=Status.choices,
        verbose_name=_('Status')
    )

    class Meta:
        db_table = 'order'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return '{} - {}'.format(self.id, self.date)


class OrderItem(ModelBase):
    order = models.ForeignKey(
        to='Order',
        on_delete=models.DO_NOTHING,
        db_column='id_order',
        null=False,
        verbose_name=_('Order')
    )
    product = models.ForeignKey(
        to='Product',
        on_delete=models.DO_NOTHING,
        db_column='id_product',
        null=False,
        verbose_name=_('Product')
    )
    quantity = models.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=3,
        verbose_name=_('Quantity')
    )
    unit_price = models.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Unit price')
    )

    class Meta:
        db_table = 'order_item'
        verbose_name = _('Order item')
        verbose_name_plural = _('Order items')

    def __str__(self):
        return '{} - {}'.format(self.order, self.product.name)


class MeansPaymentOrder(ModelBase):
    order = models.ForeignKey(
        to='Order',
        on_delete=models.DO_NOTHING,
        db_column='id_order',
        null=False,
        verbose_name=_('Order')
    )
    means_payment = models.ForeignKey(
        to='MeansPayment',
        on_delete=models.DO_NOTHING,
        db_column='id_means_payment',
        null=False,
        verbose_name=_('Means payment')
    )
    value = models.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=2,
        verbose_name=_('Value')
    )

    class Meta:
        db_table = 'means_payment_order'
        verbose_name = _('Means payment order')
        verbose_name_plural = _('Means payment orders')

    def __str__(self):
        return '{} - {}'.format(self.order, self.means_payment.description)
