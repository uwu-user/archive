# ba_meta require api 6


#==============================================================================#             
#     
#     Demo version v1.0
#     Create by Unknown_#7004 
#     Github https://github.com/uwu-user/Bs-console
#
#==============================================================================#             


from __future__ import annotations
from typing import TYPE_CHECKING, cast

import ba
import _ba
import math
import os
import shutil
import json
import sys
import random
import pipes as pip # hm 
import subprocess, platform
from subprocess import call
from time import gmtime, strftime
from bastd.ui import party
from bastd.ui.party import PartyWindow
from bastd.ui.mainmenu import MainMenuWindow
from bastd.ui.popup import PopupMenuWindow, PopupWindow, PopupMenu
from bastd.ui.mainmenu import MainMenuWindow

if TYPE_CHECKING:
    from typing import Any, Sequence, Callable, List, Dict, Tuple, Optional, Union

#==============================================================================#             

_testN = "1371"
_version = "1.0"
_by = "Unknown_#7004"

#==============================================================================#             

# Colors (edit it or use ColorScheme.py)  :3
_text_color = (1,1,1)
_buttons_color = (0,0,0)
_root_color = (0.4, 0.4, 0.4)
_scroll_color = (0,0,0)

#==============================================================================#             

# console Config   

console_config = {
   'log': "Empty",
   'console_colors_type': True,
   'console_color': (1,1,1),
   'console_time': True,
   'console_save': False,
   'save_file_type_text': '.txt'
}


# Config

if "console" in ba.app.config:
    old_config = ba.app.config["console"]

    for setting in console_config:
        if setting not in old_config:
            ba.app.config["console"] = console_config
else:
    ba.app.config["console"] = console_config
ba.app.config.apply_and_commit()


# Reset config

reset_console_config = {
   'log': "Empty",
   'console_colors_type': True,
   'console_color': (1,1,1),
   'console_time': True,
   'console_save': False,
   'save_file_type_text': '.txt'
}

if "reset_console" in ba.app.config:
    old_config = ba.app.config["reset_console"]

    for setting in reset_console_config:
        if setting not in old_config:
            ba.app.config["reset_console"] = reset_console_config
else:
    ba.app.config["reset_console"] = reset_console_config
ba.app.config.apply_and_commit()

# config <sys:Not - save - it>

old_console_config= {
   'log': "Empty",
   'console_colors_type': True,
   'console_color': (1,1,1),
   'console_time': True,
   'console_save': False,
   'save_file_type_text': '.txt'
}

if "old_console" in ba.app.config:
    old_config = ba.app.config["old_console"]

    for setting in old_console_config:
        if setting in old_config:
            ba.app.config["old_console"] = old_console_config
else:
    ba.app.config["old_console"] = old_console_config
ba.app.config.apply_and_commit()
  
#==============================================================================#             
 
# file type [.py, .json, .txt, .log]
file_format = ba.app.config["console"]["save_file_type_text"]

#==============================================================================#             
 
   
# file name - Rename it?

_format = "%Y-%m-%d"
file_name = "»" + strftime("『"+ _format + "』", gmtime()) + "«"

#==============================================================================#             

py_user = _ba.env()['python_directory_user']
folder_name = '/log/'
save_log_file = py_user + folder_name + file_name + file_format

def installFiles():      
       if not os.path.exists(py_user + folder_name):
        os.makedirs(py_user + folder_name)
       if not os.path.exists(save_log_file):
        with open(save_log_file, 'w') as f:
            data = py_user + folder_name + " -Done- "
            json.dump(data, f)
            f.close()

#==============================================================================#             
      
      
# About                 
class AboutWindow(ba.Window):
   def __init__(self, origin: Sequence[float] = (0, 0)):
     
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         color=_root_color,
                         scale=2.0,
                         size=(240, 100),
                         stack_offset=(0, -10))
     
     # About
     self.about = ba.textwidget(parent=self._root_widget,
                          position=(130, 80),
                          size=(0, 0),
                          scale=1,
                          color=_text_color,
                          maxwidth=100,
                          text="» About",
                          h_align='center',
                          v_align='center')
    
     # About logo                       
     self.about_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(25, 25),
                                     position=(60, 70),
                                     texture=ba.gettexture('logIcon'))         
                                     
     # devs
     self.about = ba.textwidget(parent=self._root_widget,
                          position=(120, 40),
                          size=(0, 0),
                          scale=1,
                          color=_text_color,
                          maxwidth=190,
                          text="» Demo version " + _version + " (test: " + _testN + ")",
                          h_align='center',
                          v_align='center')
                                                                     
     # back
     self._back_button = btn = ba.buttonwidget(parent=self._root_widget,
                                      autoselect=True,
                                      position=(18.5, 68),
                                      size=(30, 30),
                                      scale=1.1,
                                      on_activate_call=self._back,
                                      label=ba.charstr(ba.SpecialChar.BACK),
                                      button_type='backSmall')
     ba.containerwidget(edit=self._root_widget, cancel_button=btn)
                                 
    # back  Activate                            
   def _back(self):
        ba.containerwidget(edit=self._root_widget, transition='out_scale')
        
#==============================================================================#             
                    
# Credits                                  
class CreditsWindow(ba.Window):
   def __init__(self, origin: Sequence[float] = (0, 0)):
     
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         color=_root_color,
                         scale=2.0,
                         size=(240, 100),
                         stack_offset=(0, -10))
     
     # Credits
     self.credits = ba.textwidget(parent=self._root_widget,
                          position=(140, 80),
                          size=(0, 0),
                          scale=1,
                          color=_text_color,
                          maxwidth=100,
                          text="» Credits",
                          h_align='center',
                          v_align='center')
    
     # Credits logo                       
     self.credits_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(25, 25),
                                     position=(60, 70),
                                     texture=ba.gettexture('star'))         
                                     
     # devs
     self.devs = ba.textwidget(parent=self._root_widget,
                          position=(120, 40),
                          size=(0, 0),
                          scale=1,
                          color=_text_color,
                          maxwidth=190,
                          text="» Create by Unknown_#7004",
                          h_align='center',
                          v_align='center')
                                                                     
     # back
     self._back_button = btn = ba.buttonwidget(parent=self._root_widget,
                                      autoselect=True,
                                      position=(18.5, 68),
                                      size=(30, 30),
                                      scale=1.1,
                                      on_activate_call=self._back,
                                      label=ba.charstr(ba.SpecialChar.BACK),
                                      button_type='backSmall')
     ba.containerwidget(edit=self._root_widget, cancel_button=btn)
     
   # back  Activate
   def _back(self):
        ba.containerwidget(edit=self._root_widget, transition='out_scale')
             
#==============================================================================#             
          
# Help                             
class HelpWindow(ba.Window):
   def __init__(self, origin: Sequence[float] = (0, 0)):
   	
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         color=_root_color,
                         scale=2.0,
                         size=(540, 250),
                         stack_offset=(0, -10))
     
     # Scroll widget
     self._scrollwidget = ba.scrollwidget(parent=self._root_widget,
                                      size=(480, 180),
                                      position=(25, 30),
                                      color=_scroll_color)                  
     self._subcontainer = ba.containerwidget(parent=self._scrollwidget, background=False)
        
     # Help
     self.help_text= ba.textwidget(parent=self._root_widget,
                          position=(125, 230),
                          size=(0, 0),
                          scale=1,
                          color=_text_color,
                          maxwidth=100,
                          text="» Help",
                          h_align='center',
                          v_align='center')
    
     # Help logo                       
     self.help_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(25, 25),
                                     position=(60, 217),
                                     texture=ba.gettexture('achievementEmpty'))                                                               

     # help message
     self.devs = ba.textwidget(parent=self._subcontainer,
                          position=(40, -10),
                          size=(0, 0),
                          scale=1,
                          color=_text_color,
                          maxwidth=80,
                          text="» not yet",
                          h_align='center',
                          v_align='center')
               
     # back
     self._back_button = btn = ba.buttonwidget(parent=self._root_widget,
                                      autoselect=True,
                                      position=(18.5, 218),
                                      size=(30, 30),
                                      scale=1.1,
                                      on_activate_call=self._back,
                                      label=ba.charstr(ba.SpecialChar.BACK),
                                      button_type='backSmall')
     ba.containerwidget(edit=self._root_widget, cancel_button=btn)
     
   # back Activate                          
   def _back(self):
        ba.containerwidget(edit=self._root_widget, transition='out_scale')
                                                  
 
#==============================================================================#             
  
# settings      
class SettingsWindow(ba.Window):
   def __init__(self, origin: Sequence[float] = (0, 0)):
     
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         color=_root_color,
                         scale=2.0,
                         size=(600, 300),
                         stack_offset=(0, -10))
     
     # Settings
     self._settings = ba.textwidget(parent=self._root_widget,
                          position=(140, 280),
                          size=(0, 0),
                          scale=1,
                          color=_text_color,
                          maxwidth=100,
                          text="» Settings",
                          h_align='center',
                          v_align='center')
    
     # Settings logo                       
     self._settings_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(25, 25),
                                     position=(61, 265),
                                     texture=ba.gettexture('settingsIcon'))                                                               
     
     # back
     self._back_button = btn = ba.buttonwidget(parent=self._root_widget,
                                      autoselect=True,
                                      position=(12, 240),
                                      size=(30, 30),
                                      scale=1.1,
                                      on_activate_call=self.cancel_settings,
                                      label=ba.charstr(ba.SpecialChar.BACK),
                                      button_type='backSmall')
     ba.containerwidget(edit=self._root_widget, cancel_button=btn)
                                       
     # Console Colors   
     self.Console_colors = ba.checkboxwidget(parent=self._root_widget,
                text="Console Colors", 
                value=ba.app.config["console"]["console_colors_type"],
                maxwidth=80,
                color=_buttons_color,
                on_value_change_call=ba.Call(self.save_settingsV1, "console_colors_type"),
                position=(60, 219),
                size=(200, 50),
                textcolor=(1,1,1))
                
     # Console Time
     self.Console_time = ba.checkboxwidget(parent=self._root_widget,
                text="Show Time", 
                value=ba.app.config["console"]["console_time"],
                maxwidth=80,
                color=_buttons_color,
                on_value_change_call=ba.Call(self.save_settingsV1, "console_time"),
                position=(60, 185),
                size=(200, 50),
                textcolor=(1,1,1)) 
      
     # save file type text
     self.save_file_type_text = ba.textwidget(parent=self._root_widget,
                          position=(120, 155),
                          size=(0, 0),
                          scale=1,
                          color=_text_color,
                          maxwidth=120,
                          text="save file type: ",
                          h_align='center',
                          v_align='center')
      
      # files format
     save_list = [".py",".json",".txt",".log"]
     dis_save_list = [".py",".json",".txt",".log"]
     
     # save file menu
     save_list_ch = PopupMenu(parent=self._root_widget,
                        position=(40, 80),
                        width=100,
                        scale=2.0,
                        choices=save_list,
                        choices_display=self._create_list(dis_save_list),
                        current_choice=ba.app.config["console"]["save_file_type_text"],
                        on_value_change_call=self.save_settingsV2)
     
     # save button
     self.save_button = ba.buttonwidget(parent=self._root_widget,
                                      color=_buttons_color,
                                      position=(425, 70),
                                      size=(220, 50),
                                      label='Save',
                                      on_activate_call=self.save_settings,
                                      button_type='regular',
                                      scale=0.55) 
      
     # Cancel button   
     self.cancel_button = ba.buttonwidget(parent=self._root_widget,
                                      color=_buttons_color,
                                      position=(425, 40),
                                      size=(220, 50),
                                      label='Cancel',
                                      on_activate_call=self.cancel_settings,
                                      button_type='regular',
                                      scale=0.55)
      
   def _create_list(self, m):
        return (ba.Lstr(value=i) for i in m)
    
   def save_settingsV1(self, settings, m):
        ba.app.config["old_console"][settings] = False if m==0 else True
        ba.app.config.apply_and_commit()
    
   def save_settingsV2(self, m):
        ba.app.config["old_console"]["save_file_type_text"] = m
        ba.app.config.apply_and_commit()
        
   def save_settings(self):
       if not ba.app.config["console"]["console_colors_type"] == ba.app.config["old_console"]["console_colors_type"]:
            ba.app.config["console"]["console_colors_type"] = ba.app.config["old_console"]["console_colors_type"]
            ba.app.config.apply_and_commit()
            ba.containerwidget(edit=self._root_widget, transition='out_scale')
       if not ba.app.config["console"]["console_time"] == ba.app.config["old_console"]["console_time"]:
            ba.app.config["console"]["console_time"] = ba.app.config["old_console"]["console_time"]
            ba.app.config.apply_and_commit()
            ba.containerwidget(edit=self._root_widget, transition='out_scale')
       if not ba.app.config["console"]["save_file_type_text"] == ba.app.config["old_console"]["save_file_type_text"]:
            ba.app.config["console"]["save_file_type_text"] = ba.app.config["old_console"]["save_file_type_text"]
            ba.app.config.apply_and_commit()
            ba.screenmessage("You must restart the game for this to take effect.", color=(1.0, 0.5, 0.0)) # not yet
            ba.screenmessage("log will be saved in the old file, if you do not restart the game.", color=(1.0, 0.5, 0.0)) # fixed in v1.1
            ba.containerwidget(edit=self._root_widget, transition='out_scale')
       if ba.app.config["console"]["console_colors_type"] == ba.app.config["old_console"]["console_colors_type"] and ba.app.config["console"]["console_time"] == ba.app.config["old_console"]["console_time"] and ba.app.config["console"]["save_file_type_text"] == ba.app.config["old_console"]["save_file_type_text"]:
            ba.containerwidget(edit=self._root_widget, transition='out_scale')
            
   def cancel_settings(self):
       if not ba.app.config["old_console"]["console_colors_type"] == ba.app.config["reset_console"]["console_colors_type"]:
            ba.app.config["old_console"]["console_colors_type"] = ba.app.config["reset_console"]["console_colors_type"]
            ba.app.config.apply_and_commit()
            ba.containerwidget(edit=self._root_widget, transition='out_scale')
       if not ba.app.config["old_console"]["console_time"] == ba.app.config["reset_console"]["console_time"]:
            ba.app.config["old_console"]["console_time"] = ba.app.config["reset_console"]["console_time"]
            ba.app.config.apply_and_commit()
            ba.containerwidget(edit=self._root_widget, transition='out_scale')
       if not ba.app.config["old_console"]["save_file_type_text"] == ba.app.config["reset_console"]["save_file_type_text"]:
            ba.app.config["old_console"]["save_file_type_text"] = ba.app.config["reset_console"]["save_file_type_text"]
            ba.app.config.apply_and_commit()
            ba.containerwidget(edit=self._root_widget, transition='out_scale')
       if ba.app.config["old_console"]["console_colors_type"] == ba.app.config["reset_console"]["console_colors_type"] and ba.app.config["old_console"]["console_time"] == ba.app.config["reset_console"]["console_time"] and ba.app.config["old_console"]["save_file_type_text"] == ba.app.config["reset_console"]["save_file_type_text"]:
        	ba.containerwidget(edit=self._root_widget, transition='out_scale')    

   # back  Activate                                                 
   def _back(self):
        ba.containerwidget(edit=self._root_widget, transition='out_scale')

#==============================================================================#             
                             
send_log = print
                            
#==============================================================================#             
                           
class logWindow(ba.Window):
   def __init__(self, origin: Sequence[float] = (0, 0)):      
     if ba.app.config["console"]["console_colors_type"] == True and ba.app.config["console"]["console_time"] == True:
     	self.Console_S_Time_Color()
     elif ba.app.config["console"]["console_colors_type"] == False and ba.app.config["console"]["console_time"] == True:
     	self.Console_S_Time()
     elif ba.app.config["console"]["console_colors_type"] == True and ba.app.config["console"]["console_time"] == False:
     	self.Console_S_Color()
     elif ba.app.config["console"]["console_colors_type"] == False and ba.app.config["console"]["console_time"] == False:
     	self.Console_S()
     else: self.Console_S()
     
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         color=_root_color,
                         scale=2.0,
                         size=(660, 350),
                         stack_offset=(0, -10))
        
     # Scroll widget
     self._scrollwidget = ba.scrollwidget(parent=self._root_widget,
                                      size=(560, 280),
                                      position=(55, 38),
                                      color=_scroll_color)                    
     self._subcontainer = ba.containerwidget(parent=self._scrollwidget, size=(660, 280), background=False, claims_left_right=False, claims_tab=False)
          
     # Console
     self.console = ba.textwidget(parent=self._root_widget,
                          position=(145, 330),
                          size=(0, 0),
                          scale=1,
                          color=_text_color,
                          maxwidth=125,
                          text="» Console log " + _version + " (test)",
                          h_align='center',
                          v_align='center')
    
     # Console logo                       
     self.console_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(25, 25),
                                     position=(60, 317),
                                     texture=ba.gettexture('logo'))
                 
     # back
     self._back_button = btn = ba.buttonwidget(parent=self._root_widget,
                                      autoselect=True,
                                      position=(12, 240),
                                      size=(30, 30),
                                      scale=1.1,
                                      on_activate_call=self._back,
                                      label=ba.charstr(ba.SpecialChar.BACK),
                                      button_type='backSmall')
     ba.containerwidget(edit=self._root_widget, cancel_button=btn)
    
     # Settings                              
     self.settings_button = ba.buttonwidget(parent=self._root_widget,
                                      color=_buttons_color,
                                      position=(7, 185),
                                      size=(70, 70),
                                      on_activate_call=SettingsWindow,
                                      label='',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)
     self.settings_button_icon = ba.imagewidget(parent=self._root_widget,
                                     size=(35, 35),
                                     draw_controller=self.settings_button,
                                     position=(9, 186.5),
                                     texture=ba.gettexture('settingsIcon'))  

     # Replay                         
     self.replay_button = ba.buttonwidget(parent=self._root_widget,
                                      color=_buttons_color,
                                      position=(7, 140),
                                      size=(70, 70),
                                      on_activate_call=self.refresh_button,
                                      label='',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)
     self.replay_button_icon = ba.imagewidget(parent=self._root_widget,
                                     size=(35, 35),
                                     draw_controller=self.replay_button,
                                     position=(9, 141.5),
                                     texture=ba.gettexture('replayIcon'))                              

     # help 
     self.help_button = ba.buttonwidget(parent=self._root_widget,
                                      color=_buttons_color,
                                      position=(7, 95),
                                      size=(70, 70),
                                      on_activate_call=HelpWindow,
                                      label='',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)
     self.help_button_icon = ba.imagewidget(parent=self._root_widget,
                                     size=(35, 35),
                                     draw_controller=self.help_button,
                                     position=(8, 96.5),
                                     texture=ba.gettexture('achievementEmpty'))                              
      
     # About                     
     self.about_button = ba.buttonwidget(parent=self._root_widget,
                                      color=_buttons_color,
                                      position=(11, 55),
                                      size=(50, 50),
                                      on_activate_call=AboutWindow,
                                      label='',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)
     self.about_button_icon = ba.imagewidget(parent=self._root_widget,
                                     size=(27, 27),
                                     draw_controller=self.about_button,
                                     position=(11.5, 55.5),
                                     texture=ba.gettexture('logIcon'))                              
                                                                        
     # Credits
     self.credits_button = ba.buttonwidget(parent=self._root_widget,
                                      color=_buttons_color,
                                      position=(65, 8),
                                      size=(50, 50),
                                      on_activate_call=CreditsWindow,
                                      label='',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)
     self.credits_button_icon = ba.imagewidget(parent=self._root_widget,
                                     size=(27, 27),
                                     draw_controller=self.credits_button,
                                     position=(65.5, 8.5),
                                     texture=ba.gettexture('star'))                                                           
      
     # Copy
     self.test_button = ba.buttonwidget(parent=self._root_widget,
                                      color=_buttons_color,
                                      position=(110, 8),
                                      size=(198, 50),
                                      on_activate_call=self.console_copy,
                                      label='Copy',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55) 
                                      
     # Show Time
     self.test_button = ba.buttonwidget(parent=self._root_widget,
                                      color=_buttons_color,
                                      position=(220, 8),
                                      size=(198, 50),
                                      on_activate_call=self.show_time,
                                      label='Show Time',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55) 
                         
     # delete
     self.delete_button = ba.buttonwidget(parent=self._root_widget,
                                      color=_buttons_color,
                                      position=(330, 8),
                                      size=(198, 50),
                                      on_activate_call=self.delete_log,
                                      label='delete log',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)
                        
    # Save                                                              
     self.save_button = ba.buttonwidget(parent=self._root_widget,
                                      color=_buttons_color,
                                      position=(440, 8),
                                      size=(198, 50),
                                      on_activate_call=self.save_log,
                                      label='save to ' + ba.app.config["console"]["save_file_type_text"] + ' file',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)       
   
     # log 
     self.log = ba.textwidget(parent=self._subcontainer,
                                      scale=0.5,
                                      color=ba.app.config["console"]["console_color"],
                                      text=ba.app.config["console"]["log"],
                                      size=(0, 0),
                                      autoselect=True,
                                      position=(1, 247),
                                      maxwidth=800.0,
                                      h_align='left',
                                      v_align='center')
 
#==============================================================================#             
                                     
     if not _ba.getlog() == "" and not ba.app.config["console"]["log"] == "" and not ba.app.config["console"]["log"] == "Empty" and ba.app.config["console"]["console_save"] == False:	
         ba.textwidget(parent=self._subcontainer, edit=self.log, position=(1, 250 + (len(ba.textwidget(query=self.log))/8)))                                
         ba.containerwidget(edit=self._subcontainer, size=(660, 280 + (len(ba.textwidget(query=self.log))/4)))
     else:
         ba.textwidget(parent=self._subcontainer, edit=self.log, position=(1, 247))                                
         ba.containerwidget(edit=self._subcontainer, size=(660, 280))
  
#==============================================================================#             
       
   # Colors=true, Time=true,
   def Console_S_Time_Color(self):
       if not _ba.getlog() == "" and not ba.app.config["console"]["log"] == "" and not ba.app.config["console"]["log"] == "Empty" and ba.app.config["console"]["console_save"] == False:
           ba.app.config["console"]["log"] = strftime("[%Y/%m/%d] - [%B/%A] - [%w/7] - [%j/360day] - [%I:%M:%S %p] / [%H:%M:%S] (%z)", gmtime()) + "\n" + _ba.getlog()
           ba.app.config["console"]["console_color"] = (1,0,0)
           ba.app.config.apply_and_commit()
       elif ba.app.config["console"]["log"] == "Empty": # Console Welcome
           ba.app.config["console"]["log"] = strftime("[%Y/%m/%d] - [%B/%A] - [%w/7] - [%j/360day] - [%I:%M:%S %p] / [%H:%M:%S] (%z)", gmtime()) + "\n" + "» Oh Hello :3\n» Click the Replay icon to refresh the page :3"
           ba.app.config["console"]["console_color"] = (1,0,2)
           ba.app.config.apply_and_commit()
       elif ba.app.config["console"]["log"] == "": # Console deleted
           ba.app.config["console"]["log"] = strftime("[%Y/%m/%d] - [%B/%A] - [%w/7] - [%j/360day] - [%I:%M:%S %p] / [%H:%M:%S] (%z)", gmtime()) + "\n" + "» log deleted :3\n» Click the Replay icon to refresh the page :3\n» Or close the window and open it again :3"
           ba.app.config["console"]["console_color"] = (0,1,3)
           ba.app.config.apply_and_commit()
       else:
           ba.app.config["console"]["log"] = strftime("[%Y/%m/%d] - [%B/%A] - [%w/7] - [%j/360day] - [%I:%M:%S %p] / [%H:%M:%S] (%z)", gmtime()) + "\n" + "» No error found yet\n» Click the Replay icon to refresh the page :3\n» Or close the window and open it again :3"
           ba.app.config["console"]["console_color"] = (0,1,0) 
           ba.app.config.apply_and_commit()
           
   # Colors=false, time=true       
   def Console_S_Time(self):
       if not _ba.getlog() == "" and not ba.app.config["console"]["log"] == "" and not ba.app.config["console"]["log"] == "Empty" and ba.app.config["console"]["console_save"] == False:
           ba.app.config["console"]["log"] = strftime("[%Y/%m/%d] - [%B/%A] - [%w/7] - [%j/360day] - [%I:%M:%S %p] / [%H:%M:%S] (%z)", gmtime()) + "\n" + _ba.getlog()
           ba.app.config["console"]["console_color"] = (1,1,1)
           ba.app.config.apply_and_commit()
       elif ba.app.config["console"]["log"] == "Empty": # Console Welcome
           ba.app.config["console"]["log"] = strftime("[%Y/%m/%d] - [%B/%A] - [%w/7] - [%j/360day] - [%I:%M:%S %p] / [%H:%M:%S] (%z)", gmtime()) + "\n" + "» Oh Hello :3\n» Click the Replay icon to refresh the page :3"
           ba.app.config["console"]["console_color"] = (1,1,1)
           ba.app.config.apply_and_commit()
       elif ba.app.config["console"]["log"] == "": # Console deleted
           ba.app.config["console"]["log"] = strftime("[%Y/%m/%d] - [%B/%A] - [%w/7] - [%j/360day] - [%I:%M:%S %p] / [%H:%M:%S] (%z)", gmtime()) + "\n" + "» log deleted :3\n» Click the Replay icon to refresh the page :3\n» Or close the window and open it again :3"
           ba.app.config["console"]["console_color"] = (1,1,1)
           ba.app.config.apply_and_commit()
       else:
           ba.app.config["console"]["log"] = strftime("[%Y/%m/%d] - [%B/%A] - [%w/7] - [%j/360day] - [%I:%M:%S %p] / [%H:%M:%S] (%z)", gmtime()) + "\n" + "» No error found yet\n» Click the Replay icon to refresh the page :3\n» Or close the window and open it again :3"
           ba.app.config["console"]["console_color"] = (1,1,1) 
           ba.app.config.apply_and_commit()
           
   # Colors=true, Time=false  
   def Console_S_Color(self):
       if not _ba.getlog() == "" and not ba.app.config["console"]["log"] == "" and not ba.app.config["console"]["log"] == "Empty" and ba.app.config["console"]["console_save"] == False:
           ba.app.config["console"]["log"] = _ba.getlog()
           ba.app.config["console"]["console_color"] = (1,0,0)
           ba.app.config.apply_and_commit()
       elif ba.app.config["console"]["log"] == "Empty": # Console Welcome
           ba.app.config["console"]["log"] = "» Oh Hello :3\n» Click the Replay icon to refresh the page :3"
           ba.app.config["console"]["console_color"] = (1,0,2)
           ba.app.config.apply_and_commit()
       elif ba.app.config["console"]["log"] == "": # Console deleted
           ba.app.config["console"]["log"] = "» log deleted :3\n» Click the Replay icon to refresh the page :3\n» Or close the window and open it again :3"
           ba.app.config["console"]["console_color"] = (0,1,3)
           ba.app.config.apply_and_commit()
       else:
           ba.app.config["console"]["log"] = "» No error found yet\n» Click the Replay icon to refresh the page :3\n» Or close the window and open it again :3"
           ba.app.config["console"]["console_color"] = (0,1,0) 
           ba.app.config.apply_and_commit() 
        
   # Colors=false, Time=false  
   def Console_S(self):
       if not _ba.getlog() == "" and not ba.app.config["console"]["log"] == "" and not ba.app.config["console"]["log"] == "Empty" and ba.app.config["console"]["console_save"] == False:
           ba.app.config["console"]["log"] = _ba.getlog()
           ba.app.config["console"]["console_color"] = (1,1,1)
           ba.app.config.apply_and_commit()
       elif ba.app.config["console"]["log"] == "Empty": # Console Welcome
           ba.app.config["console"]["log"] = "» Oh Hello :3\n» Click the Replay icon to refresh the page :3"
           ba.app.config["console"]["console_color"] = (1,1,1)
           ba.app.config.apply_and_commit()
       elif ba.app.config["console"]["log"] == "": # Console deleted
           ba.app.config["console"]["log"] = "» log deleted :3\n» Click the Replay icon to refresh the page :3\n» Or close the window and open it again :3"
           ba.app.config["console"]["console_color"] = (1,1,1)
           ba.app.config.apply_and_commit()
       else:
           ba.app.config["console"]["log"] = "» No error found yet\n» Click the Replay icon to refresh the page :3\n» Or close the window and open it again :3"
           ba.app.config["console"]["console_color"] = (1,1,1) 
           ba.app.config.apply_and_commit() 

#==============================================================================#             
    
   # save log type
   def save_log(self):
       if not _ba.getlog() == "" and not ba.app.config["console"]["log"] == "" and not ba.app.config["console"]["log"] == "Empty" and ba.app.config["console"]["console_save"] == False:
           self.save_log_now()
       else:
           ba.screenmessage('» Nothing to save it?', (1, 0, 0))
           ba.playsound(ba.getsound('ticking'))
        
    # save log   
   def save_log_now(self) -> None:
      try:
          with open(save_log_file, 'w') as f:
              f.write(ba.app.config["console"]["log"])
              f.close()
              ba.playsound(ba.getsound("fanfare"))
              send_log('[?] » ' + strftime("『%I:%M:%S %p』/ 『%H:%M:%S』(%z)", gmtime()) + ', file saved it ' + ba.app.config["console"]["save_file_type_text"] + ' format')
      except:
          ba.print_exception()
          ba.screenmessage('» Error', (1, 0, 0))
          ba.playsound(ba.getsound("ticking"))
     
   # delete log
   def delete_log(self):
       if not _ba.getlog() == "" and not ba.app.config["console"]["log"] == "" and not ba.app.config["console"]["log"] == "Empty" and ba.app.config["console"]["console_save"] == False:
           ba.screenmessage('» deleted', (0, 1, 0))
           ba.playsound(ba.getsound("hiss"))
           ba.app.config["console"]["log"] = ""
           os.system('cls' if os.name == 'nt' else 'clear') # not work in Android
           send_log('[?] » ' + strftime("『%I:%M:%S %p』/ 『%H:%M:%S』(%z)", gmtime()) + ', log deleted')
           ba.app.config.apply_and_commit()
       else:
           ba.screenmessage('» Nothing to delete it?', (1, 0, 0))
           ba.playsound(ba.getsound('ticking'))
            
    # time
   def show_time(self):
   	    #send_log('[?]» ' + strftime("『%I:%M:%S %p』/ 『%H:%M:%S』(%z)", gmtime())) #no, its bad
       	ba.screenmessage(strftime("[%I:%M:%S %p] / [%H:%M:%S] (%z)", gmtime()))
       	ba.playsound(ba.getsound("laser"))

   # Copy
   def console_copy(self):
       if not _ba.getlog() == "" and not ba.app.config["console"]["log"] == "" and not ba.app.config["console"]["log"] == "Empty" and ba.app.config["console"]["console_save"] == False:
           ba.clipboard_set_text(ba.app.config["console"]["log"])
           send_log('[?] » ' + strftime("『%I:%M:%S %p』/ 『%H:%M:%S』(%z)", gmtime()) + ', copied to clipboard.')
           ba.playsound(ba.getsound("woodDebrisFall"))
       else:
           ba.screenmessage('» Nothing to copy it?', (1, 0, 0))
           ba.playsound(ba.getsound('ticking'))
    
   # Refresh
   def refresh_button(self):
           ba.playsound(ba.getsound("warnBeeps"))
           ba.containerwidget(edit=self._root_widget, transition='out_scale')
           logWindow()
         
   # back  Activate                                                 
   def _back(self):
        ba.containerwidget(edit=self._root_widget, transition='out_scale')
        ba.app.ui.set_main_menu_window(MainMenuWindow(transition='in_left').get_root_widget())


#==============================================================================#                 
                            
def Call_log(self):
       ba.containerwidget(edit=self._root_widget,transition='out_left')
       logWindow()

#==============================================================================#             

# ba_meta export plugin
class log(ba.Plugin):
  #if platform == 'android':                   ok no
    MainMenuWindow._old_refresh = MainMenuWindow._refresh
    def _new_refresh(self) -> None:
        self._old_refresh()
        if not self._in_game:
            uiscale = ba.app.ui.uiscale
            extra_y = 100 if uiscale is ba.UIScale.SMALL else 0
            this_b_width = self._button_width * 0.25 * 1.7
            this_b_height = self._button_height * 0.82 * 1.7
            self._button = tb = ba.buttonwidget(
                parent=self._root_widget,
                position=(625, 160 + extra_y*0.55),
                size=(this_b_width - 37, this_b_height - 37),
                autoselect=self._use_autoselect,
                button_type='square',
                label='',
                transition_delay=self._tdelay,
                on_activate_call=ba.Call(Call_log ,self))
            icon_size = this_b_width * 0.5
            ba.imagewidget(parent=self._root_widget,
                           size=(icon_size, icon_size),
                           draw_controller=tb,
                           transition_delay=self._tdelay,
                           position=(628, 160 + extra_y*0.55),
                           texture=ba.gettexture('settingsIcon'))
    MainMenuWindow._refresh = _new_refresh
    
    #files
    def __init__(self):
    	installFiles()