import unittest2 as unittest

from Products.CMFCore.utils import getToolByName
from Products.PythonScripts.PythonScript import PythonScript
from collective.portlet.pythonscript.content.interface import IPythonScriptManager

from collective.viewlet.pythonscript.testing import COLLECTIVE_VIEWLET_PYTHONSCRIPT_INTEGRATION

class TestBase(unittest.TestCase):
    """Base test case."""

    layer = COLLECTIVE_VIEWLET_PYTHONSCRIPT_INTEGRATION

    def setUp(self):
        """Setup fixture."""
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
        self.ploneSite = self.app.plone

    def createPythonScript(self, id_, title, code):
        """Creare new Python Script object."""
        ps = PythonScript(id_)
        if title:
            ps.ZPythonScript_setTitle(title)
        ps.write(code)
        ps._makeFunction()
        return ps

    def addPythonScript(self, id_, title, code, container=None):
        """Add new Python Script to Plone Site."""
        ps = self.createPythonScript(id_, title, code)
        if container is None:
            container = self.ploneSite
        container[id_] = ps
        return ps

    def getScriptManager(self):
        """Return script manager for Plone site."""
        return IPythonScriptManager(self.ploneSite)
