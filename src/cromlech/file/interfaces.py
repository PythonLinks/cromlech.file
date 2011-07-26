# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope import schema


class IFile(Interface):
    """Defines a file that is aware of its filename.
    """
    filename = schema.TextLine(
        title=u"Name of file",
        required=False,
        default=u'')

    content_type = schema.BytesLine(
        title=u'Content type',
        description=u'The content type identifies the type of data.',
        default='',
        required=False,
        missing_value='')

    data = schema.Bytes(
        title=u'Data',
        description=u'The actual content of the object.',
        default='',
        missing_value='',
        required=False)

    size = schema.Int(
        title=u"Size",
        description=u"Size in bytes",
        readonly=True,
        required=True)


class IFileField(Interface):
    """A field storing binary datas.
    """


class IImageField(IFileField):
    """Marker interface for fields storing images.
    """
