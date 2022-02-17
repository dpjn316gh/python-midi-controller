from abc import ABC, abstractmethod
from typing import List


class MidiInterfaceService(ABC):

    @abstractmethod
    def list_input_ports(self) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def list_output_ports(self) -> List[str]:
        raise NotImplementedError
