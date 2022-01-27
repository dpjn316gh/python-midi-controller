from typing import Optional

from confz.confz import ConfZ


class ControllerChangeConfig(ConfZ):
    continues_controller: str
    min: Optional[int] = 0
    max: Optional[int] = 127
    from_global_channel: Optional[bool] = True
