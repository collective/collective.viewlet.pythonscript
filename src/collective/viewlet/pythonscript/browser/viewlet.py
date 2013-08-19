import logging
import sys

from Acquisition import aq_acquire
from ZODB.POSException import ConflictError
from zope.component import getMultiAdapter

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase

from collective.portlet.pythonscript.browser.portlet import PythonScriptPortletRenderer

logger = logging.getLogger('pythonscript.vielet')

class PythonScriptViewlet(ViewletBase, PythonScriptPortletRenderer):
    """ Viewlet for displaying the python script results """

    index = ViewPageTemplateFile("pythonscript-viewlet.pt")
    error_message = "<!-- Unable to render pyhtonscript vielets content -->"

    def __init__(self, context, request, view, manager=None):
        super(PythonScriptViewlet, self).__init__(context, request, view, manager=None)
        self.viewlet_title = context.Schema().get('viewlet_title').get(context)
        self.script_name = context.Schema().get('script_name').get(context)
        self.template_name = context.Schema().get('template_name').get(context)
        self.limit_results = context.Schema().get('limit_results').get(context)

    @property
    def data(self):
        return self

    def safe_render(self):
        try:
            return self.renderResults()
        except ConflictError:
            raise
        except Exception:
            logger.exception('Error while rendering %r' % self)
            aq_acquire(self.context, 'error_log').raising(sys.exc_info())
            return self.error_message
