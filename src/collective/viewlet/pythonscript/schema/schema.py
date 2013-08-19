
from zope.component import adapts
from zope.interface import implements
from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from Products.Archetypes import public as atapi
from Products.CMFPlone import PloneMessageFactory as _

from collective.viewlet.pythonscript.interfaces import IViewletConfigFieldsExtender

class ExtensionBooleanField(ExtensionField, atapi.BooleanField):
    """ Extension boolean field """


class ExtensionStringField(ExtensionField, atapi.StringField):
    """ Extension string field """


class ExtensionIntField(ExtensionField, atapi.IntegerField):
    """ Extension integer field """


class ViewletConfigFieldsExtender(object):
    adapts(IViewletConfigFieldsExtender)
    implements(ISchemaExtender)

    fields = [
        ExtensionBooleanField(
        	"inherit_viewlet_settings",
        	schemata = "Listing",
        	widget = atapi.BooleanWidget(
            	label=_(u"Inherit viewlet settinngs"),
            	description=_(u"If checked - the settings will be inherited from parent."),
            ),
        ),
        ExtensionStringField(
        	"viewlet_title",
        	schemata = "Listing",
        	widget = atapi.StringWidget(
            	label=_(u"Viewlet title"),
            ),
        ),
        ExtensionStringField(
        	"script_name",
        	vocabulary_factory = "python-scripts",
        	schemata = "Listing",
        	widget = atapi.SelectionWidget(
            	label=_(u"Python Script"),
            	description=_(u"Python Script used to generate list of results"),
            ),
        ),
        ExtensionIntField(
        	"limit_results",
        	schemata = "Listing",
        	widget = atapi.IntegerWidget(
            	label=_(u"Limit results"),
            	description=_(u"How many results should be displayed (none means all)"),
            ),
        ),
        ExtensionStringField(
        	"template_name",
        	vocabulary_factory = "python-scripts-templates",
        	schemata = "Listing",
        	widget = atapi.SelectionWidget(
            	label=_(u"Template"),
            	description=_(u"Template to use to render list of results"),
            ),
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
