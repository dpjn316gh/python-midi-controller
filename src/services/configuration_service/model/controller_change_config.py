from typing import Optional

from pydantic import BaseModel


class ControllerChangeConfig(BaseModel):
    continues_controller: str
    min: Optional[int] = 0
    max: Optional[int] = 127
    use_global_channel: Optional[bool] = False
