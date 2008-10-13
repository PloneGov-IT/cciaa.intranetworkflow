# -*- coding: utf-8 -*-

from zope.interface import implements
from plone.app.workflow.interfaces import ISharingPageRole
from cciaa.intranetworkflow import config

from Products.CMFPlone import PloneMessageFactory as _

class DUffRole(object):
    implements(ISharingPageRole)
    
    title = _(u"title_duff", default=u"Può gestire contenuti")
    required_permission = config.DelegateEditorRole

class CUffRole(object):
    implements(ISharingPageRole)
    
    title = _(u"title_cuff", default=u"Può gestire l'ufficio")
    required_permission = config.DelegateCuffRole
    
class CSerRole(object):
    implements(ISharingPageRole)
    
    title = _(u"area_cser", default=u"Può gestire il servizio")
    required_permission = config.DelegateCSerRole

class SegGenRole(object):
    implements(ISharingPageRole)
    
    title = _(u"ufficio_seggen", default=u"Può dirigere l'Ente")
    required_permission = config.DelegateSegGenRole