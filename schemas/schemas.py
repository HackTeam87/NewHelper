from pydantic import BaseModel
from datetime import date


class Device(BaseModel):
    id: int
    ip: str
    # created: date
    # up: date
    # down: date
    status: int
    api_login: str
    api_pass: str
    api_port: str
    community_r: str
    community_rw: str
    desc: str
    modules_id: int
    group_id: int
    sort_id: int

