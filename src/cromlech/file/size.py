# -*- coding: utf-8 -*-

import grokcore.component as grok
from cromlech.file import IFile
from zope.size import byteDisplay
from zope.size.interfaces import ISized


class Sized(grok.Adapter):
    grok.context(IFile)
    grok.implements(ISized)

    def sizeForSorting(self):
        return "byte", self.context.size

    def sizeForDisplay(self):
        return byteDisplay(self.context.size)
