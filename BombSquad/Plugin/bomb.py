"""
Created by Jetz
"""

# ba_meta require api 6
from __future__ import annotations
from typing import TYPE_CHECKING

import ba
from bastd.gameutils import SharedObjects

if TYPE_CHECKING:
    from typing import Sequence, Any

class EggObject(ba.Actor):
    def __init__(self, scale: float = 3.0, position: Sequence[float] = (0.0, 1.0, 0.0)):
        super().__init__()

        shared = SharedObjects.get()
        model = ba.getmodel('impactBomb')
        tex = ba.gettexture('bombStickyColor')
        materials = [shared.object_material, ba.Material]

        self.old_pos = position
        self.scale = scale
        self.position = (position[0]-5, position[1]+2, position[2])
        self.node = ba.newnode('prop', delegate=self, attrs={'position': self.position, 'model': model, 'color_texture': tex, 'body': 'capsule', 'model_scale': self.scale, 'body_scale': 0.2 * self.scale, 'shadow_size': 0.5, 'reflection': 'powerup', 'reflection_scale': [1.0], 'materials': materials})
        ba.animate(self.node, 'model_scale', {0: 0.3, 0.2: 1.3 * self.scale, 3.26: self.scale})

    def handlemessage(self, msg: Any) -> Any:
        position_node = self.node.position
        velocity_node = self.node.velocity
        if isinstance(msg, ba.DieMessage):
            if self.node:
                self.node.delete()
            EggObject(scale=self.scale, position=self.old_pos).autoretain()
        elif isinstance(msg, ba.HitMessage):
            if self.node:
                ba.emitfx(position=position_node, velocity=velocity_node, scale=3.2, count=23, spread=0.67, chunk_type='spark')
                ba.animate(self.node, 'model_scale', {0: 2.76, 0.2: self.scale})
        else:
            return super().handlemessage(msg)

super_map = ba.Map.__init__
def new_map(self, *args, **kwargs):
    super_map(self, *args, **kwargs)
    spawn2 = self.defs.points['spawn2']
    EggObject(position=spawn2).autoretain()

def plugin():
    ba.Map.__init__ = new_map

# ba_meta export plugin
class UwUuser(ba.Plugin):
    plugin()