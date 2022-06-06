# ba_meta require api 6


#==============================================================================#             
#     
#     version v1.0 (test)
#     Create by Unknown_#7004 
#     Github https://github.com/uwu-user
#
#==============================================================================#             


from __future__ import annotations
from typing import TYPE_CHECKING, cast

import ba
import _ba
import random
import copy
import time
import threading
from enum import Enum
from dataclasses import dataclass
from bastd.ui.gather import GatherTab
from bastd.gameutils import SharedObjects
from bastd.ui.partyqueue import PartyQueueWindow
from bastd.ui.colorpicker import ColorPicker, ColorPickerExact
import bastd.ui.gather.publictab as GP

if TYPE_CHECKING:
    from typing import Any, Sequence, Callable, List, Dict, Tuple, Optional, Union
    from bastd.ui.gather import GatherWindow

#==============================================================================#             

party_name_logo = "\ue043"
menu_logo = "\ue048"

# or 
# menu_logo = ""

#==============================================================================#             

_testN = "3841"
_version = "1.1"
_by = "Unknown_#7004"

#==============================================================================#             

#ping / s

ping_s = 1000.0

# try to change it to 100.0 lol

#==============================================================================#             

# Config   

public_config = {
   'party_auto_update': True,
   'party_menu': True,
   'party_ping': True,
   'party_size': True,
   'party_ip': True,
   'party_language': True,
   'party_ping_color': (1,1,1),
   'party_size_color': (1,1,1),
   'party_name_color': (1,1,1),
   'party_language_color': (1,1,1),
   'party_ping_rainbow_color': True,
   'party_size_rainbow_color': True,
   'party_name_rainbow_color': True,
   'party_language_rainbow_color': True,
   'party_stats_name': "BombSquad Party",
   'party_stats_address': "127.0.0.1",
   'party_stats_port': 43210,
   'party_stats_language': "France",
   'party_stats_url': "Empty",
   'party_stats_queue': "Empty",
   'party_stats_size': 0,
   'party_stats_size_max': 10,
   'party_stats_index': 0,
   'party_stats_ping': 9999,
   'party_stats_version': 13700,
   'bombSquad_version': True,
   'Servers_counts': 0,
   'Servers_founded': 0
}

if "public_config" in ba.app.config:
    old_config = ba.app.config["public_config"]

    for setting in public_config:
        if setting not in old_config:
            ba.app.config["public_config"] = public_config
else:
    ba.app.config["public_config"] = public_config
ba.app.config.apply_and_commit()

#==============================================================================#             



# Old Config   

old_public_config = {
   'party_auto_update': True,
   'party_menu': True,
   'party_ping': True,
   'party_size': True,
   'party_ip': True,
   'party_language': True,
   'party_ping_color': (1,1,1),
   'party_size_color': (1,1,1),
   'party_name_color': (1,1,1),
   'party_language_color': (1,1,1),
   'party_ping_rainbow_color': True,
   'party_size_rainbow_color': True,
   'party_name_rainbow_color': True,
   'party_language_rainbow_color': True,
   'party_stats_name': "BombSquad Party",
   'party_stats_address': "127.0.0.1",
   'party_stats_port': 43210,
   'party_stats_language': "France",
   'party_stats_url': "Empty",
   'party_stats_queue': "Empty",
   'party_stats_size': 0,
   'party_stats_size_max': 10,
   'party_stats_index': 0,
   'party_stats_ping': 9999,
   'party_stats_version': 13700,
   'bombSquad_version': True,
   'Servers_counts': 0,
   'Servers_founded': 0
}

if "old_public_config" in ba.app.config:
    old_config = ba.app.config["old_public_config"]

    for setting in old_public_config:
        if setting in old_config:
            ba.app.config["old_public_config"] = old_public_config
else:
    ba.app.config["old_public_config"] = old_public_config
ba.app.config.apply_and_commit()

#==============================================================================#             



# Reset Config   

reset_public_config = {
   'party_auto_update': True,
   'party_menu': True,
   'party_ping': True,
   'party_size': True,
   'party_ip': True,
   'party_language': True,
   'party_ping_color': (1,1,1),
   'party_size_color': (1,1,1),
   'party_name_color': (1,1,1),
   'party_language_color': (1,1,1),
   'party_ping_rainbow_color': True,
   'party_size_rainbow_color': True,
   'party_name_rainbow_color': True,
   'party_language_rainbow_color': True,
   'party_stats_name': "BombSquad Party",
   'party_stats_address': "127.0.0.1",
   'party_stats_port': 43210,
   'party_stats_language': "France",
   'party_stats_url': "Empty",
   'party_stats_queue': "Empty",
   'party_stats_size': 0,
   'party_stats_size_max': 10,
   'party_stats_index': 0,
   'party_stats_ping': 9999,
   'party_stats_version': 13700,
   'bombSquad_version': True,
   'Servers_counts': 0,
   'Servers_founded': 0
}

if "reset_public_config" in ba.app.config:
    old_config = ba.app.config["reset_public_config"]

    for setting in reset_public_config:
        if setting in old_config:
            ba.app.config["reset_public_config"] = reset_public_config
else:
    ba.app.config["reset_public_config"] = reset_public_config
ba.app.config.apply_and_commit()

#==============================================================================#             


# Print a bit of info about pings, queries, etc.
# Note: this print() info only

DEBUG_SERVER_COMMUNICATION = False
DEBUG_PROCESSING = False

#==============================================================================#             


class SubTabType(Enum):
    """Available sub-tabs."""
    JOIN = 'join'
    HOST = 'host'


@dataclass
class PartyEntry:
    """Info about a public party."""
    address: str
    index: int
    queue: Optional[str] = None
    port: int = -1
    version: int = -1
    name: str = ''
    language: str = ''
    size: int = -1
    size_max: int = -1
    claimed: bool = False
    ping: Optional[float] = None
    ping_interval: float = -1.0
    next_ping_time: float = -1.0
    ping_attempts: int = 0
    ping_responses: int = 0
    stats_addr: Optional[str] = None
    clean_display_index: Optional[int] = None

    def get_key(self) -> str:
        """Return the key used to store this party."""
        return f'{self.address}_{self.port}'

#==============================================================================#             

class Reset_settings:
    """Reset public party."""
    ba.app.config["public_config"]["party_stats_name"] = "BombSquad Party"
    ba.app.config["public_config"]["party_stats_address"] = "127.0.0.1"
    ba.app.config["public_config"]["party_stats_port"] = 43210
    ba.app.config["public_config"]["party_stats_language"] = "France"
    ba.app.config["public_config"]["party_stats_url"] = "Empty"
    ba.app.config["public_config"]["party_stats_queue"] = "Empty",
    ba.app.config["public_config"]["party_stats_version"] = "1.6.4",
    ba.app.config["public_config"]["party_stats_size"] = 0
    ba.app.config["public_config"]["party_stats_size_max"] = 10
    ba.app.config.apply_and_commit()
    
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
                          text="» Version " + _version + " (test: " + _testN + ")",
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

# Info 
class InfoWindow(ba.Window):
   def __init__(self, origin: Sequence[float] = (0, 0)):
     
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         scale=2.0,
                         size=(600, 300),
                         stack_offset=(0, -10))
     # back
     self._back_button = btn = ba.buttonwidget(parent=self._root_widget,
                                      autoselect=True,
                                      position=(8, 140),
                                      size=(30, 30),
                                      scale=1.1,
                                      on_activate_call=self._back,
                                      label=ba.charstr(ba.SpecialChar.BACK),
                                      button_type='backSmall')
     ba.containerwidget(edit=self._root_widget, cancel_button=btn)                                                                 
     
     # info
     self._info = ba.textwidget(parent=self._root_widget,
                          position=(120, 210),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=80,
                          text=str(ba.app.config["public_config"]),
                          h_align='center',
                          v_align='center')
    
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
                          maxwidth=50,
                          text="» Empty",
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
  
# settings      
class SettingsWindow(ba.Window):
   def __init__(self, origin: Sequence[float] = (0, 0)):
     
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         scale=2.0,
                         size=(600, 300),
                         stack_offset=(0, -10))
     
     # Settings
     self._settings = ba.textwidget(parent=self._root_widget,
                          position=(140, 280),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=100,
                          text="» Settings",
                          h_align='center',
                          v_align='center')
    
     # Settings logo                       
     self._settings_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(25, 25),
                                     position=(61, 265),
                                     texture=ba.gettexture('settingsIcon'))                                                               
     
     # Auto Update
     self.auto_update= ba.checkboxwidget(parent=self._root_widget,
                text="Auto Update", 
                value=ba.app.config["public_config"]["party_auto_update"],
                maxwidth=80,
                position=(60, 219),
                size=(140, 50),
                on_value_change_call=ba.Call(self.save_settingsV1, "party_auto_update"),
                textcolor=(1,1,1))
                
     # Show Ping
     self.show_ping = ba.checkboxwidget(parent=self._root_widget,
                text="Show Ping", 
                value=ba.app.config["public_config"]["party_ping"],
                maxwidth=80,
                position=(60, 185),
                on_value_change_call=ba.Call(self.save_settingsV1, "party_ping"),
                size=(140, 50),
                textcolor=(1,1,1)) 
      
     # Show Size
     self.show_size = ba.checkboxwidget(parent=self._root_widget,
                text="Show Size", 
                value=ba.app.config["public_config"]["party_size"],
                maxwidth=80,
                position=(60, 151),
                on_value_change_call=ba.Call(self.save_settingsV1, "party_size"),
                size=(140, 50),
                textcolor=(1,1,1))
                
     # Show language
     self.show_size = ba.checkboxwidget(parent=self._root_widget,
                text="Show language", 
                value=ba.app.config["public_config"]["party_language"],
                maxwidth=80,
                position=(60, 117),
                on_value_change_call=ba.Call(self.save_settingsV1, "party_language"),
                size=(140, 50),
                textcolor=(1,1,1))
                
     # Show Menu
     self.show_menu = ba.checkboxwidget(parent=self._root_widget,
                text="Show Menu", 
                value=ba.app.config["public_config"]["party_menu"],
                maxwidth=80,
                position=(60, 83),
                on_value_change_call=ba.Call(self.save_settingsV1, "party_menu"),
                size=(140, 50),
                textcolor=(1,1,1)) 
                
     # Show ip
     self.showIp = ba.checkboxwidget(parent=self._root_widget,
                text="Show ip:port", 
                value=ba.app.config["public_config"]["party_ip"],
                maxwidth=80,
                position=(60, 49),
                on_value_change_call=ba.Call(self.save_settingsV1, "party_ip"),
                size=(140, 50),
                textcolor=(1,1,1))           
                
     # Show Menu
     self.show_version= ba.checkboxwidget(parent=self._root_widget,
                text="Show Bs Version", 
                value=ba.app.config["public_config"]["bombSquad_version"],
                maxwidth=80,
                position=(60, 15),
                on_value_change_call=ba.Call(self.save_settingsV1, "bombSquad_version"),
                size=(140, 50),
                textcolor=(1,1,1)) 

     # party name color text
     self.party_name_color_text = ba.textwidget(parent=self._root_widget,
                          position=(280, 245),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=140,
                          text="party name color:",
                          h_align='center',
                          v_align='center')
       
     # party name color
     self._party_name_color_button = ba.buttonwidget(
            parent=self._root_widget,
            autoselect=True,
            position=(210,  190),
            size=(40, 40),
            label='',
            button_type='square',
            color=ba.app.config["public_config"]["party_name_color"],
            on_activate_call=self._make_name_picker)
          
     # » ?
     self._text = ba.textwidget(parent=self._root_widget,
                          position=(268, 227),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=80,
                          text="»",
                          h_align='center',
                          v_align='center')
                          
    # Party Name Rainbow Color
     self.party_name_rainbow_color = ba.checkboxwidget(parent=self._root_widget,
                text="Random", 
                value=ba.app.config["public_config"]["party_name_rainbow_color"],
                maxwidth=50,
                position=(260, 175),
                on_value_change_call=ba.Call(self.save_settingsV1, "party_name_rainbow_color"),
                size=(110, 50),
                textcolor=(1,1,1)) 
                
     # party Ping color text
     self.party_ping_color_text = ba.textwidget(parent=self._root_widget,
                          position=(440, 245),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=140,
                          text="Ping color:",
                          h_align='center',
                          v_align='center')
       
     # party ping color
     self._party_ping_color_button = ba.buttonwidget(
            parent=self._root_widget,
            autoselect=True,
            position=(380,  190),
            size=(40, 40),
            label='',
            button_type='square',
            color=ba.app.config["public_config"]["party_ping_color"],
            on_activate_call=self._make_ping_picker)
          
     # » ??
     self._text = ba.textwidget(parent=self._root_widget,
                          position=(438, 227),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=80,
                          text="»",
                          h_align='center',
                          v_align='center')
                          
    # Party Name Rainbow Color
     self.party_name_rainbow_color = ba.checkboxwidget(parent=self._root_widget,
                text="Random", 
                value=ba.app.config["public_config"]["party_ping_rainbow_color"],
                maxwidth=50,
                position=(430, 175),
                on_value_change_call=ba.Call(self.save_settingsV1, "party_ping_rainbow_color"),
                size=(110, 50),
                textcolor=(1,1,1)) 

     # party name color text
     self.party_Size_color_text = ba.textwidget(parent=self._root_widget,
                          position=(280, 145),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=140,
                          text="Party Size color:",
                          h_align='center',
                          v_align='center')
       
     # party size color
     self._party_size_color_button = ba.buttonwidget(
            parent=self._root_widget,
            autoselect=True,
            position=(210,  90),
            size=(40, 40),
            label='',
            button_type='square',
            color=ba.app.config["public_config"]["party_size_color"],
            on_activate_call=self._make_size_picker)
          
     # » ??? 
     self._text = ba.textwidget(parent=self._root_widget,
                          position=(268, 127),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=80,
                          text="»",
                          h_align='center',
                          v_align='center')
                          
    # Party Name Rainbow Color
     self.party_name_rainbow_color = ba.checkboxwidget(parent=self._root_widget,
                text="Random", 
                value=ba.app.config["public_config"]["party_size_rainbow_color"],
                maxwidth=50,
                position=(260, 75),
                on_value_change_call=ba.Call(self.save_settingsV1, "party_size_rainbow_color"),
                size=(110, 50),
                textcolor=(1,1,1)) 
   
     # party language color text
     self.party_language_color_text = ba.textwidget(parent=self._root_widget,
                          position=(440, 145),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=140,
                          text="party language color:",
                          h_align='center',
                          v_align='center')
       
     # party language color
     self._party_language_color_button = ba.buttonwidget(
            parent=self._root_widget,
            autoselect=True,
            position=(380,  90),
            size=(40, 40),
            label='',
            button_type='square',
            color=ba.app.config["public_config"]["party_language_color"],
            on_activate_call=self._make_language_picker)
          
     # » ??? :3?
     self._text = ba.textwidget(parent=self._root_widget,
                          position=(438, 127),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=80,
                          text="»",
                          h_align='center',
                          v_align='center')
                          
    # Party language Rainbow Color
     self.party_language_rainbow_color = ba.checkboxwidget(parent=self._root_widget,
                text="Random", 
                value=ba.app.config["public_config"]["party_language_rainbow_color"],
                maxwidth=50,
                position=(430, 75),
                on_value_change_call=ba.Call(self.save_settingsV1, "party_language_rainbow_color"),
                size=(110, 50),
                textcolor=(1,1,1))
          
     # button ???
     self.save_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(210, 20),
                                      size=(150, 50),
                                      label='...',
                                      on_activate_call=self.huh,
                                      button_type='regular',
                                      scale=0.55) 
                
     # reset button
     self.save_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(300, 20),
                                      size=(220, 50),
                                      label='Reset',
                                      on_activate_call=self.reset_settings,
                                      button_type='regular',
                                      scale=0.55) 
                                      
     # disable colors button
     self.disable_colors= ba.buttonwidget(parent=self._root_widget,
                                      position=(300, 50),
                                      size=(220, 50),
                                      label='Disable colors',
                                      on_activate_call=self._disable_colors,
                                      button_type='regular',
                                      scale=0.55)                            
            
     # save button
     self.save_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(425, 50),
                                      size=(220, 50),
                                      label='Save',
                                      on_activate_call=self.save_settings,
                                      button_type='regular',
                                      scale=0.55) 
     
     # Cancel button   
     self.cancel_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(425, 20),
                                      size=(220, 50),
                                      label='Cancel',
                                      on_activate_call=self.cancel_settings,
                                      button_type='regular',
                                      scale=0.55)                     
      
     # help button
     self.help_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(0, 180),
                                      size=(90, 90),
                                      on_activate_call=HelpWindow,
                                      label='',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)
     self.help_button_icon = ba.imagewidget(parent=self._root_widget,
                                     size=(43, 43),
                                     draw_controller=self.help_button,
                                     position=(2, 183),
                                     texture=ba.gettexture('achievementEmpty'))                              
       
     # About button                 
     self.about_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(0, 130),
                                      size=(90, 90),
                                      on_activate_call=AboutWindow,
                                      label='',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)
     self.about_button_icon = ba.imagewidget(parent=self._root_widget,
                                     size=(43, 43),
                                     draw_controller=self.about_button,
                                     position=(2, 133.5),
                                     texture=ba.gettexture('logIcon'))                              
                                     
     # info button                 
     self.info_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(0, 80),
                                      size=(90, 90),
                                      on_activate_call=InfoWindow,
                                      label='',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)
     self.info_button_icon = ba.imagewidget(parent=self._root_widget,
                                     size=(43, 43),
                                     draw_controller=self.info_button,
                                     position=(2, 83.5),
                                     texture=ba.gettexture('file'))                                                      
          
     # Credits
     self.credits_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(10, 50),
                                      size=(50, 50),
                                      on_activate_call=CreditsWindow,
                                      label='',
                                      autoselect=True,
                                      button_type='square',
                                      scale=0.55)
     self.credits_button_icon = ba.imagewidget(parent=self._root_widget,
                                     size=(27, 27),
                                     draw_controller=self.credits_button,
                                     position=(10.5, 50.5),
                                     texture=ba.gettexture('star'))                             
                                                      
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

    # sus                                      
   def huh(self):
        ba.screenmessage(random.choice(["huh", "dont", "No", "sus", "huh"]), color=(random.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]), random.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]), random.choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])))
      
   def save_settingsV1(self, settings, m):
        ba.app.config["old_public_config"][settings] = False if m==0 else True
        ba.app.config.apply_and_commit()
             
   def _make_name_picker(self) -> None:
        ColorPicker(parent=self._root_widget, position=(0,0), initial_color=ba.app.config["public_config"]["party_name_color"], delegate=self, tag="name_color")
            
   def _make_ping_picker(self) -> None:
        ColorPicker(parent=self._root_widget, position=(0,0), initial_color=ba.app.config["public_config"]["party_ping_color"], delegate=self, tag="ping_color")
        
   def _make_size_picker(self) -> None:
        ColorPicker(parent=self._root_widget, position=(0,0), initial_color=ba.app.config["public_config"]["party_name_color"], delegate=self, tag="size_color")
    
   def _make_language_picker(self) -> None:
        ColorPicker(parent=self._root_widget, position=(0,0), initial_color=ba.app.config["public_config"]["party_language_color"], delegate=self, tag="language_color")
    
   # yea add "tag" = "test" :3
      
   def color_picker_closing(self, picker: ColorPicker) -> None:
        """Called when a color picker is closing."""
        if not self._root_widget:
            return
        tag = picker.get_tag()
        if tag == 'name_color':
            ba.containerwidget(edit=self._root_widget, selected_child=self._party_name_color_button)
        elif tag == 'ping_color':
            ba.containerwidget(edit=self._root_widget, selected_child=self._party_ping_color_button)
        elif tag == 'size_color':
            ba.containerwidget(edit=self._root_widget, selected_child=self._party_size_color_button)                     
        elif tag == 'language_color':
            ba.containerwidget(edit=self._root_widget, selected_child=self._party_language_color_button)                     
        else:
            print('color_picker_closing got unknown tag ' + str(tag))

   def color_picker_selected_color(self, picker: ColorPicker, color: Tuple[float, float, float]) -> None:
        """Called when a color is selected in a color picker."""
        if not self._root_widget:
            return
        tag = picker.get_tag()
        if tag == 'name_color':
            ba.app.config["old_public_config"]["party_name_color"] = color
            ba.app.config.apply_and_commit()
            ba.buttonwidget(edit=self._party_name_color_button, color=color)
        elif tag == 'ping_color':
            ba.app.config["old_public_config"]["party_ping_color"] = color
            ba.app.config.apply_and_commit()
            ba.buttonwidget(edit=self._party_ping_color_button, color=color)
        elif tag == 'size_color':
            ba.app.config["old_public_config"]["party_size_color"] = color
            ba.app.config.apply_and_commit()
            ba.buttonwidget(edit=self._party_size_color_button, color=color)
        elif tag == 'language_color':
            ba.app.config["old_public_config"]["party_language_color"] = color
            ba.app.config.apply_and_commit()
            ba.buttonwidget(edit=self._party_language_color_button, color=color)
        else:
            print('color_picker_selected_color got unknown tag ' + str(tag))

   def _disable_colors(self):
        ba.app.config["public_config"]["party_name_rainbow_color"] = False
        ba.app.config["public_config"]["party_ping_rainbow_color"] = False
        ba.app.config["public_config"]["party_size_rainbow_color"] = False
        ba.app.config["public_config"]["party_language_rainbow_color"] = False
        ba.app.config["public_config"]["party_name_color"] = (1,1,1)
        ba.app.config["public_config"]["party_ping_color"] = (1,1,1)
        ba.app.config["public_config"]["party_size_color"] = (1,1,1)
        ba.app.config["public_config"]["party_language_color"] = (1,1,1)
        ba.app.config["old_public_config"]["party_name_rainbow_color"] = False
        ba.app.config["old_public_config"]["party_ping_rainbow_color"] = False
        ba.app.config["old_public_config"]["party_size_rainbow_color"] = False
        ba.app.config["old_public_config"]["party_language_rainbow_color"] = False
        ba.app.config["old_public_config"]["party_name_color"] = (1,1,1)
        ba.app.config["old_public_config"]["party_ping_color"] = (1,1,1)
        ba.app.config["old_public_config"]["party_size_color"] = (1,1,1)
        ba.app.config["old_public_config"]["party_language_color"] = (1,1,1)
        ba.app.config.apply_and_commit()
        ba.containerwidget(edit=self._root_widget, transition='out_scale')
                        
   def reset_settings(self):
        if not ba.app.config["public_config"]["party_auto_update"] == ba.app.config["reset_public_config"]["party_auto_update"]:
            ba.app.config["public_config"]["party_auto_update"] = ba.app.config["reset_public_config"]["party_auto_update"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["public_config"]["party_ping"] == ba.app.config["reset_public_config"]["party_ping"]:
            ba.app.config["public_config"]["party_ping"] = ba.app.config["reset_public_config"]["party_ping"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["public_config"]["party_size"] == ba.app.config["reset_public_config"]["party_size"]:
            ba.app.config["public_config"]["party_size"] = ba.app.config["reset_public_config"]["party_size"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["public_config"]["party_language"] == ba.app.config["reset_public_config"]["party_language"]:
            ba.app.config["public_config"]["party_language"] = ba.app.config["reset_public_config"]["party_language"]
            ba.app.config.apply_and_commit()               
        if not ba.app.config["public_config"]["party_menu"] == ba.app.config["reset_public_config"]["party_menu"]:
            ba.app.config["public_config"]["party_menu"] = ba.app.config["reset_public_config"]["party_menu"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["public_config"]["party_ip"] == ba.app.config["reset_public_config"]["party_ip"]:
            ba.app.config["public_config"]["party_ip"] = ba.app.config["reset_public_config"]["party_ip"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["public_config"]["bombSquad_version"] == ba.app.config["reset_public_config"]["bombSquad_version"]:
            ba.app.config["public_config"]["bombSquad_version"] = ba.app.config["reset_public_config"]["bombSquad_version"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["public_config"]["party_name_rainbow_color"] == ba.app.config["reset_public_config"]["party_name_rainbow_color"]:
            ba.app.config["public_config"]["party_name_rainbow_color"] = ba.app.config["reset_public_config"]["party_name_rainbow_color"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["public_config"]["party_ping_rainbow_color"] == ba.app.config["reset_public_config"]["party_ping_rainbow_color"]:
            ba.app.config["public_config"]["party_ping_rainbow_color"] = ba.app.config["reset_public_config"]["party_ping_rainbow_color"]
            ba.app.config.apply_and_commit()               
        if not ba.app.config["public_config"]["party_size_rainbow_color"] == ba.app.config["reset_public_config"]["party_size_rainbow_color"]:
            ba.app.config["public_config"]["party_size_rainbow_color"] = ba.app.config["reset_public_config"]["party_size_rainbow_color"]
            ba.app.config.apply_and_commit()            
        if not ba.app.config["public_config"]["party_language_rainbow_color"] == ba.app.config["reset_public_config"]["party_language_rainbow_color"]:
            ba.app.config["public_config"]["party_language_rainbow_color"] = ba.app.config["reset_public_config"]["party_language_rainbow_color"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["public_config"]["party_name_color"] == ba.app.config["reset_public_config"]["party_name_color"]:
            ba.app.config["public_config"]["party_name_color"] = ba.app.config["reset_public_config"]["party_name_color"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["public_config"]["party_ping_color"] == ba.app.config["reset_public_config"]["party_ping_color"]:
            ba.app.config["public_config"]["party_ping_color"] = ba.app.config["reset_public_config"]["party_ping_color"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["public_config"]["party_size_color"] == ba.app.config["reset_public_config"]["party_size_color"]:
            ba.app.config["public_config"]["party_size_color"] = ba.app.config["reset_public_config"]["party_size_color"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["public_config"]["party_language_color"] == ba.app.config["reset_public_config"]["party_language_color"]:
            ba.app.config["public_config"]["party_language_color"] = ba.app.config["reset_public_config"]["party_language_color"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["old_public_config"]["party_auto_update"] == ba.app.config["reset_public_config"]["party_auto_update"]:
            ba.app.config["old_public_config"]["party_auto_update"] = ba.app.config["reset_public_config"]["party_auto_update"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["old_public_config"]["party_ping"] == ba.app.config["reset_public_config"]["party_ping"]:
            ba.app.config["old_public_config"]["party_ping"] = ba.app.config["reset_public_config"]["party_ping"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["old_public_config"]["party_size"] == ba.app.config["reset_public_config"]["party_size"]:
            ba.app.config["old_public_config"]["party_size"] = ba.app.config["reset_public_config"]["party_size"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["old_public_config"]["party_language"] == ba.app.config["reset_public_config"]["party_language"]:
            ba.app.config["old_public_config"]["party_language"] = ba.app.config["reset_public_config"]["party_language"]
            ba.app.config.apply_and_commit()               
        if not ba.app.config["old_public_config"]["party_menu"] == ba.app.config["reset_public_config"]["party_menu"]:
            ba.app.config["old_public_config"]["party_menu"] = ba.app.config["reset_public_config"]["party_menu"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["old_public_config"]["party_ip"] == ba.app.config["reset_public_config"]["party_ip"]:
            ba.app.config["old_public_config"]["party_ip"] = ba.app.config["reset_public_config"]["party_ip"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["old_public_config"]["bombSquad_version"] == ba.app.config["reset_public_config"]["bombSquad_version"]:
            ba.app.config["old_public_config"]["bombSquad_version"] = ba.app.config["reset_public_config"]["bombSquad_version"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["old_public_config"]["party_name_rainbow_color"] == ba.app.config["reset_public_config"]["party_name_rainbow_color"]:
            ba.app.config["old_public_config"]["party_name_rainbow_color"] = ba.app.config["reset_public_config"]["party_name_rainbow_color"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["old_public_config"]["party_ping_rainbow_color"] == ba.app.config["reset_public_config"]["party_ping_rainbow_color"]:
            ba.app.config["old_public_config"]["party_ping_rainbow_color"] = ba.app.config["reset_public_config"]["party_ping_rainbow_color"]
            ba.app.config.apply_and_commit()               
        if not ba.app.config["old_public_config"]["party_size_rainbow_color"] == ba.app.config["reset_public_config"]["party_size_rainbow_color"]:
            ba.app.config["old_public_config"]["party_size_rainbow_color"] = ba.app.config["reset_public_config"]["party_size_rainbow_color"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["old_public_config"]["party_language_rainbow_color"] == ba.app.config["reset_public_config"]["party_language_rainbow_color"]:
            ba.app.config["old_public_config"]["party_language_rainbow_color"] = ba.app.config["reset_public_config"]["party_language_rainbow_color"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["old_public_config"]["party_name_color"] == ba.app.config["reset_public_config"]["party_name_color"]:
            ba.app.config["old_public_config"]["party_name_color"] = ba.app.config["reset_public_config"]["party_name_color"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["old_public_config"]["party_ping_color"] == ba.app.config["reset_public_config"]["party_ping_color"]:
            ba.app.config["old_public_config"]["party_ping_color"] = ba.app.config["reset_public_config"]["party_ping_color"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["old_public_config"]["party_size_color"] == ba.app.config["reset_public_config"]["party_size_color"]:
            ba.app.config["old_public_config"]["party_size_color"] = ba.app.config["reset_public_config"]["party_size_color"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["old_public_config"]["party_language_color"] == ba.app.config["reset_public_config"]["party_language_color"]:
            ba.app.config["old_public_config"]["party_language_color"] = ba.app.config["reset_public_config"]["party_language_color"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["public_config"]["party_auto_update"] == ba.app.config["reset_public_config"]["party_auto_update"] and ba.app.config["public_config"]["party_ping"] == ba.app.config["reset_public_config"]["party_ping"] and ba.app.config["public_config"]["party_size"] == ba.app.config["reset_public_config"]["party_size"] and ba.app.config["public_config"]["party_language"] == ba.app.config["reset_public_config"]["party_language"] and ba.app.config["public_config"]["party_menu"] == ba.app.config["reset_public_config"]["party_menu"] and ba.app.config["public_config"]["party_ip"] == ba.app.config["reset_public_config"]["party_ip"] and ba.app.config["public_config"]["bombSquad_version"] == ba.app.config["reset_public_config"]["bombSquad_version"] and ba.app.config["public_config"]["party_name_rainbow_color"] == ba.app.config["reset_public_config"]["party_name_rainbow_color"] and ba.app.config["public_config"]["party_ping_rainbow_color"] == ba.app.config["reset_public_config"]["party_ping_rainbow_color"] and ba.app.config["public_config"]["party_size_rainbow_color"] == ba.app.config["reset_public_config"]["party_size_rainbow_color"] and ba.app.config["public_config"]["party_language_rainbow_color"] == ba.app.config["reset_public_config"]["party_language_rainbow_color"] and ba.app.config["public_config"]["party_name_color"] == ba.app.config["reset_public_config"]["party_name_color"] and ba.app.config["public_config"]["party_ping_color"] == ba.app.config["reset_public_config"]["party_ping_color"] and ba.app.config["public_config"]["party_size_color"] == ba.app.config["reset_public_config"]["party_size_color"] and ba.app.config["public_config"]["party_language_color"] == ba.app.config["reset_public_config"]["party_language_color"] and ba.app.config["old_public_config"]["party_auto_update"] == ba.app.config["reset_public_config"]["party_auto_update"] and ba.app.config["old_public_config"]["party_ping"] == ba.app.config["reset_public_config"]["party_ping"] and ba.app.config["old_public_config"]["party_size"] == ba.app.config["reset_public_config"]["party_size"] and ba.app.config["old_public_config"]["party_language"] == ba.app.config["reset_public_config"]["party_language"] and ba.app.config["old_public_config"]["party_menu"] == ba.app.config["reset_public_config"]["party_menu"] and ba.app.config["old_public_config"]["party_ip"] == ba.app.config["reset_public_config"]["party_ip"] and ba.app.config["old_public_config"]["bombSquad_version"] == ba.app.config["reset_public_config"]["bombSquad_version"] and ba.app.config["old_public_config"]["party_name_rainbow_color"] == ba.app.config["reset_public_config"]["party_name_rainbow_color"]and ba.app.config["old_public_config"]["party_ping_rainbow_color"] == ba.app.config["reset_public_config"]["party_ping_rainbow_color"] and ba.app.config["old_public_config"]["party_size_rainbow_color"] == ba.app.config["reset_public_config"]["party_size_rainbow_color"] and ba.app.config["old_public_config"]["party_language_rainbow_color"] == ba.app.config["reset_public_config"]["party_language_rainbow_color"] and ba.app.config["old_public_config"]["party_name_color"] == ba.app.config["reset_public_config"]["party_name_color"] and ba.app.config["old_public_config"]["party_ping_color"] == ba.app.config["reset_public_config"]["party_ping_color"] and ba.app.config["old_public_config"]["party_size_color"] == ba.app.config["reset_public_config"]["party_size_color"] and ba.app.config["old_public_config"]["party_language_color"] == ba.app.config["reset_public_config"]["party_language_color"]:
           ba.containerwidget(edit=self._root_widget, transition='out_scale')
        ba.containerwidget(edit=self._root_widget, transition='out_scale')
                        
   def save_settings(self):
        if not ba.app.config["public_config"]["party_auto_update"] == ba.app.config["old_public_config"]["party_auto_update"]:
            ba.app.config["public_config"]["party_auto_update"] = ba.app.config["old_public_config"]["party_auto_update"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["public_config"]["party_ping"] == ba.app.config["old_public_config"]["party_ping"]:
            ba.app.config["public_config"]["party_ping"] = ba.app.config["old_public_config"]["party_ping"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["public_config"]["party_size"] == ba.app.config["old_public_config"]["party_size"]:
            ba.app.config["public_config"]["party_size"] = ba.app.config["old_public_config"]["party_size"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["public_config"]["party_language"] == ba.app.config["old_public_config"]["party_language"]:
            ba.app.config["public_config"]["party_language"] = ba.app.config["old_public_config"]["party_language"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["public_config"]["party_menu"] == ba.app.config["old_public_config"]["party_menu"]:
            ba.app.config["public_config"]["party_menu"] = ba.app.config["old_public_config"]["party_menu"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["public_config"]["party_ip"] == ba.app.config["old_public_config"]["party_ip"]:
            ba.app.config["public_config"]["party_ip"] = ba.app.config["old_public_config"]["party_ip"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["public_config"]["bombSquad_version"] == ba.app.config["old_public_config"]["bombSquad_version"]:
            ba.app.config["public_config"]["bombSquad_version"] = ba.app.config["old_public_config"]["bombSquad_version"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["public_config"]["party_name_rainbow_color"] == ba.app.config["old_public_config"]["party_name_rainbow_color"]:
            ba.app.config["public_config"]["party_name_rainbow_color"] = ba.app.config["old_public_config"]["party_name_rainbow_color"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["public_config"]["party_ping_rainbow_color"] == ba.app.config["old_public_config"]["party_ping_rainbow_color"]:
            ba.app.config["public_config"]["party_ping_rainbow_color"] = ba.app.config["old_public_config"]["party_ping_rainbow_color"]
            ba.app.config.apply_and_commit()               
        if not ba.app.config["public_config"]["party_size_rainbow_color"] == ba.app.config["old_public_config"]["party_size_rainbow_color"]:
            ba.app.config["public_config"]["party_size_rainbow_color"] = ba.app.config["old_public_config"]["party_size_rainbow_color"]
            ba.app.config.apply_and_commit()                
        if not ba.app.config["public_config"]["party_language_rainbow_color"] == ba.app.config["old_public_config"]["party_language_rainbow_color"]:
            ba.app.config["public_config"]["party_language_rainbow_color"] = ba.app.config["old_public_config"]["party_language_rainbow_color"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["public_config"]["party_name_color"] == ba.app.config["old_public_config"]["party_name_color"]:
            ba.app.config["public_config"]["party_name_color"] = ba.app.config["old_public_config"]["party_name_color"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["public_config"]["party_ping_color"] == ba.app.config["old_public_config"]["party_ping_color"]:
            ba.app.config["public_config"]["party_ping_color"] = ba.app.config["old_public_config"]["party_ping_color"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["public_config"]["party_size_color"] == ba.app.config["old_public_config"]["party_size_color"]:
            ba.app.config["public_config"]["party_size_color"] = ba.app.config["old_public_config"]["party_size_color"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["public_config"]["party_language_color"] == ba.app.config["old_public_config"]["party_language_color"]:
            ba.app.config["public_config"]["party_language_color"] = ba.app.config["old_public_config"]["party_language_color"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["public_config"]["party_auto_update"] == ba.app.config["old_public_config"]["party_auto_update"] and ba.app.config["public_config"]["party_ping"] == ba.app.config["old_public_config"]["party_ping"] and ba.app.config["public_config"]["party_size"] == ba.app.config["old_public_config"]["party_size"] and ba.app.config["public_config"]["party_language"] == ba.app.config["old_public_config"]["party_language"] and ba.app.config["public_config"]["party_menu"] == ba.app.config["old_public_config"]["party_menu"] and ba.app.config["public_config"]["party_ip"] == ba.app.config["old_public_config"]["party_ip"] and ba.app.config["public_config"]["bombSquad_version"] == ba.app.config["old_public_config"]["bombSquad_version"] and ba.app.config["public_config"]["party_name_rainbow_color"] == ba.app.config["old_public_config"]["party_name_rainbow_color"] and ba.app.config["public_config"]["party_ping_rainbow_color"] == ba.app.config["old_public_config"]["party_ping_rainbow_color"] and ba.app.config["public_config"]["party_size_rainbow_color"] == ba.app.config["old_public_config"]["party_size_rainbow_color"] and ba.app.config["public_config"]["party_language_rainbow_color"] == ba.app.config["old_public_config"]["party_language_rainbow_color"] and ba.app.config["public_config"]["party_name_color"] == ba.app.config["old_public_config"]["party_name_color"] and ba.app.config["public_config"]["party_ping_color"] == ba.app.config["old_public_config"]["party_ping_color"] and ba.app.config["public_config"]["party_size_color"] == ba.app.config["old_public_config"]["party_size_color"] and ba.app.config["public_config"]["party_language_color"] == ba.app.config["old_public_config"]["party_language_color"]:
           ba.containerwidget(edit=self._root_widget, transition='out_scale')
        ba.containerwidget(edit=self._root_widget, transition='out_scale')  
            
   def cancel_settings(self):
        if not ba.app.config["old_public_config"]["party_auto_update"] == ba.app.config["reset_public_config"]["party_auto_update"]:
            ba.app.config["old_public_config"]["party_auto_update"] = ba.app.config["reset_public_config"]["party_auto_update"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["old_public_config"]["party_ping"] == ba.app.config["reset_public_config"]["party_ping"]:
            ba.app.config["old_public_config"]["party_ping"] = ba.app.config["reset_public_config"]["party_ping"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["old_public_config"]["party_size"] == ba.app.config["reset_public_config"]["party_size"]:
            ba.app.config["old_public_config"]["party_size"] = ba.app.config["reset_public_config"]["party_size"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["old_public_config"]["party_language"] == ba.app.config["reset_public_config"]["party_language"]:
            ba.app.config["old_public_config"]["party_language"] = ba.app.config["reset_public_config"]["party_language"]
            ba.app.config.apply_and_commit()               
        if not ba.app.config["old_public_config"]["party_menu"] == ba.app.config["reset_public_config"]["party_menu"]:
            ba.app.config["old_public_config"]["party_menu"] = ba.app.config["reset_public_config"]["party_menu"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["old_public_config"]["party_ip"] == ba.app.config["reset_public_config"]["party_ip"]:
            ba.app.config["old_public_config"]["party_ip"] = ba.app.config["reset_public_config"]["party_ip"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["old_public_config"]["bombSquad_version"] == ba.app.config["reset_public_config"]["bombSquad_version"]:
            ba.app.config["old_public_config"]["bombSquad_version"] = ba.app.config["reset_public_config"]["bombSquad_version"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["old_public_config"]["party_name_rainbow_color"] == ba.app.config["reset_public_config"]["party_name_rainbow_color"]:
            ba.app.config["old_public_config"]["party_name_rainbow_color"] = ba.app.config["reset_public_config"]["party_name_rainbow_color"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["old_public_config"]["party_ping_rainbow_color"] == ba.app.config["reset_public_config"]["party_ping_rainbow_color"]:
            ba.app.config["old_public_config"]["party_ping_rainbow_color"] = ba.app.config["reset_public_config"]["party_ping_rainbow_color"]
            ba.app.config.apply_and_commit()               
        if not ba.app.config["old_public_config"]["party_size_rainbow_color"] == ba.app.config["reset_public_config"]["party_size_rainbow_color"]:
            ba.app.config["old_public_config"]["party_size_rainbow_color"] = ba.app.config["reset_public_config"]["party_size_rainbow_color"]
            ba.app.config.apply_and_commit()               
        if not ba.app.config["old_public_config"]["party_language_rainbow_color"] == ba.app.config["reset_public_config"]["party_language_rainbow_color"]:
            ba.app.config["old_public_config"]["party_language_rainbow_color"] = ba.app.config["reset_public_config"]["party_language_rainbow_color"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["old_public_config"]["party_name_color"] == ba.app.config["reset_public_config"]["party_name_color"]:
            ba.app.config["old_public_config"]["party_name_color"] = ba.app.config["reset_public_config"]["party_name_color"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["old_public_config"]["party_ping_color"] == ba.app.config["reset_public_config"]["party_ping_color"]:
            ba.app.config["old_public_config"]["party_ping_color"] = ba.app.config["reset_public_config"]["party_ping_color"]
            ba.app.config.apply_and_commit()                  
        if not ba.app.config["old_public_config"]["party_size_color"] == ba.app.config["reset_public_config"]["party_size_color"]:
            ba.app.config["old_public_config"]["party_size_color"] = ba.app.config["reset_public_config"]["party_size_color"]
            ba.app.config.apply_and_commit()
        if not ba.app.config["old_public_config"]["party_language_color"] == ba.app.config["reset_public_config"]["party_language_color"]:
            ba.app.config["old_public_config"]["party_language_color"] = ba.app.config["reset_public_config"]["party_language_color"]
            ba.app.config.apply_and_commit()
        if ba.app.config["old_public_config"]["party_auto_update"] == ba.app.config["reset_public_config"]["party_auto_update"] and ba.app.config["old_public_config"]["party_ping"] == ba.app.config["reset_public_config"]["party_ping"] and ba.app.config["old_public_config"]["party_size"] == ba.app.config["reset_public_config"]["party_size"] and ba.app.config["old_public_config"]["party_menu"] == ba.app.config["reset_public_config"]["party_menu"] and ba.app.config["old_public_config"]["party_ip"] == ba.app.config["reset_public_config"]["party_ip"] and ba.app.config["old_public_config"]["bombSquad_version"] == ba.app.config["reset_public_config"]["bombSquad_version"] and ba.app.config["old_public_config"]["party_name_rainbow_color"] == ba.app.config["reset_public_config"]["party_name_rainbow_color"] and ba.app.config["old_public_config"]["party_ping_rainbow_color"] == ba.app.config["reset_public_config"]["party_ping_rainbow_color"] and ba.app.config["old_public_config"]["party_size_rainbow_color"] == ba.app.config["reset_public_config"]["party_size_rainbow_color"] and ba.app.config["old_public_config"]["party_name_color"] == ba.app.config["reset_public_config"]["party_name_color"] and ba.app.config["old_public_config"]["party_ping_color"] == ba.app.config["reset_public_config"]["party_ping_color"] and ba.app.config["old_public_config"]["party_size_color"] == ba.app.config["reset_public_config"]["party_size_color"]:
            ba.containerwidget(edit=self._root_widget, transition='out_scale')
        ba.containerwidget(edit=self._root_widget, transition='out_scale')
                       
              
#==============================================================================#             

# menu
class MenuWindow(ba.Window):
   def __init__(self, origin: Sequence[float] = (0, 0)):
     
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         scale=2.0,
                         size=(600, 300),
                         stack_offset=(0, -10))
     
     # menu
     self._menu = ba.textwidget(parent=self._root_widget,
                          position=(140, 280),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=100,
                          text="» Menu",
                          h_align='center',
                          v_align='center')
    
     # Menu logo                       
     self._menu_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(25, 25),
                                     position=(61, 265),
                                     texture=ba.gettexture('settingsIcon'))                                                               
     
     # Host logo                       
     self._host_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(150, 150),
                                     position=(-5, 125),
                                     texture=ba.gettexture('tv'))
                                     
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
                                                  
                                                  
     if ba.app.config["public_config"]["party_stats_ping"] <= 10:
          p_ping_color = (0,1,0)
     elif ba.app.config["public_config"]["party_stats_ping"] <= 40:
          p_ping_color = (4.4, 0.8, 0.5)
     elif ba.app.config["public_config"]["party_stats_ping"] <= 70:
          p_ping_color = (0.4, 1, 0.3)
     elif ba.app.config["public_config"]["party_stats_ping"] <= 90:
          p_ping_color = (0.7, 0, 0.7)
     elif ba.app.config["public_config"]["party_stats_ping"] <= 150:
          p_ping_color = (0.8, 0.2, 0.4)
     elif ba.app.config["public_config"]["party_stats_ping"] <= 250:
          p_ping_color = (1,0,0)
     elif ba.app.config["public_config"]["party_stats_ping"] <= 500:
          p_ping_color = (0.8, 0.3, 1)
     elif ba.app.config["public_config"]["party_stats_ping"] <= 999:
          p_ping_color = (1, 0.5, 0.7)
     elif ba.app.config["public_config"]["party_stats_ping"] <= 99999:
          p_ping_color = (0.2, 0, 0.5)
        
     Bsversion = "Unknown"
	
     # thx for This Github.com
     if ba.app.config["public_config"]["party_stats_version"] == 0:
            Bsversion = "Error"
     if ba.app.config["public_config"]["party_stats_version"] >= 13700:
            Bsversion = "1.3"
     if ba.app.config["public_config"]["party_stats_version"] >= 14000:
        	Bsversion = "1.4"
     if ba.app.config["public_config"]["party_stats_version"] >= 14233:
        	Bsversion = "1.4.95"
     if ba.app.config["public_config"]["party_stats_version"] >= 14241:
        	Bsversion = "1.4.96"
     if ba.app.config["public_config"]["party_stats_version"] >= 14244:
        	Bsversion = "1.4.97"
     if ba.app.config["public_config"]["party_stats_version"] >= 14248:
        	Bsversion = "1.4.98"
     if ba.app.config["public_config"]["party_stats_version"] >= 14252:
        	Bsversion = "1.4.99"
     if ba.app.config["public_config"]["party_stats_version"] >= 14264:
        	Bsversion = "1.4.100"
     if ba.app.config["public_config"]["party_stats_version"] >= 14268:
        	Bsversion = "1.4.101"
     if ba.app.config["public_config"]["party_stats_version"] >= 14280:
        	Bsversion = "1.4.106"
     if ba.app.config["public_config"]["party_stats_version"] >= 14286:
        	Bsversion = "1.4.111"
     if ba.app.config["public_config"]["party_stats_version"] >= 14298:
        	Bsversion = "1.4.118"
     if ba.app.config["public_config"]["party_stats_version"] >= 14302:
        	Bsversion = "1.4.121"
     if ba.app.config["public_config"]["party_stats_version"] >= 14306:
        	Bsversion = "1.4.125"
     if ba.app.config["public_config"]["party_stats_version"] >= 14307:
        	Bsversion = "1.4.126"
     if ba.app.config["public_config"]["party_stats_version"] >= 14313:
        	Bsversion = "1.4.130"
     if ba.app.config["public_config"]["party_stats_version"] >= 14315:
        	Bsversion = "1.4.131"
     if ba.app.config["public_config"]["party_stats_version"] >= 14316:
        	Bsversion = "1.4.132"
     if ba.app.config["public_config"]["party_stats_version"] >= 14318:
        	Bsversion = "1.4.133"
     if ba.app.config["public_config"]["party_stats_version"] >= 14322:
        	Bsversion = "1.4.134"
     if ba.app.config["public_config"]["party_stats_version"] >= 14324:
        	Bsversion = "1.4.135"
     if ba.app.config["public_config"]["party_stats_version"] >= 14327:
        	Bsversion = "1.4.136"
     if ba.app.config["public_config"]["party_stats_version"] >= 14331:
        	Bsversion = "1.4.137"
     if ba.app.config["public_config"]["party_stats_version"] >= 14336:
        	Bsversion = "1.4.138"
     if ba.app.config["public_config"]["party_stats_version"] >= 14340:
        	Bsversion = "1.4.139"
     if ba.app.config["public_config"]["party_stats_version"] >= 14343:
        	Bsversion = "1.4.140"
     if ba.app.config["public_config"]["party_stats_version"] >= 14344:
        	Bsversion = "1.4.141"
     if ba.app.config["public_config"]["party_stats_version"] >= 14346:
        	Bsversion = "1.4.142"
     if ba.app.config["public_config"]["party_stats_version"] >= 14347:
        	Bsversion = "1.4.143"
     if ba.app.config["public_config"]["party_stats_version"] >= 14350:
        	Bsversion = "1.4.144"
     if ba.app.config["public_config"]["party_stats_version"] >= 14351:
        	Bsversion = "1.4.145"
     if ba.app.config["public_config"]["party_stats_version"] >= 14354:
        	Bsversion = "1.4.146"
     if ba.app.config["public_config"]["party_stats_version"] >= 14364:
        	Bsversion = "1.4.147"
     if ba.app.config["public_config"]["party_stats_version"] >= 14365:
        	Bsversion = "1.4.148"
     if ba.app.config["public_config"]["party_stats_version"] >= 14367:
        	Bsversion = "1.4.149"
     if ba.app.config["public_config"]["party_stats_version"] >= 14369:
        	Bsversion = "1.4.150"
     if ba.app.config["public_config"]["party_stats_version"] >= 14371:
        	Bsversion = "1.4.151"
     if ba.app.config["public_config"]["party_stats_version"] >= 14372:
        	Bsversion = "1.4.152"
     if ba.app.config["public_config"]["party_stats_version"] >= 14374:
        	Bsversion = "1.4.153"
     if ba.app.config["public_config"]["party_stats_version"] >= 14375:
        	Bsversion = "1.4.154"
     if ba.app.config["public_config"]["party_stats_version"] >= 14377:
        	Bsversion = "1.4.155" 
     if ba.app.config["public_config"]["party_stats_version"] >= 20001:
        	Bsversion = "1.5.0"  
     if ba.app.config["public_config"]["party_stats_version"] >= 20062:
        	Bsversion = "1.5.1"
     if ba.app.config["public_config"]["party_stats_version"] >= 20063:
        	Bsversion = "1.5.2"
     if ba.app.config["public_config"]["party_stats_version"] >= 20065:
        	Bsversion = "1.5.3"
     if ba.app.config["public_config"]["party_stats_version"] >= 20067:
        	Bsversion = "1.5.4"
     if ba.app.config["public_config"]["party_stats_version"] >= 20069:
        	Bsversion = "1.5.5"
     if ba.app.config["public_config"]["party_stats_version"] >= 20072:
        	Bsversion = "1.5.6"
     if ba.app.config["public_config"]["party_stats_version"] >= 20077:
        	Bsversion = "1.5.7"
     if ba.app.config["public_config"]["party_stats_version"] >= 20079:
        	Bsversion = "1.5.8"
     if ba.app.config["public_config"]["party_stats_version"] >= 20081:
        	Bsversion = "1.5.9"
     if ba.app.config["public_config"]["party_stats_version"] >= 20083:
        	Bsversion = "1.5.10"
     if ba.app.config["public_config"]["party_stats_version"] >= 20084:
        	Bsversion = "1.5.11"
     if ba.app.config["public_config"]["party_stats_version"] >= 20087:
        	Bsversion = "1.5.12"
     if ba.app.config["public_config"]["party_stats_version"] >= 20095:
        	Bsversion = "1.5.13"
     if ba.app.config["public_config"]["party_stats_version"] >= 20096:
        	Bsversion = "1.5.14"
     if ba.app.config["public_config"]["party_stats_version"] >= 20097:
        	Bsversion = "1.5.15"
     if ba.app.config["public_config"]["party_stats_version"] >= 20099:
        	Bsversion = "1.5.16"
     if ba.app.config["public_config"]["party_stats_version"] >= 20102:
        	Bsversion = "1.5.17"
     if ba.app.config["public_config"]["party_stats_version"] >= 20106:
        	Bsversion = "1.5.18"
     if ba.app.config["public_config"]["party_stats_version"] >= 20114:
        	Bsversion = "1.5.19"
     if ba.app.config["public_config"]["party_stats_version"] >= 20126:
        	Bsversion = "1.5.20"
     if ba.app.config["public_config"]["party_stats_version"] >= 20136:
        	Bsversion = "1.5.21"
     if ba.app.config["public_config"]["party_stats_version"] >= 20145:
        	Bsversion = "1.5.23"
     if ba.app.config["public_config"]["party_stats_version"] >= 20159:
        	Bsversion = "1.5.24"
     if ba.app.config["public_config"]["party_stats_version"] >= 20164:
        	Bsversion = "1.5.25"
     if ba.app.config["public_config"]["party_stats_version"] >= 20178:
        	Bsversion = "1.5.26"
     if ba.app.config["public_config"]["party_stats_version"] >= 20218:
        	Bsversion = "1.5.27"
     if ba.app.config["public_config"]["party_stats_version"] >= 20238:
        	Bsversion = "1.5.27"
     if ba.app.config["public_config"]["party_stats_version"] >= 20239:
        	Bsversion = "1.5.28"
     if ba.app.config["public_config"]["party_stats_version"] >= 20247:
        	Bsversion = "1.5.29"
     if ba.app.config["public_config"]["party_stats_version"] >= 20263:
        	Bsversion = "1.5.30"
     if ba.app.config["public_config"]["party_stats_version"] >= 20268:
        	Bsversion = "1.6.0"
     if ba.app.config["public_config"]["party_stats_version"] >= 20362:
        	Bsversion = "1.6.1"
     if ba.app.config["public_config"]["party_stats_version"] >= 20365:
        	Bsversion = "1.6.2"
     if ba.app.config["public_config"]["party_stats_version"] >= 20366:
        	Bsversion = "1.6.3"
     if ba.app.config["public_config"]["party_stats_version"] >= 20367:
        	Bsversion = "1.6.4"
     if ba.app.config["public_config"]["party_stats_version"] >= 20388:
        	Bsversion = "1.6.5"
     if ba.app.config["public_config"]["party_stats_version"] >= 20436:
        	Bsversion = "1.6.6"
     if ba.app.config["public_config"]["party_stats_version"] >= 20394:
        	Bsversion = "1.6.7"
     if ba.app.config["public_config"]["party_stats_version"] >= 20444:
        	Bsversion = "1.6.8"
     if ba.app.config["public_config"]["party_stats_version"] >= 20461:
        	Bsversion = "1.6.9"
     if ba.app.config["public_config"]["party_stats_version"] >= 20501:
        	Bsversion = "1.6.10"
     if ba.app.config["public_config"]["party_stats_version"] >= 20514:
        	Bsversion = "1.6.11"
     if ba.app.config["public_config"]["party_stats_version"] >= 20542:
        	Bsversion = "1.6.12"
     if ba.app.config["public_config"]["party_stats_version"] >= 20599:
        	Bsversion = "1.6.12"
     if ba.app.config["public_config"]["party_stats_version"] >= 20577:
        	Bsversion = "1.7.0"
     if ba.app.config["public_config"]["party_stats_version"] >= 20592:
        	Bsversion = "1.7.1"
     if ba.app.config["public_config"]["party_stats_version"] >= 20602:
        	Bsversion = "1.7.2"
 
     # ping 
     self._ping = ba.textwidget(parent=self._root_widget,
                          position=(69.1, 199),
                          size=(0, 0),
                          scale=1,
                          color=p_ping_color,
                          maxwidth=45,
                          text="»" + str(ba.app.config["public_config"]["party_stats_ping"]) + "«",
                          h_align='center',
                          v_align='center')              
                          
     # version
     self._version = ba.textwidget(parent=self._root_widget,
                          position=(69.1, 182.5),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=45,
                          text="»" + str(ba.app.config["public_config"]["party_stats_version"]) + "«",
                          h_align='center',
                          v_align='center')              
                          
     # build number
     self._version = ba.textwidget(parent=self._root_widget,
                          position=(69.1, 167.5),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=45,
                          text="»" + Bsversion + "«",
                          h_align='center',
                          v_align='center')                                  
                          
     # name
     self._name = ba.textwidget(parent=self._root_widget,
                          position=(210, 210),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=140,
                          text="» " + ba.app.config["public_config"]["party_stats_name"],
                          h_align='center',
                          v_align='center')              
                          
     # ip
     self._ip = ba.textwidget(parent=self._root_widget,
                          position=(210, 180),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=120,
                          text="» " + ba.app.config["public_config"]["party_stats_address"] + ":" + str(ba.app.config["public_config"]["party_stats_port"]),
                          h_align='center',
                          v_align='center')                                                
                                               
     # size
     self._size = ba.textwidget(parent=self._root_widget,
                          position=(210, 150),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=40,
                          text="» "+ str(ba.app.config["public_config"]["party_stats_size"]) + "/" + str(ba.app.config["public_config"]["party_stats_size_max"]),
                          h_align='center',
                          v_align='center')    

     # language
     self._language = ba.textwidget(parent=self._root_widget,
                          position=(50, 120),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=(50),
                          text="» "+ ba.app.config["public_config"]["party_stats_language"],
                          h_align='center',
                          v_align='center')                    
                          
     # URL
     if ba.app.config["public_config"]["party_stats_url"] == "Empty":
         urlp=(60, 100)
     else:
         urlp=(100, 100)
     
     self._url = ba.textwidget(parent=self._root_widget,
                          position=urlp,
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=(50 if ba.app.config["public_config"]["party_stats_url"] == "Empty" else 140),
                          text="» " + ba.app.config["public_config"]["party_stats_url"],
                          h_align='center',
                          v_align='center')     

     # queue
     self._queue = ba.textwidget(parent=self._root_widget,
                          position=(175, 80),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=300,
                          text="» " + ba.app.config["public_config"]["party_stats_queue"],
                          h_align='center',
                          v_align='center')   
                          
     # Connect button
     self.connect_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(415, 240),
                                      size=(220, 50),
                                      label='Connect',
                                      on_activate_call=self._connect,
                                      button_type='regular',
                                      scale=0.55) 
                                      
     # Connect by ip button
     self.connect_by_ip_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(415, 210),
                                      size=(220, 50),
                                      label='Connect by ip',
                                      on_activate_call=self._connect_by_ip,
                                      button_type='regular',
                                      scale=0.55)                   

     # Copy button
     self.copy_ip_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(415, 180),
                                      size=(220, 50),
                                      label='Copy ip',
                                      on_activate_call=self._copy_ip,
                                      button_type='regular',
                                      scale=0.55) 
                                      
     # Queue
     self.connect_by_ip_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(415, 150),
                                      size=(220, 50),
                                      label='Copy Queue',
                                      on_activate_call=self._copy_queue,
                                      button_type='regular',
                                      scale=0.55)                   
     
     # url button type
     if ba.app.config["public_config"]["party_stats_url"] == "Empty":
     	BUTTON_URL_NAME = "Empty" 
     elif 'yout' in ba.app.config["public_config"]["party_stats_url"]:
    	 BUTTON_URL_NAME = "YouTube" 
     elif 'whats' in ba.app.config["public_config"]["party_stats_url"]:
    	 BUTTON_URL_NAME = "WhatsApp" 
     elif 'discord' in ba.app.config["public_config"]["party_stats_url"]:
     	 BUTTON_URL_NAME = "Discord" 
     elif 'dev' in ba.app.config["public_config"]["party_stats_url"]:
     	 BUTTON_URL_NAME = "Devs url"
     elif 't.me' in ba.app.config["public_config"]["party_stats_url"]:
    	 BUTTON_URL_NAME = "Telegram" 
     elif 'facebook' in ba.app.config["public_config"]["party_stats_url"]:
     	 BUTTON_URL_NAME = "Facebook" 
     elif 'github' in ba.app.config["public_config"]["party_stats_url"]:
     	 BUTTON_URL_NAME = "Github" 
     elif 'shop' in ba.app.config["public_config"]["party_stats_url"]:
     	 BUTTON_URL_NAME = "Shop" 
     else: 
     	 BUTTON_URL_NAME = ba.app.config["public_config"]["party_stats_url"][8:20]
    
     # Url button
     self.url_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(415, 120),
                                      size=(220, 50),
                                      label=BUTTON_URL_NAME,
                                      on_activate_call=self._open_url,
                                      button_type='regular',
                                      scale=0.55)                

     # Copy Url button
     self.copy_url_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(415, 999 if ba.app.config["public_config"]["party_stats_url"] == "Empty" else 90),
                                      size=(220, 50),
                                      label="copy " + BUTTON_URL_NAME + " URL",
                                      on_activate_call=self._copy_url,
                                      button_type='regular',
                                      scale=0.55)                                                     

     # Save To Manual button
     self.save_to_manual = ba.buttonwidget(parent=self._root_widget,
                                      position=(415, 90 if ba.app.config["public_config"]["party_stats_url"] == "Empty" else 60),
                                      size=(220, 50),
                                      label='Save to Manual',
                                      on_activate_call=self._save_to_manual,
                                      button_type='regular',
                                      scale=0.55)                         

#==============================================================================#             

                                                   
   # Connect Activate                                                 
   def _connect(self):
      if ba.app.config["public_config"]["party_stats_queue"] == "Empty":
          ba.screenmessage("» No Queue found try to connrct by ip", color=(1,0,0))
      else:
          self.try_to_connect = PartyQueueWindow(ba.app.config["public_config"]["party_stats_queue"], ba.app.config["public_config"]["party_stats_address"], ba.app.config["public_config"]["party_stats_port"])
      self._back()
        
   # Connect by ip Activate                                                 
   def _connect_by_ip(self):
        _ba.connect_to_party(ba.app.config["public_config"]["party_stats_address"], port=ba.app.config["public_config"]["party_stats_port"])
 
   # Save To Manual Activate                                                 
   def _save_to_manual(self):
      try:
          ba.app.config['Saved Servers'] = {}
          ba.app.config['Saved Servers']["{"+ba.app.config["public_config"]["party_stats_address"] + "@" + str(ba.app.config["public_config"]["party_stats_port"]) + "}"] = {
                    'addr': ba.app.config["public_config"]["party_stats_address"],
                    'port': ba.app.config["public_config"]["party_stats_port"],
                    'name': ba.app.config["public_config"]["party_stats_name"]
                }
          ba.app.config.apply_and_commit()
          ba.playsound(ba.getsound("fanfare"))
          ba.screenmessage("» Done")
      except:
          ba.print_exception()
          ba.screenmessage('» Error', (1, 0, 0))
          ba.playsound(ba.getsound("ticking"))
         
   # Copy ip
   def _copy_ip(self):
       ba.clipboard_set_text(ba.app.config["public_config"]["party_stats_address"] + ":" + str(ba.app.config["public_config"]["party_stats_port"]))
       ba.playsound(ba.getsound("woodDebrisFall"))
       
   # Copy Queue
   def _copy_queue(self):
       ba.clipboard_set_text(ba.app.config["public_config"]["party_stats_queue"])
       ba.playsound(ba.getsound("woodDebrisFall"))

   # open url Activate                                                 
   def _open_url(self):
      if ba.app.config["public_config"]["party_stats_url"] == "Empty":
          ba.screenmessage("» Party Stats URL is Empty", color=(1,0,0))
      else:
     	 ba.open_url(ba.app.config["public_config"]["party_stats_url"])
          
   # Copy url Activate                                                 
   def _copy_url(self):
      if ba.app.config["public_config"]["party_stats_url"] == "Empty":
          ba.screenmessage("» Error", color=(1,0,0))
      else:
          self.copy = ba.clipboard_set_text(ba.app.config["public_config"]["party_stats_url"])
          ba.playsound(ba.getsound("woodDebrisFall"))
           
   # back  Activate                                                 
   def _back(self):
        ba.containerwidget(edit=self._root_widget, transition='out_scale')
        Reset_settings()                                                
                        
                        
#==============================================================================#             

                       
# Connect
class ConnectWindow(ba.Window):
   def __init__(self, origin: Sequence[float] = (0, 0)):
     
     # Root widget
     self._root_widget = ba.containerwidget(
                         transition='in_scale',
                         parent=_ba.get_special_widget('overlay_stack'),
                         scale_origin_stack_offset=origin,
                         scale=2.0,
                         size=(350, 165),
                         stack_offset=(0, -10))
     
     # Connect
     self._connect_name = ba.textwidget(parent=self._root_widget,
                          position=(168, 150),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=160,
                          text="» Connect To Server",
                          h_align='center',
                          v_align='center')
    
     # Connect logo                       
     self._connect_logo = ba.imagewidget(parent=self._root_widget,
                                     size=(35, 35),
                                     position=(45, 135),
                                     texture=ba.gettexture('tv'))                                                                                                          
 
     # name
     self._name = ba.textwidget(parent=self._root_widget,
                          position=(85, 120),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=120,
                          text="» " + ba.app.config["public_config"]["party_stats_name"],
                          h_align='center',
                          v_align='center')              
                          
     # ip
     self._ip = ba.textwidget(parent=self._root_widget,
                          position=(85, 95),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=120,
                          text="» " + ba.app.config["public_config"]["party_stats_address"] + ":" + str(ba.app.config["public_config"]["party_stats_port"]),
                          h_align='center',
                          v_align='center')                                   
                          
     # queue
     self._queue = ba.textwidget(parent=self._root_widget,
                          position=(175, 70),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=300,
                          text="» " + ba.app.config["public_config"]["party_stats_queue"],
                          h_align='center',
                          v_align='center')                                  
                                               
     # size
     self._size = ba.textwidget(parent=self._root_widget,
                          position=(260, 120),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=40,
                          text="» "+ str(ba.app.config["public_config"]["party_stats_size"]) + "/" + str(ba.app.config["public_config"]["party_stats_size_max"]),
                          h_align='center',
                          v_align='center')               
                          
     # language
     self._language = ba.textwidget(parent=self._root_widget,
                          position=(260, 90),
                          size=(0, 0),
                          scale=1,
                          color=(1,1,1),
                          maxwidth=50,
                          text="» "+ ba.app.config["public_config"]["party_stats_language"],
                          h_align='center',
                          v_align='center')                                
            
     # save button
     self.connect_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(30, 20),
                                      size=(160, 60),
                                      label='Connect',
                                      on_activate_call=self._connect,
                                      button_type='regular',
                                      scale=0.55) 
                                      
     # Connect by ip button
     self.connect_by_ip_button = ba.buttonwidget(parent=self._root_widget,
                                      position=(130, 20),
                                      size=(160, 60),
                                      label='Connect by ip',
                                      on_activate_call=self._connect_by_ip,
                                      button_type='regular',
                                      scale=0.55)                     

     # Save To Manual button
     self.save_to_manual = ba.buttonwidget(parent=self._root_widget,
                                      position=(230, 20),
                                      size=(160, 60),
                                      label='Save to Manual',
                                      on_activate_call=self._save_to_manual,
                                      button_type='regular',
                                      scale=0.55)                                         
         
     # back
     self._back_button = btn = ba.buttonwidget(parent=self._root_widget,
                                      autoselect=True,
                                      position=(8, 140),
                                      size=(30, 30),
                                      scale=1.1,
                                      on_activate_call=self._back,
                                      label=ba.charstr(ba.SpecialChar.BACK),
                                      button_type='backSmall')
     ba.containerwidget(edit=self._root_widget, cancel_button=btn)                                                                 
                                  
#==============================================================================#             

                                  
   # Connect Activate                                                 
   def _connect(self):
      if ba.app.config["public_config"]["party_stats_queue"] == "Empty":
          ba.screenmessage("» No Queue found try to connrct by ip", color=(1,0,0))
      else:
          self.try_to_connect = PartyQueueWindow(ba.app.config["public_config"]["party_stats_queue"], ba.app.config["public_config"]["party_stats_address"], ba.app.config["public_config"]["party_stats_port"])
      self._back()
        
   # Connect by ip Activate                                                 
   def _connect_by_ip(self):
        _ba.connect_to_party(ba.app.config["public_config"]["party_stats_address"], port=ba.app.config["public_config"]["party_stats_port"])
    
   # Save To Manual Activate                                                 
   def _save_to_manual(self):
      try:
          ba.app.config['Saved Servers'] = {}
          ba.app.config['Saved Servers']["{"+ba.app.config["public_config"]["party_stats_address"] + "@" + str(ba.app.config["public_config"]["party_stats_port"]) + "}"] = {
                    'addr': ba.app.config["public_config"]["party_stats_address"],
                    'port': ba.app.config["public_config"]["party_stats_port"],
                    'name': ba.app.config["public_config"]["party_stats_name"]
                }
          ba.app.config.apply_and_commit()
          ba.playsound(ba.getsound("fanfare"))
          ba.screenmessage("» Done")
      except:
          ba.print_exception()
          ba.screenmessage('» Error', (1, 0, 0))
          ba.playsound(ba.getsound("ticking"))
        
   # back  Activate                                                 
   def _back(self):
        ba.containerwidget(edit=self._root_widget, transition='out_scale')
        Reset_settings()                                                                    
                    
#==============================================================================#             

class NewUIRow:
    """Wrangles UI for a row in the party list."""
    
    def __init__(self) -> None:
        self._name_widget: Optional[ba.Widget] = None
        self._size_widget: Optional[ba.Widget] = None
        self._ping_widget: Optional[ba.Widget] = None
        self._stats_button: Optional[ba.Widget] = None
        self._language_widget: Optional[ba.Widget] = None

    def __del__(self) -> None:
        self._clear()

    def _clear(self) -> None:
        for widget in [
                self._name_widget, self._size_widget, self._ping_widget,
                self._language_widget, self._stats_button
        ]:
            if widget:
                widget.delete()
                
    def update(self, index: int, party: PartyEntry, sub_scroll_width: float,
               sub_scroll_height: float, lineheight: float,
               columnwidget: ba.Widget, join_text: ba.Widget,
               filter_text: ba.Widget, existing_selection: Optional[Selection],
               tab: PublicGatherTab) -> None:
        """Update for the given data."""
        # pylint: disable=too-many-locals

        if party.clean_display_index == index:
            return

        ping_good = _ba.get_v1_account_misc_read_val('pingGood', 10)
        ping_med = _ba.get_v1_account_misc_read_val('pingMed', 80)
 
        self._clear()
        Reset_settings()
        Bsversion = "Unonwon - (" + str(party.version) + ")"

        # thx for This Github.com
        if party.version == 0:
            Bsversion = "??? - (" + str(party.version) + ")"
        if party.version >= 13700:
            Bsversion = "1.3 - (" + str(party.version) + ")"
        if party.version >= 14000:
        	Bsversion = "1.4 - (" + str(party.version) + ")"
        if party.version >= 14233:
        	Bsversion = "1.4.95 - (" + str(party.version) + ")"
        if party.version >= 14241:
        	Bsversion = "1.4.96 - (" + str(party.version) + ")"
        if party.version >= 14244:
        	Bsversion = "1.4.97 - (" + str(party.version) + ")"
        if party.version >= 14248:
        	Bsversion = "1.4.98 - (" + str(party.version) + ")"
        if party.version >= 14252:
        	Bsversion = "1.4.99 - (" + str(party.version) + ")"
        if party.version >= 14264:
        	Bsversion = "1.4.100 - (" + str(party.version) + ")"
        if party.version >= 14268:
        	Bsversion = "1.4.101 - (" + str(party.version) + ")"
        if party.version >= 14280:
        	Bsversion = "1.4.106 - (" + str(party.version) + ")"
        if party.version >= 14286:
        	Bsversion = "1.4.111 - (" + str(party.version) + ")"
        if party.version >= 14298:
        	Bsversion = "1.4.118 - (" + str(party.version) + ")"
        if party.version >= 14302:
        	Bsversion = "1.4.121 - (" + str(party.version) + ")"
        if party.version >= 14306:
        	Bsversion = "1.4.125 - (" + str(party.version) + ")"
        if party.version >= 14307:
        	Bsversion = "1.4.126 - (" + str(party.version) + ")"
        if party.version >= 14313:
        	Bsversion = "1.4.130 - (" + str(party.version) + ")"
        if party.version >= 14315:
        	Bsversion = "1.4.131 - (" + str(party.version) + ")"
        if party.version >= 14316:
        	Bsversion = "1.4.132 - (" + str(party.version) + ")"
        if party.version >= 14318:
        	Bsversion = "1.4.133 - (" + str(party.version) + ")"
        if party.version >= 14322:
        	Bsversion = "1.4.134 - (" + str(party.version) + ")"
        if party.version >= 14324:
        	Bsversion = "1.4.135 - (" + str(party.version) + ")"
        if party.version >= 14327:
        	Bsversion = "1.4.136 - (" + str(party.version) + ")"
        if party.version >= 14331:
        	Bsversion = "1.4.137 - (" + str(party.version) + ")"
        if party.version >= 14336:
        	Bsversion = "1.4.138 - (" + str(party.version) + ")"
        if party.version >= 14340:
        	Bsversion = "1.4.139 - (" + str(party.version) + ")"
        if party.version >= 14343:
        	Bsversion = "1.4.140 - (" + str(party.version) + ")"
        if party.version >= 14344:
        	Bsversion = "1.4.141 - (" + str(party.version) + ")"
        if party.version >= 14346:
        	Bsversion = "1.4.142 - (" + str(party.version) + ")"
        if party.version >= 14347:
        	Bsversion = "1.4.143 - (" + str(party.version) + ")"
        if party.version >= 14350:
        	Bsversion = "1.4.144 - (" + str(party.version) + ")"
        if party.version >= 14351:
        	Bsversion = "1.4.145 - (" + str(party.version) + ")"
        if party.version >= 14354:
        	Bsversion = "1.4.146 - (" + str(party.version) + ")"
        if party.version >= 14364:
        	Bsversion = "1.4.147 - (" + str(party.version) + ")"
        if party.version >= 14365:
        	Bsversion = "1.4.148 - (" + str(party.version) + ")"
        if party.version >= 14367:
        	Bsversion = "1.4.149 - (" + str(party.version) + ")"
        if party.version >= 14369:
        	Bsversion = "1.4.150 - (" + str(party.version) + ")"
        if party.version >= 14371:
        	Bsversion = "1.4.151 - (" + str(party.version) + ")"
        if party.version >= 14372:
        	Bsversion = "1.4.152 - (" + str(party.version) + ")"
        if party.version >= 14374:
        	Bsversion = "1.4.153 - (" + str(party.version) + ")"
        if party.version >= 14375:
        	Bsversion = "1.4.154 - (" + str(party.version) + ")"
        if party.version >= 14377:
        	Bsversion = "1.4.155 - (" + str(party.version) + ")" 
        if party.version >= 20001:
        	Bsversion = "1.5.0 - (" + str(party.version) + ")"  
        if party.version >= 20062:
        	Bsversion = "1.5.1 - (" + str(party.version) + ")"
        if party.version >= 20063:
        	Bsversion = "1.5.2 - (" + str(party.version) + ")"
        if party.version >= 20065:
        	Bsversion = "1.5.3 - (" + str(party.version) + ")"
        if party.version >= 20067:
        	Bsversion = "1.5.4 - (" + str(party.version) + ")"
        if party.version >= 20069:
        	Bsversion = "1.5.5 - (" + str(party.version) + ")"
        if party.version >= 20072:
        	Bsversion = "1.5.6 - (" + str(party.version) + ")"
        if party.version >= 20077:
        	Bsversion = "1.5.7 - (" + str(party.version) + ")"
        if party.version >= 20079:
        	Bsversion = "1.5.8 - (" + str(party.version) + ")"
        if party.version >= 20081:
        	Bsversion = "1.5.9 - (" + str(party.version) + ")"
        if party.version >= 20083:
        	Bsversion = "1.5.10 - (" + str(party.version) + ")"
        if party.version >= 20084:
        	Bsversion = "1.5.11 - (" + str(party.version) + ")"
        if party.version >= 20087:
        	Bsversion = "1.5.12 - (" + str(party.version) + ")"
        if party.version >= 20095:
        	Bsversion = "1.5.13 - (" + str(party.version) + ")"
        if party.version >= 20096:
        	Bsversion = "1.5.14 - (" + str(party.version) + ")"
        if party.version >= 20097:
        	Bsversion = "1.5.15 - (" + str(party.version) + ")"
        if party.version >= 20099:
        	Bsversion = "1.5.16 - (" + str(party.version) + ")"
        if party.version >= 20102:
        	Bsversion = "1.5.17 - (" + str(party.version) + ")"
        if party.version >= 20106:
        	Bsversion = "1.5.18 - (" + str(party.version) + ")"
        if party.version >= 20114:
        	Bsversion = "1.5.19 - (" + str(party.version) + ")"
        if party.version >= 20126:
        	Bsversion = "1.5.20 - (" + str(party.version) + ")"
        if party.version >= 20136:
        	Bsversion = "1.5.21 - (" + str(party.version) + ")"
        if party.version >= 20145:
        	Bsversion = "1.5.23 - (" + str(party.version) + ")"
        if party.version >= 20159:
        	Bsversion = "1.5.24 - (" + str(party.version) + ")"
        if party.version >= 20164:
        	Bsversion = "1.5.25 - (" + str(party.version) + ")"
        if party.version >= 20178:
        	Bsversion = "1.5.26 - (" + str(party.version) + ")"
        if party.version >= 20218:
        	Bsversion = "1.5.27 - (" + str(party.version) + ")"
        if party.version >= 20238:
        	Bsversion = "1.5.27 - (" + str(party.version) + ")"
        if party.version >= 20239:
        	Bsversion = "1.5.28 - (" + str(party.version) + ")"
        if party.version >= 20247:
        	Bsversion = "1.5.29 - (" + str(party.version) + ")"
        if party.version >= 20263:
        	Bsversion = "1.5.30 - (" + str(party.version) + ")"
        if party.version >= 20268:
        	Bsversion = "1.6.0 - (" + str(party.version) + ")"
        if party.version >= 20362:
        	Bsversion = "1.6.1 - (" + str(party.version) + ")"
        if party.version >= 20365:
        	Bsversion = "1.6.2 - (" + str(party.version) + ")"
        if party.version >= 20366:
        	Bsversion = "1.6.3 - (" + str(party.version) + ")"
        if party.version >= 20367:
        	Bsversion = "1.6.4 - (" + str(party.version) + ")"
        if party.version >= 20388:
        	Bsversion = "1.6.5 - (" + str(party.version) + ")"
        if party.version >= 20436:
        	Bsversion = "1.6.6 - (" + str(party.version) + ")"
        if party.version >= 20394:
        	Bsversion = "1.6.7 - (" + str(party.version) + ")"
        if party.version >= 20444:
        	Bsversion = "1.6.8 - (" + str(party.version) + ")"
        if party.version >= 20461:
        	Bsversion = "1.6.9 - (" + str(party.version) + ")"
        if party.version >= 20501:
        	Bsversion = "1.6.10 - (" + str(party.version) + ")"
        if party.version >= 20514:
        	Bsversion = "1.6.11 - (" + str(party.version) + ")"
        if party.version >= 20542:
        	Bsversion = "1.6.12 - (" + str(party.version) + ")"
        if party.version >= 20577:
        	Bsversion = "1.7.0 - (" + str(party.version) + ")"
        if party.version >= 20592:
        	Bsversion = "1.7.1 - (" + str(party.version) + ")"     
        if party.version >= 20600:
        	Bsversion = "1.7.1+ (" + str(party.version) + ")"     
        
        # Party Name
        if ba.app.config["public_config"]["party_ip"] == True and ba.app.config["public_config"]["bombSquad_version"] == True:
        	HostName = "» " + str(party.name) + "\n» " +str(party.address)+":"+str(party.port) + " « " + party_name_logo + " » bombSquad: " + Bsversion + " «"
        elif ba.app.config["public_config"]["party_ip"] == False and ba.app.config["public_config"]["bombSquad_version"] == True:
        	HostName = "» " + str(party.name) + "\n» bombSquad: " + Bsversion + " «"
        elif ba.app.config["public_config"]["party_ip"] == True and ba.app.config["public_config"]["bombSquad_version"] == False:
        	HostName = "» " + str(party.name) + "\n» " +str(party.address)+":"+str(party.port) + " «"
        elif ba.app.config["public_config"]["party_ip"] == False and ba.app.config["public_config"]["bombSquad_version"] == False:
        	HostName = "» " + str(party.name) + " « "
        else: 
            HostName = "» " + str(party.name) + "\n» " +str(party.address)+":"+str(party.port) + " « " + party_name_logo + " » bombSquad: " + str(party.version) + "  «"
        
        # party name scale
        if ba.app.config["public_config"]["party_ip"] == True and ba.app.config["public_config"]["bombSquad_version"] == True:
            Cscale = 1
        elif ba.app.config["public_config"]["party_ip"] == False and ba.app.config["public_config"]["bombSquad_version"] == True:
            Cscale = 0.6
        elif ba.app.config["public_config"]["party_ip"] == True and ba.app.config["public_config"]["bombSquad_version"] == False:
            Cscale = 0.6
        elif ba.app.config["public_config"]["party_ip"] == False and ba.app.config["public_config"]["bombSquad_version"] == False:
            Cscale = 1.5
        else: 
            Cscale = 1
         
        if ba.app.config["public_config"]["party_name_rainbow_color"]:
        	pName_Color = random.choice([(2,0,0),(2,1.5,0.5),(2,2,0),(0,2,0),(0,2,2),(0,0,2),(2,0,0)])
        else:
        	pName_Color = ba.app.config["public_config"]["party_name_color"]
        
        hpos = 20 
        vpos = sub_scroll_height - lineheight * index - 50
        self._name_widget = ba.textwidget(
            text=HostName,
            parent=columnwidget,
            size=(sub_scroll_width * 0.63 - 10, 30),
            position=(0 + hpos, 4 + vpos),
            selectable=True,
            on_select_call=ba.WeakCall(tab.set_public_party_selection,Selection(party.get_key(), SelectionComponent.NAME)),
            on_activate_call=ba.WeakCall(tab.on_public_party_activate, party),
            click_activate=True,
            maxwidth=sub_scroll_width * 0.45,
            corner_scale=Cscale,
            autoselect=True,
            color=pName_Color,
            h_align='left',
            v_align='center')
        ba.widget(edit=self._name_widget,left_widget=join_text,show_buffer_top=64.0,show_buffer_bottom=64.0)
        if existing_selection == Selection(party.get_key(), SelectionComponent.NAME):
            ba.containerwidget(edit=columnwidget, selected_child=self._name_widget)
                               
        if ba.app.config["public_config"]["party_menu"]:
            self._stats_button = ba.buttonwidget(
                textcolor=(1.0, 1.0, 1.0),
                label=menu_logo,
                parent=columnwidget,
                autoselect=True,
                on_select_call=ba.WeakCall(tab.set_public_party_selection, Selection(party.get_key(),SelectionComponent.STATS_BUTTON)),
                on_activate_call=ba.WeakCall(tab._public_party_activate, party),
                size=(50, 40),
                position=(sub_scroll_width * 0.66 + 180 + hpos, 1 + vpos),
                scale=0.9)
            if existing_selection == Selection(
                    party.get_key(), SelectionComponent.STATS_BUTTON):
                ba.containerwidget(edit=columnwidget,
                                   selected_child=self._stats_button)
                  
        if ba.app.config["public_config"]["party_size_rainbow_color"]:
        	pSize_color = random.choice([(2,0,0),(2,1.5,0.5),(2,2,0),(0,2,0),(0,2,2),(0,0,2),(2,0,0)])
        else:
        	pSize_color = ba.app.config["public_config"]["party_size_color"]
        
        if ba.app.config["public_config"]["party_size"]:                 
           self._size_widget = ba.textwidget(
               text=str(party.size) + '/' + str(party.size_max),
               parent=columnwidget,
               size=(0, 0),
               position=(sub_scroll_width * 0.86 - 60 + hpos, 20 + vpos),
               scale=0.5,
               color=pSize_color,
               h_align='right',
               v_align='center')

        if index == 0:
            ba.widget(edit=self._name_widget, up_widget=filter_text)
            if self._stats_button:
                ba.widget(edit=self._stats_button, up_widget=filter_text)
     
        if ba.app.config["public_config"]["party_ping_rainbow_color"]:
        	pPing_color = random.choice([(2,0,0),(2,1.5,0.5),(2,2,0),(0,2,0),(0,2,2),(0,0,2),(2,0,0)])
        else:
        	pPing_color = ba.app.config["public_config"]["party_ping_color"]
        	
        if ba.app.config["public_config"]["party_ping"]:
           self._ping_widget = ba.textwidget(parent=columnwidget,
                                             size=(0, 0),
                                             position=(sub_scroll_width * 0.94 - 75 +
                                                       hpos, 20 + vpos),
                                             scale=0.5,
                                             h_align='right',
                                             v_align='center')
                   
           Scounts = ba.app.config["public_config"]["Servers_counts"]                               
           if party.ping is None:
               ba.textwidget(edit=self._ping_widget,
                             text="-",
                             color=pPing_color)
               ba.app.config["public_config"]["Servers_founded"] = Scounts + 1
               ba.app.config["public_config"]["party_stats_ping"] = 9999
               ba.app.config.apply_and_commit()
           else:
               ba.textwidget(edit=self._ping_widget, 
                             text=str(int(party.ping)),
                             color=pPing_color)
               ba.app.config["public_config"]["Servers_counts"] = Scounts + 1                 
               ba.app.config["public_config"]["party_stats_ping"] = int(party.ping)
               ba.app.config.apply_and_commit()
           
        if ba.app.config["public_config"]["party_language_rainbow_color"]:
        	pSize_color = random.choice([(2,0,0),(2,1.5,0.5),(2,2,0),(0,2,0),(0,2,2),(0,0,2),(2,0,0)])
        else:
        	pSize_color = ba.app.config["public_config"]["party_language_color"]
        
        if ba.app.config["public_config"]["party_language"]:    
           ba.app.config["public_config"]["party_stats_language"] = party.language    
           self._language_widget = ba.textwidget(
               text=ba.app.config["public_config"]["party_stats_language"],
               parent=columnwidget,
               size=(0, 0),
               position=(sub_scroll_width * 0.86 - 130 + hpos, 20 + vpos),
               scale=0.5,
               color=pSize_color,
               h_align='right',
               v_align='center')
               
        party.clean_display_index = index
 
#==============================================================================#             

           
@dataclass
class State:
    """State saved/restored only while the app is running."""
    sub_tab: SubTabType = SubTabType.JOIN
    parties: Optional[List[Tuple[str, PartyEntry]]] = None
    next_entry_index: int = 0
    filter_value: str = ''
    have_server_list_response: bool = False
    have_valid_server_list: bool = False


class SelectionComponent(Enum):
    """Describes what part of an entry is selected."""
    NAME = 'name'
    STATS_BUTTON = 'stats_button'


@dataclass
class Selection:
    """Describes the currently selected list element."""
    entry_key: str
    component: SelectionComponent

#==============================================================================#             


class NewAddrFetchThread(threading.Thread):
    """Thread for fetching an address in the bg."""

    def __init__(self, call: Callable[[Any], Any]):
        super().__init__()
        self._call = call

    def run(self) -> None:
        try:
            # FIXME: Update this to work with IPv6 at some point, Ericccc fix this >:3
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect(('8.8.8.8', 80))
            val = sock.getsockname()[0]
            sock.close()
            ba.pushcall(ba.Call(self._call, val), from_other_thread=True)
        except Exception as exc:
            from efro.error import is_udp_network_error
            # Ignore expected network errors; log others.
            if is_udp_network_error(exc):
                pass
            else:
                ba.print_exception()

#==============================================================================#             

        
class NewPingThread(threading.Thread):
    """Thread for sending out game pings."""

    def __init__(self, address: str, port: int,
                 call: Callable[[str, int, Optional[float]], Optional[int]]):
        super().__init__()
        self._address = address
        self._port = port
        self._call = call

    def run(self) -> None:
        ba.app.ping_thread_count += 1
        sock: Optional[socket.socket] = None
        try:
            import socket
            from ba.internal import get_ip_address_type
            socket_type = get_ip_address_type(self._address)
            sock = socket.socket(socket_type, socket.SOCK_DGRAM)
            sock.connect((self._address, self._port))

            accessible = False
            starttime = time.time()

            # Send a few pings and wait a second for
            # a response.
            sock.settimeout(1)
            for _i in range(3):
                sock.send(b'\x0b')
                result: Optional[bytes]
                try:
                    # 11: BA_PACKET_SIMPLE_PING
                    result = sock.recv(10)
                except Exception:
                    result = None
                if result == b'\x0c':
                    # 12: BA_PACKET_SIMPLE_PONG
                    accessible = True
                    break
                time.sleep(1)
            ping = (time.time() - starttime) * ping_s
            ba.pushcall(ba.Call(self._call, self._address, self._port,
                                ping if accessible else None),
                        from_other_thread=True)
        except Exception as exc:
            from efro.error import is_udp_network_error
            if is_udp_network_error(exc):
                pass
            else:
                ba.print_exception('Error on gather ping', once=True)
        finally:
            try:
                if sock is not None:
                    sock.close()
            except Exception:
                ba.print_exception('Error on gather ping cleanup', once=True)

        ba.app.ping_thread_count -= 1

#==============================================================================#             


class NewPublicGatherTab(GatherTab):
    """The public tab in the gather UI"""

    def __init__(self, window: GatherWindow) -> None:
        super().__init__(window)
        self._container: Optional[ba.Widget] = None
        self._join_text_button: Optional[ba.Widget] = None
        self._host_text_button: Optional[ba.Widget] = None
        self._filter_text: Optional[ba.Widget] = None
        self._local_address: Optional[str] = None
        self._last_connect_attempt_time: Optional[float] = None
        self._sub_tab: SubTabType = SubTabType.JOIN
        self._selection: Optional[Selection] = None
        self._refreshing_list = False
        self._update_timer: Optional[ba.Timer] = None
        self._host_scrollwidget: Optional[ba.Widget] = None
        self._host_name_text: Optional[ba.Widget] = None
        self._host_toggle_button: Optional[ba.Widget] = None
        self._last_server_list_query_time: Optional[float] = None
        self._join_list_column: Optional[ba.Widget] = None
        self._join_status_text: Optional[ba.Widget] = None
        self._host_max_party_size_value: Optional[ba.Widget] = None
        self._host_max_party_size_minus_button: (Optional[ba.Widget]) = None
        self._host_max_party_size_plus_button: (Optional[ba.Widget]) = None
        self._host_status_text: Optional[ba.Widget] = None
        self._signed_in = False
        self._ui_rows: List[NewUIRow] = []
        self._refresh_ui_row = 0
        self._have_user_selected_row = False
        self._first_valid_server_list_time: Optional[float] = None

        # Parties indexed by id:
        self._parties: Dict[str, PartyEntry] = {}

        # Parties sorted in display order:
        self._parties_sorted: List[Tuple[str, PartyEntry]] = []
        self._party_lists_dirty = True

        # Sorted parties with filter applied:
        self._parties_displayed: Dict[str, PartyEntry] = {}

        self._next_entry_index = 0
        self._have_server_list_response = False
        self._have_valid_server_list = False
        self._filter_value = ''
        self._pending_party_infos: List[Dict[str, Any]] = []
        self._last_sub_scroll_height = 0.0

    def on_activate(
        self,
        parent_widget: ba.Widget,
        tab_button: ba.Widget,
        region_width: float,
        region_height: float,
        region_left: float,
        region_bottom: float,
    ) -> ba.Widget:
        c_width = region_width
        c_height = region_height - 20
        self._container = ba.containerwidget(
            parent=parent_widget,
            position=(region_left,
                      region_bottom + (region_height - c_height) * 0.5),
            size=(c_width, c_height),
            background=False,
            selection_loops_to_parent=True)
        v = c_height - 30
        ba.app.config["public_config"]["Servers_counts"] = 0
        ba.app.config["public_config"]["Servers_founded"] = 0
        ba.app.config.apply_and_commit()
        
        self._join_text_button = ba.buttonwidget(parent=self._container,
            color=(0.6, 1.0, 0.6),
            position=(c_width * 0.5 - 445, v - 9),
            scale=1.3,
            size=(150, 25),
            on_activate_call=lambda: self._set_sub_tab(SubTabType.JOIN, region_width, region_height, playsound=True),
            label=ba.Lstr(resource='gatherWindow.''joinPublicPartyDescriptionText'),
            autoselect=True,
            button_type='square')                                                               
                            
        self._host_text_button = ba.buttonwidget(parent=self._container,
            color=(0.6, 1.0, 0.6),
            position=(c_width * 0.5 - 445, v - 55),
            scale=1.3,
            size=(150, 25),
            on_activate_call=lambda: self._set_sub_tab(SubTabType.HOST, region_width, region_height, playsound=True),
            label=ba.Lstr(resource='gatherWindow.''hostPublicPartyDescriptionText'),
            autoselect=True,
            button_type='square')
            
        ba.widget(edit=self._join_text_button, up_widget=tab_button)
        ba.widget(edit=self._host_text_button,
                  left_widget=self._join_text_button,
                  up_widget=tab_button)
        ba.widget(edit=self._join_text_button, right_widget=self._host_text_button)
        
        # Attempt to fetch our local address so we have it for error messages.
        if self._local_address is None:
            NewAddrFetchThread(ba.WeakCall(self._fetch_local_addr_cb)).start()

        self._set_sub_tab(self._sub_tab, region_width, region_height)
        if ba.app.config["public_config"]["party_auto_update"]: 
           self._update_timer = ba.Timer(0.1,
                                      ba.WeakCall(self._update),
                                      repeat=True,
                                      timetype=ba.TimeType.REAL)
        else: 
           self._update_timer = ba.Timer(0.1,
                                      ba.WeakCall(self._update),
                                      repeat=False,
                                      timetype=ba.TimeType.REAL)
                                      
        return self._container

    def on_deactivate(self) -> None:
        self._update_timer = None

    def save_state(self) -> None:

        # Save off a small number of parties with the lowest ping; we'll
        # display these immediately when our UI comes back up which should
        # be enough to make things feel nice and crisp while we do a full
        # server re-query or whatnot.
        ba.app.ui.window_states[type(self)] = State(
            sub_tab=self._sub_tab,
            parties=[(i, copy.copy(p)) for i, p in self._parties_sorted[:40]],
            next_entry_index=self._next_entry_index,
            filter_value=self._filter_value,
            have_server_list_response=self._have_server_list_response,
            have_valid_server_list=self._have_valid_server_list)

    def restore_state(self) -> None:
        state = ba.app.ui.window_states.get(type(self))
        if state is None:
            state = State()
        assert isinstance(state, State)
        self._sub_tab = state.sub_tab

        # Restore the parties we stored.
        if state.parties:
            self._parties = {
                key: copy.copy(party)
                for key, party in state.parties
            }
            self._parties_sorted = list(self._parties.items())
            self._party_lists_dirty = True

            self._next_entry_index = state.next_entry_index

            # FIXME: should save/restore these too?..
            self._have_server_list_response = state.have_server_list_response
            self._have_valid_server_list = state.have_valid_server_list
        self._filter_value = state.filter_value

    def _set_sub_tab(self,
                     value: SubTabType,
                     region_width: float,
                     region_height: float,
                     playsound: bool = False) -> None:
        assert self._container
        if playsound:
            ba.playsound(ba.getsound('click01'))

        # Reset our selection.
        # (prevents selecting something way down the list if we switched away
        # and came back)
        self._selection = None
        self._have_user_selected_row = False

        # Reset refresh to the top and make sure everything refreshes.
        self._refresh_ui_row = 0
        for party in self._parties.values():
            party.clean_display_index = None

        self._sub_tab = value
        active_color = (0.6, 1.0, 0.6)
        inactive_color = (0.5, 0.4, 0.5)
        ba.buttonwidget(
            edit=self._join_text_button,
            color=active_color if value is SubTabType.JOIN else inactive_color)
        ba.buttonwidget(
            edit=self._host_text_button,
            color=active_color if value is SubTabType.HOST else inactive_color)

        # Clear anything existing in the old sub-tab.
        for widget in self._container.get_children():
            if widget and widget not in {self._host_text_button, self._join_text_button}:
                widget.delete()

        if value is SubTabType.JOIN:
            self._build_join_tab(region_width, region_height)

        if value is SubTabType.HOST:
            self._build_host_tab(region_width, region_height)

    def _build_join_tab(self, region_width: float,
                        region_height: float) -> None:
        c_width = region_width
        c_height = region_height - 20
        sub_scroll_height = c_height - 125
        sub_scroll_width = 830
        v = c_height - 35
        v -= 60
        filter_txt = ba.Lstr(resource='filterText')
        self._filter_text = ba.textwidget(parent=self._container,
                                          text=self._filter_value,
                                          size=(300, 40),
                                          position=(220, v + 25),
                                          h_align='left',
                                          v_align='center',
                                          editable=True,
                                          description=filter_txt)
        ba.widget(edit=self._filter_text, up_widget=self._join_text_button)
        ba.textwidget(text=filter_txt,
                      parent=self._container,
                      size=(0, 0),
                      position=(265, v + 77),
                      maxwidth=60,
                      scale=0.8,
                      color=(0.5, 0.46, 0.5),
                      flatness=1.0,
                      h_align='right',
                      v_align='center')

        ba.textwidget(text=ba.Lstr(resource='nameText'),
                      parent=self._container,
                      size=(0, 0),
                      position=(90, v - 8),
                      maxwidth=60,
                      scale=0.6,
                      color=(0.5, 0.46, 0.5),
                      flatness=1.0,
                      h_align='center',
                      v_align='center')
        if ba.app.config["public_config"]["party_language"]:                 
        	ba.textwidget(text="language",
                         parent=self._container,
                         size=(0, 0),
                         position=(630, v - 8),
                         maxwidth=60,
                         scale=0.6,
                         color=(0.5, 0.46, 0.5),
                         flatness=1.0,
                         h_align='center',
                         v_align='center')                      
        if ba.app.config["public_config"]["party_size"]: 
           ba.textwidget(text="Size",
                         parent=self._container,
                         size=(0, 0),
                         position=(707, v - 8),
                         maxwidth=60,
                         scale=0.6,
                         color=(0.5, 0.46, 0.5),
                         flatness=1.0,
                         h_align='center',
                         v_align='center')
        if ba.app.config["public_config"]["party_ping"]:            
            ba.textwidget(text="Ping",
                         parent=self._container,
                         size=(0, 0),
                         position=(762, v - 8),
                         maxwidth=60,
                         scale=0.6,
                         color=(0.5, 0.46, 0.5),
                         flatness=1.0,
                         h_align='center',
                         v_align='center')
        if ba.app.config["public_config"]["party_menu"]:
           ba.textwidget(text="Menu",
                          parent=self._container,
                          size=(0, 0),
                          position=(814, v - 8),
                          maxwidth=60,
                          scale=0.6,
                          color=(0.5, 0.46, 0.5),
                          flatness=1.0,
                          h_align='center',
                          v_align='center')
                 
        ba.textwidget(text="Servers counts: " + str(ba.app.config["public_config"]["Servers_counts"]),
                      parent=self._container,
                      size=(0, 0),
                      position=(600, v + 60),
                      maxwidth=200,
                      scale=0.6,
                      color=(0.5, 0.46, 0.5),
                      flatness=1.0,
                      h_align='center',
                      v_align='center')                
        ba.textwidget(text="Servers founded: " + str(ba.app.config["public_config"]["Servers_founded"]),
                      parent=self._container,
                      size=(0, 0),
                      position=(605, v + 30),
                      maxwidth=200,
                      scale=0.6,
                      color=(0.5, 0.46, 0.5),
                      flatness=1.0,
                      h_align='center',
                      v_align='center')                
     
        v -= sub_scroll_height + 23
        self._host_scrollwidget = scrollw = ba.scrollwidget(
            parent=self._container,
            simple_culling_v=10,
            position=((c_width - sub_scroll_width) * 0.5, v),
            size=(sub_scroll_width, sub_scroll_height),
            claims_up_down=False,
            claims_left_right=True,
            autoselect=True)
        self._join_list_column = ba.containerwidget(parent=scrollw,
                                                    background=False,
                                                    size=(400, 400),
                                                    claims_left_right=True)
        self._join_status_text = ba.textwidget(parent=self._container,
                                               text='',
                                               size=(0, 0),
                                               scale=0.9,
                                               flatness=1.0,
                                               shadow=0.0,
                                               h_align='center',
                                               v_align='top',
                                               maxwidth=c_width,
                                               color=(0.6, 0.6, 0.6),
                                               position=(c_width * 0.5,
                                                         c_height * 0.5))                                                   
     
        self.settings_button = ba.buttonwidget(parent=self._container,
             position=(820, 340),
             size=(130, 130),
             label='',
             on_activate_call=SettingsWindow,
             autoselect=True,
             button_type='square',
             scale=0.55)
        self.settings_button_icon = ba.imagewidget(parent=self._container,
            size=(65, 65),
            draw_controller=self.settings_button,
            position=(821.2, 341),
            texture=ba.gettexture('settingsIcon'))  

        self.replay_button = ba.buttonwidget(parent=self._container,
            position=(730, 340),
            size=(130, 130),
            label='',
            on_activate_call=lambda: self._set_sub_tab(SubTabType.JOIN, region_width, region_height, playsound=True),
            autoselect=True,
            button_type='square',
            scale=0.55)
        self.replay_button_icon = ba.imagewidget(parent=self._container,
            size=(65, 65),
            draw_controller=self.replay_button,
            position=(731.2, 341),
            texture=ba.gettexture('replayIcon'))                              

    def _build_host_tab(self, region_width: float,
                        region_height: float) -> None:
        c_width = region_width
        c_height = region_height - 20
        v = c_height - 35
        v -= 25
        is_public_enabled = _ba.get_public_party_enabled()
        v -= 30

        ba.textwidget(
            parent=self._container,
            size=(0, 0),
            h_align='center',
            v_align='center',
            maxwidth=c_width * 0.9,
            scale=0.7,
            flatness=1.0,
            color=(0.5, 0.46, 0.5),
            position=(region_width * 0.5, v + 10),
            text=ba.Lstr(resource='gatherWindow.publicHostRouterConfigText'))
        v -= 30

        party_name_text = ba.Lstr(
            resource='gatherWindow.partyNameText',
            fallback_resource='editGameListWindow.nameText')
        ba.textwidget(parent=self._container,
                      size=(0, 0),
                      h_align='right',
                      v_align='center',
                      maxwidth=200,
                      scale=0.8,
                      color=ba.app.ui.infotextcolor,
                      position=(210, v - 9),
                      text=party_name_text)
        self._host_name_text = ba.textwidget(parent=self._container,
                                             editable=True,
                                             size=(535, 40),
                                             position=(230, v - 30),
                                             text=ba.app.config.get(
                                                 'Public Party Name', ''),
                                             maxwidth=494,
                                             shadow=0.3,
                                             flatness=1.0,
                                             description=party_name_text,
                                             autoselect=True,
                                             v_align='center',
                                             corner_scale=1.0)

        v -= 60
        ba.textwidget(parent=self._container,
                      size=(0, 0),
                      h_align='right',
                      v_align='center',
                      maxwidth=200,
                      scale=0.8,
                      color=ba.app.ui.infotextcolor,
                      position=(210, v - 9),
                      text=ba.Lstr(resource='maxPartySizeText',
                                   fallback_resource='maxConnectionsText'))
        self._host_max_party_size_value = ba.textwidget(
            parent=self._container,
            size=(0, 0),
            h_align='center',
            v_align='center',
            scale=1.2,
            color=(1, 1, 1),
            position=(240, v - 9),
            text=str(_ba.get_public_party_max_size()))
        btn1 = self._host_max_party_size_minus_button = (ba.buttonwidget(
            parent=self._container,
            size=(40, 40),
            on_activate_call=ba.WeakCall(
                self._on_max_public_party_size_minus_press),
            position=(280, v - 26),
            label='-',
            autoselect=True))
        btn2 = self._host_max_party_size_plus_button = (ba.buttonwidget(
            parent=self._container,
            size=(40, 40),
            on_activate_call=ba.WeakCall(
                self._on_max_public_party_size_plus_press),
            position=(350, v - 26),
            label='+',
            autoselect=True))
        v -= 50
        v -= 70
        if is_public_enabled:
            label = ba.Lstr(
                resource='gatherWindow.makePartyPrivateText',
                fallback_resource='gatherWindow.stopAdvertisingText')
        else:
            label = ba.Lstr(
                resource='gatherWindow.makePartyPublicText',
                fallback_resource='gatherWindow.startAdvertisingText')
        self._host_toggle_button = ba.buttonwidget(
            parent=self._container,
            label=label,
            size=(400, 80),
            on_activate_call=self._on_stop_advertising_press
            if is_public_enabled else self._on_start_advertizing_press,
            position=(c_width * 0.5 - 200, v),
            autoselect=True,
            up_widget=btn2)
        ba.widget(edit=self._host_name_text, down_widget=btn2)
        ba.widget(edit=btn2, up_widget=self._host_name_text)
        ba.widget(edit=btn1, up_widget=self._host_name_text)
        ba.widget(edit=self._join_text_button, down_widget=self._host_name_text)
        v -= 10
        self._host_status_text = ba.textwidget(
            parent=self._container,
            text=ba.Lstr(resource='gatherWindow.'
                         'partyStatusNotPublicText'),
            size=(0, 0),
            scale=0.7,
            flatness=1.0,
            h_align='center',
            v_align='top',
            maxwidth=c_width * 0.9,
            color=(0.6, 0.56, 0.6),
            position=(c_width * 0.5, v))
        v -= 90
        ba.textwidget(
            parent=self._container,
            text=ba.Lstr(resource='gatherWindow.dedicatedServerInfoText'),
            size=(0, 0),
            scale=0.7,
            flatness=1.0,
            h_align='center',
            v_align='center',
            maxwidth=c_width * 0.9,
            color=(0.5, 0.46, 0.5),
            position=(c_width * 0.5, v))

        # If public sharing is already on,
        # launch a status-check immediately.
        if _ba.get_public_party_enabled():
            self._do_status_check()

    def _on_public_party_query_result(
            self, result: Optional[Dict[str, Any]]) -> None:
        starttime = time.time()
        self._have_server_list_response = True

        if result is None:
            self._have_valid_server_list = False
            return

        if not self._have_valid_server_list:
            self._first_valid_server_list_time = time.time()

        self._have_valid_server_list = True
        parties_in = result['l']

        assert isinstance(parties_in, list)
        self._pending_party_infos += parties_in

        # To avoid causing a stutter here, we do most processing of
        # these entries incrementally in our _update() method.
        # The one thing we do here is prune parties not contained in
        # this result.
        for partyval in list(self._parties.values()):
            partyval.claimed = False
        for party_in in parties_in:
            addr = party_in['a']
            assert isinstance(addr, str)
            port = party_in['p']
            assert isinstance(port, int)
            party_key = f'{addr}_{port}'
            party = self._parties.get(party_key)
            if party is not None:
                party.claimed = True
        self._parties = {
            key: val
            for key, val in list(self._parties.items()) if val.claimed
        }
        self._parties_sorted = [
            p for p in self._parties_sorted if p[1].claimed
        ]
        self._party_lists_dirty = True

        if DEBUG_PROCESSING:
            print(f'Handled public party query results in '
                  f'{time.time()-starttime:.5f}s.')

    def _update(self) -> None:
        """Periodic updating."""

        # Special case: if a party-queue window is up, don't do any of this
        # (keeps things smoother).
        # if ba.app.ui.have_party_queue_window:
        #     return

        if self._sub_tab is SubTabType.JOIN:

            # Keep our filter-text up to date from the UI.
            text = self._filter_text
            if text:
                filter_value = cast(str, ba.textwidget(query=text))
                if filter_value != self._filter_value:
                    self._filter_value = filter_value
                    self._party_lists_dirty = True

                    # Also wipe out party clean-row states.
                    # (otherwise if a party disappears from a row due to
                    # filtering and then reappears on that same row when
                    # the filter is removed it may not update)
                    for party in self._parties.values():
                        party.clean_display_index = None

            self._query_party_list_periodically()
            self._ping_parties_periodically()

        # If any new party infos have come in, apply some of them.
        self._process_pending_party_infos()

        # Anytime we sign in/out, make sure we refresh our list.
        signed_in = _ba.get_v1_account_state() == 'signed_in'
        if self._signed_in != signed_in:
            self._signed_in = signed_in
            self._party_lists_dirty = True

        # Update sorting to account for ping updates, new parties, etc.
        self._update_party_lists()

        # If we've got a party-name text widget, keep its value plugged
        # into our public host name.
        text = self._host_name_text
        if text:
            name = cast(str, ba.textwidget(query=self._host_name_text))
            _ba.set_public_party_name(name)

        # Update status text.
        status_text = self._join_status_text
        if status_text:
            if not signed_in:
                ba.textwidget(edit=status_text,
                              text=ba.Lstr(resource='notSignedInText'))
            else:
                # If we have a valid list, show no status; just the list.
                # Otherwise show either 'loading...' or 'error' depending
                # on whether this is our first go-round.
                if self._have_valid_server_list:
                    ba.textwidget(edit=status_text, text='')
                else:
                    if self._have_server_list_response:
                        ba.textwidget(edit=status_text,
                                      text=ba.Lstr(resource='errorText'))
                    else:
                        ba.textwidget(
                            edit=status_text,
                            text=ba.Lstr(
                                value='${A}...',
                                subs=[('${A}',
                                       ba.Lstr(resource='store.loadingText'))],
                            ))

        self._update_party_rows()

    def _update_party_rows(self) -> None:
        columnwidget = self._join_list_column
        if not columnwidget:
            return

        assert self._join_text_button
        assert self._filter_text

        # Janky - allow escaping when there's nothing in our list.
        assert self._host_scrollwidget
        ba.containerwidget(edit=self._host_scrollwidget,
                           claims_up_down=(len(self._parties_displayed) > 0))

        # Clip if we have more UI rows than parties to show.
        clipcount = len(self._ui_rows) - len(self._parties_displayed)
        if clipcount > 0:
            clipcount = max(clipcount, 50)
            self._ui_rows = self._ui_rows[:-clipcount]

        # If we have no parties to show, we're done.
        if not self._parties_displayed:
            return

        sub_scroll_width = 830
        lineheight = 42
        sub_scroll_height = lineheight * len(self._parties_displayed) + 50
        ba.containerwidget(edit=columnwidget,
                           size=(sub_scroll_width, sub_scroll_height))

        # Any time our height changes, reset the refresh back to the top
        # so we don't see ugly empty spaces appearing during initial list
        # filling.
        if sub_scroll_height != self._last_sub_scroll_height:
            self._refresh_ui_row = 0
            self._last_sub_scroll_height = sub_scroll_height

            # Also note that we need to redisplay everything since its pos
            # will have changed.. :(
            for party in self._parties.values():
                party.clean_display_index = None

        # Ew; this rebuilding generates deferred selection callbacks
        # so we need to push deferred notices so we know to ignore them.
        def refresh_on() -> None:
            self._refreshing_list = True

        ba.pushcall(refresh_on)

        # Ok, now here's the deal: we want to avoid creating/updating this
        # entire list at one time because it will lead to hitches. So we
        # refresh individual rows quickly in a loop.
        rowcount = min(12, len(self._parties_displayed))

        party_vals_displayed = list(self._parties_displayed.values())
        while rowcount > 0:
            refresh_row = self._refresh_ui_row % len(self._parties_displayed)
            if refresh_row >= len(self._ui_rows):
                self._ui_rows.append(NewUIRow())
                refresh_row = len(self._ui_rows) - 1

            # For the first few seconds after getting our first server-list,
            # refresh only the top section of the list; this allows the lowest
            # ping servers to show up more quickly.
            if self._first_valid_server_list_time is not None:
                if time.time() - self._first_valid_server_list_time < 4.0:
                    if refresh_row > 40:
                        refresh_row = 0

            self._ui_rows[refresh_row].update(
                refresh_row,
                party_vals_displayed[refresh_row],
                sub_scroll_width=sub_scroll_width,
                sub_scroll_height=sub_scroll_height,
                lineheight=lineheight,
                columnwidget=columnwidget,
                join_text=self._join_text_button,
                existing_selection=self._selection,
                filter_text=self._filter_text,
                tab=self)
            self._refresh_ui_row = refresh_row + 1
            rowcount -= 1

        # So our selection callbacks can start firing..
        def refresh_off() -> None:
            self._refreshing_list = False

        ba.pushcall(refresh_off)

    def _process_pending_party_infos(self) -> None:
        starttime = time.time()

        # We want to do this in small enough pieces to not cause UI hitches.
        chunksize = 30
        parties_in = self._pending_party_infos[:chunksize]
        self._pending_party_infos = self._pending_party_infos[chunksize:]
        for party_in in parties_in:
            addr = party_in['a']
            assert isinstance(addr, str)
            port = party_in['p']
            assert isinstance(port, int)
            party_key = f'{addr}_{port}'
            party = self._parties.get(party_key)
            if party is None:
                # If this party is new to us, init it.
                party = PartyEntry(address=addr,
                                   next_ping_time=ba.time(ba.TimeType.REAL) +
                                   0.001 * party_in['pd'],
                                   index=self._next_entry_index)
                self._parties[party_key] = party
                self._parties_sorted.append((party_key, party))
                self._party_lists_dirty = True
                self._next_entry_index += 1
                assert isinstance(party.address, str)
                assert isinstance(party.next_ping_time, float)

            # Now, new or not, update its values.
            party.queue = party_in.get('q')
            assert isinstance(party.queue, (str, type(None)))
            party.port = port
            party.name = party_in['n']
            assert isinstance(party.name, str)
            party.size = party_in['s']
            assert isinstance(party.size, int)
            party.size_max = party_in['sm']
            assert isinstance(party.size_max, int)
            party.language = party_in['l']
            assert isinstance(party.language, str)
            party.version = party_in['b'] 
            assert isinstance(party.version, int)
     
            # Server provides this in milliseconds; we use seconds.
            party.ping_interval = 0.001 * party_in['pi']
            assert isinstance(party.ping_interval, float)
            party.stats_addr = party_in['sa']
            assert isinstance(party.stats_addr, (str, type(None)))

            # Make sure the party's UI gets updated.
            party.clean_display_index = None

        if DEBUG_PROCESSING and parties_in:
            print(f'Processed {len(parties_in)} raw party infos in'
                  f' {time.time()-starttime:.5f}s.')

    def _update_party_lists(self) -> None:
        if not self._party_lists_dirty:
            return
        starttime = time.time()
        assert len(self._parties_sorted) == len(self._parties)

        self._parties_sorted.sort(key=lambda p: (
            p[1].queue is None,  # Show non-queued last.
            p[1].ping if p[1].ping is not None else 999999.0,
            p[1].index))

        # If signed out or errored, show no parties.
        if (_ba.get_v1_account_state() != 'signed_in'
                or not self._have_valid_server_list):
            self._parties_displayed = {}
        else:
            if self._filter_value:
                filterval = self._filter_value.lower()
                self._parties_displayed = {
                    k: v
                    for k, v in self._parties_sorted
                    if filterval in v.name.lower()
                }
            else:
                self._parties_displayed = dict(self._parties_sorted)

        # Any time our selection disappears from the displayed list, go back to
        # auto-selecting the top entry.
        if (self._selection is not None
                and self._selection.entry_key not in self._parties_displayed):
            self._have_user_selected_row = False

        # Whenever the user hasn't selected something, keep the first visible
        # row selected.
        if not self._have_user_selected_row and self._parties_displayed:
            firstpartykey = next(iter(self._parties_displayed))
            self._selection = Selection(firstpartykey, SelectionComponent.NAME)

        self._party_lists_dirty = False
        if DEBUG_PROCESSING:
            print(f'Sorted {len(self._parties_sorted)} parties in'
                  f' {time.time()-starttime:.5f}s.')

    def _query_party_list_periodically(self) -> None:
        now = ba.time(ba.TimeType.REAL)

        # Fire off a new public-party query periodically.
        if (self._last_server_list_query_time is None
                or now - self._last_server_list_query_time > 0.001 *
                _ba.get_v1_account_misc_read_val('pubPartyRefreshMS', 10000)):
            self._last_server_list_query_time = now
            if DEBUG_SERVER_COMMUNICATION:
                print('REQUESTING SERVER LIST')
            if _ba.get_v1_account_state() == 'signed_in':
                _ba.add_transaction(
                    {
                        'type': 'PUBLIC_PARTY_QUERY',
                        'proto': ba.app.protocol_version,
                        'lang': ba.app.lang.language
                    },
                    callback=ba.WeakCall(self._on_public_party_query_result))
                _ba.run_transactions()
            else:
                self._on_public_party_query_result(None)

    def _ping_parties_periodically(self) -> None:
        now = ba.time(ba.TimeType.REAL)

        # Go through our existing public party entries firing off pings
        # for any that have timed out.
        for party in list(self._parties.values()):
            if party.next_ping_time <= now and ba.app.ping_thread_count < 15:

                # Crank the interval up for high-latency or non-responding
                # parties to save us some useless work.
                mult = 1
                if party.ping_responses == 0:
                    if party.ping_attempts > 4:
                        mult = 10
                    elif party.ping_attempts > 2:
                        mult = 5
                if party.ping is not None:
                    mult = (10 if party.ping > 300 else
                            5 if party.ping > 150 else 2)

                interval = party.ping_interval * mult
                if DEBUG_SERVER_COMMUNICATION:
                    print(f'pinging #{party.index} cur={party.ping} '
                          f'interval={interval} '
                          f'({party.ping_responses}/{party.ping_attempts})')

                party.next_ping_time = now + party.ping_interval * mult
                party.ping_attempts += 1

                NewPingThread(party.address, party.port,
                           ba.WeakCall(self._ping_callback)).start()

    def _ping_callback(self, address: str, port: Optional[int],
                       result: Optional[float]) -> None:
        # Look for a widget corresponding to this target.
        # If we find one, update our list.
        party_key = f'{address}_{port}'
        party = self._parties.get(party_key)
        if party is not None:
            if result is not None:
                party.ping_responses += 1

            # We now smooth ping a bit to reduce jumping around in the list
            # (only where pings are relatively good).
            current_ping = party.ping
            if (current_ping is not None and result is not None
                    and result < 150):
                smoothing = 0.7
                party.ping = (smoothing * current_ping +
                              (1.0 - smoothing) * result)
            else:
                party.ping = result

            # Need to re-sort the list and update the row display.
            party.clean_display_index = None
            self._party_lists_dirty = True

    def _fetch_local_addr_cb(self, val: str) -> None:
        self._local_address = str(val)

    def _on_public_party_accessible_response(
            self, data: Optional[Dict[str, Any]]) -> None:

        # If we've got status text widgets, update them.
        text = self._host_status_text
        if text:
            if data is None:
                ba.textwidget(
                    edit=text,
                    text=ba.Lstr(resource='gatherWindow.'
                                 'partyStatusNoConnectionText'),
                    color=(1, 0, 0),
                )
            else:
                if not data.get('accessible', False):
                    ex_line: Union[str, ba.Lstr]
                    if self._local_address is not None:
                        ex_line = ba.Lstr(
                            value='\n${A} ${B}',
                            subs=[('${A}',
                                   ba.Lstr(resource='gatherWindow.'
                                           'manualYourLocalAddressText')),
                                  ('${B}', self._local_address)])
                    else:
                        ex_line = ''
                    ba.textwidget(
                        edit=text,
                        text=ba.Lstr(
                            value='${A}\n${B}${C}',
                            subs=[('${A}',
                                   ba.Lstr(resource='gatherWindow.'
                                           'partyStatusNotJoinableText')),
                                  ('${B}',
                                   ba.Lstr(resource='gatherWindow.'
                                           'manualRouterForwardingText',
                                           subs=[('${PORT}',
                                                  str(_ba.get_game_port()))])),
                                  ('${C}', ex_line)]),
                        color=(1, 0, 0))
                else:
                    ba.textwidget(edit=text,
                                  text=ba.Lstr(resource='gatherWindow.'
                                               'partyStatusJoinableText'),
                                  color=(0, 1, 0))

    def _do_status_check(self) -> None:
        from ba.internal import master_server_get
        ba.textwidget(edit=self._host_status_text,
                      color=(1, 1, 0),
                      text=ba.Lstr(resource='gatherWindow.'
                                   'partyStatusCheckingText'))
        master_server_get('bsAccessCheck', {'b': ba.app.build_number},
                          callback=ba.WeakCall(
                              self._on_public_party_accessible_response))

    def _on_start_advertizing_press(self) -> None:
        from bastd.ui.account import show_sign_in_prompt
        if _ba.get_v1_account_state() != 'signed_in':
            show_sign_in_prompt()
            return

        name = cast(str, ba.textwidget(query=self._host_name_text))
        if name == '':
            ba.screenmessage(ba.Lstr(resource='internal.invalidNameErrorText'),
                             color=(1, 0, 0))
            ba.playsound(ba.getsound('error'))
            return
        _ba.set_public_party_name(name)
        cfg = ba.app.config
        cfg['Public Party Name'] = name
        cfg.commit()
        ba.playsound(ba.getsound('shieldUp'))
        _ba.set_public_party_enabled(True)

        # In GUI builds we want to authenticate clients only when hosting
        # public parties.
        _ba.set_authenticate_clients(True)

        self._do_status_check()
        ba.buttonwidget(
            edit=self._host_toggle_button,
            label=ba.Lstr(
                resource='gatherWindow.makePartyPrivateText',
                fallback_resource='gatherWindow.stopAdvertisingText'),
            on_activate_call=self._on_stop_advertising_press)

    def _on_stop_advertising_press(self) -> None:
        _ba.set_public_party_enabled(False)

        # In GUI builds we want to authenticate clients only when hosting
        # public parties.
        _ba.set_authenticate_clients(False)
        ba.playsound(ba.getsound('shieldDown'))
        text = self._host_status_text
        if text:
            ba.textwidget(
                edit=text,
                text=ba.Lstr(resource='gatherWindow.'
                             'partyStatusNotPublicText'),
                color=(0.6, 0.6, 0.6),
            )
        ba.buttonwidget(
            edit=self._host_toggle_button,
            label=ba.Lstr(
                resource='gatherWindow.makePartyPublicText',
                fallback_resource='gatherWindow.startAdvertisingText'),
            on_activate_call=self._on_start_advertizing_press)

    def on_public_party_activate(self, party: PartyEntry) -> None:
        """Called when a party is clicked or otherwise activated."""
        if party.queue is not None:
            ba.playsound(ba.getsound('swish'))
            ba.app.config["public_config"]["party_stats_name"] = party.name
            ba.app.config["public_config"]["party_stats_address"] = party.address
            ba.app.config["public_config"]["party_stats_language"] = party.language
            ba.app.config["public_config"]["party_stats_port"] = party.port
            ba.app.config["public_config"]["party_stats_queue"] = party.queue
            ba.app.config["public_config"]["party_stats_version"] = party.version
            ba.app.config["public_config"]["party_stats_size"] = party.size
            ba.app.config["public_config"]["party_stats_size_max"] = party.size_max
            ba.app.config.apply_and_commit()
            ConnectWindow()
        else:
            # Rate limit this a bit.
            now = time.time()
            last_connect_time = self._last_connect_attempt_time
            if last_connect_time is None or now - last_connect_time > 2.0:
                ba.app.config["public_config"]["party_stats_name"] = party.name
                ba.app.config["public_config"]["party_stats_address"] = party.address
                ba.app.config["public_config"]["party_stats_language"] = party.language
                ba.app.config["public_config"]["party_stats_port"] = party.port
                ba.app.config["public_config"]["party_stats_version"] = party.version
                ba.app.config["public_config"]["party_stats_size"] = party.size
                ba.app.config["public_config"]["party_stats_size_max"] = party.size_max
                ba.app.config.apply_and_commit()
                ConnectWindow()
                self._last_connect_attempt_time = now
                
    def _public_party_activate(self, party: PartyEntry) -> None:
        """Called when a party is clicked or otherwise activated."""
        url = party.stats_addr.replace('${ACCOUNT}', _ba.get_v1_account_misc_read_val_2('resolvedAccountID', 'UNKNOWN'))
        ba.app.config["public_config"]["party_stats_name"] = party.name
        ba.app.config["public_config"]["party_stats_address"] = party.address
        ba.app.config["public_config"]["party_stats_language"] = party.language
        ba.app.config["public_config"]["party_stats_port"] = party.port
        ba.app.config["public_config"]["party_stats_queue"] = party.queue
        ba.app.config["public_config"]["party_stats_version"] = party.version
        ba.app.config["public_config"]["party_stats_size"] = party.size
        ba.app.config["public_config"]["party_stats_size_max"] = party.size_max
        ba.app.config.apply_and_commit()
                  
        if url == "":
            ba.app.config["public_config"]["party_stats_url"] = "Empty"
            ba.app.config.apply_and_commit()
        else:
            ba.app.config["public_config"]["party_stats_url"] = url
            ba.app.config.apply_and_commit()      
        MenuWindow()

    def set_public_party_selection(self, sel: Selection) -> None:
        """Set the sel."""
        if self._refreshing_list:
            return
        self._selection = sel
        self._have_user_selected_row = True

    def _on_max_public_party_size_minus_press(self) -> None:
        val = max(1, _ba.get_public_party_max_size() - 1)
        _ba.set_public_party_max_size(val)
        ba.textwidget(edit=self._host_max_party_size_value, text=str(val))

    def _on_max_public_party_size_plus_press(self) -> None:
        val = _ba.get_public_party_max_size()
        val += 1
        _ba.set_public_party_max_size(val)
        ba.textwidget(edit=self._host_max_party_size_value, text=str(val))

#==============================================================================#             

# ba_meta export plugin
class UwUuser(ba.Plugin):
    def __init__(self):
        if _ba.env().get("build_number",0) >= 20577:
            GP.UIRow = NewUIRow
            GP.AddrFetchThread = NewAddrFetchThread
            GP.PingThread = NewPingThread
            GP.PublicGatherTab = NewPublicGatherTab
            
        else:print("Public.py only runs with BobmSquad version 1.7.0+ for now.")
        
# ello why u here :3?