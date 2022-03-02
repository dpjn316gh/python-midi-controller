from typing import Optional

from pydantic import BaseModel


class FileOpenDialogViewData(BaseModel):
    root: Optional[str]
    selected_file: Optional[str]

