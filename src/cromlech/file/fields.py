# -*- coding: utf-8 -*-

from zope.schema import Field
from zope.interface import implementer
from .interfaces import IFileField, IImageField


@implementer(IFileField)
class FileField(Field):
    """A field handling a file representation.
    """


@implementer(IImageField)
class ImageField(FileField):
    """A field handling an image file representation.
    """
