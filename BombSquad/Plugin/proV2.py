# ba_meta require api 6
import ba, _ba

# ba_meta export plugin
class Pro(ba.Plugin):
    def on_app_launch(self) -> None:
        if _ba.env().get("build_number", 0) >= 20577:
            ba.app.accounts_v1.have_pro = lambda: True
            ba.app.accounts_v1.on_app_launch()
            ba.app.accounts_v2.have_pro = lambda: True
            ba.app.accounts_v2.on_app_launch()
        else:
            print("pro.py only runs with BombSquad versions higher than 1.7.0")