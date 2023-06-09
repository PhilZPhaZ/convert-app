#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.5 on Sun May 21 23:28:38 2023
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class ConversionAppFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ConversionAppFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((354, 259))
        self.SetTitle("frame")

        # Menu Bar
        self.menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Go on my github", "")
        self.Bind(wx.EVT_MENU, self.on_menu_credits_discord, item)
        self.menubar.Append(wxglade_tmp_menu, "Credits")
        self.SetMenuBar(self.menubar)
        # Menu Bar end

        self.main_panel = wx.Panel(self, wx.ID_ANY)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        value_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(value_sizer, 0, wx.ALL | wx.EXPAND, 0)

        value_label_sizer = wx.BoxSizer(wx.HORIZONTAL)
        value_sizer.Add(value_label_sizer, 0, wx.ALL | wx.EXPAND, 0)

        value_label = wx.StaticText(self.main_panel, wx.ID_ANY, "Chose the value")
        value_label.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        value_label_sizer.Add(value_label, 1, wx.LEFT, 10)

        value_input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        value_sizer.Add(value_input_sizer, 0, wx.ALL | wx.EXPAND, 7)

        self.value_input = wx.TextCtrl(self.main_panel, wx.ID_ANY, "")
        value_input_sizer.Add(self.value_input, 0, wx.ALL, 4)

        self.value_units = wx.Choice(self.main_panel, wx.ID_ANY, choices=["Meter (m)", "Millimeter (mm)", "Centimeter (cm)", "Decimeter (dm)", "Kilometer (km)", "Inch (in)", "Link (l)", "Foot (ft)", "Yard (yd)", "Rod/Perch/Pole/Lug", "Chain", "Furlong", "Mile (mi)", "Nautical Mile (sm)", "Astronomical Unit (AE)", "Light year (lj)", "Parsec (pc)"])
        self.value_units.SetSelection(0)
        value_input_sizer.Add(self.value_units, 1, wx.ALL, 4)

        convert_unit_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(convert_unit_sizer, 0, wx.EXPAND, 0)

        convert_unit_label_sizer = wx.BoxSizer(wx.HORIZONTAL)
        convert_unit_sizer.Add(convert_unit_label_sizer, 0, wx.EXPAND, 0)

        convert_unit_label = wx.StaticText(self.main_panel, wx.ID_ANY, "Chose the unit to convert")
        convert_unit_label.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        convert_unit_label_sizer.Add(convert_unit_label, 1, wx.LEFT, 10)

        convert_unit_input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        convert_unit_sizer.Add(convert_unit_input_sizer, 0, wx.ALL | wx.EXPAND, 7)

        self.convert_unit_input = wx.Choice(self.main_panel, wx.ID_ANY, choices=["Meter (m)", "Millimeter (mm)", "Centimeter (cm)", "Decimeter (dm)", "Kilometer (km)", "Inch (in)", "Link (l)", "Foot (ft)", "Yard (yd)", "Rod/Perch/Pole/Lug", "Chain", "Furlong", "Mile (mi)", "Nautical Mile (sm)", "Astronomical Unit (AE)", "Light year (lj)", "Parsec (pc)"])
        self.convert_unit_input.SetSelection(0)
        convert_unit_input_sizer.Add(self.convert_unit_input, 1, wx.ALL, 4)

        result_sizer = wx.WrapSizer(wx.HORIZONTAL)
        main_sizer.Add(result_sizer, 0, wx.EXPAND | wx.LEFT, 10)

        result_label_sizer = wx.BoxSizer(wx.HORIZONTAL)
        result_sizer.Add(result_label_sizer, 1, wx.EXPAND, 10)

        label_1 = wx.StaticText(self.main_panel, wx.ID_ANY, "Result :")
        label_1.SetFont(wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        result_label_sizer.Add(label_1, 0, 0, 0)

        result_resulr_sizer = wx.BoxSizer(wx.HORIZONTAL)
        result_sizer.Add(result_resulr_sizer, 1, wx.EXPAND | wx.TOP, 4)

        self.result_result = wx.TextCtrl(self.main_panel, wx.ID_ANY, "")
        result_resulr_sizer.Add(self.result_result, 0, wx.ALL, 2)

        result_unit_sizer = wx.BoxSizer(wx.HORIZONTAL)
        result_sizer.Add(result_unit_sizer, 1, wx.EXPAND | wx.TOP, 4)

        self.result_unit = wx.TextCtrl(self.main_panel, wx.ID_ANY, "")
        result_unit_sizer.Add(self.result_unit, 0, wx.ALL, 2)

        self.main_panel.SetSizer(main_sizer)

        self.Layout()

        self.Bind(wx.EVT_CHOICE, self.on_unit_selected, self.value_units)
        self.Bind(wx.EVT_CHOICE, self.on_unit_selected, self.convert_unit_input)
        # end wxGlade

    def on_menu_credits_discord(self, event):  # wxGlade: ConversionAppFrame.<event_handler>
        print("Event handler 'on_menu_credits_discord' not implemented!")
        event.Skip()

    def on_unit_selected(self, event):  # wxGlade: ConversionAppFrame.<event_handler>
        print("Event handler 'on_unit_selected' not implemented!")
        event.Skip()

# end of class ConversionAppFrame

class ConversionApp(wx.App):
    def OnInit(self):
        self.frame = ConversionAppFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class ConversionApp

if __name__ == "__main__":
    app = ConversionApp(0)
    app.MainLoop()
