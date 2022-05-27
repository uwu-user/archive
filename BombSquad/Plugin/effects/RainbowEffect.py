# ba_meta require api 6

from __future__ import annotations
from typing import TYPE_CHECKING

import ba, _ba
import random
from bastd.actor.spaz import Spaz

if TYPE_CHECKING:
    from typing import Any, Type, Optional, Tuple, List, Dict

# ba_meta export plugin
class UwUuser(ba.Plugin):
    Spaz._old_init = Spaz.__init__
    def _new_init(self,
                 color: Sequence[float] = (1.0, 1.0, 1.0),
                 highlight: Sequence[float] = (0.5, 0.5, 0.5),
                 character: str = 'Spaz',
                 source_player: ba.Player = None,
                 start_invincible: bool = True,
                 can_accept_powerups: bool = True,
                 powerups_expire: bool = False,
                 demo_mode: bool = True):
        self._old_init(color,highlight,character,source_player,
                       start_invincible,can_accept_powerups,
                       powerups_expire,demo_mode)

        def Rainbow() -> None:
            ba.animate_array(self.node,'color',3,
            {0:(random.choice([1,2,3,4,5,6,7,8,9]), random.choice([1,2,3,4,5,6,7,8,9]), random.choice([1,2,3,4,5,6,7,8,9])),
            0.2: (2,0,2),
            0.4: (2,2,0),
            0.6: (0,2,0),
            0.8: (0,2,2),
            1: (0,0,2),
            1.2: (2,0,0)},
            loop = True)
        ba.timer(1.5, Rainbow, repeat=True)
        
    Spaz.__init__ = _new_init
