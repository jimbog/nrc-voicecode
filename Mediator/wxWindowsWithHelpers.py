##############################################################################
# VoiceCode, a programming-by-voice environment
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
# (C)2002, National Research Council of Canada
#
##############################################################################

"""Subclasses of various wx.Python widgets with additional helper methods.

Among other things, those helper methods are useful for unit testing GUIs

"""

import wx
import util
import debug


class CanBeSentKeys:
    def __init__(self):
       pass
       
    def SendKey(self, key_code):
        key_event = wx.KeyEvent(wx.EVT_CHAR)
        key_event.m_keyCode = key_code
        self.ProcessEvent(key_event)

class wxTextCtrlWithHelpers(wx.TextCtrl):
    def __init__(self, id, init_value, pos, size, style):
       wx.TextCtrl.__init__(self, id, init_value, pos, size, style)

       
    def GetANSIValue(self):
       value = self.GetValue() 
       if util.wx.Python_is_unicode_build():
          value.encode("ascii", "ignore")
       return value
       

class wxButtonWithHelpers(wx.Button):
    """A wx.Button with methods for simulating user actions on it.
    """
    def __init__(self, parent, ID, Caption, position, size):
        wx.Button.__init__(self, parent, ID, Caption, position, size)
    
    def Click(self):
        click_event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, self.GetId())
        self.ProcessEvent(click_event)

class wxListCtrlWithHelpers(wx.ListCtrl, CanBeSentKeys):
    """A wx.ListCtrl subclass with helpers for finding more about the data
    that is displayed in it.
    """
    def __init__(self, frame, id, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_SINGLE_SEL):
       wx.ListCtrl.__init__(self, frame, id, pos, size, style)
       CanBeSentKeys.__init__(self)
        
    def GetCellContentsString(self, row, column ):
       return self.GetItem(row, column).m_text
    
    def NumberOfColumns(self):
       num_cols = 0
       while(1):
          col = self.GetColumn(num_cols)
          if col:
             num_cols = num_cols + 1
          else:
             break
       return num_cols

    def NumberOfRows(self):
       return self.GetItemCount()
       
    def AllCellsContentsString(self):
       contents = []
       for row_num in range(self.NumberOfRows()):
          row = []
          for col_num in range(self.NumberOfColumns()):
             row.append(self.GetCellContentsString(row_num, col_num))
          contents.append(row)
       return contents
       
    def GetColumnContents(self, col_num):
       contents = []
       for row_num in range(self.NumberOfRows()):
          contents.append(self.GetCellContentsString(row_num, col_num))
       return contents
       
   
    def ActivateNth(self, nth):
       """activates the nth item in the list and invokes the appropriate 
       event handler.
       
       Note: This  is not the same as self.Select(nth), because the later
       changes the selection without invoking the selection event handler.
       """   
       self.Select(nth)
       evt = wx.ListEvent(wx.EVT_COMMAND_LIST_ITEM_ACTIVATED, self.GetId())
       
       # AD: This fails in wx.Python < 2.5 (m_itemIndex is private attribute)
       evt.m_itemIndex = nth

       self.ProcessEvent(evt)
              
    def HandleUpOrDownArrow(self, keycode):
       """Invoke this with an up or down arrow character to move cursor
       up or down the list.
       
       **INPUTS**
       
       *INT keycode* -- the code for the key.
       
       **OUTPUTS**
       
       *INT direction* -- 1 or -1 depending on the direction of the key. If None, 
       then the key was not an arrow key.she
       
       **SIDE EFFECTS**
       
       If the key was an arrow key, moves the cursor up or down the list.
       """
       direction = None       
       if keycode == wx.WXK_UP:
           direction = -1
       elif keycode == wx.WXK_DOWN:
           direction = 1

       if direction:
          row_index = self.GetFirstSelected() + direction
          if row_index >= 0 and row_index < self.NumberOfRows():
              self.Select(row_index)

       return direction
               
class MockListSelectionEvent(wx.ListEvent):
    def __init__(self, nth):
       wx.ListEvent.__init__(self)
       self.nth = nth

    def GetIndex(self):
       return self.nth
       
class Mock_wxListActivationEvent(wx.ListEvent):
    def __init__(self, list_id, item_index):
       wx.ListEvent.__init__(self, wx.EVT_COMMAND_LIST_ITEM_ACTIVATED, list_id)
       self._itemIndex = item_index
       
    def GetIndex(self):
       return self._itemIndex
       
class wxDialogWithHelpers(wx.Dialog):
    """a frame subclass with methods for simulating user events being
    done on elements of the frame (ex: button clicks)"""
    
    def __init__(self, parent, id, title, pos, size, style):
       wx.Dialog.__init__(self, parent, id, title, pos, size, style)
       
    def ClickButton(self, button):
        """simulate the event of a user clicking on a button
        
        **INPUTS**
        
        *wx.Button button* -- the button to be clicked.
        """
        button_event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, button.GetId())
        button.ProcessEvent(button_event)
          
       
# defaults for vim - otherwise ignore
# vim:sw=4