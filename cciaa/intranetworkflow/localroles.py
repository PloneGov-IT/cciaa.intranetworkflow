# -*- coding: utf-8 -*-

from zope.interface import implements
from plone.app.workflow.interfaces import ISharingPageRole

from Products.CMFPlone import PloneMessageFactory as _

class DUffRole(object):
    implements(ISharingPageRole)
    
    title = _(u"title_duff", default=u"Può lavorare")
    required_permission = None

class CUffRole(object):
    implements(ISharingPageRole)
    
    title = _(u"title_cuff", default=u"Può dirigere l'ufficio")
    required_permission = None
    
class CSerRole(object):
    implements(ISharingPageRole)
    
    title = _(u"area_cser", default=u"Può dirigere il servizio")
    required_permission = None

class SegGenRole(object):
    implements(ISharingPageRole)
    
    title = _(u"ufficio_seggen", default=u"Può dirigere l'Ente")
    required_permission = None