# ba_meta require api 6


#==============================================================================#             
#     
#     Demo version v1.0
#     Create by Unknown_#7004 
#     Github https://github.com/uwu-user
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
from bastd.ui.settings import plugins

if TYPE_CHECKING:
    from typing import Any, Sequence, Callable, List, Dict, Tuple, Optional, Union

#==============================================================================#             

_testN = 2816
_version = 1.0
_by = "Unknown_#7004"

#==============================================================================#             

auto_delete_backup = True 
# backup the file, before deleted

#==============================================================================#             

py_user = _ba.env()['python_directory_user']
folder_name = '/backup/'
delete_folder = folder_name + '/.delete_backup/'

def installFiles():      
       if not os.path.exists(py_user + folder_name):
        os.makedirs(py_user + folder_name)
       if not os.path.exists(py_user + delete_folder):
        os.makedirs(py_user + delete_folder)
   
#==============================================================================#             
         
# Credits                                  
class CreditsWindow(ba.Window):
   def __init__(self, origin: Sequence[float] = (0, 0)):
     
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         scale=2.0,
                         size=(240, 100),
                         stack_offset=(0, -10))
     
     # Credits
     self.credits = ba.textwidget(parent=self._root_widget,
                          position=(140, 80),
                          size=(0, 0),
                          scale=1,
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
                          color=(1,1,1),
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
                         scale=2.0,
                         size=(540, 250),
                         stack_offset=(0, -10))
     
     # Scroll widget
     self._scrollwidget = ba.scrollwidget(parent=self._root_widget,
                                      size=(480, 180),
                                      position=(25, 30))                  
     self._subcontainer = ba.containerwidget(parent=self._scrollwidget, background=False)
        
     # Help
     self.help_text= ba.textwidget(parent=self._root_widget,
                          position=(125, 230),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
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
                          color=(1,1,1),
                          maxwidth=80,
                          text="» it's Empty?",
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
 
 
# About                 
class AboutWindow(ba.Window):
   def __init__(self, origin: Sequence[float] = (0, 0)):
     
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         scale=2.0,
                         size=(240, 100),
                         stack_offset=(0, -10))
     
     # About
     self.about = ba.textwidget(parent=self._root_widget,
                          position=(130, 80),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
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
                          color=(1,1,1),
                          maxwidth=190,
                          text="» Version " + str(_version) + " (test: " + str(_testN) + ")",
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
 
# delete the mod     
class DeleteModWindow(ba.Window):
   def __init__(self, availplug, origin: Sequence[float] = (0, 0)):
     
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         scale=2.0,
                         size=(290, 140),
                         stack_offset=(0, -10))
     
     pluging_name = (availplug.display_name).evaluate()
     path = _ba.env()['python_directory_user'] + "/" + pluging_name.split('.')[0] + ".py"
     
     # Settings
     self._settings = ba.textwidget(parent=self._root_widget,
                          position=(110, 120),
                          size=(0, 0),
                          scale=1,
                          maxwidth=100,
                          text="» Delete?",
                          h_align='center',
                          v_align='center')
    
     # Settings logo                       
     self._settings_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(25, 25),
                                     position=(31, 105),
                                     texture=ba.gettexture('settingsIcon'))                                                               
                                     
    # info
     self._info = ba.textwidget(parent=self._root_widget,
                          position=(120, 80),
                          size=(0, 0),
                          scale=6.5,
                          maxwidth=200,
                          text="» Are you sure to delete this file?",
                          h_align='center',
                          v_align='center')
                          
     # No button
     self.no_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(25, 20),
                                      size=(200, 60),
                                      label='No',
                                      on_activate_call=self._back,
                                      autoselect=True,
                                      scale=0.55)
                                      
    # Yes button
     self.yes_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(145, 20),
                                      size=(200, 60),
                                      label='Yes',
                                      on_activate_call=ba.Call(self.delete_backup, path, pluging_name),
                                      autoselect=True,
                                      scale=0.55)                            

   # Delete files backup
   def delete_backup(self, path, pluging_name):
      try:
          if os.path.exists(path) and os.path.isfile(path):
             if auto_delete_backup:
                shutil.copyfile(_ba.env()['python_directory_user'] + "/" + pluging_name.split('.')[0] + ".py", _ba.env()['python_directory_user'] + "/backup/.delete_backup/" + pluging_name.split('.')[0] + ".py")
                self.delete_it_now(path)
             else:
               self.delete_it_now(path)
          else:
              ba.screenmessage('» Error404', (1, 0, 0))
              ba.playsound(ba.getsound("ticking"))
      except:
          ba.print_exception()
          ba.screenmessage('» Error', (1, 0, 0))
          ba.playsound(ba.getsound("ticking"))         
      ba.containerwidget(edit=self._root_widget, transition='out_scale')
     
   # Delete Activate                                                 
   def delete_it_now(self, path): 
     os.remove(path)
     ba.screenmessage('» deleted', (0, 1, 0))
     ba.playsound(ba.getsound("hiss"))
     ba.containerwidget(edit=self._root_widget, transition='out_scale')

   # back  Activate                                              
   def _back(self):
        ba.containerwidget(edit=self._root_widget, transition='out_scale')

#==============================================================================#             
                                
# settings      
class SettingsWindow(ba.Window):
   def __init__(self, availplug, origin: Sequence[float] = (0, 0)):
     
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         scale=2.0,
                         size=(270, 230),
                         stack_offset=(0, -10))
                         
     pluging_name = (availplug.display_name).evaluate()
     path = _ba.env()['python_directory_user'] + "/" + pluging_name.split('.')[0] + ".py"
     
     # Settings
     self._settings = ba.textwidget(parent=self._root_widget,
                          position=(140, 220),
                          size=(0, 0),
                          scale=1,
                          maxwidth=100,
                          text="» Settings",
                          h_align='center',
                          v_align='center')
    
     # Settings logo                       
     self._settings_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(25, 25),
                                     position=(61, 205),
                                     texture=ba.gettexture('settingsIcon'))                                                               
     
     # delete button
     self.delete_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(20, 140),
                                      size=(420, 100),
                                      label='delete',
                                      on_activate_call=ba.Call(self.show_delete_mod_window, availplug, path),
                                      autoselect=True,
                                      button_type='regular',
                                      scale=0.55)
                                      
     # backup button
     self.backup_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(20, 80),
                                      size=(420, 100),
                                      label='backup',
                                      on_activate_call=ba.Call(self.do_backup, pluging_name),
                                      autoselect=True,
                                      button_type='regular',
                                      scale=0.55)                                 

     # RR button
     self.RR_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(20, 20),
                                      size=(420, 100),
                                      label='more?',
                                      on_activate_call=self.RR,
                                      autoselect=True,
                                      button_type='regular',
                                      scale=0.55)
                                      
     # back
     self._back_button = btn = ba.buttonwidget(parent=self._root_widget,
                                      autoselect=True,
                                      position=(12, 205),
                                      size=(30, 30),
                                      scale=1.1,
                                      on_activate_call=self._back,
                                      label=ba.charstr(ba.SpecialChar.BACK),
                                      button_type='backSmall')
     ba.containerwidget(edit=self._root_widget, cancel_button=btn)
       
   # delete Window call Activate                                                 
   def show_delete_mod_window(self, availplug, path):
        if os.path.exists(path) and os.path.isfile(path):
           DeleteModWindow(availplug)
           ba.containerwidget(edit=self._root_widget, transition='out_scale')
        else:
           ba.screenmessage('» Error404', (1, 0, 0))
           ba.playsound(ba.getsound("ticking"))
           ba.containerwidget(edit=self._root_widget, transition='out_scale')           
              
   # RR
   def RR(self): 
    	ba.open_url("https://youtu.be/dQw4w9WgXcQ") #xd
    
   # backup
   def do_backup(self, pluging_name): 
      try:
          if os.path.exists(_ba.env()['python_directory_user'] + "/" + pluging_name.split('.')[0] + ".py"):
              shutil.copyfile(_ba.env()['python_directory_user'] + "/" + pluging_name.split('.')[0] + ".py", _ba.env()['python_directory_user'] + "/backup/" + pluging_name.split('.')[0] + ".py")
              ba.screenmessage('» Done!', (0, 1, 0))
              ba.playsound(ba.getsound("woodDebrisFall"))
          else: 
              ba.screenmessage('» Error404', (1, 0, 0))
              ba.playsound(ba.getsound('ticking'))
      except:
          ba.print_exception()
          ba.screenmessage('» Error', (1, 0, 0))
          ba.playsound(ba.getsound("ticking"))         
      ba.containerwidget(edit=self._root_widget, transition='out_scale')
     
   # back  Activate                                                 
   def _back(self):
        ba.containerwidget(edit=self._root_widget, transition='out_scale')

#==============================================================================#             
                                   
# Plugins Window
class ShowPluginsWindow(ba.Window):
   def __init__(self, availplug, origin: Sequence[float] = (0, 0)):
     
     # pylint: disable=too-many-locals
     app = ba.app
     self.plugins = app.plugins
     self.meta = app.meta
      
     self.plugins.load_plugins()
     pluging_name = (availplug.display_name).evaluate()
     path = _ba.env()['python_directory_user'] + "/" + pluging_name.split('.')[0] + ".py"
     active = availplug.class_path in ba.app.plugins.active_plugins
     text_color = ((0.8, 0.3, 0.3) if not availplug.available else (0, 1, 0) if active else (0.6, 0.6, 0.6))
     status = ("Error404" if not availplug.available else "its Work" if active else "Unknown")
     status_img = ("logo" if not availplug.available else "achievementsIcon" if active else "nextLevelIcon")
            
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         scale=2.0,
                         size=(350, 125),
                         stack_offset=(0, -10))
     
    # plugins name
     self._plugins_name = ba.textwidget(parent=self._root_widget,
                          position=(80, 110),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=150,
                          text="» " + pluging_name.split('.')[0],
                          v_align='center')
    
     # host logo                       
     self._host_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(35, 35),
                                     position=(45, 95),
                                     texture=ba.gettexture('tv'))                                                                                                          
 
     # pluging image
     pluging_image = ba.imagewidget(parent=self._root_widget, position=(30, 50), size=(38, 38), texture=ba.gettexture('nub'))                                                                       
     ba.imagewidget(edit=pluging_image, color=text_color)
       
     # name
     self._name = ba.textwidget(parent=self._root_widget,
                          position=(70, 80),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=70,
                          text="» " + status)              
                                       
     # back
     self._back_button = btn = ba.buttonwidget(parent=self._root_widget,
                                      autoselect=True,
                                      position=(8, 100),
                                      size=(30, 30),
                                      scale=1.1,
                                      on_activate_call=self._back,
                                      label=ba.charstr(ba.SpecialChar.BACK),
                                      button_type='backSmall')
     ba.containerwidget(edit=self._root_widget, cancel_button=btn)                 
            
     # status button
     self.status_button = ba.buttonwidget(
            parent=self._root_widget,
            autoselect=True,
            position=(240, 30),
            size=(60, 60),
            label="",
            on_select_call=ba.WeakCall(self.pbutton, availplug, pluging_name, path),
            button_type='square')
     self.status_button_icon = ba.imagewidget(parent=self._root_widget,
            size=(53, 53),
            draw_controller=self.status_button,
            position=(243.5, 32.5),
            texture=ba.gettexture(status_img))                                     
                                     
   def pbutton(self, availplug, pluging_name, path):
        if os.path.exists(path) and os.path.isfile(path):
           if ba.app.config['Plugins'][availplug.class_path].get('enabled', False) == False: self.on_complete_call(self.enable_plugin, availplug, pluging_name)
           else: self.disable_plugin(availplug, pluging_name)
        else:
           ba.screenmessage('» Error404', (1, 0, 0))
           ba.playsound(ba.getsound("ticking"))
        ba.containerwidget(edit=self._root_widget, transition='out_scale')                          

   def enable_plugin(self, plug, pluging_name):
        if ba.app.config['Plugins'][plug.class_path].get('enabled', False) == False:
           ba.app.config['Plugins'][plug.class_path] = dict(enabled=True)
           ba.screenmessage("» Plugin enabled: " + pluging_name.split('.')[1] + " » " + pluging_name.split('.')[0] + ".py", (0,1,0))
           ba.app.config.apply_and_commit()
           self.plugins.load_plugins()
        else: ba.screenmessage("» Plugin enabled already", (0,1,0))
          
   def disable_plugin(self, plug, pluging_name):
        if ba.app.config['Plugins'][plug.class_path].get('enabled', False) == True:
           ba.app.config['Plugins'][plug.class_path] = dict(enabled=False)
           ba.screenmessage("» Plugin disable: " + pluging_name.split('.')[1] + " » " + pluging_name.split('.')[0] + ".py", (1,0,0))
           ba.app.config.apply_and_commit()
        else: ba.screenmessage("» Plugin disable already", (0,1,0))
        
   def on_complete_call(self, callback, *args):
        if not self.plugins.potential_plugins:
            self.timer = ba.Timer(0.2, ba.Call(self.on_complete_call, callback, *args))
            return
        callback(*args)
               
   # back  Activate                                           
   def _back(self):
        ba.containerwidget(edit=self._root_widget, transition='out_scale')                          
                    
#==============================================================================#             

# Plugins info Window
class ShowinfoPluginsWindow(ba.Window):
   def __init__(self, availplug, origin: Sequence[float] = (0, 0)):
     
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         scale=2.0,
                         size=(500, 200),
                         stack_offset=(0, -10))
     
     # menu
     self._menu = ba.textwidget(parent=self._root_widget,
                          position=(140, 180),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=100,
                          text="» Plugins info",
                          h_align='center',
                          v_align='center')
    
     # Menu logo                       
     self._menu_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(25, 25),
                                     position=(61, 165),
                                     texture=ba.gettexture('settingsIcon'))                                                               
     
     # Host logo                       
     self._host_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(150, 150),
                                     position=(-5, 25),
                                     texture=ba.gettexture('tv'))
                                     
     # back
     self._back_button = btn = ba.buttonwidget(parent=self._root_widget,
                                      autoselect=True,
                                      position=(12, 140),
                                      size=(30, 30),
                                      scale=1.1,
                                      on_activate_call=self._back,
                                      label=ba.charstr(ba.SpecialChar.BACK),
                                      button_type='backSmall')
     ba.containerwidget(edit=self._root_widget, cancel_button=btn)                                   
                                                                                               
     Bsversion = "Unknown"
	
     # thx for This Github.com
     if _ba.env().get("build_number",0) == 0:
            Bsversion = "Error"
     if _ba.env().get("build_number",0) >= 20001:
        	Bsversion = "1.5.0"  
     if _ba.env().get("build_number",0) >= 20062:
        	Bsversion = "1.5.1"
     if _ba.env().get("build_number",0) >= 20063:
        	Bsversion = "1.5.2"
     if _ba.env().get("build_number",0) >= 20065:
        	Bsversion = "1.5.3"
     if _ba.env().get("build_number",0) >= 20067:
        	Bsversion = "1.5.4"
     if _ba.env().get("build_number",0) >= 20069:
        	Bsversion = "1.5.5"
     if _ba.env().get("build_number",0) >= 20072:
        	Bsversion = "1.5.6"
     if _ba.env().get("build_number",0) >= 20077:
        	Bsversion = "1.5.7"
     if _ba.env().get("build_number",0) >= 20079:
        	Bsversion = "1.5.8"
     if _ba.env().get("build_number",0) >= 20081:
        	Bsversion = "1.5.9"
     if _ba.env().get("build_number",0) >= 20083:
        	Bsversion = "1.5.10"
     if _ba.env().get("build_number",0) >= 20084:
        	Bsversion = "1.5.11"
     if _ba.env().get("build_number",0) >= 20087:
        	Bsversion = "1.5.12"
     if _ba.env().get("build_number",0) >= 20095:
        	Bsversion = "1.5.13"
     if _ba.env().get("build_number",0) >= 20096:
        	Bsversion = "1.5.14"
     if _ba.env().get("build_number",0) >= 20097:
        	Bsversion = "1.5.15"
     if _ba.env().get("build_number",0) >= 20099:
        	Bsversion = "1.5.16"
     if _ba.env().get("build_number",0) >= 20102:
        	Bsversion = "1.5.17"
     if _ba.env().get("build_number",0) >= 20106:
        	Bsversion = "1.5.18"
     if _ba.env().get("build_number",0) >= 20114:
        	Bsversion = "1.5.19"
     if _ba.env().get("build_number",0) >= 20126:
        	Bsversion = "1.5.20"
     if _ba.env().get("build_number",0) >= 20136:
        	Bsversion = "1.5.21"
     if _ba.env().get("build_number",0) >= 20145:
        	Bsversion = "1.5.23"
     if _ba.env().get("build_number",0) >= 20159:
        	Bsversion = "1.5.24"
     if _ba.env().get("build_number",0) >= 20164:
        	Bsversion = "1.5.25"
     if _ba.env().get("build_number",0) >= 20178:
        	Bsversion = "1.5.26"
     if _ba.env().get("build_number",0) >= 20218:
        	Bsversion = "1.5.27"
     if _ba.env().get("build_number",0) >= 20238:
        	Bsversion = "1.5.27"
     if _ba.env().get("build_number",0) >= 20239:
        	Bsversion = "1.5.28"
     if _ba.env().get("build_number",0) >= 20247:
        	Bsversion = "1.5.29"
     if _ba.env().get("build_number",0) >= 20263:
        	Bsversion = "1.5.30"
     if _ba.env().get("build_number",0) >= 20268:
        	Bsversion = "1.6.0"
     if _ba.env().get("build_number",0) >= 20362:
        	Bsversion = "1.6.1"
     if _ba.env().get("build_number",0) >= 20365:
        	Bsversion = "1.6.2"
     if _ba.env().get("build_number",0) >= 20366:
        	Bsversion = "1.6.3"
     if _ba.env().get("build_number",0) >= 20367:
        	Bsversion = "1.6.4"
     if _ba.env().get("build_number",0) >= 20388:
        	Bsversion = "1.6.5"
     if _ba.env().get("build_number",0) >= 20436:
        	Bsversion = "1.6.6"
     if _ba.env().get("build_number",0) >= 20394:
        	Bsversion = "1.6.7"
     if _ba.env().get("build_number",0) >= 20444:
        	Bsversion = "1.6.8"
     if _ba.env().get("build_number",0) >= 20461:
        	Bsversion = "1.6.9"
     if _ba.env().get("build_number",0) >= 20501:
        	Bsversion = "1.6.10"
     if _ba.env().get("build_number",0) >= 20514:
        	Bsversion = "1.6.11"
     if _ba.env().get("build_number",0) >= 20542:
        	Bsversion = "1.6.12"
     if _ba.env().get("build_number",0) >= 20599:
        	Bsversion = "1.6.12"
     if _ba.env().get("build_number",0) >= 20577:
        	Bsversion = "1.7.0"
     if _ba.env().get("build_number",0) >= 20592:
        	Bsversion = "1.7.1"
     if _ba.env().get("build_number",0) >= 20600:
        	Bsversion = "1.7.2"
     if _ba.env().get("build_number",0) >= 20602:
        	Bsversion = "1.7.2+"
        
     pluging_name = (availplug.display_name).evaluate()
      
     # version
     self._version = ba.textwidget(parent=self._root_widget,
                          position=(69.1, 98.5),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=45,
                          text="»" + str(_ba.env().get("build_number",0)) + "«",
                          h_align='center',
                          v_align='center')              
                          
     # build number
     self._build = ba.textwidget(parent=self._root_widget,
                          position=(69.1, 77.5),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=45,
                          text="»" + Bsversion + "«",
                          h_align='center',
                          v_align='center')                                  
                          
     # name
     self._name = ba.textwidget(parent=self._root_widget,
                          position=(140, 125),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=(70 if len(pluging_name.split('.')[0]) <= 5 else 120),
                          text="» name: " + pluging_name)              
                          
     # package name
     self._package_name = ba.textwidget(parent=self._root_widget,
                          position=(140, 105),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=(70 if len(pluging_name.split('.')[0]) <= 5 else 120),
                          text="» package name: " + pluging_name.split('.')[1])
         
     # name
     self._file_name = ba.textwidget(parent=self._root_widget,
                          position=(140, 85.1),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=(70 if len(pluging_name.split('.')[0]) <= 5 else 120),
                          text="» file name: " + pluging_name.split('.')[0] + ".py")                            
                          
     # path
     self.pluging_path = ba.textwidget(parent=self._root_widget,
                          position=(140, 65),
                          size=(0, 0),
                          scale=(0.4 if len(pluging_name.split('.')[0]) <= 5 else 0.45),
                          text="» " + _ba.env()['python_directory_user'] + "/" + pluging_name.split('.')[0] + ".py")
            
     # size 
     if os.path.exists(_ba.env()['python_directory_user'] + "/" + pluging_name.split('.')[0] + ".py"):
        _B = str(os.path.getsize(_ba.env()['python_directory_user'] + "/" + pluging_name.split('.')[0] + ".py"))
        _Size = self.formatBytes(_B)
     
        self.size_b_path = ba.textwidget(parent=self._root_widget,
                             position=(140, 146),
                             size=(0, 0),
                             scale=(0.4 if len(pluging_name.split('.')[0]) <= 5 else 0.45),
                             text="» file size: " + _B + "B" + " / " + str(_Size))
     else: pass # file deleted!
                          
   def formatBytes(self, a=0, b=0): 
      c = 1024
      d = b if not b==0 else 2
      e = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
      f = math.floor(math.log(int(a)) / math.log(int(c)))
      if a == 0: return "0 Bytes" # what are you doing here >:3??
      else: return str(round(int(a) / int(math.pow(c, f)), d)) + e[f]

   # back  Activate                                                  
   def _back(self):
        ba.containerwidget(edit=self._root_widget, transition='out_scale')

#==============================================================================#             

class NewPluginSettingsWindow(ba.Window):
    """Window for configuring plugins."""

    def __init__(self,
                 transition: str = 'in_right',
                 origin_widget: ba.Widget = None):
        # pylint: disable=too-many-locals
        app = ba.app
        self.plugins = app.plugins
        self.meta = app.meta

        # If they provided an origin-widget, scale up from that.
        scale_origin: Optional[Tuple[float, float]]
        if origin_widget is not None:
            self._transition_out = 'out_scale'
            scale_origin = origin_widget.get_screen_space_center()
            transition = 'in_scale'
        else:
            self._transition_out = 'out_right'
            scale_origin = None

        uiscale = ba.app.ui.uiscale
        self._width = 870.0 if uiscale is ba.UIScale.SMALL else 670.0
        x_inset = 100 if uiscale is ba.UIScale.SMALL else 0
        self._height = (390.0 if uiscale is ba.UIScale.SMALL else
                        450.0 if uiscale is ba.UIScale.MEDIUM else 520.0)
        top_extra = 10 if uiscale is ba.UIScale.SMALL else 0
        super().__init__(root_widget=ba.containerwidget(
            size=(self._width, self._height + top_extra),
            transition=transition,
            toolbar_visibility='menu_minimal',
            scale_origin_stack_offset=scale_origin,
            scale=(2.06 if uiscale is ba.UIScale.SMALL else
                   1.4 if uiscale is ba.UIScale.MEDIUM else 1.0),
            stack_offset=(0, -25) if uiscale is ba.UIScale.SMALL else (0, 0)))

        self._scroll_width = self._width - (100 + 2 * x_inset)
        self._scroll_height = self._height - 115.0
        self._sub_width = self._scroll_width * 0.95
        self._sub_height = 724.0
        
        self.SizeWindow = (0.01 if (app.ui.uiscale is ba.UIScale.SMALL) else 120.0)
                     
        # help button
        self.help_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(671 - self.SizeWindow, self._height - 63),
                                      size=(90, 90),
                                      on_activate_call=HelpWindow,
                                      label='',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)
        self.help_button_icon = ba.imagewidget(parent=self._root_widget,
                                     size=(43, 43),
                                     draw_controller=self.help_button,
                                     position=(673 - self.SizeWindow, self._height - 61),
                                     texture=ba.gettexture('achievementEmpty'))                              
                                     
        # About button                 
        self.about_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(615 - self.SizeWindow, self._height - 63),
                                      size=(90, 90),
                                      on_activate_call=AboutWindow,
                                      label='',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)
        self.about_button_icon = ba.imagewidget(parent=self._root_widget,
                                     size=(43, 43),
                                     draw_controller=self.about_button,
                                     position=(618 - self.SizeWindow, self._height - 61),
                                     texture=ba.gettexture('logIcon'))                              
                  
        # Credits
        self.credits_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(578 - self.SizeWindow, self._height - 61),
                                      size=(50, 50),
                                      on_activate_call=CreditsWindow,
                                      label='',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)
        self.credits_button_icon = ba.imagewidget(parent=self._root_widget,
                                     size=(27, 27),
                                     draw_controller=self.credits_button,
                                     position=(578.5 - self.SizeWindow, self._height - 60),
                                     texture=ba.gettexture('star'))                                     
                                     
        if app.ui.use_toolbars and uiscale is ba.UIScale.SMALL:
            ba.containerwidget(edit=self._root_widget,
                               on_cancel_call=self._do_back)
            self._back_button = None
        else:
            self._back_button = ba.buttonwidget(
                parent=self._root_widget,
                position=(53 + x_inset, self._height - 60),
                size=(140, 60),
                scale=0.8,
                autoselect=True,
                label=ba.Lstr(resource='backText'),
                button_type='back',
                on_activate_call=self._do_back)
            ba.containerwidget(edit=self._root_widget,
                               cancel_button=self._back_button)
    
        self._title_text = ba.textwidget(parent=self._root_widget,
                                         position=(-185, self._height - 46),
                                         size=(self._width, 25), 
                                         text="» " + ba.Lstr(resource='pluginsText').evaluate(),
                                         color=app.ui.title_color,
                                         h_align='center',
                                         v_align='top')

        if self._back_button is not None:
            ba.buttonwidget(edit=self._back_button,
                            button_type='backSmall',
                            size=(60, 60),
                            label=ba.charstr(ba.SpecialChar.BACK))

        self._scrollwidget = ba.scrollwidget(parent=self._root_widget,
                                             position=(50 + x_inset, 50),
                                             simple_culling_v=20.0,
                                             highlight=False,
                                             size=(self._scroll_width,
                                                   self._scroll_height),
                                             selection_loops_to_parent=True)
        ba.widget(edit=self._scrollwidget, right_widget=self._scrollwidget)
        self._subcontainer = ba.columnwidget(parent=self._scrollwidget,
                                             selection_loops_to_parent=True)
        
        pluglist = ba.app.plugins.potential_plugins
        plugstates: Dict[str, Dict] = ba.app.config.setdefault('Plugins', {})
        assert isinstance(plugstates, dict)
       
        for i, availplug in enumerate(pluglist):
            active = availplug.class_path in ba.app.plugins.active_plugins
            plugstate = plugstates.setdefault(availplug.class_path, {})
            checked = plugstate.get('enabled', False)
            assert isinstance(checked, bool)
            text_color= ((0.8, 0.3, 0.3) if not availplug.available else (0, 1, 0) if active else (0.6, 0.6, 0.6))
            
            pluging_name = (availplug.display_name).evaluate()
            ppath = "» " + _ba.env()['python_directory_user'] + "/" + pluging_name.split('.')[0] + ".py"
            
            # menu tab
            tab = ba.containerwidget(parent=self._subcontainer ,size=(540, 90), background=False,selection_loops_to_parent=True)
            
            # button
            button = ba.buttonwidget(parent=tab, size=(540, 80), on_activate_call=ba.Call(ShowPluginsWindow, availplug), label="", autoselect=True)
            
            # check button
            check = ba.checkboxwidget(parent=tab, position=(70, 48.5), size=(15, 15), value=checked, text="", maxwidth=self._scroll_width - 100, on_value_change_call=ba.Call(self._check_value_changed, availplug))
           
            # pluging image
            pluging_image = ba.imagewidget(parent=tab, position=(28, 20), size=(38, 38), texture=ba.gettexture('nub'))
            
            # pluging name
            pluging_name_text = ba.textwidget(parent=tab, position=(5, 25), size=(self._scroll_width - 40, 50), scale=0.6, text="» " + pluging_name, color=text_color)
            
            # path text 
            pluging_path = ba.textwidget(parent=tab, position=(-34, -5), size=(self._scroll_width - 40, 50), scale=0.6, text=ppath, color=(0.6, 0.6, 0.6))
               
            # settings button
            settings_button = ba.buttonwidget(parent=tab, position=(455, 18.5), size=(90, 90), label='', on_activate_call=ba.Call(SettingsWindow, availplug), autoselect=True, button_type='square', scale=0.55)
            settings_button_icon = ba.imagewidget(parent=tab, position=(457.5, 20), size=(43, 43), draw_controller=settings_button, texture=ba.gettexture('settingsIcon'))  
                                                  
            # info button
            info_button = ba.buttonwidget(parent=tab, position=(415, 37), size=(54, 54), label='', on_activate_call=ba.Call(ShowinfoPluginsWindow, availplug), autoselect=True, button_type='square', scale=0.55)
            info_button_icon = ba.imagewidget(parent=tab, position=(417.5, 39), size=(25, 25), draw_controller=info_button, texture=ba.gettexture('logIcon'))                              
                 
           # button ???
            sus_button = ba.buttonwidget(parent=tab, position=(378, 37), size=(54, 54), label='...', on_activate_call=self.huh, button_type='square', scale=0.55)                                                    
            ba.imagewidget(edit=pluging_image, color=text_color)
       
            # Make sure we scroll all the way to the end when using
            # keyboard/button nav.
            ba.widget(edit=check, show_buffer_top=40, show_buffer_bottom=40)

            # Keep last from looping to back button when down is pressed.
            if i == len(pluglist) - 1:
                ba.widget(edit=check, down_widget=check)
        ba.containerwidget(edit=self._root_widget,
                           selected_child=self._scrollwidget)

        self._restore_state() 

   # sus
    def huh(self):
        ba.screenmessage(random.choice(["No", "hmm", "sus", "bruh", "-.-", "don't click me", ">:3"]), color=(random.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]), random.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]), random.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])))
      
    def _check_value_changed(self, plug: ba.PotentialPlugin, value: bool) -> None:
        plugstates: Dict[str, Dict] = ba.app.config.setdefault('Plugins', {})
        assert isinstance(plugstates, dict)
        pluging_name = (plug.display_name).evaluate()
        path = _ba.env()['python_directory_user'] + "/" + pluging_name.split('.')[0] + ".py"
        if os.path.exists(path) and os.path.isfile(path):
           if value: self.on_complete_call(self.enable_plugin, plug, pluging_name)
           else: self.disable_plugin(plug, pluging_name)
        else:
           ba.screenmessage('» Error404', (1, 0, 0))
           ba.playsound(ba.getsound("ticking"))
        
    def enable_plugin(self, plug, pluging_name):
        if ba.app.config['Plugins'][plug.class_path].get('enabled', False) == False:
           ba.app.config['Plugins'][plug.class_path] = dict(enabled=True)
           ba.screenmessage("» Plugin enabled: " + pluging_name.split('.')[1] + " » " + pluging_name.split('.')[0] + ".py", (0,1,0))
           ba.app.config.apply_and_commit()
           self.plugins.load_plugins()
        else: ba.screenmessage("» Plugin enabled already", (0,1,0))
          
    def disable_plugin(self, plug, pluging_name):
        if ba.app.config['Plugins'][plug.class_path].get('enabled', False) == True:
           ba.app.config['Plugins'][plug.class_path] = dict(enabled=False)
           ba.screenmessage("» Plugin disable: " + pluging_name.split('.')[1] + " » " + pluging_name.split('.')[0] + ".py", (1,0,0))
           ba.app.config.apply_and_commit()
        else: ba.screenmessage("» Plugin disable already", (0,1,0))
        
    def meta_rescan(self):
        self.plugins.potential_plugins: List[ba.PotentialPlugin] = []
        self.plugins.active_plugins: Dict[str, ba.Plugin] = {}
        self.meta.metascan = None
        self.meta.start_scan()

    def on_complete_call(self, callback, *args):
        if not self.plugins.potential_plugins:
            self.timer = ba.Timer(0.2, ba.Call(self.on_complete_call, callback, *args))
            return
        callback(*args)
  
    def _save_state(self) -> None:
    	self.plugins.load_plugins()

    def _restore_state(self) -> None:
    	self.meta_rescan()

    def _do_back(self) -> None:
        # pylint: disable=cyclic-import
        from bastd.ui.settings.advanced import AdvancedSettingsWindow
        self._save_state()
        ba.containerwidget(edit=self._root_widget,
                           transition=self._transition_out)
        ba.app.ui.set_main_menu_window(
            AdvancedSettingsWindow(transition='in_left').get_root_widget())

#==============================================================================#             

# ba_meta export plugin
class UwUuser(ba.Plugin):
    plugins.PluginSettingsWindow = NewPluginSettingsWindow
    #files
    def __init__(self):
    	installFiles()