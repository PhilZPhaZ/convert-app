import contextlib
import wx
from convertion_dict import length
import webbrowser

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class ConversionApp(wx.Frame):
    def __init__(self, *args, **kwds):
        self.length = length
        
        # begin wxGlade: ConversionApp.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((354, 259))
        self.SetTitle("Conversion Application")
        self.SetIcon(wx.Icon("app.ico"))

        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.frame_menubar.help_github = wxglade_tmp_menu.Append(wx.ID_ANY, "Check my github", "Go on my github")
        self.Bind(wx.EVT_MENU, self.on_menu_credits_github, self.frame_menubar.help_github)
        self.frame_menubar.Append(wxglade_tmp_menu, "Credits")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        value_sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(value_sizer, 0, wx.EXPAND, 0)

        value_label_sizer = wx.BoxSizer(wx.HORIZONTAL)
        value_sizer.Add(value_label_sizer, 0, wx.ALL | wx.EXPAND, 0)

        value_label = wx.StaticText(self.panel_1, wx.ID_ANY, "Chose the value")
        value_label.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        value_label_sizer.Add(value_label, 1, wx.LEFT, 10)

        value_input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        value_sizer.Add(value_input_sizer, 0, wx.ALL | wx.EXPAND, 7)

        self.value_input = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        value_input_sizer.Add(self.value_input, 0, wx.ALL, 4)

        self.value_units = wx.Choice(self.panel_1, wx.ID_ANY, choices=["Meter (m)", "Millimeter (mm)", "Centimeter (cm)", "Decimeter (dm)", "Kilometer (km)", "Inch (in)", "Link (l)", "Foot (ft)", "Yard (yd)", "Rod/Perch/Pole/Lug", "Chain", "Furlong", "Mile (mi)", "Nautical Mile (sm)", "Astronomical Unit (AE)", "Light year (lj)", "Parsec (pc)"])
        self.value_units.SetSelection(0)
        value_input_sizer.Add(self.value_units, 1, wx.ALL, 4)

        convert_unit_sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(convert_unit_sizer, 0, wx.EXPAND, 0)

        convert_unit_label_sizer = wx.BoxSizer(wx.HORIZONTAL)
        convert_unit_sizer.Add(convert_unit_label_sizer, 0, wx.EXPAND, 0)

        convert_unit_label = wx.StaticText(self.panel_1, wx.ID_ANY, "Choose the unit to convert")
        convert_unit_label.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        convert_unit_label_sizer.Add(convert_unit_label, 1, wx.LEFT, 9)

        convert_unit_input_sizer = wx.BoxSizer(wx.HORIZONTAL)
        convert_unit_sizer.Add(convert_unit_input_sizer, 0, wx.ALL | wx.EXPAND, 7)

        self.convert_unit_input = wx.Choice(self.panel_1, wx.ID_ANY, choices=["Meter (m)", "Millimeter (mm)", "Centimeter (cm)", "Decimeter (dm)", "Kilometer (km)", "Inch (in)", "Link (l)", "Foot (ft)", "Yard (yd)", "Rod/Perch/Pole/Lug", "Chain", "Furlong", "Mile (mi)", "Nautical Mile (sm)", "Astronomical Unit (AE)", "Light year (lj)", "Parsec (pc)"])
        self.convert_unit_input.SetSelection(0)
        convert_unit_input_sizer.Add(self.convert_unit_input, 1, wx.ALL, 4)

        result_sizer = wx.WrapSizer(wx.HORIZONTAL)
        sizer_1.Add(result_sizer, 0, wx.ALL | wx.EXPAND, 0)

        result_label_sizer = wx.BoxSizer(wx.HORIZONTAL)
        result_sizer.Add(result_label_sizer, 1, wx.EXPAND, 0)

        result_label = wx.StaticText(self.panel_1, wx.ID_ANY, "Result :")
        result_label.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        result_label_sizer.Add(result_label, 0, 0, 0)

        result_result_sizer = wx.BoxSizer(wx.HORIZONTAL)
        result_sizer.Add(result_result_sizer, 1, wx.EXPAND, 0)

        self.result_result = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        result_result_sizer.Add(self.result_result, 1, wx.ALL, 4)

        result_units_sizer = wx.BoxSizer(wx.HORIZONTAL)
        result_sizer.Add(result_units_sizer, 1, wx.ALL | wx.EXPAND, 4)

        self.result_units = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        result_units_sizer.Add(self.result_units, 0, 0, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()

        self.Bind(wx.EVT_CHOICE, self.on_event_select_first_units, self.value_units)
        self.Bind(wx.EVT_CHOICE, self.on_event_select_second_units, self.convert_unit_input)
        # end wxGlade

    def on_menu_credits_github(self, event):  # wxGlade: ConversionApp.<event_handler>
        webbrowser.open("https://github.com/PhilZPhaZ")
        event.Skip()

    def on_event_select_first_units(self, event):  # wxGlade: ConversionApp.<event_handler>
        self._calculate_converted_value(event)

    def on_event_select_second_units(self, event):  # wxGlade: ConversionApp.<event_handler>
        self._calculate_converted_value(event)

    # TODO Rename this here and in `on_event_select_first_units` and `on_event_select_second_units`
    def _calculate_converted_value(self, event):
        with contextlib.suppress(ValueError):
            self.first_value_index = list(self.length.values())[
                self.value_units.GetCurrentSelection()
            ]
            self.converted_first_value = (
                int(self.value_input.GetValue()) * self.first_value_index
            )
            self.second_value_index = list(self.length.values())[
                self.convert_unit_input.GetCurrentSelection()
            ]
            self.converted = self.converted_first_value / self.second_value_index
            self.converted_unit = list(self.length.keys())[
                self.convert_unit_input.GetCurrentSelection()
            ]
            self.result_result.Clear()
            self.result_result.write(str(self.converted))
            self.result_units.Clear()
            self.result_units.write(self.converted_unit)
        event.Skip()

# end of class ConversionApp

class ConvertionApp(wx.App):
    def OnInit(self):
        self.frame = ConversionApp(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class ConvertionApp

if __name__ == "__main__":
    app = ConvertionApp(0)
    app.MainLoop()
