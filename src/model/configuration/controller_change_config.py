from typing import Optional

from confz.confz import ConfZ


class ControllerChange(ConfZ):
    continues_controller: str
    min: Optional[int] = 0
    max: Optional[int] = 127
