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

        def emit() -> None:
            ba.emitfx(position=self.node.position,
                      velocity=self.node.velocity,
                      count=int(1.0+random.random()*9),
                      scale=0.5,
                      spread=0.10,
                      chunk_type='splinter')
        ba.timer(0.5, emit, repeat=True)
    Spaz.__init__ = _new_init
