from django.db import models
from django.db.models.base import ModelBase


class ProxyInheritanceMetaclass(ModelBase):
    def __call__(cls, *args, **kwargs):
        obj = super(ProxyInheritanceMetaclass, cls).__call__(*args, **kwargs)
        return obj.get_object()


class BaseInheritanceModel(models.Model):

    __metaclass__ = ProxyInheritanceMetaclass
    object_class = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.object_class:
            self.object_class = type(self).__name__
        super().save(*args, **kwargs)

    def get_object(self):
        SUBCLASSES = dict([(cls.__name__, cls) for cls in self.__class__.__subclasses__()])
        if self.object_class in SUBCLASSES:
            self.__class__ = SUBCLASSES[self.object_class]
        return self
