# ba_meta require api 6
import ba, _ba

# ba_meta export plugin
class UwUuser(ba.Plugin):
    def on_app_launch(self) -> None:
    	_ba.set_server_device_name("v1.4")
        _ba.set_server_name("Rick Astley")