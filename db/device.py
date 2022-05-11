import sqlalchemy 
from .base import metadata
import datetime

devices = sqlalchemy.Table(
    "devices",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True ),
    sqlalchemy.Column("ip", sqlalchemy.String,  unique=True ),
    sqlalchemy.Column("created", sqlalchemy.DateTime, default=datetime.datetime.utcnow ),
    sqlalchemy.Column("up", sqlalchemy.DateTime, default=datetime.datetime.utcnow ),
    sqlalchemy.Column("down", sqlalchemy.DateTime, default=datetime.datetime.utcnow ),
    sqlalchemy.Column("status", sqlalchemy.Integer ),
    sqlalchemy.Column("api_login", sqlalchemy.String ),
    sqlalchemy.Column("api_pass", sqlalchemy.String ),
    sqlalchemy.Column("api_port", sqlalchemy.Integer ),
    sqlalchemy.Column("community_r", sqlalchemy.String ),
    sqlalchemy.Column("community_rw", sqlalchemy.String ),
    sqlalchemy.Column("desc", sqlalchemy.String ),
    sqlalchemy.Column("modules_id", sqlalchemy.Integer ),
    sqlalchemy.Column("group_id", sqlalchemy.Integer ),
    sqlalchemy.Column("sort_id", sqlalchemy.Integer ),
    
)
