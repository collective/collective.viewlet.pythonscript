from Products.Archetypes.browser.edit import Edit as BaseEdit
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFPlone import PloneMessageFactory as _

class Edit(BaseEdit):

    def __call__(self, context=None, request=None):
        try:
            inherit = self.fields(['Listing'])[0].get(self.context)
        except KeyError:
            return self
        if inherit:
            settings_provider = [i for i in self.context.aq_chain \
                if getattr(i, 'inherit_viewlet_settings', False)][-1].aq_parent
            IStatusMessage(self.context.REQUEST).addStatusMessage(
                _("Viewlet settings are inherited from %s." % \
                    '/'.join(settings_provider.getPhysicalPath())),
                type="info"
            )
        return self
