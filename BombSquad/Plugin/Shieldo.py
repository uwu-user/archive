# ba_meta require api 6


#==============================================================================#             
#     
#     version v1.0
#     Create by Unknown_#7004 
#     Github https://github.com/uwu-user
#
#==============================================================================#             


from __future__ import annotations
from typing import TYPE_CHECKING, cast

import ba
import _ba
import random
from ba._map import Map
from bastd import mainmenu
from bastd.gameutils import SharedObjects

if TYPE_CHECKING:
    from typing import Any, Sequence, Callable, List, Dict, Tuple, Optional, Union

#==============================================================================#             

# ba_meta export plugin
class UwUuser(ba.Plugin):
    Map._old_init = Map.__init__
    def _new_init(self, vr_overlay_offset: Optional[Sequence[float]] = None) -> None:
        self._old_init(vr_overlay_offset)   
        in_game = not isinstance(_ba.get_foreground_host_session(), mainmenu.MainMenuSession)
        if not in_game: return
        
        def path():
            shield = ba.newnode("shield", attrs={'color': (1,1,1), 'position': (-5.750,4.3515026107,2.0), 'radius': 1.4})
            ba.animate_array(shield, 'color',3,{0:(random.choice([1,2,3,4,5,6,7,8,9]), random.choice([1,2,3,4,5,6,7,8,9]), random.choice([1,2,3,4,5,6,7,8,9])),0.2: (2,0,2), 0.4: (2,2,0), 0.6: (0,2,0),0.8: (0,2,2)},  loop = True)
            flash = ba.newnode("flash", attrs={'position':(0,0,0), 'size':0.6, 'color': (1,1,1)})
            shield.connectattr('position', flash, 'position')
            ba.animate_array(shield, 'position', 3,
                            {0: (1.830634, 4.830635, 3.830636),
                            10: (4.8306378, 4.83063588, -6.830639),
                            20: (-5.422572086, 4.228850685, 2.803988636),
                            25: (-6.859406739, 4.429165244, -6.588618549),
                            30: (-6.859406739, 4.429165244, -6.588618549),
                            35: (3.148493267, 4.429165244, -6.588618549),
                            40: (1.830377363, 4.228850685, 2.803988636),
                            45: (-5.422572086, 4.228850685, 2.803988636),
                            50: (-5.422572086, 4.228850685, 2.803988636),
                            55: (1.830377363, 4.228850685, 2.803988636),
                            60: (3.148493267, 4.429165244, -6.588618549),
                            70: (1.830377363, 4.228850685, 2.803988636),
                            75: (3.148493267, 4.429165244, -6.588618549),
                            80: (-5.422572086, 4.228850685, 2.803988636),
                            90: (-6.859406739, 4.429165244, -6.588618549),
                            95: (-6.859406739, 4.429165244, -6.588618549),      
                            100: (-6.859406739, 4.429165244, -6.588618549),
                            105: (-6.859406739, 4.429165244, -6.588618549),
                            110: (-5.422572086, 4.228850685, 2.803988636),
                            115: (3.148493267, 4.429165244, -6.588618549),
                            120: (1.830377363, 4.228850685, 2.803988636),
                            125: (3.148493267, 4.429165244, -6.588618549),
                            130: (1.830377363, 4.228850685, 2.803988636),
                            135: (-5.422572086, 4.228850685, 2.803988636),
                            140: (-5.422572086, 4.228850685, 2.803988636),
                            145: (1.830377363, 4.228850685, 2.803988636),
                            150: (3.148493267, 4.429165244, -6.588618549),
                            155: (-6.859406739, 4.429165244, -6.588618549),
                            160: (-6.859406739, 4.429165244, -6.588618549),
                            156: (-5.422572086, 4.228850685, 2.803988636),
                            170: (4.8306378, 4.83063588, -6.830639),
                            175: (1.830634, 4.830635, 3.830636)},                             
                            loop = True)                   

        ba.timer(0.1, path)
    Map.__init__ = _new_init
