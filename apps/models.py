from django.db import models
from django.db.models import CharField, CASCADE, IntegerField, ForeignKey, Model
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = CharField(max_length=200, null=True, blank=True)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    def __str__(self):
        return self.name

    # @property
    # def product_count(self):
    #     return self.product_set.count()


class Product(Model):
    title = CharField(max_length=200, null=True, blank=True)
    price = IntegerField()
    category = ForeignKey('Category', CASCADE)

    def __str__(self) -> str:
        return self.title


