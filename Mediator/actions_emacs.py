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
# (C)2000, National Research Council of Canada
#
##############################################################################

"""Actions specific for Emacs"""

from actions_gen import *
import debug
import sr_interface
import time

class ActionEmacsListBuffers(Action):
    """open the Emacs buffer list.

    **INSTANCE ATTRIBUTES**

    *none*
    """
    
    def __init__(self, **args_super):
        self.deep_construct(ActionEmacsListBuffers, 
                            {}, 
                            args_super, 
                            {})

    def execute(self, app, cont, state = None):
        """Execute the action.
        
        **INPUTS**
        
        [AppState] app -- Application on which to execute the action
        
        [Context] app_cont -- Context of the application that
        determines the parameters of how the action will be executed.

        [InterpState] state -- interface to the interpreter state
        
                
        **OUTPUTS**
        
        *none* -- 

        .. [AppState] file:///./AppState.AppState.html"""
        debug.trace('ActionEmacsListBuffers.execute', '** invoked')
        # AD: This is probably better handled through a new
        #     'switch_buffer_dlg' message type. But sending
        #     keys will do for now.
        app.app_change_buffer()
        debug.trace('ActionEmacsListBuffers.execute', 
                    '** app.curr_buffer().name()=%s' % app.curr_buffer().name())
#        ActionCompileSymbols().execute(app=app, cont=cont, state=state)


    def doc(self):
        """Returns a documentation string for the action.
        
        **INPUTS**
        
        *none* -- 
        

        **OUTPUTS**
        
        *none* -- 
        """
        return "Opens the Emacs buffer list."

        