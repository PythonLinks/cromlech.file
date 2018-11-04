# -*- coding: utf-8 -*-

from cromlech.file import IFile
from zope.size import byteDisplay
from zope.size.interfaces import ISized
from zope.interface import implementer
from zope.component import adapts

@implementer(ISized)
class Sized(object):
    adapts(IFile)


    def __init__(self, context):
        self.context = context

    def sizeForSorting(self):
        return "byte", self.context.size

    def sizeForDisplay(self):
        return byteDisplay(self.context.size)
