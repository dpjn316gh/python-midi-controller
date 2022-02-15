from typing import List

from pydantic import BaseModel


class PerformancesOpenDialogViewData(BaseModel):
    number: int
    name: str
    layers: int


class PerformancesOpenDialogViewDataList(BaseModel):
    performances: List[PerformancesOpenDialogViewData]
