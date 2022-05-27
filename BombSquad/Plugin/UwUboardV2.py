# Keyboard mod for chat's only
# Unknown_#7004 - Discord :3

# ba_meta require api 6

from __future__ import annotations
from typing import TYPE_CHECKING

import ba, _ba
from ba._generated.enums import SpecialChar
from ba._generated.enums import InputType
from _ba import charstr

if TYPE_CHECKING: pass

# ba_meta export keyboard
class UwUboard(ba.Keyboard):
    name = 'UwUn\'t say OwO'
    chars = [('\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1'),
           ('\ue0b1','\ue0b1','\ue0b1','\ue002','\ue00c','\ue001','\ue0b1','\ue0b1','\ue0b1'),
           ('\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1')]
    nums = ('\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1',
           '\ue0b1','\ue0b1','\ue0b1','\ue002','\ue00c','\ue001','\ue0b1','\ue0b1','\ue0b1',
           '\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1','\ue0b1')
    pages: dict[str, tuple[str, ...]] = {
        'page_1': (
           charstr(SpecialChar.MUSHROOM),
           charstr(SpecialChar.HEART),
           charstr(SpecialChar.EYE_BALL),
           charstr(SpecialChar.YIN_YANG),
           charstr(SpecialChar.HAL),
           charstr(SpecialChar.LOGO),
           charstr(SpecialChar.MOON),
           charstr(SpecialChar.FEDORA),
           charstr(SpecialChar.NINJA_STAR),
           charstr(SpecialChar.SKULL),
           charstr(SpecialChar.DRAGON),
           charstr(SpecialChar.VIKING_HELMET),
           charstr(SpecialChar.FIREBALL),
           charstr(SpecialChar.SPIDER),
           charstr(SpecialChar.HELMET),
           charstr(SpecialChar.CROWN),
           charstr(SpecialChar.MIKIROG),
           charstr(SpecialChar.TICKET),
           charstr(SpecialChar.TICKET_BACKING),
           charstr(SpecialChar.PARTY_ICON),
           charstr(SpecialChar.STEAM_LOGO),
           charstr(SpecialChar.GOOGLE_PLAY_GAMES_LOGO),
           charstr(SpecialChar.GAME_CENTER_LOGO),
           charstr(SpecialChar.GAME_CIRCLE_LOGO),
           charstr(SpecialChar.ALIBABA_LOGO),
           charstr(SpecialChar.NVIDIA_LOGO)),
           'page_2': (
           charstr(SpecialChar.LOGO_FLAT),
           charstr(SpecialChar.BACK),
           charstr(SpecialChar.SHIFT),
           charstr(SpecialChar.UP_ARROW),
           charstr(SpecialChar.LEFT_ARROW),
           charstr(SpecialChar.RIGHT_ARROW),
           charstr(SpecialChar.DOWN_ARROW),
           charstr(SpecialChar.TOP_BUTTON),
           charstr(SpecialChar.LEFT_BUTTON),
           charstr(SpecialChar.BOTTOM_BUTTON),
           charstr(SpecialChar.RIGHT_BUTTON),
           charstr(SpecialChar.REWIND_BUTTON),
           charstr(SpecialChar.PLAY_PAUSE_BUTTON),
           charstr(SpecialChar.FAST_FORWARD_BUTTON),
           charstr(SpecialChar.DPAD_CENTER_BUTTON),
           charstr(SpecialChar.OCULUS_LOGO),
           '=','69', '@','#','$','□','*','☆','♡',
           charstr(SpecialChar.DELETE)),
           'page_3': ('°','¤','○','~','♤','£','¥','₩', '+','×','÷','/','-','_','◇','Ξ','π','ε','χ','λ','ω','β','?','!','¡','¿'),
           'page_4': (
           '\ue019', 
           '\ue01a', 
           '\ue01b',
           '\ue01c',
           charstr(SpecialChar.TROPHY1),
           charstr(SpecialChar.TROPHY2),
           charstr(SpecialChar.TROPHY3),
           charstr(SpecialChar.TROPHY4),
           charstr(SpecialChar.TROPHY0A),
           charstr(SpecialChar.TROPHY0B),
           charstr(SpecialChar.DICE_BUTTON1),
           charstr(SpecialChar.DICE_BUTTON2),
           charstr(SpecialChar.DICE_BUTTON3),
           charstr(SpecialChar.DICE_BUTTON4),
           charstr(SpecialChar.TEST_ACCOUNT),
           charstr(SpecialChar.OUYA_LOGO),
           charstr(SpecialChar.LOCAL_ACCOUNT),
           charstr(SpecialChar.V2_LOGO)),
           'page_5': ('OwO', 'Owo', 'owo', 'owO', 'OnO', 'OsO', 'OgO', 'OmO', 'OuO', 'OyO', 'OrO', 'OvO', 'Ojo', 'ObO', 'OxO', 'OoO', 'OdO', 'OaO', 'OcO','O-O', 'O_O', 'O~O', 'O☆O', 'O♡O', 'O□O', 'O^O'),
           'page_6': ('UwU', 'Uwu', 'uwu', 'uwU', 'UnU', 'UsU', 'UgU', 'UmU', 'UuU', 'UyU', 'UrU', 'UvU', 'Uju', 'UbU', 'UxU', 'UoU', 'UdU', 'UaU', 'UcU', 'U-U', 'U_U', 'U~U', 'U☆U', 'U♡U', 'U□U', 'U^U'),  
           'page_7': ('(￣ー￣)//','^o^','(о＾ω＾о)','╹﹏╹','ʘ‿ʘ','((((^_^)','(#×_×)','(･ิ_･ิ)っ','(>д<)','(¬‿¬)','＼（^-^）／','(╥﹏╥)','（￣～￣）','^_^/','(^▽^)','(–˛ — º)','^_^','(ㆆ_ㆆ)','(ò_ó)','(>_<)','T^T','( ͡° ͜ʖ ͡°)','⋟^≏^⋞','(≧∇≦)/'),
           'page_8': ('-(^.^)','¯\_(ツ)_/¯','(¬_¬)','(｡- ω -)','(*^^*)','(-＿-)','(-、-)','(∪｡∪)','(○o○)','(￣ε￣)','(☆´3｀)','|°з°|','(°ε°)','(*＾3＾)','(・_・?)','(¬､¬)','(¬＿¬)','o(>< )o','(＞д＜)','(*≧m≦*)','ヽ(`皿′)ﾉ','(゜ρ゜)ノ','ヾ(-_-; )','（’-’*)','(⌒▽⌒)☆','(^～^)'),
           'page_9': ('(・ω・)','∩( ・ω・)∩','Ò,ó','(=ω=;)','(⊙ヮ⊙)','(⊙_◎)','(⋋▂⋌)','ō_ō','⊙０⊙','⊙﹏⊙','⊙︿⊙','⊙△⊙','⊙▃⊙','⊙▂⊙','⊙ω⊙','(^～^)','(о-ω･)'
           'page_10': ('ඞ','இ')
    }