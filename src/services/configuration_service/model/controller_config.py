from pydantic import BaseModel


class ControllerConfig(BaseModel):
    config_folder: str
    performance_folder: str
    default_performance: int
    performances_folder_path: str
