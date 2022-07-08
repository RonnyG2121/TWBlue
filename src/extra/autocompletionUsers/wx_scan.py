# -*- coding: utf-8 -*-
import wx
import widgetUtils
import application

class autocompletionScanDialog(widgetUtils.BaseDialog):
    def __init__(self):
        super(autocompletionScanDialog, self).__init__(parent=None, id=-1, title=_(u"Autocomplete users' settings"))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.followers = wx.CheckBox(panel, -1, _("Add followers to the database"))
        self.friends = wx.CheckBox(panel, -1, _("Add  friends to database"))
        sizer.Add(self.followers, 0, wx.ALL, 5)
        sizer.Add(self.friends, 0, wx.ALL, 5)
        ok = wx.Button(panel, wx.ID_OK)
        cancel = wx.Button(panel, wx.ID_CANCEL)
        sizerBtn = wx.BoxSizer(wx.HORIZONTAL)
        sizerBtn.Add(ok, 0, wx.ALL, 5)
        sizer.Add(cancel, 0, wx.ALL, 5)
        sizer.Add(sizerBtn, 0, wx.ALL, 5)
        panel.SetSizer(sizer)
        self.SetClientSize(sizer.CalcMin())

def show_success_dialog():
    with wx.MessageDialog(None, _("{0}'s database of users has been updated.").format(application.name,), _(u"Done"), wx.OK)as dlg:
        dlg.ShowModal()

def confirm():
    with wx.MessageDialog(None, _("This process will retrieve the users you selected from Twitter, and add them to the user autocomplete database. Please note that if there are many users or you have tried to perform this action less than 15 minutes ago, TWBlue may reach a limit in Twitter API calls when trying to load the users into the database. If this happens, we will show you an error, in which case you will have to try this process again in a few minutes. Do you want to continue?"), _("Attention"), style=wx.ICON_QUESTION|wx.YES_NO) as result:
        if result.ShowModal() == wx.ID_YES:
            return True
        return False

def get_progress_dialog():
    return wx.ProgressDialog(_("Retrieving Twitter users from account..."), _("working..."),  parent=None, maximum=100)
