import uuid

from django.db import models
from django.db.models import CharField, CASCADE, IntegerField, ForeignKey, Model, UUIDField, DateTimeField, TextField, \
    ImageField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel



class Category(MPTTModel):
    name = CharField(max_length=200, null=True, blank=True)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # @property
    # def product_count(self):
    #     return self.product_set.count()


class Blog(Model):
    title = CharField(max_length=200, null=True, blank=True)
    description = TextField()
    view_count = IntegerField(default=0)
    image = ImageField(upload_to='post/image/')
    # owner = ForeignKey('')
    category = ForeignKey('Category', CASCADE)
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
