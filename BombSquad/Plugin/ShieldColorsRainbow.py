# ba_meta require api 6

import ba, _ba
import random
from bastd.actor.spazfactory import SpazFactory
from bastd.actor import spaz

def new_equip_shields(OwO):
    def _equip_shields(self, decay: bool = False) -> None:
        if not self.node.exists(): return

        factory = SpazFactory.get()
        if self.shield is None:
            self.shield = ba.newnode('shield',
                                     owner=self.node,
                                     attrs={
                                         'color': (1,1,1),
                                         'radius': 1.3
                                     })
            ba.animate_array(self.shield,'color',3,
            {0:(random.choice([1,2,3,4,5,6,7,8,9]), random.choice([1,2,3,4,5,6,7,8,9]), random.choice([1,2,3,4,5,6,7,8,9])),
            0.2: (2,0,2),
            0.4: (2,2,0),
            0.6: (0,2,0),
            0.8: (0,2,2),
            1: (0,0,2),
            1.2: (2,0,0)},
            loop = True)                     
            self.node.connectattr('position_center', self.shield, 'position')
        self.shield_hitpoints = self.shield_hitpoints_max = 650
        self.shield_decay_rate = factory.shield_decay_rate if decay else 0
        self.shield.hurt = 0
        ba.playsound(factory.shield_up_sound, 1.0, position=self.node.position)

        if self.shield_decay_rate > 0:
            self.shield_decay_timer = ba.Timer(0.5,
                                               ba.WeakCall(self.shield_decay),
                                               repeat=True)
            self.shield.always_show_health_bar = True
    return _equip_shields

# ba_meta export plugin
class UwUuser(ba.Plugin):
    def __init__(self):
        spaz.Spaz.equip_shields = new_equip_shields(spaz.Spaz.equip_shields)
