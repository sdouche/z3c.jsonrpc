##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""
$Id$
"""
__docformat__ = "reStructuredText"

import sys
import unittest
import persistent
import zope.interface
from zope.publisher.interfaces import Retry
from zope.testing import doctest
from z3c.jsonrpc import testing
from z3c.jsonrpc import publisher
from ZODB.POSException import ConflictError


class IDemoContent(zope.interface.Interface):
    """Demo content interface."""


class DemoContent(persistent.Persistent):
    """Demo content."""
    zope.interface.implements(IDemoContent)


class DemoView(publisher.MethodPublisher):
    """Sample JSON view."""

    def goodResult(self):
        return u'good'

    def badResult(self):
        raise ConflictError


def test_suite():
    return unittest.TestSuite((
        testing.FunctionalDocFileSuite('retry.txt',
            setUp=testing.setUp, tearDown=testing.tearDown,
            optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS,
            ),
        ))


if __name__=='__main__':
    unittest.main(defaultTest='test_suite')
