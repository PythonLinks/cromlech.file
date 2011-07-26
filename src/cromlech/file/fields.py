# -*- coding: utf-8 -*-

from zope.schema import Field
from zope.interface import implements
from cromlech.file import IFileField, IImageField


class FileField(Field):
    """A field handling a file representation.
    """
    implements(IFileField)


class ImageField(FileField):
    """A field handling an image file representation.
    """
    implements(IImageField)
