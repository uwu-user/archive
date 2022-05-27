# ba_meta require api 6

from __future__ import annotations
from typing import TYPE_CHECKING

import ba

if TYPE_CHECKING: pass

class Player(ba.Player['Team']):
    """Our player type for this game."""


class Team(ba.Team[Player]):
    """Our team type for this game."""

# ba_meta export game
class DeathMatchGame(ba.TeamGameActivity[Player, Team]):
    name = 'Empty'
    description = '...'
    announce_player_deaths = False

    @classmethod
    def get_available_settings(
            cls, sessiontype: Type[ba.Session]) -> List[ba.Setting]:
        settings = [
            ba.IntChoiceSetting(
                'Time Limit',
                choices=[ # memes
                    ('No time', 0),
                    ('1 Minute', 60),
                    ('2 Minutes', 120),
                    ('5 Minutes', 300),
                    ('10 Minutes', 600),
                    ('15 Minutes', 900),
                    ('30 Minutes', 1800),
                    ('60 Minutes', 3600),
                    ('2 Hours', 7200),
                    ('3 Hours', 10800),
                    ('4 Hours', 14400),
                    ('5 Hours', 18000),
                    ('6 Hours', 21600),
                    ('7 Hours', 25200),
                    ('8 Hours', 28800),
                    ('9 Hours', 32400),
                    ('10 Hours', 36000),
                    ('11 Hours', 39600),
                    ('12 Hours', 43200),
                    ('13 Hours', 46800),
                    ('14 Hours', 50400),
                    ('15 Hours', 54000),
                    ('16 Hours', 57600),
                    ('17 Hours', 61200),
                    ('18 Hours', 64800),
                    ('19 Hours', 68400),
                    ('20 Hours', 72000),
                    ('21 Hours', 75600),
                    ('22 Hours', 79200),
                    ('23 Hours', 82800),
                    ('1 days', 86400),
                    ('2 days', 172800),
                    ('3 days', 259200),
                    ('4 days', 345600),
                    ('5 days', 432000),
                    ('6 days', 518400),
                    ('7 days', 604800),
                    ('8 days', 691200),
                    ('9 days', 777600),
                    ('10 days', 864000), # ...
                    ('11 days', 950400), # ...?
                ],
                default=0,
            ),
            ba.FloatChoiceSetting(
                'Respawn Times',
                choices=[
                    ('No time', 0.001),
                    ('Shorter', 0.25),
                    ('Short', 0.5),
                    ('Normal', 1.0),
                    ('Long', 2.0),
                    ('Longer', 4.0),
                    ('?', 9999.0),
                ],
                default=1.0,
            )
        ]
        return settings

    @classmethod
    def supports_session_type(cls, sessiontype: Type[ba.Session]) -> bool:
        return (issubclass(sessiontype, ba.FreeForAllSession))

    def __init__(self, settings: dict): # time
        super().__init__(settings)
        self._time_limit = float(settings['Time Limit'])

    def on_begin(self) -> None: # time
        super().on_begin()
        self.setup_standard_time_limit(self._time_limit)
        
    def handlemessage(self, msg: Any) -> Any: # Respawn
        if isinstance(msg, ba.PlayerDiedMessage):
            super().handlemessage(msg)

            player = msg.getplayer(Player)
            self.respawn_player(player)
        return None
