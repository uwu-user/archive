# ba_meta require api 6
import ba, _ba

# ba_meta export plugin
class Pro(ba.Plugin):
    def on_app_launch(self) -> None:
        ba.app.accounts.have_pro = lambda: True
        ba.app.accounts.on_app_launch()