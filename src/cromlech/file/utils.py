# -*- coding: utf-8 -*-

import re

_nameFinder = re.compile(r'(.*[\\/:])?(.+)')


def clean_filename(name):
    """Uploaded files may have dirty filenames (eg. IE)
    """
    match = _nameFinder.match(name)
    if match is not None:
        match = match.group(2)
    if isinstance(name, unicode):
        return match
    return unicode(match, 'utf-8')
