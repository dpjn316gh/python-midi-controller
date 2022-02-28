from typing import List, Tuple

from pydantic import BaseModel


class MidiPorts(BaseModel):
    input_ports_names: List[str] = []
    output_ports_names: List[str] = []

    input_ports: List[Tuple] = []
    output_ports: List[Tuple] = []
