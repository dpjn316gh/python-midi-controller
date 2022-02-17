from typing import List

from pydantic import BaseModel


class MidiInterfaceViewData(BaseModel):
    input_ports: List[str] = []
    output_ports: List[str] = []