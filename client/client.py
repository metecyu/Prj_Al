import sys

import wx
import wx.lib.agw.ultimatelistctrl as ULC

class MyFrame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, -1, "UltimateListCtrl Demo")

        list = ULC.UltimateListCtrl(self, wx.ID_ANY, style = 0 ,agwStyle = 0 )

        list.InsertColumn(0, "Column 1")
        list.InsertColumn(1, "Column 2")

        index = list.InsertStringItem(sys.maxint, "Item 1")
        list.SetStringItem(index, 1, "Sub-item 1")

        index = list.InsertStringItem(sys.maxint, "Item 2")
        list.SetStringItem(index, 1, "Sub-item 2")

        choice = wx.Choice(list, -1, choices=["one", "two"])
        index = list.InsertStringItem(sys.maxint, "A widget")

        list.SetItemWindow(index, 1, choice, expand=True)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(list, 1, wx.EXPAND)
        self.SetSizer(sizer)


# our normal wxApp-derived class, as usual

app = wx.App(0)

frame = MyFrame()
app.SetTopWindow(frame)
frame.Show()

app.MainLoop()