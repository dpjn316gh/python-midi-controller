from typing import List

from pydantic import BaseModel


class MidiPorts(BaseModel):
    input_ports: List[str] = []
    output_ports: List[str] = []
