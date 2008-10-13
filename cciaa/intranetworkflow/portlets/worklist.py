# -*- coding: utf-8 -*-

from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider

from DateTime import DateTime
from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

# This interface defines the configurable options (if any) for the portlet.
# It will be used to generate add and edit forms.

class IWorklistPortlet(IPortletDataProvider):
    """Marker interface for CCIAA Worklist portlets"""

# The assignment is a persistent object used to store the configuration of
# a particular instantiation of the portlet.

class Assignment(base.Assignment):
    implements(IWorklistPortlet)

    @property
    def title(self):
        return u"Lista di revisione CCIAA"

# The renderer is like a view (in fact, like a content provider/viewlet). The
# item self.data will typically be the assignment (although it is possible
# that the assignment chooses to return a different object - see 
# base.Assignment).

class Renderer(base.Renderer):

    # render() will be called to render the portlet
    
    render = ViewPageTemplateFile('camcom_portlet_review.pt')
    
    def getMember(self):
        context = self.context
        mtool = getToolByName(context, 'portal_membership')
        return mtool.getAuthenticatedMember()
    
# Define the add forms and edit forms, based on zope.formlib. These use
# the interface to determine which fields to render.

class AddForm(base.NullAddForm):
    label = u"Aggiungi lista di revisione camerale"
    description = "Aggiunge la lista di revisione che usa i ruoli camerali"

    # This method must be implemented to actually construct the object.
    # The 'data' parameter is a dictionary, containing the values entered
    # by the user.

    def create(self):
        assignment = Assignment()
        return assignment
